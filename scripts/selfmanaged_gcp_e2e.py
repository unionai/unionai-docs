"""
Selfmanaged GCP E2E test — Flyte 2 function style.

Local sign-off run (requires `gcloud auth application-default login` and
`UNION_API_KEY` in the shell):
    flyte run --local selfmanaged_gcp_e2e.py main \\
      --control_plane_url https://myorg.union.ai \\
      --cluster_name my-test-cluster --project_id my-gcp-project \\
      --skip_teardown True

Remote-run credential stashing for GCP is a follow-up (the shared
``stash_credentials`` / ``hydrate_credentials`` path in ``selfmanaged_common``
only carries AWS STS creds today). Run locally until that lands.
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from dataclasses import dataclass, field

import flyte

from selfmanaged_common import (
    E2E_CREDS_ENV_VAR,
    E2E_CREDS_SECRET_KEY,
    BaseConfig,
    DataplaneValues,
    E2EResult,
    HelmRelease,
    TestResult,
    base_image,
    bootstrap_env,
    cluster_wait_healthy,
    collect_debug_dumps,
    create_eager_api_key,
    create_test_project_and_route,
    helm_install,
    helm_uninstall,
    init_union_client,
    provision_dataplane,
    resolve_chart_ref,
    say,
    sh,
    sh_ok,
)
from smoke_tests import run_smoke_suite

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-7s %(name)s - %(message)s",
)
logger = logging.getLogger("flyte.e2e.gcp")

# ============================================================================
# Configuration
# ============================================================================


@dataclass
class Config(BaseConfig):
    """GCP knobs + derived names. Pure data — no subprocess calls."""

    project_id: str = ""
    region: str = "us-central1"

    # GKE default pool
    gke_machine_type: str = "e2-standard-4"
    gke_num_nodes: int = 1

    # buildkit pool (Image Builder needs 4 CPU + 50Gi ephemeral per pod)
    buildkit_machine_type: str = "e2-standard-8"
    buildkit_disk_size_gb: int = 200
    buildkit_min_nodes: int = 1
    buildkit_max_nodes: int = 2

    gke_cluster_name: str = ""
    gcs_metadata_bucket: str = ""
    gcs_fast_reg_bucket: str = ""
    ar_repository: str = ""
    gsa_name: str = ""

    def __post_init__(self):
        super().__post_init__()
        cn = self.cluster_name
        if not self.gke_cluster_name:
            self.gke_cluster_name = f"union-e2e-{cn}"
        if not self.gcs_metadata_bucket:
            self.gcs_metadata_bucket = f"union-e2e-{cn}-metadata"
        if not self.gcs_fast_reg_bucket:
            self.gcs_fast_reg_bucket = f"union-e2e-{cn}-fast-reg"
        if not self.ar_repository:
            self.ar_repository = f"union-e2e-{cn}"
        if not self.gsa_name:
            self.gsa_name = f"union-e2e-{cn}"


# ============================================================================
# Per-resource outputs and the final aggregated result
# ============================================================================


@dataclass(frozen=True)
class GKECluster:
    name: str
    region: str
    project_id: str


@dataclass(frozen=True)
class GCSBucket:
    name: str
    region: str


@dataclass(frozen=True)
class ARRepo:
    name: str
    region: str
    project_id: str


@dataclass(frozen=True)
class ServiceAccount:
    name: str
    email: str
    project_id: str


@dataclass
class GCPResources:
    """Aggregated state returned by main()."""
    project_id: str = ""
    dataplane: DataplaneValues | None = None
    gke: GKECluster | None = None
    gcs_metadata: GCSBucket | None = None
    gcs_fast_reg: GCSBucket | None = None
    ar: ARRepo | None = None
    gsa: ServiceAccount | None = None
    helm: HelmRelease | None = None
    project: str = ""
    smoke_run_name: str = ""
    test_results: list[TestResult] = field(default_factory=list)


# ============================================================================
# TaskEnvironment — base image + gcloud CLI
# ============================================================================

_image = base_image().with_commands([
    # gcloud CLI via official apt repo
    "echo 'deb [signed-by=/usr/share/keyrings/cloud.google.asc] "
    "https://packages.cloud.google.com/apt cloud-sdk main'"
    " > /etc/apt/sources.list.d/google-cloud-sdk.list"
    " && curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg"
    " > /usr/share/keyrings/cloud.google.asc"
    " && apt-get update && apt-get install -y google-cloud-cli"
    " && rm -rf /var/lib/apt/lists/*",
])

env = flyte.TaskEnvironment(
    name="selfmanaged-gcp-e2e",
    image=_image,
    resources=flyte.Resources(cpu="2", memory="2Gi"),
    secrets=[flyte.Secret(key=E2E_CREDS_SECRET_KEY, as_env_var=E2E_CREDS_ENV_VAR)],
    cache="disable",
)


# ============================================================================
# Credential hydration (GCP-specific, local-only for now)
# ============================================================================


async def hydrate_gcp_credentials(cfg: Config) -> None:
    """Ensure gcloud is authenticated and `project` is set. Local-only for now.

    Local path: relies on `gcloud auth application-default login` + ambient
    UNION_API_KEY. Remote path (GCP service-account JSON in a secret) is a
    follow-up extension to selfmanaged_common.
    """
    if os.environ.get(E2E_CREDS_ENV_VAR):
        raise RuntimeError(
            "Remote GCP credential hydration is not implemented yet. "
            "Run this entrypoint locally with `gcloud auth application-default login` "
            "and UNION_API_KEY exported."
        )
    if not os.environ.get("UNION_API_KEY"):
        raise RuntimeError(
            "UNION_API_KEY is not set. Export it in the shell before running."
        )
    if cfg.project_id:
        await sh(f"gcloud config set project {cfg.project_id}", check=False)


async def resolve_project_id(cfg: Config) -> str:
    """Return cfg.project_id, falling back to ``gcloud config get-value project``."""
    if cfg.project_id:
        return cfg.project_id
    out = (await sh("gcloud config get-value project", check=False)).strip()
    if not out:
        raise RuntimeError(
            "project_id is not set and `gcloud config get-value project` is empty. "
            "Pass --project_id <id> or run `gcloud config set project <id>` first."
        )
    return out


# ============================================================================
# Phase 1 — Infrastructure (each task self-contained, returns its record)
# ============================================================================


@env.task(short_name="provision-dataplane")
async def provision_gcp_dataplane(cfg: Config) -> DataplaneValues:
    await hydrate_gcp_credentials(cfg)
    return await provision_dataplane(cfg, provider="gcp")


@env.task(short_name="create-gke", retries=1)
async def create_gke(cfg: Config) -> GKECluster:
    """Create GKE cluster + buildkit node pool (or adopt existing), update kubeconfig."""
    await hydrate_gcp_credentials(cfg)

    # Enable required APIs (idempotent).
    await sh(
        f"gcloud services enable container.googleapis.com --project {cfg.project_id}",
        check=False,
    )

    cluster_exists = await sh_ok(
        f"gcloud container clusters describe {cfg.gke_cluster_name} "
        f"--region {cfg.region} --project {cfg.project_id}"
    )
    if cluster_exists:
        say(f"create_gke: {cfg.gke_cluster_name} already exists in {cfg.region}; reusing")
    else:
        say(f"create_gke: creating {cfg.gke_cluster_name} in {cfg.region} "
            f"(machine={cfg.gke_machine_type}, nodes-per-zone={cfg.gke_num_nodes}) "
            f"— usually ~5-10 minutes")
        await sh(
            f"gcloud container clusters create {cfg.gke_cluster_name} "
            f"--project {cfg.project_id} "
            f"--region {cfg.region} "
            f"--release-channel regular "
            f"--machine-type {cfg.gke_machine_type} "
            f"--num-nodes {cfg.gke_num_nodes} "
            f"--workload-pool {cfg.project_id}.svc.id.goog"
        )

    # buildkit node pool — must exist independently of whether the cluster is
    # new. If cluster creation skipped but the pool was never created (or was
    # deleted), the Image Builder buildkit pod sits Pending forever on the
    # default pool because it requests 4 CPU + 50Gi ephemeral.
    pool_exists = await sh_ok(
        f"gcloud container node-pools describe buildkit-pool "
        f"--cluster {cfg.gke_cluster_name} "
        f"--region {cfg.region} --project {cfg.project_id}"
    )
    if not pool_exists:
        say(f"create_gke: creating buildkit-pool ({cfg.buildkit_machine_type}, "
            f"{cfg.buildkit_disk_size_gb}GB, min={cfg.buildkit_min_nodes}, "
            f"max={cfg.buildkit_max_nodes})")
        await sh(
            f"gcloud container node-pools create buildkit-pool "
            f"--cluster {cfg.gke_cluster_name} "
            f"--region {cfg.region} "
            f"--project {cfg.project_id} "
            f"--machine-type {cfg.buildkit_machine_type} "
            f"--disk-size {cfg.buildkit_disk_size_gb}GB "
            f"--num-nodes {cfg.buildkit_min_nodes} "
            f"--enable-autoscaling "
            f"--min-nodes {cfg.buildkit_min_nodes} "
            f"--max-nodes {cfg.buildkit_max_nodes}"
        )

    say(f"create_gke: updating kubeconfig for {cfg.gke_cluster_name}")
    await sh(
        f"gcloud container clusters get-credentials {cfg.gke_cluster_name} "
        f"--region {cfg.region} --project {cfg.project_id}"
    )
    return GKECluster(
        name=cfg.gke_cluster_name,
        region=cfg.region,
        project_id=cfg.project_id,
    )


_GCS_CORS_CONFIG = (
    '[{"origin":["https://*.unionai.cloud","https://*.union.ai"],'
    '"method":["HEAD","GET"],"responseHeader":["ETag"],"maxAgeSeconds":3600}]'
)


@env.task(short_name="create-gcs")
async def create_gcs_bucket(cfg: Config, bucket_name: str) -> GCSBucket:
    """Create one GCS bucket with CORS enabled."""
    await hydrate_gcp_credentials(cfg)
    exists = await sh_ok(
        f"gcloud storage buckets describe gs://{bucket_name} --project {cfg.project_id}"
    )
    if exists:
        say(f"create_gcs_bucket: {bucket_name} already exists; reusing")
    else:
        say(f"create_gcs_bucket: creating gs://{bucket_name} in {cfg.region}")
        await sh(
            f"gcloud storage buckets create gs://{bucket_name} "
            f"--project {cfg.project_id} --location {cfg.region}"
        )

    # Apply CORS via a temp file — cors config is JSON, easier than inlining.
    import tempfile
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    tmp.write(_GCS_CORS_CONFIG)
    tmp.close()
    try:
        await sh(f"gcloud storage buckets update gs://{bucket_name} --cors-file={tmp.name}")
    finally:
        os.unlink(tmp.name)
    say(f"create_gcs_bucket: {bucket_name} ready with CORS")
    return GCSBucket(name=bucket_name, region=cfg.region)


@env.task(short_name="create-ar")
async def create_ar_repo(cfg: Config) -> ARRepo:
    await hydrate_gcp_credentials(cfg)
    exists = await sh_ok(
        f"gcloud artifacts repositories describe {cfg.ar_repository} "
        f"--project {cfg.project_id} --location {cfg.region}"
    )
    if exists:
        say(f"create_ar_repo: {cfg.ar_repository} already exists; reusing")
    else:
        say(f"create_ar_repo: creating {cfg.ar_repository} in {cfg.region}")
        await sh(
            f"gcloud artifacts repositories create {cfg.ar_repository} "
            f"--project {cfg.project_id} "
            f"--location {cfg.region} "
            f"--repository-format docker "
            f'--description "Union Image Builder repository"'
        )
    say(f"create_ar_repo: {cfg.ar_repository} ready")
    return ARRepo(
        name=cfg.ar_repository, region=cfg.region, project_id=cfg.project_id,
    )


@env.task(short_name="create-workload-identity")
async def create_workload_identity(
    cfg: Config,
    gke: GKECluster,
    gcs_meta: GCSBucket,
    gcs_fast: GCSBucket,
    ar: ARRepo,
) -> ServiceAccount:
    """Create GSA, bind to KSAs, grant GCS/AR/token-creator access. Idempotent."""
    await hydrate_gcp_credentials(cfg)

    gsa_email = f"{cfg.gsa_name}@{cfg.project_id}.iam.gserviceaccount.com"
    member = f"serviceAccount:{gsa_email}"

    if await sh_ok(
        f"gcloud iam service-accounts describe {gsa_email} --project {cfg.project_id}"
    ):
        say(f"create_workload_identity: GSA {gsa_email} exists; reusing")
    else:
        say(f"create_workload_identity: creating GSA {gsa_email}")
        await sh(
            f"gcloud iam service-accounts create {cfg.gsa_name} "
            f"--project {cfg.project_id} "
            f'--display-name "Union data plane service account"'
        )

    # KSA → GSA bindings (both union-system and union service accounts use WI).
    for ksa in ("union-system", "union"):
        wi_member = (
            f"serviceAccount:{cfg.project_id}.svc.id.goog"
            f"[{cfg.helm_namespace}/{ksa}]"
        )
        await sh(
            f"gcloud iam service-accounts add-iam-policy-binding {gsa_email} "
            f"--project {cfg.project_id} "
            f"--role roles/iam.workloadIdentityUser "
            f'--member "{wi_member}"',
            check=False,
        )

    # Bucket access.
    for bucket in (gcs_meta.name, gcs_fast.name):
        for role in ("roles/storage.objectAdmin", "roles/storage.legacyBucketReader"):
            await sh(
                f"gcloud storage buckets add-iam-policy-binding gs://{bucket} "
                f"--member {member} --role {role}",
                check=False,
            )

    # Artifact Registry write.
    await sh(
        f"gcloud artifacts repositories add-iam-policy-binding {ar.name} "
        f"--project {cfg.project_id} --location {cfg.region} "
        f"--member {member} --role roles/artifactregistry.writer",
        check=False,
    )

    # Token creator (Image Builder requirement).
    await sh(
        f"gcloud projects add-iam-policy-binding {cfg.project_id} "
        f"--member {member} --role roles/iam.serviceAccountTokenCreator",
        check=False,
    )

    say(f"create_workload_identity: ready at {gsa_email}")
    return ServiceAccount(
        name=cfg.gsa_name, email=gsa_email, project_id=cfg.project_id,
    )


# ============================================================================
# Phase 2 — Patch values YAML and helm install
# ============================================================================


@flyte.trace
async def patch_values_yaml(
    yaml_text: str,
    cfg: Config,
    gsa: ServiceAccount,
    gcs_meta: GCSBucket,
    gcs_fast: GCSBucket,
    ar: ARRepo,
) -> str:
    """Apply GCP-specific overrides to the uctl-generated values YAML."""
    import yaml

    # Placeholder substitutions at text level before parsing — uctl emits some
    # of these inside scalar string values.
    yaml_text = yaml_text.replace("<GCP_BUCKET_NAME>", gcs_meta.name)
    yaml_text = yaml_text.replace("<GCP_SERVICE_ACCOUNT>", gsa.email)
    yaml_text = yaml_text.replace("<UNION_FLYTE_ROLE_ARN>", gsa.email)

    data = yaml.safe_load(yaml_text) or {}

    def _set(path: list[str], value) -> None:
        node = data
        for key in path[:-1]:
            node = node.setdefault(key, {})
            if not isinstance(node, dict):
                raise ValueError(f"yaml path conflict at {path!r}: {key} is not a dict")
        node[path[-1]] = value

    _set(["global", "METADATA_BUCKET"],          gcs_meta.name)
    _set(["global", "FAST_REGISTRATION_BUCKET"], gcs_fast.name)
    _set(["global", "BACKEND_IAM_ROLE_ARN"],     gsa.email)
    _set(["global", "WORKER_IAM_ROLE_ARN"],      gsa.email)

    _set(["storage", "bucketName"],                  gcs_meta.name)
    _set(["storage", "fastRegistrationBucketName"], gcs_fast.name)
    _set(["storage", "region"],                      cfg.region)
    _set(["storage", "gcp", "projectId"],            cfg.project_id)

    _set(
        ["commonServiceAccount", "annotations", "iam.gke.io/gcp-service-account"],
        gsa.email,
    )
    _set(["imageBuilder", "registryName"], ar.name)

    say(
        f"patch_values_yaml: applied GCP overrides "
        f"(project={cfg.project_id}, gsa={gsa.email}, region={cfg.region})"
    )
    return yaml.safe_dump(data, sort_keys=False, default_flow_style=False)


@env.task(short_name="deploy-dataplane")
async def deploy_dataplane(
    cfg: Config,
    dp: DataplaneValues,
    gsa: ServiceAccount,
    gcs_meta: GCSBucket,
    gcs_fast: GCSBucket,
    ar: ARRepo,
) -> HelmRelease:
    """Phase 2: patch values and install the helm chart. Also mints EAGER_API_KEY."""
    await hydrate_gcp_credentials(cfg)
    patched = await patch_values_yaml(dp.yaml_text, cfg, gsa, gcs_meta, gcs_fast, ar)
    chart_ref = await resolve_chart_ref(cfg)
    release = await helm_install(cfg, patched, chart_ref)
    await create_eager_api_key(cfg)
    return release


# ============================================================================
# Phase 4 — Teardown
# ============================================================================


async def teardown_gcp(cfg: Config, resources: GCPResources) -> str:
    """Reverse-order delete of everything in GCPResources. Best-effort.

    Not an ``@env.task`` — see the rationale in the AWS module's teardown.
    """
    await hydrate_gcp_credentials(cfg)

    gsa_email = (
        resources.gsa.email if resources.gsa
        else f"{cfg.gsa_name}@{cfg.project_id}.iam.gserviceaccount.com"
    )

    logger.info("\n--- Teardown ---")
    logger.info(f"  gke cluster: {cfg.gke_cluster_name}")
    logger.info(f"  gcs buckets: {cfg.gcs_metadata_bucket}, {cfg.gcs_fast_reg_bucket}")
    logger.info(f"  ar repo    : {cfg.ar_repository}")
    logger.info(f"  gsa        : {gsa_email}")

    errors = await helm_uninstall(cfg)
    member = f"serviceAccount:{gsa_email}"

    # Project-level IAM.
    await sh(
        f"gcloud projects remove-iam-policy-binding {cfg.project_id} "
        f"--member {member} --role roles/iam.serviceAccountTokenCreator",
        check=False,
    )

    # Bucket IAM bindings.
    for bucket in (cfg.gcs_metadata_bucket, cfg.gcs_fast_reg_bucket):
        for role in ("roles/storage.objectAdmin", "roles/storage.legacyBucketReader"):
            await sh(
                f"gcloud storage buckets remove-iam-policy-binding gs://{bucket} "
                f"--member {member} --role {role}",
                check=False,
            )

    # AR IAM binding.
    await sh(
        f"gcloud artifacts repositories remove-iam-policy-binding {cfg.ar_repository} "
        f"--project {cfg.project_id} --location {cfg.region} "
        f"--member {member} --role roles/artifactregistry.writer",
        check=False,
    )

    # GSA.
    if await sh_ok(
        f"gcloud iam service-accounts describe {gsa_email} --project {cfg.project_id}"
    ):
        logger.info(f"Deleting GSA {gsa_email}...")
        await sh(
            f"gcloud iam service-accounts delete {gsa_email} "
            f"--project {cfg.project_id} --quiet",
            check=False,
        )

    # AR repo.
    if await sh_ok(
        f"gcloud artifacts repositories describe {cfg.ar_repository} "
        f"--project {cfg.project_id} --location {cfg.region}"
    ):
        logger.info(f"Deleting Artifact Registry repo {cfg.ar_repository}...")
        await sh(
            f"gcloud artifacts repositories delete {cfg.ar_repository} "
            f"--project {cfg.project_id} --location {cfg.region} --quiet",
            check=False,
        )

    # GCS buckets.
    for bucket in (cfg.gcs_metadata_bucket, cfg.gcs_fast_reg_bucket):
        if await sh_ok(
            f"gcloud storage buckets describe gs://{bucket} --project {cfg.project_id}"
        ):
            logger.info(f"Deleting GCS bucket gs://{bucket}...")
            await sh(f"gcloud storage rm -r gs://{bucket}", check=False)

    # GKE cluster (longest — last).
    if await sh_ok(
        f"gcloud container clusters describe {cfg.gke_cluster_name} "
        f"--region {cfg.region} --project {cfg.project_id}"
    ):
        logger.info(f"Deleting GKE cluster {cfg.gke_cluster_name} (~5-10 min)...")
        await sh(
            f"gcloud container clusters delete {cfg.gke_cluster_name} "
            f"--project {cfg.project_id} --region {cfg.region} --quiet",
            check=False,
        )

    if errors:
        return f"teardown complete with errors: {'; '.join(errors)}"
    return "teardown complete"


@env.task(short_name="teardown-cluster", entrypoint=True, cache="disable")
async def teardown_cluster(
    control_plane_url: str,
    cluster_name: str,
    project_id: str = "",
    region: str = "us-central1",
) -> str:
    """Short-circuit entry point — invoke teardown directly."""
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
    )
    cfg.project_id = await resolve_project_id(cfg)
    resources = GCPResources(project_id=cfg.project_id)
    say(f"teardown_cluster: starting for cluster '{cluster_name}' (project={cfg.project_id})")
    result_str = await teardown_gcp(cfg, resources)
    say(f"teardown_cluster: done — {result_str}")
    return result_str


# ============================================================================
# Main orchestrator
# ============================================================================


@env.task(short_name="e2e-gcp", entrypoint=True, cache="disable")
async def main(
    control_plane_url: str,
    cluster_name: str,
    project_id: str = "",
    region: str = "us-central1",
    skip_teardown: bool = False,
    skip_smoke_tests: bool = False,
    helm_values_override: str = "",
    dataplane_image_sha: str = "",
) -> E2EResult:
    """Four phases: infra → deploy → verify → (teardown).

    Pass helm_values_override="values-legacy.yaml" to test with legacy defaults.
    Pass dataplane_image_sha=<sha> to override the dataplane image tag.

    ``skip_smoke_tests`` skips Phase 3's run_smoke_suite — useful while the
    cluster-pool-attributes permission issue is unresolved, or when you only
    want to validate the infra + deploy path.
    """
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
        skip_teardown=skip_teardown,
        helm_values_override=helm_values_override,
        dataplane_image_sha=dataplane_image_sha,
    )
    cfg.project_id = await resolve_project_id(cfg)
    await hydrate_gcp_credentials(cfg)
    await init_union_client(cfg)
    say(f"main: starting e2e for cluster '{cluster_name}' on {control_plane_url} "
        f"(project={cfg.project_id}, region={region}, skip_teardown={skip_teardown})")

    result = E2EResult()
    resources = GCPResources(project_id=cfg.project_id)
    debug_dir = os.path.join(
        os.path.dirname(__file__), ".debug", time.strftime("%Y%m%d-%H%M%S"),
    )

    try:
        # ---- Phase 1: Infrastructure (fan out) ----
        say("===== Phase 1/4: Infrastructure =====")
        with flyte.group("1-infra"):
            dp, gke, gcs_meta, gcs_fast, ar = await asyncio.gather(
                provision_gcp_dataplane(cfg),
                create_gke(cfg),
                create_gcs_bucket(cfg, cfg.gcs_metadata_bucket),
                create_gcs_bucket(cfg, cfg.gcs_fast_reg_bucket),
                create_ar_repo(cfg),
            )
            resources.dataplane = dp
            resources.gke = gke
            resources.gcs_metadata = gcs_meta
            resources.gcs_fast_reg = gcs_fast
            resources.ar = ar

            # Workload Identity depends on GKE + bucket/repo names.
            gsa = await create_workload_identity(cfg, gke, gcs_meta, gcs_fast, ar)
            resources.gsa = gsa

        # ---- Phase 2: Deploy data plane ----
        say("===== Phase 2/4: Deploy data plane =====")
        with flyte.group("2-deploy"):
            helm = await deploy_dataplane(cfg, dp, gsa, gcs_meta, gcs_fast, ar)
            resources.helm = helm

        # ---- Phase 3: Verify ----
        say("===== Phase 3/4: Verify =====")
        with flyte.group("3-verify"):
            org = await cluster_wait_healthy(cfg)
            if not org:
                org = dp.org_name
            await init_union_client(cfg, org=org)
            project = await create_test_project_and_route(cfg, org)
            resources.project = project

            if skip_smoke_tests:
                say("Phase 3: skip_smoke_tests=True — skipping run_smoke_suite")
            else:
                test_results = await run_smoke_suite(cfg, org)
                resources.test_results = test_results
                result.test_results = test_results

        failed = [r for r in result.test_results if not r.passed]
        if failed:
            result.overall = "FAILED"
            result.error = f"{len(failed)}/{len(result.test_results)} verification tests failed: " \
                           + ", ".join(r.name for r in failed)
        else:
            result.overall = "PASSED"

    except Exception as e:
        logger.info(f"\n=== E2E test FAILED: {e} ===")
        result.overall = "FAILED"
        result.error = str(e)[:500]
        try:
            await collect_debug_dumps(cfg, debug_dir)
        except Exception as de:
            logger.info(f"Debug dump failed: {de}")
    finally:
        if not cfg.skip_teardown:
            say("===== Phase 4/4: Teardown =====")
            with flyte.group("4-teardown"):
                try:
                    result.teardown_result = await teardown_gcp(cfg, resources)
                except Exception as te:
                    result.teardown_result = f"teardown failed: {te}"
                    say(result.teardown_result)
        else:
            result.teardown_result = "skipped (skip_teardown=True)"
            say("===== Phase 4/4: Teardown skipped =====")

    logger.info("\n" + result.summary())
    return result


# ============================================================================
# Remote launcher (local-side helper)
# ============================================================================


@bootstrap_env.task
async def launch_remote(
    control_plane_url: str,
    cluster_name: str,
    project_id: str = "",
    region: str = "us-central1",
    skip_teardown: bool = False,
    dataplane_image_sha: str = "",
) -> str:
    """flyte.run(main, ...) against the remote control plane.

    NOTE: remote GCP credential stashing is not implemented yet — ``main``
    raises on remote. Keep runs local until that lands.
    """
    flyte.init_from_config()
    run = flyte.run(
        main,
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
        skip_teardown=skip_teardown,
        dataplane_image_sha=dataplane_image_sha,
    )
    logger.info(f"Launched remote run: {run.name}")
    logger.info(f"  URL: {run.url}")
    return run.url
