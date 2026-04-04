"""
Shared utilities for selfmanaged E2E tests.

Contains base configuration, encryption, shell helpers, debug collection,
Docker image construction, Helm chart management, and verification logic
that is reused across cloud providers (AWS, GCP, etc.).
"""

from __future__ import annotations

import base64
import json
import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

# =============================================================================
# Constants
# =============================================================================

_KEYS_DIR = Path(__file__).parent / ".e2e-keys"
_PUBLIC_KEY_PATH = _KEYS_DIR / "e2e_public.pem"
_PRIVATE_KEY_PATH = _KEYS_DIR / "e2e_private.pem"
_FLYTE_SECRET_NAME = "E2E_RSA_PRIVATE_KEY"

# Tool versions pinned for reproducibility
_HELM_VERSION = "3.17.3"
_KUBECTL_VERSION = "1.31.4"
_YQ_VERSION = "4.45.4"
_UCTL_VERSION = "0.1.20"

# =============================================================================
# Base configuration
# =============================================================================


@dataclass
class BaseConfig:
    """Fields shared across all cloud providers."""

    # Required — Union control plane
    control_plane_url: str = ""
    cluster_name: str = ""

    # Helm
    helm_namespace: str = "union"
    helm_release_name: str = "union"
    helm_chart_repo: str = "https://github.com/unionai/helm-charts.git"
    helm_chart_branch: str = "enghabu/sane-defaults"  # git branch; empty = use published release
    helm_chart_path: str = "charts/dataplane"  # path inside the repo

    # Timeouts (seconds)
    cluster_healthy_timeout: int = 300
    validate_timeout: int = 300

    # Behavior
    skip_teardown: bool = False

    # Encrypted credentials blob (JSON string from _encrypt_env_vars).
    # Empty when running locally (credentials come from local env vars).
    encrypted_credentials: str = ""

    # Union org name (parsed from uctl output if not set)
    org_name: str = ""

    # Project to use for test executions (defaults to cluster_name)
    test_project: str = ""

    def __post_init__(self):
        if not self.control_plane_url:
            self.control_plane_url = os.environ.get("UNION_CONTROL_PLANE_URL", "")
        if not self.cluster_name:
            self.cluster_name = os.environ.get("UNION_CLUSTER_NAME", "")
        if not self.test_project:
            self.test_project = self.cluster_name


@dataclass
class BaseInfraState:
    """Fields shared across all cloud providers."""

    values_file_path: str = ""
    debug_dir: str = ""


# =============================================================================
# Shell helpers
# =============================================================================


def _sh(cmd: str, check: bool = True, capture: bool = True) -> str:
    """Run a shell command, return stdout."""
    print(f"  $ {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=capture,
        text=True,
    )
    if capture and result.stdout:
        print(result.stdout.rstrip())
    if capture and result.stderr:
        print(result.stderr.rstrip())
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed (exit {result.returncode}): {cmd}\n{result.stderr}"
        )
    return result.stdout if capture else ""


