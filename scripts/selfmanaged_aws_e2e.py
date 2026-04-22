# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "cryptography>=46.0.6",
# ]
# ///
"""
Selfmanaged AWS E2E Test — as a Flyte 2 workflow.

Sets up AWS infrastructure, deploys the Union dataplane Helm chart,
verifies the cluster is healthy, runs example workflows, and tears down.

Usage (local — uses your local AWS/uctl credentials):
  flyte run --local selfmanaged_aws_e2e.py e2e_test \\
    --control_plane_url https://myorg.union.ai \\
    --cluster_name my-test-cluster

Usage (remote — credentials encrypted with RSA envelope):
  # One-time: generate RSA key pair and push private key as a Flyte secret.
  flyte run --local selfmanaged_aws_e2e.py setup_keys

  # Launch remotely. Reads AWS creds + UNION_API_KEY from your local env,
  # encrypts with the public key, passes as a task argument.
  flyte run --local selfmanaged_aws_e2e.py launch \\
    --control_plane_url https://myorg.union.ai \\
    --cluster_name my-test-cluster

  # Individual phases (local):
  flyte run --local selfmanaged_aws_e2e.py setup_infra ...
  flyte run --local selfmanaged_aws_e2e.py verify ...
  flyte run --local selfmanaged_aws_e2e.py teardown ...
"""

from __future__ import annotations

import json
import logging
import os
import time
from dataclasses import dataclass
from pathlib import Path

import flyte

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-7s %(name)s - %(message)s")
logger = logging.getLogger("flyte.e2e.aws")

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

_EKSCTL_VERSION = "0.204.0"


@dataclass
class Config(BaseConfig):
    """AWS-specific knobs for the E2E test."""

    # AWS
    aws_region: str = "us-east-2"
    aws_account_id: str = ""  # auto-detected if empty

    # EKS
    eks_k8s_version: str = "1.31"
    eks_node_type: str = "m5.2xlarge"
    eks_node_count: int = 3

    # Derived names (computed in __post_init__)
    eks_cluster_name: str = ""
    s3_metadata_bucket: str = ""
    s3_fast_reg_bucket: str = ""
    ecr_repo_name: str = ""
    iam_role_name: str = ""
    iam_s3_policy_name: str = ""
    iam_ecr_policy_name: str = ""

    def __post_init__(self):
        super().__post_init__()
        if not self.aws_account_id:
            self.aws_account_id = _sh(
                "aws sts get-caller-identity --query Account --output text"
            ).strip()

        cn = self.cluster_name
        if not self.eks_cluster_name:
            self.eks_cluster_name = f"union-e2e-{cn}"
        if not self.s3_metadata_bucket:
            self.s3_metadata_bucket = f"union-e2e-{cn}-metadata"
        if not self.s3_fast_reg_bucket:
            self.s3_fast_reg_bucket = f"union-e2e-{cn}-fast-reg"
        if not self.ecr_repo_name:
            self.ecr_repo_name = f"union-e2e-{cn}/imagebuilder"
        if not self.iam_role_name:
            self.iam_role_name = f"union-e2e-{cn}-system-role"
        if not self.iam_s3_policy_name:
            self.iam_s3_policy_name = f"union-e2e-{cn}-s3-access"
        if not self.iam_ecr_policy_name:
            self.iam_ecr_policy_name = f"union-e2e-{cn}-ecr-access"


@dataclass
class InfraState(BaseInfraState):
    """Tracks what AWS resources were created so teardown knows what to clean up."""

    eks_created: bool = False
    s3_metadata_created: bool = False
    s3_fast_reg_created: bool = False
    ecr_created: bool = False
    iam_role_created: bool = False
    iam_role_arn: str = ""


# =============================================================================
# Task environment
# =============================================================================

_image = base_image().with_commands([
    # AWS CLI v2
    "curl -fsSL https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o /tmp/awscli.zip"
    " && unzip -q /tmp/awscli.zip -d /tmp && /tmp/aws/install && rm -rf /tmp/aws /tmp/awscli.zip",
    # eksctl
    f"curl -fsSL https://github.com/eksctl-io/eksctl/releases/download/v{_EKSCTL_VERSION}/eksctl_Linux_amd64.tar.gz"
    f" | tar xz -C /usr/local/bin",
])

env = flyte.TaskEnvironment(
    name="selfmanaged-aws-e2e",
    image=_image,
    resources=flyte.Resources(cpu="2", memory="2Gi"),
    secrets=flyte.Secret(key=_FLYTE_SECRET_NAME, mount=Path("/etc/flyte/secrets")),
)


