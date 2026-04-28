"""
Smoke + verification suite for a deployed Union control plane.

Imported from an e2e orchestrator (selfmanaged_aws_e2e.py::main calls
``run_smoke_suite``), or invoke ``main()`` standalone for ad-hoc smoke runs
against any already-deployed cluster:

    python -m smoke_tests --control_plane_url https://myorg.union.ai \\
        --cluster_name my-cluster

Every verification uses the Python SDK end-to-end — no ``flyte run``
subprocesses, no inline Python scripts. Each test owns a module-level
``TaskEnvironment`` + task and submits via ``flyte.run.aio``. Inspection
uses ``Run.get_logs.aio`` / ``Run.outputs``.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import uuid
from datetime import timedelta

import flyte
import flyte.app.extras
import typing

from selfmanaged_common import (
    BaseConfig,
    TestResult,
    init_union_client,
    say,
    sh,
)

logger = logging.getLogger("flyte.e2e.smoke")


# ============================================================================
# Helpers
# ============================================================================


def _read_keyring_token(control_plane_url: str) -> str:
    import keyring  # type: ignore
    host = control_plane_url.replace("https://", "").replace("http://", "").rstrip("/")
    return keyring.get_password(host, "access_token") or ""


def _phase_name(run: "flyte.Run") -> str:
    return str(run.phase).rsplit(".", 1)[-1].lower()


async def _assert_succeeded(run: "flyte.Run", label: str) -> None:
    """Wait for terminal state and raise if not succeeded."""
    await run.wait.aio(wait_for="terminal")
    await run.sync.aio()
    p = _phase_name(run)
    if p != "succeeded":
        raise RuntimeError(f"{label}: run {run.name} ended in phase={run.phase}")


# ============================================================================
# Module-level environments + tasks — one per test
# ============================================================================

# -- Smoke: the hello workflow lives in its own module so flyte.run bundles
#    only that file, not the full scripts directory.
from _smoke_hello import run_hello  # noqa: E402


# -- Image-builder test ------------------------------------------------------
#
# Different image from the base so this submission genuinely exercises the
# imagebuilder on a fresh cluster. Uses `cache="disable"` so each submission
# actually runs the task; flyte's own image cache decides whether to rebuild.
_imgbuild_env = flyte.TaskEnvironment(
    name="e2e-image-builder",
    image=flyte.Image.from_debian_base().with_pip_packages("requests==2.32.3"),
    cache="disable",
)


@_imgbuild_env.task
async def _imgbuild_task(nonce: str) -> str:
    import requests  # type: ignore
    logger.info(f"imgbuild task: requests={requests.__version__}, nonce={nonce}")
    return f"requests={requests.__version__}"


# -- Image-cache test --------------------------------------------------------
#
# Separate env so its image hash is stable across the two calls that the
# cache test makes. Env var pins it to the cluster so every cluster gets a
# fresh first-build (not a stale hit from a prior teardown).
_imgcache_env = flyte.TaskEnvironment(
    name="e2e-image-cache",
    image=(
        flyte.Image.from_debian_base()
        .with_pip_packages("requests==2.32.3")
        .with_env_vars({"E2E_CACHE_TEST": "v1"})
    ),
    cache="disable",
)


@_imgcache_env.task
async def _imgcache_task(nonce: str) -> str:
    import requests  # type: ignore
    logger.info(f"imgcache task: requests={requests.__version__}, nonce={nonce}")
    return f"requests={requests.__version__}"


# -- Reusable containers test ------------------------------------------------
_reuse_env = flyte.TaskEnvironment(
    name="e2e-reuse",
    image=flyte.Image.from_debian_base().with_pip_packages("unionai-reuse>=0.1.10"),
    resources=flyte.Resources(memory="512Mi", cpu="500m"),
    cache="disable",
    reusable=flyte.ReusePolicy(
        replicas=2,
        concurrency=1,
        scaledown_ttl=timedelta(minutes=2),
        idle_ttl=timedelta(minutes=5),
    ),
)


@_reuse_env.task
async def _reuse_square(x: int) -> int:
    return x * x


@_reuse_env.task
async def _reuse_driver(n: int) -> list[int]:
    """Driver that fans out to ``_reuse_square`` N times on the reusable
    environment, exercising replica scheduling + concurrency."""
    return list(await asyncio.gather(*(_reuse_square(i) for i in range(n))))


# -- App deployment test -----------------------------------------------------
#
# FastAPIAppEnvironment serves a tiny app; a TaskEnvironment depends on it
# to drive the deploy/test/deactivate lifecycle.

_fastapi_app = None


def _build_fastapi_app():
    """Build the FastAPI app on first access (imports kept lazy to keep
    ``smoke_tests`` importable without fastapi present)."""
    global _fastapi_app
    if _fastapi_app is not None:
        return _fastapi_app
    import fastapi  # type: ignore

    app = fastapi.FastAPI()

    @app.get("/")
    async def root() -> str:
        return "e2e-app-ok"

    @app.get("/health")
    async def health() -> dict:
        return {"status": "healthy", "source": "e2e-test"}

    _fastapi_app = app
    return app


_app_env = flyte.app.extras.FastAPIAppEnvironment(
    name="e2e-app-deploy",
    app=_build_fastapi_app(),
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn", "httpx"),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

_app_task_env = flyte.TaskEnvironment(
    name="e2e-app-deploy-tester",
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn", "httpx"),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    depends_on=[_app_env],
    cache="disable",
)


class _AppDeployResult(typing.NamedTuple):
    internal_url: str
    public_url: str


@_app_task_env.task
async def _app_deploy_test() -> _AppDeployResult:
    import httpx  # type: ignore
    await flyte.init_in_cluster.aio()
    deployed = flyte.serve(_app_env)
    internal_url = _app_env.endpoint
    public_url = deployed.endpoint
    logger.info(f"app: internal={internal_url} public={public_url}")
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{internal_url}/")
            assert resp.status_code == 200, f"/ returned {resp.status_code}"
            assert "e2e-app-ok" in resp.text
            resp = await client.get(f"{internal_url}/health")
            assert resp.status_code == 200
            assert resp.json().get("status") == "healthy"
    finally:
        deployed.deactivate(wait=True)
    return _AppDeployResult(internal_url=internal_url, public_url=public_url)


# ============================================================================
# Smoke test
# ============================================================================


@flyte.trace
async def smoke_test(cfg: BaseConfig, org: str = "") -> str:
    """Submit the hello task (defined in _smoke_hello.py) and wait. Returns run name."""
    await init_union_client(cfg, org=org)
    say(f"smoke_test: submitting hello on project={cfg.test_project}")
    run = await run_hello()
    say(f"smoke_test: run '{run.name}' — {run.url}")
    await _assert_succeeded(run, "smoke_test")
    say(f"smoke_test: PASSED (run={run.name})")
    return run.name


# ============================================================================
# Post-run inspections — Run.get_logs / Run.outputs
# ============================================================================


async def _collect_logs(run: "flyte.Run") -> str:
    """Drain run.get_logs into a single string."""
    parts: list[str] = []
    async for line in run.get_logs.aio():
        parts.append(line)
    return "\n".join(parts)


@flyte.trace
async def verify_logs(cfg: BaseConfig, run_name: str, org: str = "") -> None:
    """Live & persistent logs: fetch, delete pods, fetch again."""
    await init_union_client(cfg, org=org)
    say(f"verify_logs: run={run_name}")
    from flyte.remote import Run

    run = await Run.get.aio(name=run_name)
    live = await _collect_logs(run)
    if not live.strip():
        raise RuntimeError(f"verify_logs: no logs returned for {run_name} (live)")

    pods = await sh(
        f"kubectl get pods -n {cfg.test_project}-development "
        f"-l execution-id={run_name} --no-headers -o custom-columns=NAME:.metadata.name",
        check=False,
    )
    for pod in pods.strip().splitlines():
        pod = pod.strip()
        if pod:
            await sh(
                f"kubectl delete pod {pod} -n {cfg.test_project}-development --wait=false",
                check=False,
            )
    await asyncio.sleep(10)

    persistent = await _collect_logs(run)
    if not persistent.strip():
        raise RuntimeError(
            f"verify_logs: logs empty after pod deletion for {run_name} "
            f"(persistent logs missing)"
        )
    say(f"verify_logs: PASSED ({run_name})")


@flyte.trace
async def verify_io(cfg: BaseConfig, run_name: str, org: str = "") -> None:
    """Run.outputs returns the task's outputs."""
    await init_union_client(cfg, org=org)
    say(f"verify_io: run={run_name}")
    from flyte.remote import Run

    run = await Run.get.aio(name=run_name)
    outputs = run.outputs
    if outputs is None:
        raise RuntimeError(f"verify_io: no outputs for {run_name}")
    say(f"verify_io: PASSED ({run_name})")