def _sh_ok(cmd: str) -> bool:
    """Run a command and return True if it succeeds."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode == 0


# =============================================================================
# RSA envelope encryption — one secret, many credentials
# =============================================================================


def _generate_key_pair() -> None:
    """Generate RSA-4096 key pair and store in _KEYS_DIR."""
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization

    _KEYS_DIR.mkdir(parents=True, exist_ok=True)

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    _PRIVATE_KEY_PATH.write_bytes(
        private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
    )
    _PUBLIC_KEY_PATH.write_bytes(
        private_key.public_key().public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )
    _PRIVATE_KEY_PATH.chmod(0o600)
    print(f"Generated key pair in {_KEYS_DIR}/")
    print(f"  Public key:  {_PUBLIC_KEY_PATH}")
    print(f"  Private key: {_PRIVATE_KEY_PATH}")


def _encrypt(plaintext: str) -> str:
    """Hybrid encrypt: RSA-OAEP wraps AES-GCM key. Returns base64 blob."""
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    pub_key = serialization.load_pem_public_key(_PUBLIC_KEY_PATH.read_bytes())
    aes_key = os.urandom(32)
    nonce = os.urandom(12)
    ciphertext = AESGCM(aes_key).encrypt(nonce, plaintext.encode(), None)
    wrapped_key = pub_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    # Pack: [2-byte wrapped_key_len][wrapped_key][12-byte nonce][ciphertext]
    blob = len(wrapped_key).to_bytes(2, "big") + wrapped_key + nonce + ciphertext
    return base64.b64encode(blob).decode()


def _decrypt(token: str, private_key_pem: bytes) -> str:
    """Decrypt a token produced by _encrypt()."""
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    blob = base64.b64decode(token)
    wk_len = int.from_bytes(blob[:2], "big")
    wrapped_key = blob[2 : 2 + wk_len]
    nonce = blob[2 + wk_len : 2 + wk_len + 12]
    ciphertext = blob[2 + wk_len + 12 :]

    priv_key = serialization.load_pem_private_key(private_key_pem, password=None)
    aes_key = priv_key.decrypt(
        wrapped_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return AESGCM(aes_key).decrypt(nonce, ciphertext, None).decode()


def decrypt_and_export_credentials(encrypted_credentials: str) -> None:
    """If encrypted credentials are present, decrypt them and set as env vars."""
    if not encrypted_credentials:
        return  # Running locally — credentials already in env

    # Read the private key from the Flyte secret mount.
    candidates = [
        Path("/etc/flyte/secrets") / _FLYTE_SECRET_NAME,
        Path("/etc/flyte/secrets") / _FLYTE_SECRET_NAME.lower(),
        Path("/etc/flyte/secrets") / _FLYTE_SECRET_NAME / _FLYTE_SECRET_NAME.lower(),
    ]
    private_key_pem = None
    for secret_path in candidates:
        if secret_path.exists():
            private_key_pem = secret_path.read_bytes()
            print(f"  Found private key at {secret_path}")
            break

    if private_key_pem is None and os.environ.get(_FLYTE_SECRET_NAME):
        private_key_pem = os.environ[_FLYTE_SECRET_NAME].encode()
        print(f"  Found private key in ${_FLYTE_SECRET_NAME} env var")

    if private_key_pem is None:
        secrets_dir = Path("/etc/flyte/secrets")
        contents = list(secrets_dir.rglob("*")) if secrets_dir.exists() else []
        raise RuntimeError(
            f"Cannot find private key. Checked: {[str(p) for p in candidates]} "
            f"and ${_FLYTE_SECRET_NAME} env var. "
            f"Contents of {secrets_dir}: {[str(p) for p in contents]}"
        )

    creds = json.loads(encrypted_credentials)
    for env_var, encrypted_value in creds.items():
        if encrypted_value:
            os.environ[env_var] = _decrypt(encrypted_value, private_key_pem)
            print(f"  Decrypted {env_var} ({len(os.environ[env_var])} chars)")


def encrypt_env_vars(env_vars: dict[str, str], required: list[str]) -> str:
    """Encrypt a dict of env var name→value pairs. Returns JSON string.

    Args:
        env_vars: mapping of env var names to their values (empty string = skip).
        required: list of env var names that must be non-empty.
    """
    if not _PUBLIC_KEY_PATH.exists():
        raise RuntimeError(
            f"Public key not found at {_PUBLIC_KEY_PATH}. Run setup_keys first."
        )

    encrypted = {}
    for key, value in env_vars.items():
        if value:
            encrypted[key] = _encrypt(value)
            print(f"  Encrypted {key} ({len(value)} chars -> {len(encrypted[key])} chars)")
        else:
            encrypted[key] = ""

    for req in required:
        if not encrypted.get(req):
            raise RuntimeError(f"{req} not set in environment")

    return json.dumps(encrypted)


# =============================================================================
# Debug collection
# =============================================================================


def collect_debug_dumps(cfg: BaseConfig, debug_dir: str) -> str:
    """Dump cluster state for debugging. Returns the debug directory path."""
    if not _sh_ok("kubectl cluster-info"):
        print("WARNING: No cluster access — skipping debug dump.")
        return debug_dir

    os.makedirs(debug_dir, exist_ok=True)
    print(f"Collecting debug dumps to {debug_dir}...")

    _dump_cmd("kubectl get pods -A -o wide", f"{debug_dir}/pods-all.txt")
    _dump_cmd(
        "kubectl get events -A --sort-by='.lastTimestamp'",
        f"{debug_dir}/events.txt",
    )
    _dump_cmd("kubectl get nodes -o wide", f"{debug_dir}/nodes.txt")
    _dump_cmd(
        f"helm status {cfg.helm_release_name} -n {cfg.helm_namespace}",
        f"{debug_dir}/helm-status.txt",
    )

    pod_logs_dir = f"{debug_dir}/pod-logs"
    os.makedirs(pod_logs_dir, exist_ok=True)

    pods_output = _sh("kubectl get pods -A --no-headers", check=False)
    for line in pods_output.strip().splitlines():
        parts = line.split()
        if len(parts) < 4:
            continue
        ns, pod, _, status = parts[0], parts[1], parts[2], parts[3]
        if status in ("Running", "Succeeded", "Completed"):
            continue

        pod_dir = f"{pod_logs_dir}/{ns}--{pod}"
        os.makedirs(pod_dir, exist_ok=True)
        _dump_cmd(f"kubectl describe pod {pod} -n {ns}", f"{pod_dir}/describe.txt")

        containers = _sh(
            f"kubectl get pod {pod} -n {ns} -o jsonpath='{{.spec.containers[*].name}}'",
            check=False,
        )
        for container in containers.split():
            _dump_cmd(
                f"kubectl logs {pod} -n {ns} -c {container}",
                f"{pod_dir}/{container}.log",
            )
            _dump_cmd(
                f"kubectl logs {pod} -n {ns} -c {container} --previous",
                f"{pod_dir}/{container}.previous.log",
            )

        init_containers = _sh(
            f"kubectl get pod {pod} -n {ns} -o jsonpath='{{.spec.initContainers[*].name}}'",
            check=False,
        )
        for container in init_containers.split():
            _dump_cmd(
                f"kubectl logs {pod} -n {ns} -c {container}",
                f"{pod_dir}/init-{container}.log",
            )

    print(f"Debug dumps written to {debug_dir}")
    return debug_dir


def _dump_cmd(cmd: str, path: str):
    """Run a command and write its output to a file."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    with open(path, "w") as f:
        f.write(result.stdout)
        if result.stderr:
            f.write("\n--- stderr ---\n")
            f.write(result.stderr)
    if os.path.getsize(path) == 0:
        os.remove(path)


