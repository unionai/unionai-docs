# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "cryptography>=46.0.6",
# ]
# ///
"""
Selfmanaged GCP E2E Test — as a Flyte 2 workflow.

Sets up GCP infrastructure (GKE, GCS, Artifact Registry, Workload Identity),
deploys the Union dataplane Helm chart, verifies the cluster is healthy,
runs example workflows, and tears down.

Usage (local — uses your local gcloud/uctl credentials):
  flyte run --local selfmanaged_gcp_e2e.py e2e_test \\
    --control_plane_url https://myorg.union.ai \\
    --cluster_name my-test-cluster

Usage (remote — credentials encrypted with RSA envelope):
  flyte run --local selfmanaged_gcp_e2e.py setup_keys
  flyte run --local selfmanaged_gcp_e2e.py launch \\
    --control_plane_url https://myorg.union.ai \\
    --cluster_name my-test-cluster

  # Individual phases (local):
  flyte run --local selfmanaged_gcp_e2e.py setup_infra ...
  flyte run --local selfmanaged_gcp_e2e.py verify ...
"""

from __future__ import annotations

import json
import logging
import os
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

import flyte

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-7s %(name)s - %(message)s")
logger = logging.getLogger("flyte.e2e.gcp")

from selfmanaged_common import (
    BaseConfig,
    BaseInfraState,
    _FLYTE_SECRET_NAME,
    _sh,
    _sh_ok,
    base_image,
    collect_debug_dumps,
    create_test_project_and_route,
    decrypt_and_export_credentials,
    encrypt_env_vars,
    helm_install,
    helm_uninstall,
    provision_dataplane,
    resolve_chart_ref,
    E2EResult,
    run_example_workflow,
    setup_keys_impl,
    run_verification_tests,
    wait_for_healthy,
)


# =============================================================================
# Configuration
# =============================================================================


@dataclass
class Config(BaseConfig):
    """GCP-specific knobs for the E2E test."""

    # Matches docs: PROJECT_ID, REGION
    project_id: str = ""  # auto-detected if empty
    region: str = "us-central1"

    # GKE — docs: CLUSTER_NAME, machine-type, num-nodes
    machine_type: str = "e2-standard-4"
    num_nodes: int = 1

    # Derived names (computed in __post_init__)
    # Docs: CLUSTER_NAME, BUCKET_PREFIX, AR_REPOSITORY, GSA_NAME
    cluster_name_gke: str = ""   # the actual GKE cluster name
    bucket_prefix: str = ""
    ar_repository: str = ""
    gsa_name: str = ""

    def __post_init__(self):
        super().__post_init__()
        if not self.project_id:
            self.project_id = _sh(
                "gcloud config get-value project"
            ).strip()

        cn = self.cluster_name
        if not self.cluster_name_gke:
            self.cluster_name_gke = f"union-e2e-{cn}"
        if not self.bucket_prefix:
            self.bucket_prefix = f"union-e2e-{cn}"
        if not self.ar_repository:
            self.ar_repository = f"union-e2e-{cn}"
        if not self.gsa_name:
            self.gsa_name = f"union-e2e-{cn}"


@dataclass
class InfraState(BaseInfraState):
    """Tracks what GCP resources were created so teardown knows what to clean up."""

    gke_created: bool = False
    gcs_metadata_created: bool = False
    gcs_fast_reg_created: bool = False
    ar_created: bool = False
    gsa_created: bool = False
    gsa_email: str = ""


# =============================================================================
# Task environment
# =============================================================================