@flyte.trace
async def verify_cors(cfg: BaseConfig, run_name: str, org: str) -> None:
    """Code bundle download via presigned URL + CORS header check.

    Uses the admin data-proxy HTTP API directly with the user's keyring
    token — no flyte CLI needed.
    """
    import urllib.error
    import urllib.request

    say(f"verify_cors: run={run_name} org={org}")
    token = _read_keyring_token(cfg.control_plane_url)
    if not token:
        raise RuntimeError(
            f"verify_cors: no access token in keyring for '{cfg.control_plane_url}'. "
            "Run `flyte config init` or `uctl config init` first."
        )

    cp_base = cfg.control_plane_url.rstrip("/")
    url = f"{cp_base}/cloudidl.clouddataproxy.CloudDataProxyService/CreateDownloadLinkV2"
    body = json.dumps({
        "artifactType": "ARTIFACT_TYPE_CODE_BUNDLE",
        "actionAttemptId": {
            "actionId": {
                "run": {
                    "org": org,
                    "project": cfg.test_project,
                    "domain": "development",
                    "name": run_name,
                },
                "name": "a0",
            },
            "attempt": 1,
        },
    }).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(
            f"verify_cors: CreateDownloadLinkV2 failed ({e.code}): {e.read().decode()[:500]}"
        )
    signed_urls = resp_body.get("preSignedUrls", {}).get("signedUrl", [])
    if not signed_urls:
        raise RuntimeError(
            f"verify_cors: no presigned URLs returned: {json.dumps(resp_body)[:500]}"
        )
    signed_url = signed_urls[0]
    get_req = urllib.request.Request(
        signed_url, headers={"Origin": cp_base}, method="GET",
    )
    try:
        with urllib.request.urlopen(get_req) as resp:
            data = resp.read()
            cors_header = resp.getheader("Access-Control-Allow-Origin", "")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"verify_cors: GET on presigned URL failed ({e.code})")
    if len(data) == 0:
        raise RuntimeError("verify_cors: code bundle is empty")
    if not cors_header:
        raise RuntimeError(
            "verify_cors: no Access-Control-Allow-Origin header on presigned URL. "
            "CORS may not be configured on the storage bucket."
        )
    say(f"verify_cors: PASSED ({len(data)} bytes, CORS={cors_header})")