# =============================================================================
# Docker image builder
# =============================================================================


def base_image():
    """Return a flyte.Image with all generic tools installed (no cloud CLIs)."""
    import flyte

    return (
        flyte.Image.from_debian_base()
        .with_apt_packages(
            "curl", "ca-certificates", "git", "jq", "unzip", "gnupg", "lsb-release",
        )
        .with_pip_packages("cryptography")
        .with_commands([
            # Helm
            f"curl -fsSL https://get.helm.sh/helm-v{_HELM_VERSION}-linux-amd64.tar.gz"
            f" | tar xz -C /tmp && mv /tmp/linux-amd64/helm /usr/local/bin/ && rm -rf /tmp/linux-amd64",
            # kubectl
            f"curl -fsSLo /usr/local/bin/kubectl"
            f" https://dl.k8s.io/release/v{_KUBECTL_VERSION}/bin/linux/amd64/kubectl"
            f" && chmod +x /usr/local/bin/kubectl",
            # yq
            f"curl -fsSLo /usr/local/bin/yq"
            f" https://github.com/mikefarah/yq/releases/download/v{_YQ_VERSION}/yq_linux_amd64"
            f" && chmod +x /usr/local/bin/yq",
            # uctl
            f"curl -fsSL https://github.com/unionai/uctl/releases/download/v{_UCTL_VERSION}/uctl_Linux_x86_64.tar.gz"
            f" | tar xz -C /usr/local/bin uctl",
            # uv (for setting up flyte SDK venv during validation)
            "curl -fsSL https://astral.sh/uv/install.sh | sh"
            " && mv /root/.local/bin/uv /usr/local/bin/",
        ])
    )


# =============================================================================
# Provisioning (Phase 1)
# =============================================================================


def provision_dataplane(cfg: BaseConfig, provider: str) -> BaseInfraState:
    """Run uctl selfserve provision-dataplane-resources.

    Returns a BaseInfraState with values_file_path set.
    Also populates cfg.org_name as a side effect.
    """
    assert cfg.control_plane_url, "control_plane_url is required"
    assert cfg.cluster_name, "cluster_name is required"

    import glob
    import tempfile

    state = BaseInfraState()

    work_dir = tempfile.mkdtemp(prefix="union-e2e-provision-")
    print(f"  Provisioning in temp dir: {work_dir}")

    # config init may open a browser for OAuth — run without capturing so it
    # can interact with the terminal.
    _sh(
        f"cd {work_dir} && uctl config init --host={cfg.control_plane_url}",
        capture=False,
    )

    output = _sh(
        f"cd {work_dir} && "
        f"uctl selfserve provision-dataplane-resources "
        f"--clusterName {cfg.cluster_name} --provider {provider}"
    )

    # Parse generated filename from "Generated <file>" line
    values_file = ""
    for line in output.splitlines():
        if "Generated" in line and ".yaml" in line:
            for word in line.split():
                if word.endswith(".yaml"):
                    values_file = os.path.join(work_dir, word)
                    break
            if values_file:
                break

    # Fallback: find any *-values.yaml in the temp dir
    if not values_file or not os.path.exists(values_file):
        candidates = glob.glob(os.path.join(work_dir, "*-values.yaml"))
        if candidates:
            values_file = candidates[0]

    if not values_file or not os.path.exists(values_file):
        raise RuntimeError(
            f"Could not find generated values file in {work_dir}. uctl output:\n{output}"
        )

    # Copy to the e2e workspace for persistence across reruns
    import shutil

    workspace = os.path.join(os.path.dirname(__file__), ".e2e-workspace")
    os.makedirs(workspace, exist_ok=True)
    dest = os.path.join(workspace, os.path.basename(values_file))
    shutil.copy2(values_file, dest)

    state.values_file_path = os.path.abspath(dest)
    print(f"Generated values file: {state.values_file_path}")

    # Parse org name from the uctl output table
    if not cfg.org_name:
        for line in output.splitlines():
            if cfg.cluster_name in line and "|" in line:
                fields = [f.strip() for f in line.split("|")]
                if len(fields) >= 3 and fields[1]:
                    cfg.org_name = fields[1]
                    print(f"  Parsed org name: {cfg.org_name}")
                    break

    return state