_image = base_image().with_commands([
    # gcloud CLI via official apt repo
    "echo 'deb [signed-by=/usr/share/keyrings/cloud.google.asc] https://packages.cloud.google.com/apt cloud-sdk main'"
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
    secrets=flyte.Secret(key=_FLYTE_SECRET_NAME, mount=Path("/etc/flyte/secrets")),
)


# =============================================================================
# Credential encryption (GCP-specific)
# =============================================================================


def _encrypt_local_credentials() -> str:
    """Read GCP credentials from local env, encrypt with public key, return JSON."""
    env_vars = {
        "UNION_API_KEY": os.environ.get("UNION_API_KEY", ""),
    }

    # Read the ADC JSON file (from gcloud auth application-default login)
    gcp_creds_path = os.environ.get(
        "GOOGLE_APPLICATION_CREDENTIALS",
        os.path.expanduser("~/.config/gcloud/application_default_credentials.json"),
    )
    if os.path.exists(gcp_creds_path):
        with open(gcp_creds_path) as f:
            env_vars["GCP_SERVICE_ACCOUNT_KEY_JSON"] = f.read()
    else:
        raise RuntimeError(
            f"No GCP credentials found at {gcp_creds_path}. "
            "Set GOOGLE_APPLICATION_CREDENTIALS or run 'gcloud auth application-default login'"
        )

    return encrypt_env_vars(
        env_vars,
        required=["GCP_SERVICE_ACCOUNT_KEY_JSON"],
    )


def _activate_gcp_credentials(cfg: Config) -> None:
    """After decryption, write the key JSON to a file and activate it."""
    decrypt_and_export_credentials(cfg.encrypted_credentials)
    key_json = os.environ.get("GCP_SERVICE_ACCOUNT_KEY_JSON")
    if key_json:
        key_path = "/tmp/gcp-sa-key.json"
        with open(key_path, "w") as f:
            f.write(key_json)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
        _sh(f"gcloud auth activate-service-account --key-file={key_path}")
        _sh(f"gcloud config set project {cfg.project_id}")


# =============================================================================
# Phase 2: Infrastructure Setup
# =============================================================================


_GCS_CORS_CONFIG = json.dumps([
    {
        "origin": ["https://*.unionai.cloud", "https://*.union.ai"],
        "method": ["HEAD", "GET"],
        "responseHeader": ["ETag"],
        "maxAgeSeconds": 3600,
    }
])


@env.task
def create_gke_cluster(cfg: Config, state: InfraState) -> InfraState:
    """Create a GKE cluster with Workload Identity enabled."""
    # Enable required APIs
    _sh(f"gcloud services enable container.googleapis.com --project {cfg.project_id}", check=False)

    if _sh_ok(
        f"gcloud container clusters describe {cfg.cluster_name_gke} "
        f"--region {cfg.region} --project {cfg.project_id}"
    ):
        logger.info(f"GKE cluster {cfg.cluster_name_gke} already exists, skipping.")
    else:
        _sh(
            f"gcloud container clusters create {cfg.cluster_name_gke} "
            f"--project {cfg.project_id} "
            f"--region {cfg.region} "
            f"--release-channel regular "
            f"--machine-type {cfg.machine_type} "
            f"--num-nodes {cfg.num_nodes} "
            f"--workload-pool {cfg.project_id}.svc.id.goog"
        )
        # Add a buildkit node pool for Image Builder (needs 4 CPUs, 50Gi ephemeral)
        _sh(
            f"gcloud container node-pools create buildkit-pool "
            f"--cluster {cfg.cluster_name_gke} "
            f"--region {cfg.region} "
            f"--project {cfg.project_id} "
            f"--machine-type e2-standard-8 "
            f"--disk-size 200GB "
            f"--num-nodes 1 "
            f"--enable-autoscaling --min-nodes 1 --max-nodes 2"
        )
        state.gke_created = True

    # Always update kubeconfig
    _sh(
        f"gcloud container clusters get-credentials {cfg.cluster_name_gke} "
        f"--region {cfg.region} --project {cfg.project_id}"
    )
    return state


@env.task
def create_gcs_buckets(cfg: Config, state: InfraState) -> InfraState:
    """Create GCS metadata and fast-registration buckets with CORS."""
    for bucket, attr in [
        (f"{cfg.bucket_prefix}-metadata", "gcs_metadata_created"),
        (f"{cfg.bucket_prefix}-fast-reg", "gcs_fast_reg_created"),
    ]:
        if _sh_ok(f"gcloud storage buckets describe gs://{bucket} --project {cfg.project_id}"):
            logger.info(f"Bucket gs://{bucket} already exists, skipping creation.")
        else:
            _sh(
                f"gcloud storage buckets create gs://{bucket} "
                f"--project {cfg.project_id} "
                f"--location {cfg.region}"
            )
            setattr(state, attr, True)

        # Apply CORS policy
        cors_file = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        cors_file.write(_GCS_CORS_CONFIG)
        cors_file.close()
        _sh(f"gcloud storage buckets update gs://{bucket} --cors-file={cors_file.name}")
        os.unlink(cors_file.name)
        logger.info(f"  Bucket ready (with CORS): gs://{bucket}")
    return state


@env.task
def create_ar_repo(cfg: Config, state: InfraState) -> InfraState:
    """Create an Artifact Registry Docker repository for Image Builder."""
    if _sh_ok(
        f"gcloud artifacts repositories describe {cfg.ar_repository} "
        f"--project {cfg.project_id} --location {cfg.region}"
    ):
        logger.info(f"Artifact Registry repo {cfg.ar_repository} already exists, skipping.")
    else:
        _sh(
            f"gcloud artifacts repositories create {cfg.ar_repository} "
            f"--project {cfg.project_id} "
            f"--location {cfg.region} "
            f"--repository-format docker "
            f'--description "Union Image Builder repository"'
        )
        state.ar_created = True
    return state


@env.task
def create_workload_identity(cfg: Config, state: InfraState) -> InfraState:
    """Create GSA, bind to KSA, grant GCS/AR/token-creator access."""
    gsa_email = f"{cfg.gsa_name}@{cfg.project_id}.iam.gserviceaccount.com"
    state.gsa_email = gsa_email

    # 1. Create GSA
    if _sh_ok(
        f"gcloud iam service-accounts describe {gsa_email} --project {cfg.project_id}"
    ):
        logger.info(f"GSA {gsa_email} already exists, skipping creation.")
    else:
        _sh(
            f"gcloud iam service-accounts create {cfg.gsa_name} "
            f"--project {cfg.project_id} "
            f'--display-name "Union data plane service account"'
        )
        state.gsa_created = True

    member = f"serviceAccount:{gsa_email}"

    # 2. Bind KSA to GSA (both union-system and union service accounts)
    for ksa in ["union-system", "union"]:
        wi_member = f"serviceAccount:{cfg.project_id}.svc.id.goog[{cfg.helm_namespace}/{ksa}]"
        _sh(
            f"gcloud iam service-accounts add-iam-policy-binding {gsa_email} "
            f"--project {cfg.project_id} "
            f"--role roles/iam.workloadIdentityUser "
            f'--member "{wi_member}"',
            check=False,
        )

    # 3. Grant GCS access (objectAdmin + legacyBucketReader on each bucket)
    for bucket in [f"{cfg.bucket_prefix}-metadata", f"{cfg.bucket_prefix}-fast-reg"]:
        for role in ["roles/storage.objectAdmin", "roles/storage.legacyBucketReader"]:
            _sh(
                f"gcloud storage buckets add-iam-policy-binding gs://{bucket} "
                f"--member {member} --role {role}",
                check=False,
            )

    # 4. Grant Artifact Registry access
    _sh(
        f"gcloud artifacts repositories add-iam-policy-binding {cfg.ar_repository} "
        f"--project {cfg.project_id} "
        f"--location {cfg.region} "
        f"--member {member} "
        f"--role roles/artifactregistry.writer",
        check=False,
    )

    # 5. Grant token creator access (required for Image Builder)
    _sh(
        f"gcloud projects add-iam-policy-binding {cfg.project_id} "
        f"--member {member} "
        f"--role roles/iam.serviceAccountTokenCreator",
        check=False,
    )

    logger.info(f"Workload Identity ready: {gsa_email}")
    return state


# =============================================================================
# Phase 3: Dataplane Deployment
# =============================================================================


@env.task
def patch_and_install(cfg: Config, state: InfraState) -> InfraState:
    """Patch the generated values file and install the Helm chart."""
    f = state.values_file_path
    assert os.path.exists(f), f"Values file not found: {f}"

    metadata_bucket = f"{cfg.bucket_prefix}-metadata"
    fast_reg_bucket = f"{cfg.bucket_prefix}-fast-reg"

    # Global values
    _sh(f'yq -i \'.global.METADATA_BUCKET = "{metadata_bucket}"\' "{f}"')
    _sh(f'yq -i \'.global.FAST_REGISTRATION_BUCKET = "{fast_reg_bucket}"\' "{f}"')
    _sh(f'yq -i \'.global.BACKEND_IAM_ROLE_ARN = "{state.gsa_email}"\' "{f}"')
    _sh(f'yq -i \'.global.WORKER_IAM_ROLE_ARN = "{state.gsa_email}"\' "{f}"')

    # Storage — also set directly since the uctl-generated values file may override
    # the chart templates with hardcoded placeholders
    _sh(f'yq -i \'.storage.bucketName = "{metadata_bucket}"\' "{f}"')
    _sh(f'yq -i \'.storage.fastRegistrationBucketName = "{fast_reg_bucket}"\' "{f}"')
    _sh(f'yq -i \'.storage.region = "{cfg.region}"\' "{f}"')
    _sh(f'yq -i \'.storage.gcp.projectId = "{cfg.project_id}"\' "{f}"')

    # Replace any remaining placeholders from uctl-generated values
    _sh(f"sed -i.bak 's|<GCP_BUCKET_NAME>|{metadata_bucket}|g' \"{f}\"")
    _sh(f"sed -i.bak 's|<GCP_SERVICE_ACCOUNT>|{state.gsa_email}|g' \"{f}\"")
    _sh(f"sed -i.bak 's|<UNION_FLYTE_ROLE_ARN>|{state.gsa_email}|g' \"{f}\"")
    _sh(f'rm -f "{f}.bak"')

    # Service account annotation
    _sh(
        f'yq -i \'.commonServiceAccount.annotations."iam.gke.io/gcp-service-account" = '
        f'"{state.gsa_email}"\' "{f}"'
    )

    # Image Builder — Artifact Registry repo name
    _sh(f'yq -i \'.imageBuilder.registryName = "{cfg.ar_repository}"\' "{f}"')

    logger.info(f"Values file patched: {f}")
    logger.info(f"  global.METADATA_BUCKET = {metadata_bucket}")
    logger.info(f"  global.FAST_REGISTRATION_BUCKET = {fast_reg_bucket}")
    logger.info(f"  global.BACKEND_IAM_ROLE_ARN = {state.gsa_email}")
    logger.info(f"  storage.gcp.projectId = {cfg.project_id}")
    logger.info(f"  imageBuilder.registryName = {cfg.ar_repository}")

    chart_ref = resolve_chart_ref(cfg)
    helm_install(cfg, f, chart_ref)

    # Create a dedicated project and route it to this cluster
    create_test_project_and_route(cfg)
    return state


# =============================================================================
# Teardown
# =============================================================================


@env.task
def teardown(cfg: Config, state: InfraState) -> str:
    """Tear down all created resources in reverse order."""
    gsa_email = state.gsa_email or f"{cfg.gsa_name}@{cfg.project_id}.iam.gserviceaccount.com"

    logger.info("\n--- Teardown state ---")
    logger.info(f"  gke_created:          {state.gke_created}  (cluster: {cfg.cluster_name_gke})")
    metadata_bucket = f"{cfg.bucket_prefix}-metadata"
    fast_reg_bucket = f"{cfg.bucket_prefix}-fast-reg"
    logger.info(f"  gcs_metadata_created: {state.gcs_metadata_created}  (bucket: {metadata_bucket})")
    logger.info(f"  gcs_fast_reg_created: {state.gcs_fast_reg_created}  (bucket: {fast_reg_bucket})")
    logger.info(f"  ar_created:           {state.ar_created}  (repo: {cfg.ar_repository})")
    logger.info(f"  gsa_created:          {state.gsa_created}  (gsa: {gsa_email})")
    logger.info(f"  helm_release:         {cfg.helm_release_name} (ns: {cfg.helm_namespace})")
    logger.info(f"  skip_teardown:        {cfg.skip_teardown}")
    logger.info("---")

    if cfg.skip_teardown:
        logger.info("skip_teardown=True — leaving all resources in place.")
        return "skipped"

    errors = helm_uninstall(cfg)
    member = f"serviceAccount:{gsa_email}"

    # Remove project-level IAM bindings
    _sh(
        f"gcloud projects remove-iam-policy-binding {cfg.project_id} "
        f"--member {member} --role roles/iam.serviceAccountTokenCreator",
        check=False,
    )

    # Remove bucket IAM bindings
    for bucket in [f"{cfg.bucket_prefix}-metadata", f"{cfg.bucket_prefix}-fast-reg"]:
        for role in ["roles/storage.objectAdmin", "roles/storage.legacyBucketReader"]:
            _sh(
                f"gcloud storage buckets remove-iam-policy-binding gs://{bucket} "
                f"--member {member} --role {role}",
                check=False,
            )

    # Remove AR IAM binding
    _sh(
        f"gcloud artifacts repositories remove-iam-policy-binding {cfg.ar_repository} "
        f"--project {cfg.project_id} --location {cfg.region} "
        f"--member {member} --role roles/artifactregistry.writer",
        check=False,
    )

    # Delete GSA
    if _sh_ok(f"gcloud iam service-accounts describe {gsa_email} --project {cfg.project_id}"):
        logger.info(f"Deleting GSA {gsa_email}...")
        _sh(f"gcloud iam service-accounts delete {gsa_email} --project {cfg.project_id} --quiet", check=False)

    # Delete AR repo
    if _sh_ok(
        f"gcloud artifacts repositories describe {cfg.ar_repository} "
        f"--project {cfg.project_id} --location {cfg.region}"
    ):
        logger.info(f"Deleting Artifact Registry repo {cfg.ar_repository}...")
        _sh(
            f"gcloud artifacts repositories delete {cfg.ar_repository} "
            f"--project {cfg.project_id} --location {cfg.region} --quiet",
            check=False,
        )

    # Delete GCS buckets
    for bucket in [f"{cfg.bucket_prefix}-metadata", f"{cfg.bucket_prefix}-fast-reg"]:
        if _sh_ok(f"gcloud storage buckets describe gs://{bucket} --project {cfg.project_id}"):
            logger.info(f"Deleting GCS bucket gs://{bucket}...")
            _sh(f"gcloud storage rm -r gs://{bucket}", check=False)
        else:
            logger.info(f"GCS bucket gs://{bucket} not found, skipping.")

    # Delete GKE cluster
    if _sh_ok(
        f"gcloud container clusters describe {cfg.cluster_name_gke} "
        f"--region {cfg.region} --project {cfg.project_id}"
    ):
        logger.info(f"Deleting GKE cluster {cfg.cluster_name_gke} (takes ~5-10 min)...")
        _sh(
            f"gcloud container clusters delete {cfg.cluster_name_gke} "
            f"--project {cfg.project_id} --region {cfg.region} --quiet",
            check=False,
        )
    else:
        logger.info(f"GKE cluster {cfg.cluster_name_gke} not found, skipping.")

    if errors:
        return f"teardown completed with errors: {'; '.join(errors)}"
    return "teardown complete"


# =============================================================================
# Composable entry points
# =============================================================================


@env.task
def setup_infra(
    control_plane_url: str = "",
    cluster_name: str = "",
    project_id: str = "",
    region: str = "us-central1",
    skip_teardown: bool = True,
    encrypted_credentials: str = "",
) -> InfraState:
    """Phase 1+2: Provision credentials and create GCP infra."""
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
        skip_teardown=skip_teardown,
        encrypted_credentials=encrypted_credentials,
    )
    _activate_gcp_credentials(cfg)
    base_state = provision_dataplane(cfg, provider="gcp")
    state = InfraState(values_file_path=base_state.values_file_path)
    state = create_gke_cluster(cfg, state)
    state = create_gcs_buckets(cfg, state)
    state = create_ar_repo(cfg, state)
    state = create_workload_identity(cfg, state)
    return state