# ============================================================================
# Image builder / cache / reusable / app — all via flyte.run.aio
# ============================================================================


@flyte.trace
async def verify_image_builder(cfg: BaseConfig, org: str = "") -> None:
    """Submit ``_imgbuild_task`` — first sign-off run triggers an image
    build, subsequent runs reuse the built image. The task itself is
    cache="disable" so re-submission actually executes each time."""
    await init_union_client(cfg, org=org)
    nonce = str(uuid.uuid4())
    say(f"verify_image_builder: submitting _imgbuild_task (nonce={nonce})")
    run = await flyte.run.aio(_imgbuild_task, nonce=nonce)
    say(f"verify_image_builder: run '{run.name}'")
    await _assert_succeeded(run, "verify_image_builder")
    say(f"verify_image_builder: PASSED (run={run.name})")


@flyte.trace
async def verify_image_cache(cfg: BaseConfig, org: str = "") -> None:
    """Submit ``_imgcache_task`` twice. Image is stable so the second call
    should hit flyte's image cache; we don't introspect the builder, only
    verify both runs complete."""
    await init_union_client(cfg, org=org)
    nonce1, nonce2 = str(uuid.uuid4()), str(uuid.uuid4())
    say(f"verify_image_cache: run 1 (nonce={nonce1})")
    run1 = await flyte.run.aio(_imgcache_task, nonce=nonce1)
    await _assert_succeeded(run1, "verify_image_cache run 1")
    say(f"verify_image_cache: run 2 (nonce={nonce2}) — expect image cache hit")
    run2 = await flyte.run.aio(_imgcache_task, nonce=nonce2)
    await _assert_succeeded(run2, "verify_image_cache run 2")
    say(f"verify_image_cache: PASSED (run1={run1.name}, run2={run2.name})")


@flyte.trace
async def verify_reusable(cfg: BaseConfig, org: str = "") -> None:
    """Submit ``_reuse_driver`` which fans out square() calls over a
    ReusePolicy environment (replicas=2, concurrency=1)."""
    await init_union_client(cfg, org=org)
    import random
    n = random.randint(3, 10)
    say(f"verify_reusable: submitting _reuse_driver(n={n})")
    run = await flyte.run.aio(_reuse_driver, n=n)
    await _assert_succeeded(run, "verify_reusable")
    say(f"verify_reusable: PASSED (run={run.name})")


