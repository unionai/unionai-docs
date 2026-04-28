"""
Selfmanaged AWS E2E test — Flyte 2 function style.

Local sign-off run:
    flyte run --local selfmanaged_aws_e2e.py main \\
      --control_plane_url https://myorg.union.ai \\
      --cluster_name my-test-cluster --skip_teardown True

Remote run (after stashing creds once per shell):
    flyte run --local selfmanaged_common.py stash_credentials
    flyte run --local selfmanaged_aws_e2e.py launch_remote \\
      --control_plane_url https://myorg.union.ai \\
      --cluster_name my-test-cluster
"""

from __future__ import annotations

import asyncio
import json
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
    hydrate_credentials,
    init_union_client,
    provision_dataplane,
    resolve_chart_ref,
    say,
    sh,
    sh_ok,
)
from smoke_tests import run_smoke_suite

logger = logging.getLogger("flyte.e2e.aws")

# ============================================================================
# Configuration
# ============================================================================

_EKSCTL_VERSION = "0.204.0"


@dataclass
class Config(BaseConfig):
    """AWS knobs + derived names. Pure data — no subprocess calls."""

    aws_region: str = "us-east-2"
    aws_account_id: str = ""  # resolved by a task if empty

    eks_k8s_version: str = "1.31"
    eks_node_type: str = "m5.2xlarge"
    eks_node_count: int = 3

    eks_cluster_name: str = ""
    s3_metadata_bucket: str = ""
    s3_fast_reg_bucket: str = ""
    ecr_repo_name: str = ""
    iam_role_name: str = ""
    iam_s3_policy_name: str = ""
    iam_ecr_policy_name: str = ""

    def __post_init__(self):
        super().__post_init__()
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


# ============================================================================
# Per-resource outputs and the final aggregated result
# ============================================================================


@dataclass(frozen=True)
class EKSCluster:
    name: str
    region: str
    oidc_issuer_url: str


@dataclass(frozen=True)
class S3Bucket:
    name: str
    region: str


@dataclass(frozen=True)
class ECRRepo:
    name: str
    region: str
    account_id: str

    @property
    def arn(self) -> str:
        return f"arn:aws:ecr:{self.region}:{self.account_id}:repository/{self.name}"


@dataclass(frozen=True)
class IAMRole:
    name: str
    arn: str


@dataclass
class AWSResources:
    """Aggregated state returned by main()."""
    account_id: str = ""
    dataplane: DataplaneValues | None = None
    eks: EKSCluster | None = None
    s3_metadata: S3Bucket | None = None
    s3_fast_reg: S3Bucket | None = None
    ecr: ECRRepo | None = None
    iam: IAMRole | None = None
    helm: HelmRelease | None = None
    project: str = ""
    smoke_run_name: str = ""
    test_results: list[TestResult] = field(default_factory=list)


# ============================================================================
# TaskEnvironment — base image + aws cli + eksctl; secret injection for creds
# ============================================================================

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
    secrets=[flyte.Secret(key=E2E_CREDS_SECRET_KEY, as_env_var=E2E_CREDS_ENV_VAR)],
    # Cache task outputs so a re-run against the same control_plane_url +
    # cluster_name replays prior infra + deploy results instead of re-doing
    # the idempotent-check work. Teardown is explicitly opted out below.
    cache="auto",
)


# ============================================================================
# Phase 1 — AWS account id (separate because it shells out, not pure data)
# ============================================================================


@env.task(short_name="resolve-account-id")
async def resolve_aws_account_id(cfg: Config) -> str:
    """Return the AWS account id. Uses cfg.aws_account_id if already set."""
    await hydrate_credentials()
    if cfg.aws_account_id:
        return cfg.aws_account_id
    out = await sh("aws sts get-caller-identity --query Account --output text")
    return out.strip()


# ============================================================================
# Phase 1 — Infrastructure (each task self-contained, returns its record)
# ============================================================================