@env.task
def deploy(
    control_plane_url: str = "",
    cluster_name: str = "",
    project_id: str = "",
    region: str = "us-central1",
    encrypted_credentials: str = "",
) -> InfraState:
    """Phase 1+2+3: Provision, create infra, and deploy Helm chart."""
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
        encrypted_credentials=encrypted_credentials,
    )
    _activate_gcp_credentials(cfg)
    state = setup_infra(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
    )
    state = patch_and_install(cfg, state)
    return state


@env.task
def verify(
    control_plane_url: str = "",
    cluster_name: str = "",
    encrypted_credentials: str = "",
) -> bool:
    """Phase 4 only: Verify an already-deployed cluster."""
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        encrypted_credentials=encrypted_credentials,
    )
    _activate_gcp_credentials(cfg)
    wait_for_healthy(cfg)
    run_name = run_example_workflow(cfg)
    if run_name:
        run_verification_tests(cfg, run_name)
    return True


@env.task
def e2e_test(
    control_plane_url: str = "",
    cluster_name: str = "",
    project_id: str = "",
    region: str = "us-central1",
    skip_teardown: bool = False,
    encrypted_credentials: str = "",
    helm_values_override: str = "",
    dataplane_image_sha: str = "",
) -> E2EResult:
    """Full E2E: setup, deploy, verify, teardown.

    Pass helm_values_override="values-legacy.yaml" to test with legacy defaults.
    Pass dataplane_image_sha=<sha> to override the dataplane image tag.
    """
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
        skip_teardown=skip_teardown,
        encrypted_credentials=encrypted_credentials,
        helm_values_override=helm_values_override,
        dataplane_image_sha=dataplane_image_sha,
    )
    _activate_gcp_credentials(cfg)

    debug_dir = os.path.join(
        os.path.dirname(__file__),
        ".debug",
        time.strftime("%Y%m%d-%H%M%S"),
    )

    e2e = E2EResult()
    state = InfraState(debug_dir=debug_dir)
    try:
        logger.info("\n--- Phase 1: Interactive / Credential Setup ---")
        base_state = provision_dataplane(cfg, provider="gcp")
        state.values_file_path = base_state.values_file_path
        state.debug_dir = debug_dir

        logger.info("\n--- Phase 2: Infrastructure Setup ---")
        state = create_gke_cluster(cfg, state)
        state = create_gcs_buckets(cfg, state)
        state = create_ar_repo(cfg, state)
        state = create_workload_identity(cfg, state)

        logger.info("\n--- Phase 3: Dataplane Deployment ---")
        state = patch_and_install(cfg, state)

        logger.info("\n--- Phase 4: Verification ---")
        wait_for_healthy(cfg)
        e2e.example_run_name = run_example_workflow(cfg)
        if e2e.example_run_name:
            e2e.test_results = run_verification_tests(cfg, e2e.example_run_name)

        e2e.overall = "PASSED"
        logger.info("\n=== E2E test PASSED ===")

    except Exception as e:
        logger.info(f"\n=== E2E test FAILED: {e} ===")
        collect_debug_dumps(cfg, debug_dir)
        e2e.overall = "FAILED"
        e2e.error = str(e)[:500]
        if not cfg.skip_teardown:
            teardown(cfg, state)
        raise

    e2e.teardown_result = teardown(cfg, state)
    logger.info(e2e.summary())
    return e2e


# =============================================================================
# Key setup and remote launch — run these locally
# =============================================================================

_local_env = flyte.TaskEnvironment(name="e2e-local")


@_local_env.task
def setup_keys() -> str:
    """Generate RSA key pair and push private key as a Flyte secret."""
    return setup_keys_impl()


@_local_env.task
def launch(
    control_plane_url: str = "",
    cluster_name: str = "",
    project_id: str = "",
    region: str = "us-central1",
    skip_teardown: bool = False,
    dataplane_image_sha: str = "",
) -> str:
    """Encrypt local credentials and launch e2e_test remotely."""
    logger.info("Encrypting local credentials...")
    encrypted = _encrypt_local_credentials()

    flyte.init_from_config()
    run = flyte.run(
        e2e_test,
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        project_id=project_id,
        region=region,
        skip_teardown=skip_teardown,
        encrypted_credentials=encrypted,
        dataplane_image_sha=dataplane_image_sha,
    )
    logger.info(f"Launched remote run: {run.name}")
    logger.info(f"  URL: {run.url}")
    return run.url