# =============================================================================
# Credential encryption (AWS-specific env vars)
# =============================================================================


def _encrypt_local_credentials() -> str:
    """Read AWS credentials from local env, encrypt with public key, return JSON."""
    env_vars = {
        "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
        "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
        "AWS_SESSION_TOKEN": os.environ.get("AWS_SESSION_TOKEN", ""),
        "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", os.environ.get("AWS_REGION", "")),
        "UNION_API_KEY": os.environ.get("UNION_API_KEY", ""),
    }
    return encrypt_env_vars(
        env_vars,
        required=["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"],
    )


# =============================================================================
# Phase 2: Infrastructure Setup
# =============================================================================


_S3_CORS_CONFIG = json.dumps({
    "CORSRules": [
        {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "HEAD"],
            "AllowedOrigins": ["https://*.unionai.cloud", "https://*.union.ai"],
            "ExposeHeaders": ["ETag"],
            "MaxAgeSeconds": 3600,
        }
    ]
})


@env.task
def create_eks_cluster(cfg: Config, state: InfraState) -> InfraState:
    """Create an EKS cluster with OIDC provider."""
    if _sh_ok(
        f"aws eks describe-cluster --name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    ):
        logger.info(f"EKS cluster {cfg.eks_cluster_name} already exists, waiting for it to be active...")
    else:
        _sh(
            f"eksctl create cluster "
            f"--name {cfg.eks_cluster_name} "
            f"--region {cfg.aws_region} "
            f"--version {cfg.eks_k8s_version} "
            f"--node-type {cfg.eks_node_type} "
            f"--nodes {cfg.eks_node_count} "
            f"--with-oidc --managed"
        )
        state.eks_created = True

    # Wait for cluster to be ACTIVE (handles CREATING state from interrupted runs)
    _sh(
        f"aws eks wait cluster-active "
        f"--name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    )

    state.eks_created = True

    # Always update kubeconfig
    _sh(
        f"aws eks update-kubeconfig "
        f"--name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    )
    return state


@env.task
def create_s3_buckets(cfg: Config, state: InfraState) -> InfraState:
    """Create S3 metadata and fast-registration buckets with CORS for Code Viewer."""
    for bucket, attr in [
        (cfg.s3_metadata_bucket, "s3_metadata_created"),
        (cfg.s3_fast_reg_bucket, "s3_fast_reg_created"),
    ]:
        if _sh_ok(f"aws s3api head-bucket --bucket {bucket}"):
            logger.info(f"Bucket {bucket} already exists, skipping creation.")
        else:
            loc = (
                ""
                if cfg.aws_region == "us-east-1"
                else f"--create-bucket-configuration LocationConstraint={cfg.aws_region}"
            )
            _sh(
                f"aws s3api create-bucket --bucket {bucket} "
                f"--region {cfg.aws_region} {loc}"
            )
            setattr(state, attr, True)

        _sh(
            f"aws s3api put-bucket-cors --bucket {bucket} "
            f"--cors-configuration '{_S3_CORS_CONFIG}'"
        )
        logger.info(f"  Bucket ready (with CORS): {bucket}")
    return state


@env.task
def create_ecr_repo(cfg: Config, state: InfraState) -> InfraState:
    """Create an ECR private repository for Image Builder."""
    if _sh_ok(
        f"aws ecr describe-repositories --repository-names {cfg.ecr_repo_name} "
        f"--region {cfg.aws_region}"
    ):
        logger.info(f"ECR repo {cfg.ecr_repo_name} already exists, skipping.")
    else:
        _sh(
            f"aws ecr create-repository --repository-name {cfg.ecr_repo_name} "
            f"--region {cfg.aws_region} --image-scanning-configuration scanOnPush=true"
        )
        state.ecr_created = True
    return state


@env.task
def create_iam_role(cfg: Config, state: InfraState) -> InfraState:
    """Create IAM role with IRSA trust policy, S3 and ECR policies."""
    role_arn = f"arn:aws:iam::{cfg.aws_account_id}:role/{cfg.iam_role_name}"

    oidc_url = _sh(
        f"aws eks describe-cluster --region {cfg.aws_region} "
        f"--name {cfg.eks_cluster_name} "
        f'--query "cluster.identity.oidc.issuer" --output text'
    ).strip()
    oidc_provider = oidc_url.removeprefix("https://")

    trust_policy = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Federated": f"arn:aws:iam::{cfg.aws_account_id}:oidc-provider/{oidc_provider}"
                    },
                    "Action": "sts:AssumeRoleWithWebIdentity",
                    "Condition": {
                        "StringEquals": {
                            f"{oidc_provider}:aud": "sts.amazonaws.com",
                        },
                        "StringLike": {
                            f"{oidc_provider}:sub": "system:serviceaccount:*",
                        },
                    },
                }
            ],
        }
    )

    if _sh_ok(f"aws iam get-role --role-name {cfg.iam_role_name}"):
        logger.info(f"IAM role {cfg.iam_role_name} already exists, updating trust policy...")
        _sh(
            f"aws iam update-assume-role-policy --role-name {cfg.iam_role_name} "
            f"--policy-document '{trust_policy}'"
        )
    else:
        _sh(
            f"aws iam create-role --role-name {cfg.iam_role_name} "
            f"--assume-role-policy-document '{trust_policy}'"
        )
        state.iam_role_created = True

    state.iam_role_arn = role_arn

    s3_policy = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "S3BucketAccess",
                    "Effect": "Allow",
                    "Action": ["s3:DeleteObject*", "s3:GetObject*", "s3:ListBucket", "s3:PutObject*"],
                    "Resource": [
                        f"arn:aws:s3:::{cfg.s3_metadata_bucket}",
                        f"arn:aws:s3:::{cfg.s3_metadata_bucket}/*",
                        f"arn:aws:s3:::{cfg.s3_fast_reg_bucket}",
                        f"arn:aws:s3:::{cfg.s3_fast_reg_bucket}/*",
                    ],
                }
            ],
        }
    )
    _ensure_policy_attached(cfg.iam_role_name, cfg.iam_s3_policy_name, s3_policy, cfg.aws_account_id)

    ecr_policy = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "ECRAuth",
                    "Effect": "Allow",
                    "Action": ["ecr:GetAuthorizationToken"],
                    "Resource": "*",
                },
                {
                    "Sid": "ECRReadWrite",
                    "Effect": "Allow",
                    "Action": [
                        "ecr:BatchCheckLayerAvailability",
                        "ecr:BatchGetImage",
                        "ecr:GetDownloadUrlForLayer",
                        "ecr:DescribeImages",
                        "ecr:PutImage",
                        "ecr:InitiateLayerUpload",
                        "ecr:UploadLayerPart",
                        "ecr:CompleteLayerUpload",
                    ],
                    "Resource": f"arn:aws:ecr:{cfg.aws_region}:{cfg.aws_account_id}:repository/{cfg.ecr_repo_name}",
                },
            ],
        }
    )
    _ensure_policy_attached(cfg.iam_role_name, cfg.iam_ecr_policy_name, ecr_policy, cfg.aws_account_id)

    logger.info(f"IAM role ready: {role_arn}")
    return state