# =============================================================================
# Helm chart management (Phase 3)
# =============================================================================


def resolve_chart_ref(cfg: BaseConfig) -> str:
    """Clone from branch or use published repo. Returns chart ref string."""
    if cfg.helm_chart_branch:
        import tempfile as _tmpmod

        helm_clone_dir = _tmpmod.mkdtemp(prefix="union-e2e-helm-")
        _sh(
            f"git clone --depth 1 --branch {cfg.helm_chart_branch} "
            f"{cfg.helm_chart_repo} {helm_clone_dir}"
        )
        chart_ref = f"{helm_clone_dir}/{cfg.helm_chart_path}"
        _sh(f"helm dependency update {chart_ref}", check=False)
    else:
        _sh("helm repo add unionai https://unionai.github.io/helm-charts/", check=False)
        _sh("helm repo update")
        chart_ref = "unionai/dataplane"
    return chart_ref


def helm_install(cfg: BaseConfig, values_file: str, chart_ref: str) -> None:
    """Run helm upgrade --install and create EAGER_API_KEY."""
    _sh(
        f"helm upgrade --install {cfg.helm_release_name} {chart_ref} "
        f'-f "{values_file}" '
        f"-n {cfg.helm_namespace} --create-namespace --wait --timeout 10m"
    )
    print("Helm chart installed.")

    org_flag = f"--org {cfg.org_name}" if cfg.org_name else ""
    _sh(
        f"uctl create apikey --keyName EAGER_API_KEY {org_flag}",
        check=False,
    )
    print("EAGER_API_KEY created/propagated.")


def helm_uninstall(cfg: BaseConfig) -> list[str]:
    """Uninstall Helm release. Returns list of errors (empty = success)."""
    errors: list[str] = []
    if _sh_ok(f"helm status {cfg.helm_release_name} -n {cfg.helm_namespace}"):
        print(f"Uninstalling Helm release {cfg.helm_release_name}...")
        if not _sh_ok(
            f"helm uninstall {cfg.helm_release_name} -n {cfg.helm_namespace} --wait --timeout 5m"
        ):
            errors.append("Helm uninstall failed")
    return errors


# =============================================================================
# Project and cluster pool routing
# =============================================================================


def create_test_project_and_route(cfg: BaseConfig) -> None:
    """Create a Union project for this cluster and route it via cluster-pool-attributes.

    The project name matches the cluster name so reruns are idempotent.
    This ensures test executions land on the specific cluster we just deployed.
    """
    import tempfile

    org_flag = f"--org {cfg.org_name}" if cfg.org_name else ""
    pool_name = cfg.cluster_name  # one pool per cluster, named after it

    # 1. Create a cluster pool (idempotent)
    cp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False, prefix="clusterpool-",
    )
    cp_file.write(
        f"clusterPool:\n"
        f"  id:\n"
        f"    name: {pool_name}\n"
    )
    cp_file.close()
    _sh(
        f"uctl create clusterpool --clusterPoolSpecFile {cp_file.name} {org_flag}",
        check=False,  # may already exist
    )
    os.unlink(cp_file.name)
    print(f"Cluster pool '{pool_name}' created/verified.")

    # Assign this cluster to the pool
    _sh(
        f"uctl create clusterpoolassignment "
        f"--poolName {pool_name} --clusterName {cfg.cluster_name} {org_flag}",
        check=False,  # may already be assigned
    )
    print(f"Cluster '{cfg.cluster_name}' assigned to pool '{pool_name}'.")

    # 2. Create project (idempotent — uctl returns success if it already exists)
    _sh(
        f"uctl create project "
        f"--name {cfg.test_project} "
        f"--id {cfg.test_project} "
        f'--description "E2E test project for cluster {cfg.cluster_name}" '
        f"{org_flag}",
        check=False,
    )
    print(f"Project '{cfg.test_project}' created/verified.")

    # 3. Route the project to the cluster pool for all domains
    for domain in ["development", "staging", "production"]:
        attr_file = tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False, prefix=f"cpa-{domain}-",
        )
        attr_file.write(
            f"domain: {domain}\n"
            f"project: {cfg.test_project}\n"
            f"clusterPoolName: {pool_name}\n"
        )
        attr_file.close()
        _sh(
            f"uctl update cluster-pool-attributes --force --attrFile {attr_file.name} {org_flag}",
            check=False,
        )
        os.unlink(attr_file.name)
    print(f"Cluster pool attributes set: {cfg.test_project} -> {pool_name}")


# =============================================================================
# Verification (Phase 4) — fully cloud-agnostic
# =============================================================================