@env.task(short_name="provision-dataplane")
async def provision_aws_dataplane(cfg: Config) -> DataplaneValues:
    await hydrate_credentials()
    return await provision_dataplane(cfg, provider="aws")


@env.task(short_name="create-eks", retries=1)
async def create_eks(cfg: Config) -> EKSCluster:
    """Create EKS cluster (or adopt existing), wait active, update kubeconfig."""
    await hydrate_credentials()

    exists = await sh_ok(
        f"aws eks describe-cluster --name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    )
    if exists:
        say(f"create_eks: {cfg.eks_cluster_name} already exists in {cfg.aws_region}; reusing")
    else:
        say(f"create_eks: eksctl creating {cfg.eks_cluster_name} in {cfg.aws_region} "
            f"(k8s={cfg.eks_k8s_version}, nodes={cfg.eks_node_count}x{cfg.eks_node_type}) "
            f"— this usually takes ~15 minutes")
        await sh(
            f"eksctl create cluster "
            f"--name {cfg.eks_cluster_name} "
            f"--region {cfg.aws_region} "
            f"--version {cfg.eks_k8s_version} "
            f"--node-type {cfg.eks_node_type} "
            f"--nodes {cfg.eks_node_count} "
            f"--with-oidc --managed"
        )

    # Ensure a managed nodegroup exists. When the control plane is adopted
    # from a prior run, its nodegroup may have been deleted — pods would then
    # sit Pending forever. eksctl exits non-zero with "No nodegroups found" in
    # that case; sh_ok flips that to False.
    has_nodegroup = await sh_ok(
        f"eksctl get nodegroup --cluster {cfg.eks_cluster_name} --region {cfg.aws_region}"
    )
    if not has_nodegroup:
        say(f"create_eks: no nodegroup found; creating managed nodegroup "
            f"({cfg.eks_node_count}x{cfg.eks_node_type}) — ~5-10 minutes")
        await sh(
            f"eksctl create nodegroup "
            f"--cluster {cfg.eks_cluster_name} "
            f"--region {cfg.aws_region} "
            f"--name {cfg.eks_cluster_name}-ng "
            f"--node-type {cfg.eks_node_type} "
            f"--nodes {cfg.eks_node_count} "
            f"--managed"
        )

    say(f"create_eks: waiting for {cfg.eks_cluster_name} to become ACTIVE")
    await sh(
        f"aws eks wait cluster-active "
        f"--name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    )
    say(f"create_eks: updating kubeconfig for {cfg.eks_cluster_name}")
    await sh(
        f"aws eks update-kubeconfig "
        f"--name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    )
    oidc = (await sh(
        f"aws eks describe-cluster --region {cfg.aws_region} "
        f"--name {cfg.eks_cluster_name} "
        f'--query "cluster.identity.oidc.issuer" --output text'
    )).strip()
    say(f"create_eks: done (oidc={oidc})")
    return EKSCluster(
        name=cfg.eks_cluster_name,
        region=cfg.aws_region,
        oidc_issuer_url=oidc,
    )


_S3_CORS_CONFIG = json.dumps({
    "CORSRules": [{
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "HEAD"],
        "AllowedOrigins": ["https://*.unionai.cloud", "https://*.union.ai"],
        "ExposeHeaders": ["ETag"],
        "MaxAgeSeconds": 3600,
    }]
})


@env.task(short_name="create-s3")
async def create_s3_bucket(cfg: Config, bucket_name: str) -> S3Bucket:
    """Create one S3 bucket with CORS enabled."""
    await hydrate_credentials()
    exists = await sh_ok(f"aws s3api head-bucket --bucket {bucket_name}")
    if exists:
        say(f"create_s3_bucket: {bucket_name} already exists; reusing")
    else:
        say(f"create_s3_bucket: creating {bucket_name} in {cfg.aws_region}")
        loc_flag = (
            ""
            if cfg.aws_region == "us-east-1"
            else f"--create-bucket-configuration LocationConstraint={cfg.aws_region}"
        )
        await sh(
            f"aws s3api create-bucket --bucket {bucket_name} "
            f"--region {cfg.aws_region} {loc_flag}"
        )
    await sh(
        f"aws s3api put-bucket-cors --bucket {bucket_name} "
        f"--cors-configuration '{_S3_CORS_CONFIG}'"
    )
    say(f"create_s3_bucket: {bucket_name} ready with CORS")
    return S3Bucket(name=bucket_name, region=cfg.aws_region)


@env.task(short_name="create-ecr")
async def create_ecr(cfg: Config, account_id: str) -> ECRRepo:
    await hydrate_credentials()
    exists = await sh_ok(
        f"aws ecr describe-repositories --repository-names {cfg.ecr_repo_name} "
        f"--region {cfg.aws_region}"
    )
    if exists:
        say(f"create_ecr: {cfg.ecr_repo_name} already exists; reusing")
    else:
        say(f"create_ecr: creating {cfg.ecr_repo_name} in {cfg.aws_region}")
        await sh(
            f"aws ecr create-repository --repository-name {cfg.ecr_repo_name} "
            f"--region {cfg.aws_region} --image-scanning-configuration scanOnPush=true"
        )
    say(f"create_ecr: {cfg.ecr_repo_name} ready")
    return ECRRepo(
        name=cfg.ecr_repo_name, region=cfg.aws_region, account_id=account_id,
    )


async def _ensure_policy_attached(
    role_name: str, policy_name: str, policy_doc: str, account_id: str,
) -> None:
    """Create IAM policy if needed and attach to the role. Idempotent."""
    policy_arn = f"arn:aws:iam::{account_id}:policy/{policy_name}"
    if not await sh_ok(f"aws iam get-policy --policy-arn {policy_arn}"):
        await sh(
            f"aws iam create-policy --policy-name {policy_name} "
            f"--policy-document '{policy_doc}'"
        )
    await sh(
        f"aws iam attach-role-policy --role-name {role_name} --policy-arn {policy_arn}",
        check=False,
    )


@env.task(short_name="create-iam-role")
async def create_iam_role(
    cfg: Config,
    account_id: str,
    eks: EKSCluster,
    s3_meta: S3Bucket,
    s3_fast: S3Bucket,
    ecr: ECRRepo,
) -> IAMRole:
    """Create or update the IRSA role and attach S3 + ECR policies."""
    await hydrate_credentials()

    role_arn = f"arn:aws:iam::{account_id}:role/{cfg.iam_role_name}"
    oidc_provider = eks.oidc_issuer_url.removeprefix("https://")

    trust_policy = json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Federated": f"arn:aws:iam::{account_id}:oidc-provider/{oidc_provider}"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {f"{oidc_provider}:aud": "sts.amazonaws.com"},
                "StringLike": {f"{oidc_provider}:sub": "system:serviceaccount:*"},
            },
        }],
    })

    if await sh_ok(f"aws iam get-role --role-name {cfg.iam_role_name}"):
        say(f"create_iam_role: {cfg.iam_role_name} exists, updating trust policy")
        await sh(
            f"aws iam update-assume-role-policy --role-name {cfg.iam_role_name} "
            f"--policy-document '{trust_policy}'"
        )
    else:
        say(f"create_iam_role: creating {cfg.iam_role_name}")
        await sh(
            f"aws iam create-role --role-name {cfg.iam_role_name} "
            f"--assume-role-policy-document '{trust_policy}'"
        )

    s3_policy = json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "S3BucketAccess",
            "Effect": "Allow",
            "Action": ["s3:DeleteObject*", "s3:GetObject*", "s3:ListBucket", "s3:PutObject*"],
            "Resource": [
                f"arn:aws:s3:::{s3_meta.name}",
                f"arn:aws:s3:::{s3_meta.name}/*",
                f"arn:aws:s3:::{s3_fast.name}",
                f"arn:aws:s3:::{s3_fast.name}/*",
            ],
        }],
    })
    await _ensure_policy_attached(
        cfg.iam_role_name, cfg.iam_s3_policy_name, s3_policy, account_id,
    )

    ecr_policy = json.dumps({
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
                "Resource": ecr.arn,
            },
        ],
    })
    await _ensure_policy_attached(
        cfg.iam_role_name, cfg.iam_ecr_policy_name, ecr_policy, account_id,
    )
    say(f"create_iam_role: ready at {role_arn}")
    return IAMRole(name=cfg.iam_role_name, arn=role_arn)