def _ensure_policy_attached(role_name: str, policy_name: str, policy_doc: str, account_id: str):
    """Create IAM policy if needed and attach to role (idempotent)."""
    policy_arn = f"arn:aws:iam::{account_id}:policy/{policy_name}"
    if not _sh_ok(f"aws iam get-policy --policy-arn {policy_arn}"):
        _sh(
            f"aws iam create-policy --policy-name {policy_name} "
            f"--policy-document '{policy_doc}'"
        )
    _sh(f"aws iam attach-role-policy --role-name {role_name} --policy-arn {policy_arn}", check=False)


# =============================================================================
# Phase 3: Dataplane Deployment
# =============================================================================


@env.task
def patch_and_install(cfg: Config, state: InfraState) -> InfraState:
    """Patch the generated values file and install the Helm chart."""
    # Materialize the YAML content carried in state to a local temp file so
    # yq and helm can operate on it. This is what lets this task run in a
    # different container than provision_dataplane.
    assert state.values_file_content, "state.values_file_content is empty"

    import tempfile

    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False, prefix="union-e2e-values-",
    )
    tmp.write(state.values_file_content)
    tmp.close()
    f = tmp.name
    logger.info(f"  Wrote values file: {f}")

    # AWS-specific yq patches
    # Global values
    _sh(f'yq -i \'.global.AWS_ACCOUNT_ID = "{cfg.aws_account_id}"\' "{f}"')
    _sh(f'yq -i \'.global.METADATA_BUCKET = "{cfg.s3_metadata_bucket}"\' "{f}"')
    _sh(f'yq -i \'.global.FAST_REGISTRATION_BUCKET = "{cfg.s3_fast_reg_bucket}"\' "{f}"')
    _sh(f'yq -i \'.global.BACKEND_IAM_ROLE_ARN = "{state.iam_role_arn}"\' "{f}"')
    _sh(f'yq -i \'.global.WORKER_IAM_ROLE_ARN = "{state.iam_role_arn}"\' "{f}"')

    # Storage — also set directly since the uctl-generated values file may override
    # the chart templates with hardcoded placeholders
    _sh(f'yq -i \'.storage.bucketName = "{cfg.s3_metadata_bucket}"\' "{f}"')
    _sh(f'yq -i \'.storage.fastRegistrationBucketName = "{cfg.s3_fast_reg_bucket}"\' "{f}"')
    _sh(f'yq -i \'.storage.region = "{cfg.aws_region}"\' "{f}"')

    # Replace any remaining placeholders from uctl-generated values
    _sh(f"sed -i.bak 's|<UNION_FLYTE_ROLE_ARN>|{state.iam_role_arn}|g' \"{f}\"")
    _sh(f'rm -f "{f}.bak"')

    # Service account annotation
    _sh(
        f'yq -i \'.commonServiceAccount.annotations."eks.amazonaws.com/role-arn" = '
        f'"{state.iam_role_arn}"\' "{f}"'
    )

    # Image Builder — ECR repo name
    _sh(f'yq -i \'.imageBuilder.registryName = "{cfg.ecr_repo_name}"\' "{f}"')

    logger.info(f"Values file patched: {f}")
    logger.info(f"  global.METADATA_BUCKET = {cfg.s3_metadata_bucket}")
    logger.info(f"  global.FAST_REGISTRATION_BUCKET = {cfg.s3_fast_reg_bucket}")
    logger.info(f"  global.BACKEND_IAM_ROLE_ARN = {state.iam_role_arn}")
    logger.info(f"  storage.region = {cfg.aws_region}")
    logger.info(f"  imageBuilder.registryName = {cfg.ecr_repo_name}")

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
    logger.info("\n--- Teardown state ---")
    logger.info(f"  eks_created:          {state.eks_created}  (cluster: {cfg.eks_cluster_name})")
    logger.info(f"  s3_metadata_created:  {state.s3_metadata_created}  (bucket: {cfg.s3_metadata_bucket})")
    logger.info(f"  s3_fast_reg_created:  {state.s3_fast_reg_created}  (bucket: {cfg.s3_fast_reg_bucket})")
    logger.info(f"  ecr_created:          {state.ecr_created}  (repo: {cfg.ecr_repo_name})")
    logger.info(f"  iam_role_created:     {state.iam_role_created}  (role: {cfg.iam_role_name})")
    logger.info(f"  iam_role_arn:         {state.iam_role_arn}")
    logger.info(f"  helm_release:         {cfg.helm_release_name} (ns: {cfg.helm_namespace})")
    logger.info(f"  values_file_content:  {len(state.values_file_content)} chars")
    logger.info(f"  skip_teardown:        {cfg.skip_teardown}")
    logger.info("---")

    if cfg.skip_teardown:
        logger.info("skip_teardown=True — leaving all resources in place.")
        return "skipped"

    errors = helm_uninstall(cfg)

    # IAM cleanup
    if _sh_ok(f"aws iam get-role --role-name {cfg.iam_role_name}"):
        logger.info(f"Cleaning up IAM role {cfg.iam_role_name}...")

        policies_output = _sh(
            f"aws iam list-attached-role-policies --role-name {cfg.iam_role_name} "
            f"--query 'AttachedPolicies[].PolicyArn' --output text",
            check=False,
        )
        for arn in policies_output.split():
            _sh(f"aws iam detach-role-policy --role-name {cfg.iam_role_name} --policy-arn {arn}", check=False)

        inline_output = _sh(
            f"aws iam list-role-policies --role-name {cfg.iam_role_name} "
            f"--query 'PolicyNames[]' --output text",
            check=False,
        )
        for name in inline_output.split():
            _sh(f"aws iam delete-role-policy --role-name {cfg.iam_role_name} --policy-name {name}", check=False)

        _sh(f"aws iam delete-role --role-name {cfg.iam_role_name}", check=False)

        for policy_name in [cfg.iam_s3_policy_name, cfg.iam_ecr_policy_name]:
            policy_arn = f"arn:aws:iam::{cfg.aws_account_id}:policy/{policy_name}"
            _sh(f"aws iam delete-policy --policy-arn {policy_arn}", check=False)

    # ECR
    if _sh_ok(
        f"aws ecr describe-repositories --repository-names {cfg.ecr_repo_name} "
        f"--region {cfg.aws_region}"
    ):
        logger.info(f"Deleting ECR repository {cfg.ecr_repo_name}...")
        _sh(
            f"aws ecr delete-repository --repository-name {cfg.ecr_repo_name} "
            f"--region {cfg.aws_region} --force",
            check=False,
        )
    else:
        logger.info(f"ECR repo {cfg.ecr_repo_name} not found, skipping.")

    # S3
    for bucket in [cfg.s3_metadata_bucket, cfg.s3_fast_reg_bucket]:
        if _sh_ok(f"aws s3api head-bucket --bucket {bucket}"):
            logger.info(f"Deleting S3 bucket {bucket}...")
            _sh(f"aws s3 rb s3://{bucket} --force --region {cfg.aws_region}", check=False)
        else:
            logger.info(f"S3 bucket {bucket} not found, skipping.")

    # EKS cluster
    if _sh_ok(
        f"aws eks describe-cluster --name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    ):
        logger.info(f"Deleting EKS cluster {cfg.eks_cluster_name} (takes ~10-15 min)...")
        _sh(
            f"eksctl delete cluster --name {cfg.eks_cluster_name} "
            f"--region {cfg.aws_region} --wait",
            check=False,
        )
    else:
        logger.info(f"EKS cluster {cfg.eks_cluster_name} not found, skipping.")

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
    aws_region: str = "us-east-2",
    skip_teardown: bool = True,
    encrypted_credentials: str = "",
) -> InfraState:
    """Phase 1+2: Provision credentials and create AWS infra. Does NOT tear down."""
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
        skip_teardown=skip_teardown,
        encrypted_credentials=encrypted_credentials,
    )
    decrypt_and_export_credentials(cfg.encrypted_credentials)
    base_state = provision_dataplane(cfg, provider="aws")
    state = InfraState(values_file_content=base_state.values_file_content)
    state = create_eks_cluster(cfg, state)
    state = create_s3_buckets(cfg, state)
    state = create_ecr_repo(cfg, state)
    state = create_iam_role(cfg, state)
    return state