def wait_for_healthy(cfg: BaseConfig) -> bool:
    """Poll uctl get cluster until the cluster is ENABLED and HEALTHY."""
    deadline = time.time() + cfg.cluster_healthy_timeout

    while time.time() < deadline:
        output = _sh("uctl get cluster", check=False)
        for line in output.splitlines():
            if cfg.cluster_name not in line:
                continue
            fields = [f.strip() for f in line.split("|")]
            if len(fields) >= 5:
                state_val = fields[3]
                health_val = fields[4]
                if state_val == "STATE_ENABLED" and health_val == "HEALTHY":
                    print(f"Cluster {cfg.cluster_name} is ENABLED and HEALTHY.")
                    return True
                print(f"  state={state_val} health={health_val}, waiting...")
        time.sleep(15)

    raise RuntimeError(
        f"Cluster {cfg.cluster_name} did not become healthy within {cfg.cluster_healthy_timeout}s"
    )


def run_example_workflow(cfg: BaseConfig) -> str:
    """Run the hello.py example from flyte-sdk and verify it succeeds.

    Returns the run name on success.
    """
    workspace = os.path.join(os.path.dirname(__file__), ".e2e-workspace")
    os.makedirs(workspace, exist_ok=True)

    sdk_dir = os.path.join(workspace, "flyte-sdk")
    if os.path.isdir(sdk_dir):
        print("flyte-sdk already cloned, pulling latest...")
        _sh(f"cd {sdk_dir} && git pull --ff-only", check=False)
    else:
        _sh(
            f"git clone --depth 1 --filter=blob:none --sparse "
            f"https://github.com/flyteorg/flyte-sdk.git {sdk_dir}"
        )
        _sh(f"cd {sdk_dir} && git sparse-checkout set examples")

    example = os.path.join(sdk_dir, "examples", "basics", "hello.py")
    if not os.path.exists(example):
        raise RuntimeError(f"Example not found: {example}")

    print(f"Running example: {example}")
    run_result = subprocess.run(
        f"cd {workspace} && flyte run "
        f"--project {cfg.test_project} "
        f"--domain development "
        f"--follow "
        f"{example} main",
        shell=True,
        capture_output=True,
        text=True,
    )

    print(run_result.stdout)
    if run_result.stderr:
        print(run_result.stderr)

    # flyte run --follow may exit 0 even when the workflow fails (it successfully
    # streamed the failure). Check both the exit code and the output for failure.
    combined = (run_result.stdout or "") + (run_result.stderr or "")
    import re as _re
    ansi_clean = _re.sub(r"\x1b\[[0-9;]*m", "", combined)
    failure_indicators = [
        "FAILED",
        "exited unsuccessfully",
        "Traceback (most recent call last)",
        "Filtered traceback (most recent call last)",
        "RuntimeError:",
        "TypeError:",
        "ActionPhase.FAILED",
    ]
    workflow_failed = any(ind in ansi_clean for ind in failure_indicators)

    if run_result.returncode != 0 or workflow_failed:
        print(f"WARNING: flyte run exited with code {run_result.returncode} (workflow_failed={workflow_failed})")
        raise RuntimeError(
            f"Example workflow failed (exit code {run_result.returncode}).\n"
            f"stdout: {run_result.stdout[-500:] if run_result.stdout else '(empty)'}\n"
            f"stderr: {run_result.stderr[-500:] if run_result.stderr else '(empty)'}"
        )

    # Parse run name from output: "Created Run: <name>"
    # Strip ANSI escape codes first — flyte CLI uses rich formatting
    import re

    ansi_clean = re.sub(r"\x1b\[[0-9;]*m", "", combined)
    run_name = ""
    match = re.search(r"Created Run:\s+([a-z0-9]+)", ansi_clean)
    if match:
        run_name = match.group(1)
    print(f"Example workflow SUCCEEDED (run: {run_name})")
    return run_name


def _detect_org_name(cfg: BaseConfig) -> str:
    """Detect org name from uctl get cluster output."""
    output = _sh("uctl get cluster", check=False)
    for line in output.splitlines():
        if cfg.cluster_name in line and "|" in line:
            fields = [f.strip() for f in line.split("|")]
            if len(fields) >= 3 and fields[2]:
                cfg.org_name = fields[2]
                return fields[2]
    return ""


@dataclass
class TestResult:
    """Tracks the result of a single verification test."""
    name: str
    passed: bool = False
    error: str = ""