# ============================================================================
# Phase 2 — Patch values YAML and helm install
# ============================================================================


@flyte.trace
async def patch_values_yaml(
    yaml_text: str,
    cfg: Config,
    account_id: str,
    iam: IAMRole,
    s3_meta: S3Bucket,
    s3_fast: S3Bucket,
    ecr: ECRRepo,
) -> str:
    """Apply AWS-specific overrides to the uctl-generated values YAML.

    Pure Python — parses the YAML into a dict, mutates, re-dumps. No yq/sed
    subprocesses to escape-wrangle.
    """
    import yaml

    # The uctl-generated file uses ``<UNION_FLYTE_ROLE_ARN>`` as a placeholder
    # in a few string fields (not a single top-level key), so we substitute
    # at the text level first.
    yaml_text = yaml_text.replace("<UNION_FLYTE_ROLE_ARN>", iam.arn)

    data = yaml.safe_load(yaml_text) or {}

    def _set(path: list[str], value) -> None:
        """Create intermediate dicts as needed, then set the leaf."""
        node = data
        for key in path[:-1]:
            node = node.setdefault(key, {})
            if not isinstance(node, dict):
                raise ValueError(f"yaml path conflict at {path!r}: {key} is not a dict")
        node[path[-1]] = value

    _set(["global", "AWS_ACCOUNT_ID"],           account_id)
    _set(["global", "METADATA_BUCKET"],          s3_meta.name)
    _set(["global", "FAST_REGISTRATION_BUCKET"], s3_fast.name)
    _set(["global", "BACKEND_IAM_ROLE_ARN"],     iam.arn)
    _set(["global", "WORKER_IAM_ROLE_ARN"],      iam.arn)

    _set(["storage", "bucketName"],                  s3_meta.name)
    _set(["storage", "fastRegistrationBucketName"], s3_fast.name)
    _set(["storage", "region"],                      cfg.aws_region)

    _set(
        ["commonServiceAccount", "annotations", "eks.amazonaws.com/role-arn"],
        iam.arn,
    )
    _set(["imageBuilder", "registryName"], ecr.name)

    say(
        f"patch_values_yaml: applied AWS overrides "
        f"(account={account_id}, role={iam.arn}, region={cfg.aws_region})"
    )
    return yaml.safe_dump(data, sort_keys=False, default_flow_style=False)