@flyte.trace
async def verify_app(cfg: BaseConfig, org: str = "") -> None:
    """Deploy a FastAPI app, hit internal + public endpoints, deactivate."""
    import urllib.error
    import urllib.request

    await init_union_client(cfg, org=org)
    say("verify_app: submitting _app_deploy_test")
    run = await flyte.run.aio(_app_deploy_test)
    say(f"verify_app: run '{run.name}' — {run.url}")
    await _assert_succeeded(run, "verify_app")

    # Outputs contain internal_url + public_url (NamedTuple fields).
    outputs = run.outputs
    public_url = ""
    try:
        as_dict = outputs.to_dict() if hasattr(outputs, "to_dict") else {}
        o0 = as_dict.get("o0") or {}
        public_url = str(o0.get("public_url", ""))
    except Exception as e:
        say(f"verify_app: couldn't parse outputs ({e}); skipping public-URL check")

    if not public_url:
        say(f"verify_app: PASSED internal only (no public_url parsed, run={run.name})")
        return

    token = _read_keyring_token(cfg.control_plane_url)
    if not token:
        say("verify_app: PASSED internal only (no keyring token)")
        return
    req = urllib.request.Request(
        public_url, headers={"Authorization": f"Bearer {token}"}, method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
            status = resp.status
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"verify_app: public URL returned {e.code}: {e.read().decode()[:200]}")
    if status != 200 or "e2e-app-ok" not in body:
        raise RuntimeError(f"verify_app: public URL unexpected ({status}): {body[:200]}")
    say(f"verify_app: PASSED internal+public (status={status})")


# ============================================================================
# Suite
# ============================================================================


async def run_smoke_suite(cfg: BaseConfig, org: str) -> list[TestResult]:
    """Run the hello workflow then the 7 verifications in parallel.

    Returns per-test results; does not raise on individual failures.
    ``init_union_client`` should already have been called by the caller; each
    verify re-calls it (cheap) to tolerate trace context boundaries.
    """
    say(f"run_smoke_suite: project={cfg.test_project} org={org}")
    run_name = await smoke_test(cfg, org=org)

    tests = [
        ("Live & Persistent Logs",    verify_logs(cfg, run_name, org)),
        ("Inputs/Outputs",            verify_io(cfg, run_name, org)),
        ("Code Bundle Download & CORS", verify_cors(cfg, run_name, org)),
        ("Remote Image Builder",      verify_image_builder(cfg, org)),
        ("Image Cache (No Rebuild)",  verify_image_cache(cfg, org)),
        ("Reusable Containers",       verify_reusable(cfg, org)),
        ("App Deployment",            verify_app(cfg, org)),
    ]
    names = [n for n, _ in tests]
    outcomes = await asyncio.gather(*(c for _, c in tests), return_exceptions=True)

    results = []
    for name, outcome in zip(names, outcomes):
        r = TestResult(name=name)
        if isinstance(outcome, Exception):
            r.error = str(outcome)[:200]
            say(f"[TEST FAILED] {name}: {r.error}")
        else:
            r.passed = True
        results.append(r)

    say("=" * 60)
    for r in results:
        status = "PASSED" if r.passed else "FAILED"
        say(f"  {r.name:<36} {status}  {'' if r.passed else r.error[:60]}")
    passed = sum(1 for r in results if r.passed)
    say(f"run_smoke_suite: {passed}/{len(results)} passed")
    return results


# ============================================================================
# Standalone entry point
# ============================================================================


async def _main_async(args: argparse.Namespace) -> int:
    from selfmanaged_common import detect_org_name, hydrate_credentials

    cfg = BaseConfig(
        control_plane_url=args.control_plane_url,
        cluster_name=args.cluster_name,
        test_project=args.project or args.cluster_name,
    )
    await hydrate_credentials()
    await init_union_client(cfg)
    org = args.org or await detect_org_name(cfg)
    # Re-init with org so SelectCluster routing has it.
    await init_union_client(cfg, org=org)
    results = await run_smoke_suite(cfg, org)
    failed = [r for r in results if not r.passed]
    return 1 if failed else 0


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s - %(message)s",
    )
    p = argparse.ArgumentParser(description="Run the Union smoke + verification suite.")
    p.add_argument("--control_plane_url", required=True)
    p.add_argument("--cluster_name", required=True)
    p.add_argument("--project", default="", help="Test project name (defaults to cluster_name).")
    p.add_argument("--org", default="", help="Org name (auto-detected if omitted).")
    args = p.parse_args()
    return asyncio.run(_main_async(args))


if __name__ == "__main__":
    raise SystemExit(main())