def run_verification_tests(cfg: BaseConfig, run_name: str) -> list[TestResult]:
    """Run all post-workflow verification tests and return results."""
    tests = [
        ("Live & Persistent Logs", verify_logs),
        ("Inputs/Outputs", verify_io),
        ("Code Bundle Download & CORS", verify_code_bundle_cors),
        ("Remote Image Builder", verify_image_builder),
        ("Image Cache (No Rebuild)", verify_image_cache),
        ("Reusable Containers", verify_reusable_containers),
    ]
    results: list[TestResult] = []
    for test_name, test_fn in tests:
        result = TestResult(name=test_name)
        try:
            test_fn(cfg, run_name)
            result.passed = True
        except Exception as e:
            result.error = str(e)[:200]
            print(f"  TEST FAILED: {test_name}: {result.error}")
        results.append(result)

    # Print summary table
    print("\n" + "=" * 70)
    print(f"  {'Test':<40} {'Result':<10} {'Error'}")
    print("-" * 70)
    for r in results:
        status = "PASSED" if r.passed else "FAILED"
        error_msg = "" if r.passed else r.error[:60]
        print(f"  {r.name:<40} {status:<10} {error_msg}")
    print("=" * 70)

    passed = sum(1 for r in results if r.passed)
    total = len(results)
    print(f"  {passed}/{total} tests passed\n")

    failed = [r for r in results if not r.passed]
    if failed:
        raise RuntimeError(
            f"{len(failed)}/{total} verification tests failed: "
            + ", ".join(r.name for r in failed)
        )

    return results


# =============================================================================
# Post-run verification tests
# =============================================================================


def _wait_for_run_metadata(cfg: BaseConfig, run_name: str, domain: str = "development") -> None:
    """Wait until the control plane has indexed the run's metadata (actions, logs, etc.)."""
    cmd = f"flyte get logs {run_name} --project {cfg.test_project} --domain {domain}"
    for attempt in range(2):
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        combined = (result.stdout or "") + (result.stderr or "")
        if result.returncode == 0 and "NOT FOUND" not in combined and "NOT_FOUND" not in combined:
            print(f"  Run metadata ready (attempt {attempt + 1})")
            return
        wait = 5 * (attempt + 1)
        print(f"  Run metadata not ready yet, waiting {wait}s (attempt {attempt + 1}/6)...")
        time.sleep(wait)
    # Don't fail here — let the caller decide


def verify_logs(cfg: BaseConfig, run_name: str) -> None:
    """Live & Persistent Logs test: get logs, delete pods, get logs again."""
    print(f"\n--- Test: Live & Persistent Logs (run={run_name}) ---")
    domain = "development"

    # Wait for run metadata to be available
    _wait_for_run_metadata(cfg, run_name, domain)

    # 1. Get logs while pods are still around
    print("Getting logs (live)...")
    output1 = _sh(
        f"flyte get logs {run_name} --project {cfg.test_project} --domain {domain}",
        check=False,
    )
    if not output1.strip() or "NOT FOUND" in output1 or "NOT_FOUND" in output1:
        raise RuntimeError(f"No logs returned for run {run_name} (live)")
    print("  Live logs: OK")

    # 2. Delete the pods for this run
    print("Deleting run pods...")
    pods = _sh(
        f"kubectl get pods -n {cfg.test_project}-{domain} "
        f"-l execution-id={run_name} --no-headers -o custom-columns=NAME:.metadata.name",
        check=False,
    )
    for pod in pods.strip().splitlines():
        pod = pod.strip()
        if pod:
            _sh(f"kubectl delete pod {pod} -n {cfg.test_project}-{domain} --wait=false", check=False)
    # Wait for pods to be gone
    time.sleep(10)

    # 3. Get logs again — should still work (persistent logs via fluentbit/S3)
    print("Getting logs (persistent, after pod deletion)...")
    output2 = _sh(
        f"flyte get logs {run_name} --project {cfg.test_project} --domain {domain}",
        check=False,
    )
    if not output2.strip():
        raise RuntimeError(f"No logs returned for run {run_name} after pod deletion (persistent logs missing)")
    print("  Persistent logs: OK")
    print("--- Live & Persistent Logs: PASSED ---")


def verify_io(cfg: BaseConfig, run_name: str) -> None:
    """Inputs/Outputs test: verify flyte get io returns data."""
    print(f"\n--- Test: Inputs/Outputs (run={run_name}) ---")
    domain = "development"

    output = _sh(
        f"flyte get io {run_name} --project {cfg.test_project} --domain {domain}",
        check=False,
    )
    if not output.strip():
        raise RuntimeError(f"No I/O data returned for run {run_name}")
    print(f"  I/O data returned ({len(output)} chars)")
    print("--- Inputs/Outputs: PASSED ---")