@env.task(short_name="deploy-dataplane")
async def deploy_dataplane(
    cfg: Config,
    account_id: str,
    dp: DataplaneValues,
    iam: IAMRole,
    s3_meta: S3Bucket,
    s3_fast: S3Bucket,
    ecr: ECRRepo,
) -> HelmRelease:
    """Phase 2: patch values and install the helm chart. Also mints EAGER_API_KEY."""
    await hydrate_credentials()
    patched = await patch_values_yaml(
        dp.yaml_text, cfg, account_id, iam, s3_meta, s3_fast, ecr,
    )
    chart_ref = await resolve_chart_ref(cfg)
    release = await helm_install(cfg, patched, chart_ref)
    await create_eager_api_key(cfg)
    return release


# ============================================================================
# Phase 4 — Teardown
# ============================================================================


async def teardown(cfg: Config, resources: AWSResources) -> str:
    """Reverse-order delete of everything in AWSResources. Best-effort.

    Deliberately NOT an ``@env.task``: when invoked from ``main``'s finally
    block after a Phase 3 failure, the flyte local controller replays a
    cached task output (even with cache='disable'), so the body never runs.
    A plain async function executes inline in main's process, bypassing the
    controller and guaranteeing the delete commands actually fire.
    """
    await hydrate_credentials()

    logger.info("\n--- Teardown ---")
    logger.info(f"  eks_cluster: {cfg.eks_cluster_name}")
    logger.info(f"  s3 buckets : {cfg.s3_metadata_bucket}, {cfg.s3_fast_reg_bucket}")
    logger.info(f"  ecr repo   : {cfg.ecr_repo_name}")
    logger.info(f"  iam role   : {cfg.iam_role_name}")

    errors = await helm_uninstall(cfg)

    # IAM
    if await sh_ok(f"aws iam get-role --role-name {cfg.iam_role_name}"):
        logger.info(f"Cleaning up IAM role {cfg.iam_role_name}...")
        attached = await sh(
            f"aws iam list-attached-role-policies --role-name {cfg.iam_role_name} "
            f"--query 'AttachedPolicies[].PolicyArn' --output text",
            check=False,
        )
        for arn in attached.split():
            await sh(
                f"aws iam detach-role-policy --role-name {cfg.iam_role_name} "
                f"--policy-arn {arn}",
                check=False,
            )
        inline = await sh(
            f"aws iam list-role-policies --role-name {cfg.iam_role_name} "
            f"--query 'PolicyNames[]' --output text",
            check=False,
        )
        for name in inline.split():
            await sh(
                f"aws iam delete-role-policy --role-name {cfg.iam_role_name} "
                f"--policy-name {name}",
                check=False,
            )
        await sh(f"aws iam delete-role --role-name {cfg.iam_role_name}", check=False)
        account_id = resources.account_id
        for policy_name in (cfg.iam_s3_policy_name, cfg.iam_ecr_policy_name):
            await sh(
                f"aws iam delete-policy "
                f"--policy-arn arn:aws:iam::{account_id}:policy/{policy_name}",
                check=False,
            )

    # ECR
    if await sh_ok(
        f"aws ecr describe-repositories --repository-names {cfg.ecr_repo_name} "
        f"--region {cfg.aws_region}"
    ):
        logger.info(f"Deleting ECR repository {cfg.ecr_repo_name}...")
        await sh(
            f"aws ecr delete-repository --repository-name {cfg.ecr_repo_name} "
            f"--region {cfg.aws_region} --force",
            check=False,
        )

    # S3
    for bucket in (cfg.s3_metadata_bucket, cfg.s3_fast_reg_bucket):
        if await sh_ok(f"aws s3api head-bucket --bucket {bucket}"):
            logger.info(f"Deleting S3 bucket {bucket}...")
            await sh(
                f"aws s3 rb s3://{bucket} --force --region {cfg.aws_region}",
                check=False,
            )

    # EKS (longest — last)
    if await sh_ok(
        f"aws eks describe-cluster --name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    ):
        logger.info(f"Deleting EKS cluster {cfg.eks_cluster_name} (~10-15 min)...")
        await sh(
            f"eksctl delete cluster --name {cfg.eks_cluster_name} "
            f"--region {cfg.aws_region} --wait",
            check=False,
        )

    if errors:
        return f"teardown complete with errors: {'; '.join(errors)}"
    return "teardown complete"


@env.task(short_name="teardown-cluster", entrypoint=True, cache="disable")
async def teardown_cluster(
    control_plane_url: str,
    cluster_name: str,
    aws_region: str = "us-east-2",
) -> str:
    """Short-circuit entry point — invoke teardown directly.

    Useful when a prior ``main`` run failed mid-phase (e.g. cluster never
    became healthy) and you just want to delete the AWS infra. Resolves
    ``account_id`` from the ambient AWS identity so IAM-policy deletion
    works; every other name is derived from ``cluster_name`` the same way
    ``Config`` does.

        flyte run --local selfmanaged_aws_e2e.py teardown_cluster \\
            --control_plane_url https://... --cluster_name my-cluster
    """
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
    )
    await hydrate_credentials()
    account_id = (await sh(
        "aws sts get-caller-identity --query Account --output text"
    )).strip()
    resources = AWSResources(account_id=account_id)
    say(f"teardown_cluster: starting for cluster '{cluster_name}' (account={account_id})")
    result_str = await teardown(cfg, resources)
    say(f"teardown_cluster: done — {result_str}")
    return result_str