@env.task
def deploy(
    control_plane_url: str = "",
    cluster_name: str = "",
    aws_region: str = "us-east-2",
    encrypted_credentials: str = "",
) -> InfraState:
    """Phase 1+2+3: Provision, create infra, and deploy Helm chart."""
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
        encrypted_credentials=encrypted_credentials,
    )
    decrypt_and_export_credentials(cfg.encrypted_credentials)
    state = setup_infra(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
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
    decrypt_and_export_credentials(cfg.encrypted_credentials)
    wait_for_healthy(cfg)
    run_name = run_example_workflow(cfg)
    if run_name:
        run_verification_tests(cfg, run_name)
    return True


@env.task
def e2e_test(
    control_plane_url: str = "",
    cluster_name: str = "",
    aws_region: str = "us-east-2",
    skip_teardown: bool = False,
    encrypted_credentials: str = "",
    helm_values_override: str = "",
) -> E2EResult:
    """Full E2E: setup, deploy, verify, teardown.

    Pass helm_values_override="values-legacy.yaml" to test with legacy defaults.
    """
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
        skip_teardown=skip_teardown,
        encrypted_credentials=encrypted_credentials,
        helm_values_override=helm_values_override,
    )
    decrypt_and_export_credentials(cfg.encrypted_credentials)

    debug_dir = os.path.join(
        os.path.dirname(__file__),
        ".debug",
        time.strftime("%Y%m%d-%H%M%S"),
    )

    e2e = E2EResult()
    state = InfraState(debug_dir=debug_dir)
    try:
        logger.info("\n--- Phase 1: Interactive / Credential Setup ---")
        base_state = provision_dataplane(cfg, provider="aws")
        state.values_file_content = base_state.values_file_content
        state.debug_dir = debug_dir

        logger.info("\n--- Phase 2: Infrastructure Setup ---")
        state = create_eks_cluster(cfg, state)
        state = create_s3_buckets(cfg, state)
        state = create_ecr_repo(cfg, state)
        state = create_iam_role(cfg, state)

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
    aws_region: str = "us-east-2",
    skip_teardown: bool = False,
) -> str:
    """Encrypt local credentials and launch e2e_test remotely."""
    logger.info("Encrypting local credentials...")
    encrypted = _encrypt_local_credentials()

    flyte.init_from_config()
    run = flyte.run(
        e2e_test,
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
        skip_teardown=skip_teardown,
        encrypted_credentials=encrypted,
    )
    logger.info(f"Launched remote run: {run.name}")
    logger.info(f"  URL: {run.url}")
    return run.url