def verify_code_bundle_cors(cfg: BaseConfig, run_name: str) -> None:
    """Code bundle download & CORS test.

    1. Get an access token from keyring
    2. POST to CreateDownloadLinkV2 to get a presigned URL for the code bundle
    3. Verify the presigned URL is downloadable and has correct CORS headers
    """
    import re
    import urllib.parse
    import urllib.request

    print(f"\n--- Test: Code Bundle Download & CORS (run={run_name}) ---")
    domain = "development"

    # 1. Get access token from keyring
    try:
        import keyring
    except ImportError:
        _sh("pip install keyring", check=False)
        import keyring

    cp_host = cfg.control_plane_url.replace("https://", "").replace("http://", "").rstrip("/")
    token = keyring.get_password(cp_host, "access_token")
    if not token:
        raise RuntimeError(
            f"No access token found in keyring for '{cp_host}'. "
            "Run 'flyte config init' or 'uctl config init' to authenticate."
        )
    print(f"  Access token: found ({len(token)} chars)")

    # 2. Get the first task action name for this run
    action_name = "a0"

    # 3. POST to CreateDownloadLinkV2
    cp_base = cfg.control_plane_url.rstrip("/")
    url = f"{cp_base}/cloudidl.clouddataproxy.CloudDataProxyService/CreateDownloadLinkV2"
    body = json.dumps({
        "artifactType": "ARTIFACT_TYPE_CODE_BUNDLE",
        "actionAttemptId": {
            "actionId": {
                "run": {
                    "org": cfg.org_name or _detect_org_name(cfg),
                    "project": cfg.test_project,
                    "domain": domain,
                    "name": run_name,
                },
                "name": action_name,
            },
            "attempt": 1,
        },
    })

    req = urllib.request.Request(
        url,
        data=body.encode(),
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
            f"CreateDownloadLinkV2 failed ({e.code}): {e.read().decode()[:500]}"
        )

    signed_urls = resp_body.get("preSignedUrls", {}).get("signedUrl", [])
    if not signed_urls:
        raise RuntimeError(f"No presigned URLs returned: {json.dumps(resp_body)[:500]}")
    signed_url = signed_urls[0]
    print(f"  Presigned URL obtained ({len(signed_url)} chars)")

    # 4. HEAD request with Origin header to verify CORS
    cors_origin = cp_base
    print(f"  Using cors_origin ({cp_base})")
    head_req = urllib.request.Request(
        signed_url,
        headers={
            "Origin": cors_origin,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Content-Type,Authorization"
        },
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(head_req) as resp:
            cors_header = resp.getheader("Access-Control-Allow-Origin", "")
            content_length = resp.getheader("Content-Length", "0")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HEAD on presigned URL failed ({e.code})")

    print(f"  HEAD response: Content-Length={content_length}, CORS={cors_header}")
    if not cors_header:
        raise RuntimeError(
            f"No Access-Control-Allow-Origin header on presigned URL. "
            f"CORS may not be configured on the storage bucket."
        )
    print(f"  CORS header: {cors_header} — OK")

    # 5. GET to verify the file is actually downloadable
    get_req = urllib.request.Request(signed_url, method="GET")
    try:
        with urllib.request.urlopen(get_req) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GET on presigned URL failed ({e.code})")
    print(f"  Downloaded code bundle: {len(data)} bytes")
    if len(data) == 0:
        raise RuntimeError("Code bundle is empty")

    print("--- Code Bundle Download & CORS: PASSED ---")


# =============================================================================
# Image builder & reusable container tests
# =============================================================================


def _run_flyte_script(cfg: BaseConfig, script_path: str, entrypoint: str = "main") -> str:
    """Run a flyte script remotely and return the run name. Raises on failure."""
    import re

    result = subprocess.run(
        f"flyte run "
        f"--project {cfg.test_project} "
        f"--domain development "
        f"--follow "
        f"{script_path} {entrypoint}",
        shell=True,
        capture_output=True,
        text=True,
    )
    combined = (result.stdout or "") + (result.stderr or "")
    print(combined[:5000])

    ansi_clean = re.sub(r"\x1b\[[0-9;]*m", "", combined)
    # flyte run --follow exits 0 even on workflow failure. Detect failures from output.
    failure_indicators = [
        "FAILED",
        "exited unsuccessfully",
        "Traceback (most recent call last)",
        "Filtered traceback (most recent call last)",
        "RuntimeError:",
        "TypeError:",
        "ActionPhase.FAILED",
    ]
    workflow_failed = any(ind in ansi_clean for ind in failure_indicators)

    if result.returncode != 0 or workflow_failed:
        raise RuntimeError(f"Script failed (exit {result.returncode}):\n{ansi_clean[-500:]}")

    match = re.search(r"Created Run:\s+([a-z0-9]+)", ansi_clean)
    return match.group(1) if match else ""


def verify_image_builder(cfg: BaseConfig, _run_name: str) -> None:
    """Remote Image Builder test: trigger a fresh image build by including a unique file."""
    print("\n--- Test: Remote Image Builder ---")
    import uuid

    # Use a path without dots — Python treats dotted dirs as relative imports
    workspace = os.path.join(os.path.dirname(__file__), "e2e_workspace", "image_builder_test")
    os.makedirs(workspace, exist_ok=True)

    # Write a file with a random string so the image hash changes every run
    unique_marker = str(uuid.uuid4())
    marker_file = os.path.join(workspace, "build_marker.txt")
    with open(marker_file, "w") as f:
        f.write(unique_marker)

    # Write the test script
    script_path = os.path.join(workspace, "image_build_test.py")
    with open(script_path, "w") as f:
        f.write(f'''\
from pathlib import Path
import flyte

image = (
    flyte.Image.from_debian_base()
    .with_pip_packages("requests")
    .with_source_file(Path("{marker_file}"))
)

env = flyte.TaskEnvironment(name="image-builder-e2e", image=image)

@env.task
async def main() -> str:
    marker = Path("build_marker.txt").read_text()
    return f"Built with marker: {{marker}}"
''')

    print(f"  Marker: {unique_marker}")
    print("  Running with unique source file (should trigger image build)...")
    run_name = _run_flyte_script(cfg, script_path)

    if not run_name:
        raise RuntimeError("Could not parse run name from image builder test")
    print(f"  Image build test run: {run_name}")
    print("--- Remote Image Builder: PASSED ---")


def verify_image_cache(cfg: BaseConfig, _run_name: str) -> None:
    """Image Cache test: run the same image twice, second should skip build."""
    print("\n--- Test: Image Cache (No Rebuild) ---")

    workspace = os.path.join(os.path.dirname(__file__), "e2e_workspace", "image_cache_test")
    os.makedirs(workspace, exist_ok=True)

    # Write a deterministic script (no random marker = same hash every time)
    script_path = os.path.join(workspace, "image_cache_test.py")
    with open(script_path, "w") as f:
        f.write('''\
import flyte

image = flyte.Image.from_debian_base().with_pip_packages("requests==2.32.3")

env = flyte.TaskEnvironment(name="image-cache-e2e", image=image)

@env.task
async def main() -> str:
    import requests
    return f"requests version: {requests.__version__}"
''')

    # First run — may or may not build
    print("  Run 1 (may build)...")
    run1 = _run_flyte_script(cfg, script_path)
    print(f"  Run 1 completed: {run1}")

    # Second run — should detect existing image and skip build
    print("  Run 2 (should skip build)...")
    result2 = subprocess.run(
        f"flyte run "
        f"--project {cfg.test_project} "
        f"--domain development "
        f"--follow "
        f"{script_path} main",
        shell=True,
        capture_output=True,
        text=True,
    )
    import re

    combined2 = (result2.stdout or "") + (result2.stderr or "")
    ansi_clean2 = re.sub(r"\x1b\[[0-9;]*m", "", combined2)
    print(combined2[:2000])

    # Check that the second run skipped the build
    if "already exists, skipping build" in ansi_clean2:
        print("  Image cache hit confirmed: 'already exists, skipping build'")
    elif "Building" not in ansi_clean2:
        print("  No build step detected (image was cached)")
    else:
        print("  WARNING: Second run may have rebuilt the image (check output above)")

    workflow_failed = "FAILED" in ansi_clean2 or "exited unsuccessfully" in ansi_clean2
    if result2.returncode != 0 or workflow_failed:
        raise RuntimeError(f"Second run failed (exit {result2.returncode})")

    print("--- Image Cache (No Rebuild): PASSED ---")


def verify_reusable_containers(cfg: BaseConfig, _run_name: str) -> None:
    """Reusable Containers test: run the reusable example from flyte-sdk."""
    print("\n--- Test: Reusable Containers ---")

    workspace = os.path.join(os.path.dirname(__file__), ".e2e-workspace")
    sdk_dir = os.path.join(workspace, "flyte-sdk")
    reuse_src = os.path.join(sdk_dir, "examples", "reuse", "reusable.py")

    if not os.path.exists(reuse_src):
        _sh(f"cd {sdk_dir} && git sparse-checkout add examples/reuse", check=False)

    if not os.path.exists(reuse_src):
        raise RuntimeError(f"Reusable example not found: {reuse_src}")

    # Copy to a clean path without dots to avoid Python import issues
    import shutil

    clean_dir = os.path.join(os.path.dirname(__file__), "e2e_workspace", "reuse_test")
    os.makedirs(clean_dir, exist_ok=True)
    clean_path = os.path.join(clean_dir, "reusable.py")
    shutil.copy2(reuse_src, clean_path)

    print(f"  Running: {clean_path}")
    run_name = _run_flyte_script(cfg, clean_path, entrypoint="main --n 5")

    if not run_name:
        raise RuntimeError("Could not parse run name from reusable containers test")
    print(f"  Reusable containers run: {run_name}")
    print("--- Reusable Containers: PASSED ---")


# =============================================================================
# Key setup helper
# =============================================================================


def setup_keys_impl() -> str:
    """Generate RSA key pair and push private key as a Flyte secret."""
    import flyte
    import flyte.remote as remote

    _generate_key_pair()

    print(f"\nPushing private key as Flyte secret '{_FLYTE_SECRET_NAME}'...")
    flyte.init_from_config()
    remote.Secret.create(
        name=_FLYTE_SECRET_NAME,
        value=_PRIVATE_KEY_PATH.read_bytes(),
        type="regular",
    )
    print(f"Secret '{_FLYTE_SECRET_NAME}' created.")

    return f"Key pair in {_KEYS_DIR}/, secret '{_FLYTE_SECRET_NAME}' created."