# ============================================================================
# Main orchestrator
# ============================================================================


@env.task(short_name="e2e-aws", entrypoint=True, cache="disable")
async def main(
    control_plane_url: str,
    cluster_name: str,
    aws_region: str = "us-east-2",
    skip_teardown: bool = False,
    skip_smoke_tests: bool = False,
    helm_values_override: str = "",
) -> E2EResult:
    """Four phases: infra → deploy → verify → (teardown).

    ``skip_smoke_tests`` skips Phase 3's run_smoke_suite — useful while the
    cluster-pool-attributes permission issue is unresolved, or when you only
    want to validate the infra + deploy path.
    """
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
        skip_teardown=skip_teardown,
        helm_values_override=helm_values_override,
    )
    await hydrate_credentials()
    await init_union_client(cfg)
    say(f"main: starting e2e for cluster '{cluster_name}' on {control_plane_url} "
        f"(region={aws_region}, skip_teardown={skip_teardown})")

    result = E2EResult()
    resources = AWSResources()
    debug_dir = os.path.join(
        os.path.dirname(__file__), ".debug", time.strftime("%Y%m%d-%H%M%S"),
    )

    try:
        # ---- Phase 1: resolve account id + infrastructure (fan out) ----
        say("===== Phase 1/4: Infrastructure =====")
        with flyte.group("1-infra"):
            account_id = await resolve_aws_account_id(cfg)
            resources.account_id = account_id
            say(f"main: AWS account {account_id}")

            dp, eks, s3_meta, s3_fast, ecr = await asyncio.gather(
                provision_aws_dataplane(cfg),
                create_eks(cfg),
                create_s3_bucket(cfg, cfg.s3_metadata_bucket),
                create_s3_bucket(cfg, cfg.s3_fast_reg_bucket),
                create_ecr(cfg, account_id),
            )
            resources.dataplane = dp
            resources.eks = eks
            resources.s3_metadata = s3_meta
            resources.s3_fast_reg = s3_fast
            resources.ecr = ecr

            # IAM depends on EKS OIDC + bucket / repo names
            iam = await create_iam_role(cfg, account_id, eks, s3_meta, s3_fast, ecr)
            resources.iam = iam

        # ---- Phase 2: Deploy data plane ----
        say("===== Phase 2/4: Deploy data plane =====")
        with flyte.group("2-deploy"):
            helm = await deploy_dataplane(cfg, account_id, dp, iam, s3_meta, s3_fast, ecr)
            resources.helm = helm

        # ---- Phase 3: Verify ----
        say("===== Phase 3/4: Verify =====")
        with flyte.group("3-verify"):
            org = await cluster_wait_healthy(cfg)
            if not org:
                org = dp.org_name
            # Re-init with the real org now that we have it — SelectCluster
            # (used by flyte.run.aio code-bundle upload) needs the org to
            # route correctly.
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
        # Record the failure and let ``finally`` run teardown. We do NOT
        # re-raise: once the enclosing env.task is marked failed, flyte's
        # local controller cancels any in-flight awaits — which would kill
        # the teardown task before it runs. Return a FAILED E2EResult
        # instead; the caller sees overall='FAILED' + teardown_result.
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
                    result.teardown_result = await teardown(cfg, resources)
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
    aws_region: str = "us-east-2",
    skip_teardown: bool = False,
) -> str:
    """flyte.run(main, ...) against the remote control plane.

    Prerequisite: run `stash_credentials` once in the same shell so the remote
    task can read AWS + UNION creds from the Flyte Secret.
    """
    flyte.init_from_config()
    run = flyte.run(
        main,
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
        skip_teardown=skip_teardown,
    )
    logger.info(f"Launched remote run: {run.name}")
    logger.info(f"  URL: {run.url}")
    return run.url
