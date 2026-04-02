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

import base64
import json
import os
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path

import flyte

# =============================================================================
# RSA envelope encryption — one secret, many credentials
# =============================================================================

_KEYS_DIR = Path(__file__).parent / ".e2e-keys"
_PUBLIC_KEY_PATH = _KEYS_DIR / "e2e_public.pem"
_PRIVATE_KEY_PATH = _KEYS_DIR / "e2e_private.pem"
_FLYTE_SECRET_NAME = "E2E_RSA_PRIVATE_KEY"


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


def _decrypt_and_export_credentials(cfg: "Config") -> None:
    """If encrypted credentials are present, decrypt them and set as env vars."""
    if not cfg.encrypted_credentials:
        return  # Running locally — credentials already in env

    # Read the private key from the Flyte secret mount.
    # Flyte mounts file secrets at /etc/flyte/secrets/<SECRET_KEY>
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
        # List what's actually in /etc/flyte/secrets for debugging
        secrets_dir = Path("/etc/flyte/secrets")
        contents = list(secrets_dir.rglob("*")) if secrets_dir.exists() else []
        raise RuntimeError(
            f"Cannot find private key. Checked: {[str(p) for p in candidates]} "
            f"and ${_FLYTE_SECRET_NAME} env var. "
            f"Contents of {secrets_dir}: {[str(p) for p in contents]}"
        )

    creds = json.loads(cfg.encrypted_credentials)
    for env_var, encrypted_value in creds.items():
        if encrypted_value:
            os.environ[env_var] = _decrypt(encrypted_value, private_key_pem)
            print(f"  Decrypted {env_var} ({len(os.environ[env_var])} chars)")


def _encrypt_local_credentials() -> str:
    """Read credentials from local env, encrypt with public key, return JSON."""
    if not _PUBLIC_KEY_PATH.exists():
        raise RuntimeError(
            f"Public key not found at {_PUBLIC_KEY_PATH}. Run: python {__file__} --setup-keys"
        )

    env_vars = {
        "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
        "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
        "AWS_SESSION_TOKEN": os.environ.get("AWS_SESSION_TOKEN", ""),
        "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", os.environ.get("AWS_REGION", "")),
        "UNION_API_KEY": os.environ.get("UNION_API_KEY", ""),
    }

    encrypted = {}
    for key, value in env_vars.items():
        if value:
            encrypted[key] = _encrypt(value)
            print(f"  Encrypted {key} ({len(value)} chars -> {len(encrypted[key])} chars)")
        else:
            encrypted[key] = ""

    if not encrypted.get("AWS_ACCESS_KEY_ID"):
        raise RuntimeError("AWS_ACCESS_KEY_ID not set in environment")
    if not encrypted.get("AWS_SECRET_ACCESS_KEY"):
        raise RuntimeError("AWS_SECRET_ACCESS_KEY not set in environment")

    return json.dumps(encrypted)


# =============================================================================
# Configuration
# =============================================================================


@dataclass
class Config:
    """All knobs for the E2E test. Override via task arguments."""

    # Required — Union control plane
    control_plane_url: str = ""
    cluster_name: str = ""

    # AWS
    aws_region: str = "us-east-2"
    aws_account_id: str = ""  # auto-detected if empty

    # EKS
    eks_k8s_version: str = "1.31"
    eks_node_type: str = "m5.2xlarge"
    eks_node_count: int = 3

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

    # Encrypted credentials blob (JSON string from _encrypt_local_credentials).
    # Empty when running locally (credentials come from local env vars).
    encrypted_credentials: str = ""

    # Union org name (parsed from uctl output if not set)
    org_name: str = ""

    # Derived names (computed in __post_init__)
    eks_cluster_name: str = ""
    s3_metadata_bucket: str = ""
    s3_fast_reg_bucket: str = ""
    ecr_repo_name: str = ""
    iam_role_name: str = ""
    iam_s3_policy_name: str = ""
    iam_ecr_policy_name: str = ""

    def __post_init__(self):
        if not self.control_plane_url:
            self.control_plane_url = os.environ.get("UNION_CONTROL_PLANE_URL", "")
        if not self.cluster_name:
            self.cluster_name = os.environ.get("UNION_CLUSTER_NAME", "")
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
class InfraState:
    """Tracks what was created so teardown knows what to clean up."""

    eks_created: bool = False
    s3_metadata_created: bool = False
    s3_fast_reg_created: bool = False
    ecr_created: bool = False
    iam_role_created: bool = False
    iam_role_arn: str = ""
    values_file_path: str = ""
    debug_dir: str = ""


# =============================================================================
# Helpers
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


def _collect_debug_dumps(cfg: Config, debug_dir: str) -> str:
    """Dump cluster state for debugging. Returns the debug directory path."""
    if not _sh_ok("kubectl cluster-info"):
        print("WARNING: No cluster access — skipping debug dump.")
        return debug_dir

    os.makedirs(debug_dir, exist_ok=True)
    print(f"Collecting debug dumps to {debug_dir}...")

    # All pods
    _dump_cmd(f"kubectl get pods -A -o wide", f"{debug_dir}/pods-all.txt")
    # Events
    _dump_cmd(
        f"kubectl get events -A --sort-by='.lastTimestamp'",
        f"{debug_dir}/events.txt",
    )
    # Nodes
    _dump_cmd(f"kubectl get nodes -o wide", f"{debug_dir}/nodes.txt")
    # Helm status
    _dump_cmd(
        f"helm status {cfg.helm_release_name} -n {cfg.helm_namespace}",
        f"{debug_dir}/helm-status.txt",
    )

    # Logs from non-healthy pods
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

        # Container logs
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

        # Init container logs
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
    # Remove empty files
    if os.path.getsize(path) == 0:
        os.remove(path)


# =============================================================================
# Task environment
# =============================================================================

# Versions pinned for reproducibility
_HELM_VERSION = "3.17.3"
_KUBECTL_VERSION = "1.31.4"
_EKSCTL_VERSION = "0.204.0"
_YQ_VERSION = "4.45.4"
_UCTL_VERSION = "0.1.20"

_image = (
    flyte.Image.from_debian_base()
    .with_apt_packages(
        "curl", "ca-certificates", "git", "jq", "unzip", "gnupg", "lsb-release",
    )
    .with_pip_packages("cryptography")
    .with_commands([
        # AWS CLI v2
        "curl -fsSL https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o /tmp/awscli.zip"
        " && unzip -q /tmp/awscli.zip -d /tmp && /tmp/aws/install && rm -rf /tmp/aws /tmp/awscli.zip",
        # Helm
        f"curl -fsSL https://get.helm.sh/helm-v{_HELM_VERSION}-linux-amd64.tar.gz"
        f" | tar xz -C /tmp && mv /tmp/linux-amd64/helm /usr/local/bin/ && rm -rf /tmp/linux-amd64",
        # kubectl
        f"curl -fsSLo /usr/local/bin/kubectl"
        f" https://dl.k8s.io/release/v{_KUBECTL_VERSION}/bin/linux/amd64/kubectl"
        f" && chmod +x /usr/local/bin/kubectl",
        # eksctl
        f"curl -fsSL https://github.com/eksctl-io/eksctl/releases/download/v{_EKSCTL_VERSION}/eksctl_Linux_amd64.tar.gz"
        f" | tar xz -C /usr/local/bin",
        # yq
        f"curl -fsSLo /usr/local/bin/yq"
        f" https://github.com/mikefarah/yq/releases/download/v{_YQ_VERSION}/yq_linux_amd64"
        f" && chmod +x /usr/local/bin/yq",
        # uctl (released as a tarball)
        f"curl -fsSL https://github.com/unionai/uctl/releases/download/v{_UCTL_VERSION}/uctl_Linux_x86_64.tar.gz"
        f" | tar xz -C /usr/local/bin uctl",
        # uv (for setting up flyte SDK venv during validation)
        "curl -fsSL https://astral.sh/uv/install.sh | sh"
        " && mv /root/.local/bin/uv /usr/local/bin/",
    ])
)

env = flyte.TaskEnvironment(
    name="selfmanaged-e2e",
    image=_image,
    resources=flyte.Resources(cpu="2", memory="2Gi"),
    # Single secret: RSA private key for decrypting credentials passed as task args.
    # Credentials (AWS keys, UNION_API_KEY) are encrypted locally with the public key
    # and passed as the `encrypted_credentials` argument — no need to store them as secrets.
    secrets=flyte.Secret(key=_FLYTE_SECRET_NAME, mount=Path("/etc/flyte/secrets")),
)


# =============================================================================
# Phase 1: Interactive / Credential Setup
# =============================================================================


@env.task
def provision_dataplane(cfg: Config) -> InfraState:
    """Set up Helm repo and provision dataplane resources via uctl.

    This is the interactive step — may require authentication.
    """
    assert cfg.control_plane_url, "control_plane_url is required"
    assert cfg.cluster_name, "cluster_name is required"

    state = InfraState()

    # Run uctl in a temp directory so generated files don't clobber anything
    import glob
    import tempfile

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
        f"--clusterName {cfg.cluster_name} --provider aws"
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
    workspace = os.path.join(os.path.dirname(__file__), ".e2e-workspace")
    os.makedirs(workspace, exist_ok=True)
    dest = os.path.join(workspace, os.path.basename(values_file))
    import shutil
    shutil.copy2(values_file, dest)

    state.values_file_path = os.path.abspath(dest)
    print(f"Generated values file: {state.values_file_path}")

    # Parse org name from the uctl output table (ORGANIZATION column)
    # Table: | ORGANIZATION | HOST | CLUSTER | ... |
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
# Phase 2: Infrastructure Setup
# =============================================================================


@env.task
def create_eks_cluster(cfg: Config, state: InfraState) -> InfraState:
    """Create an EKS cluster with OIDC provider."""
    if _sh_ok(
        f"aws eks describe-cluster --name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    ):
        print(f"EKS cluster {cfg.eks_cluster_name} already exists, skipping.")
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


_S3_CORS_CONFIG = json.dumps({
    "CORSRules": [
        {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "HEAD"],
            "AllowedOrigins": ["https://*.unionai.cloud"],
            "ExposeHeaders": ["ETag"],
            "MaxAgeSeconds": 3600,
        }
    ]
})


@env.task
def create_s3_buckets(cfg: Config, state: InfraState) -> InfraState:
    """Create S3 metadata and fast-registration buckets with CORS for Code Viewer."""
    for bucket, attr in [
        (cfg.s3_metadata_bucket, "s3_metadata_created"),
        (cfg.s3_fast_reg_bucket, "s3_fast_reg_created"),
    ]:
        if _sh_ok(f"aws s3api head-bucket --bucket {bucket}"):
            print(f"Bucket {bucket} already exists, skipping creation.")
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

        # Apply CORS policy for Code Viewer (idempotent)
        _sh(
            f"aws s3api put-bucket-cors --bucket {bucket} "
            f"--cors-configuration '{_S3_CORS_CONFIG}'"
        )
        print(f"  Bucket ready (with CORS): {bucket}")
    return state


@env.task
def create_ecr_repo(cfg: Config, state: InfraState) -> InfraState:
    """Create an ECR private repository for Image Builder."""
    if _sh_ok(
        f"aws ecr describe-repositories --repository-names {cfg.ecr_repo_name} "
        f"--region {cfg.aws_region}"
    ):
        print(f"ECR repo {cfg.ecr_repo_name} already exists, skipping.")
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

    # OIDC provider
    oidc_url = _sh(
        f"aws eks describe-cluster --region {cfg.aws_region} "
        f"--name {cfg.eks_cluster_name} "
        f'--query "cluster.identity.oidc.issuer" --output text'
    ).strip()
    oidc_provider = oidc_url.removeprefix("https://")

    # Trust policy — uses StringLike for sub to allow any service account
    # in any namespace. Union platform services run in the helm namespace
    # (e.g. "union") but worker pods run in project-domain namespaces
    # (e.g. "union-health-monitoring-development"), so the policy must
    # cover both.
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
        print(f"IAM role {cfg.iam_role_name} already exists, updating trust policy...")
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

    # S3 policy
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

    # ECR policy
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

    print(f"IAM role ready: {role_arn}")
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
    f = state.values_file_path
    assert os.path.exists(f), f"Values file not found: {f}"

    # Patch with yq
    _sh(f'yq -i \'.global.AWS_ACCOUNT_ID = "{cfg.aws_account_id}"\' "{f}"')
    _sh(f'yq -i \'.storage.bucketName = "{cfg.s3_metadata_bucket}"\' "{f}"')
    _sh(f'yq -i \'.storage.fastRegistrationBucketName = "{cfg.s3_fast_reg_bucket}"\' "{f}"')
    _sh(f'yq -i \'.storage.region = "{cfg.aws_region}"\' "{f}"')

    # Replace role ARN placeholder
    _sh(f"sed -i.bak 's|<UNION_FLYTE_ROLE_ARN>|{state.iam_role_arn}|g' \"{f}\"")
    _sh(f'rm -f "{f}.bak"')

    # Also set via yq for fields that may not use the placeholder
    _sh(
        f'yq -i \'.commonServiceAccount.annotations."eks.amazonaws.com/role-arn" = '
        f'"{state.iam_role_arn}"\' "{f}"'
    )

    print(f"Values file patched: {f}")
    print(f"  storage.bucketName = {cfg.s3_metadata_bucket}")
    print(f"  storage.region = {cfg.aws_region}")
    print(f"  role-arn = {state.iam_role_arn}")

    # Resolve chart reference: local clone from branch, or published repo
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

    # Helm install (upgrade --install for idempotency)
    _sh(
        f"helm upgrade --install {cfg.helm_release_name} {chart_ref} "
        f'-f "{f}" '
        f"-n {cfg.helm_namespace} --create-namespace --wait --timeout 10m"
    )
    print("Helm chart installed.")

    # Create EAGER_API_KEY — required for v2 executions on the dataplane.
    # This is idempotent: rerunning propagates the key to new clusters.
    org_flag = f"--org {cfg.org_name}" if cfg.org_name else ""
    _sh(
        f"uctl create apikey --keyName EAGER_API_KEY {org_flag}",
        check=False,  # May already exist; that's fine
    )
    print("EAGER_API_KEY created/propagated.")

    return state


# =============================================================================
# Phase 4: Verification
# =============================================================================


@env.task
def wait_for_healthy(cfg: Config) -> bool:
    """Poll uctl get cluster until the cluster is ENABLED and HEALTHY."""
    deadline = time.time() + cfg.cluster_healthy_timeout

    while time.time() < deadline:
        output = _sh("uctl get cluster", check=False)
        for line in output.splitlines():
            if cfg.cluster_name not in line:
                continue
            # Table is pipe-delimited: | NAME | ORG | STATE | HEALTH |
            fields = [f.strip() for f in line.split("|")]
            # fields[0] is empty (before first |), then NAME, ORG, STATE, HEALTH
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


@env.task
def run_example_workflow(cfg: Config) -> bool:
    """Run the hello.py example from flyte-sdk and verify it succeeds."""
    # Clone flyte-sdk examples (or reuse)
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

    # Run the example (flyte run executes remotely by default)
    # Use --follow so flyte run blocks until completion and streams logs.
    print(f"Running example: {example}")
    run_result = subprocess.run(
        f"cd {workspace} && flyte run "
        f"--project union-health-monitoring "
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

    if run_result.returncode == 0:
        print("Validation SUCCEEDED — example workflow completed successfully.")
        return True

    # flyte run --follow failed. Log details and try to get run info.
    print(f"WARNING: flyte run exited with code {run_result.returncode}")

    # List recent runs to show what happened
    print("\nRecent runs:")
    _sh(
        "flyte get run "
        "--project union-health-monitoring "
        "--domain development "
        "--limit 5",
        check=False,
    )

    raise RuntimeError(
        f"Example workflow failed (exit code {run_result.returncode}).\n"
        f"stdout: {run_result.stdout[-500:] if run_result.stdout else '(empty)'}\n"
        f"stderr: {run_result.stderr[-500:] if run_result.stderr else '(empty)'}"
    )


# =============================================================================
# Teardown
# =============================================================================


@env.task
def teardown(cfg: Config, state: InfraState) -> str:
    """Tear down all created resources in reverse order."""
    print("\n--- Teardown state ---")
    print(f"  eks_created:          {state.eks_created}  (cluster: {cfg.eks_cluster_name})")
    print(f"  s3_metadata_created:  {state.s3_metadata_created}  (bucket: {cfg.s3_metadata_bucket})")
    print(f"  s3_fast_reg_created:  {state.s3_fast_reg_created}  (bucket: {cfg.s3_fast_reg_bucket})")
    print(f"  ecr_created:          {state.ecr_created}  (repo: {cfg.ecr_repo_name})")
    print(f"  iam_role_created:     {state.iam_role_created}  (role: {cfg.iam_role_name})")
    print(f"  iam_role_arn:         {state.iam_role_arn}")
    print(f"  helm_release:         {cfg.helm_release_name} (ns: {cfg.helm_namespace})")
    print(f"  values_file_path:     {state.values_file_path}")
    print(f"  skip_teardown:        {cfg.skip_teardown}")
    print("---")

    if cfg.skip_teardown:
        print("skip_teardown=True — leaving all resources in place.")
        return "skipped"

    errors: list[str] = []

    # Helm uninstall
    if _sh_ok(f"helm status {cfg.helm_release_name} -n {cfg.helm_namespace}"):
        print(f"Uninstalling Helm release {cfg.helm_release_name}...")
        if not _sh_ok(
            f"helm uninstall {cfg.helm_release_name} -n {cfg.helm_namespace} --wait --timeout 5m"
        ):
            errors.append("Helm uninstall failed")

    # IAM cleanup
    if _sh_ok(f"aws iam get-role --role-name {cfg.iam_role_name}"):
        print(f"Cleaning up IAM role {cfg.iam_role_name}...")

        # Detach policies
        policies_output = _sh(
            f"aws iam list-attached-role-policies --role-name {cfg.iam_role_name} "
            f"--query 'AttachedPolicies[].PolicyArn' --output text",
            check=False,
        )
        for arn in policies_output.split():
            _sh(f"aws iam detach-role-policy --role-name {cfg.iam_role_name} --policy-arn {arn}", check=False)

        # Delete inline policies
        inline_output = _sh(
            f"aws iam list-role-policies --role-name {cfg.iam_role_name} "
            f"--query 'PolicyNames[]' --output text",
            check=False,
        )
        for name in inline_output.split():
            _sh(f"aws iam delete-role-policy --role-name {cfg.iam_role_name} --policy-name {name}", check=False)

        _sh(f"aws iam delete-role --role-name {cfg.iam_role_name}", check=False)

        # Delete managed policies
        for policy_name in [cfg.iam_s3_policy_name, cfg.iam_ecr_policy_name]:
            policy_arn = f"arn:aws:iam::{cfg.aws_account_id}:policy/{policy_name}"
            _sh(f"aws iam delete-policy --policy-arn {policy_arn}", check=False)

    # ECR
    if _sh_ok(
        f"aws ecr describe-repositories --repository-names {cfg.ecr_repo_name} "
        f"--region {cfg.aws_region}"
    ):
        print(f"Deleting ECR repository {cfg.ecr_repo_name}...")
        _sh(
            f"aws ecr delete-repository --repository-name {cfg.ecr_repo_name} "
            f"--region {cfg.aws_region} --force",
            check=False,
        )
    else:
        print(f"ECR repo {cfg.ecr_repo_name} not found, skipping.")

    # S3
    for bucket in [cfg.s3_metadata_bucket, cfg.s3_fast_reg_bucket]:
        if _sh_ok(f"aws s3api head-bucket --bucket {bucket}"):
            print(f"Deleting S3 bucket {bucket}...")
            _sh(f"aws s3 rb s3://{bucket} --force --region {cfg.aws_region}", check=False)
        else:
            print(f"S3 bucket {bucket} not found, skipping.")

    # EKS cluster
    if _sh_ok(
        f"aws eks describe-cluster --name {cfg.eks_cluster_name} --region {cfg.aws_region}"
    ):
        print(f"Deleting EKS cluster {cfg.eks_cluster_name} (takes ~10-15 min)...")
        _sh(
            f"eksctl delete cluster --name {cfg.eks_cluster_name} "
            f"--region {cfg.aws_region} --wait",
            check=False,
        )
    else:
        print(f"EKS cluster {cfg.eks_cluster_name} not found, skipping.")

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
    _decrypt_and_export_credentials(cfg)
    state = provision_dataplane(cfg)
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
    _decrypt_and_export_credentials(cfg)
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
    _decrypt_and_export_credentials(cfg)
    wait_for_healthy(cfg)
    return run_example_workflow(cfg)


@env.task
def e2e_test(
    control_plane_url: str = "",
    cluster_name: str = "",
    aws_region: str = "us-east-2",
    skip_teardown: bool = False,
    encrypted_credentials: str = "",
) -> str:
    """Full E2E: setup, deploy, verify, teardown.

    This is the main entry point. When running remotely, pass encrypted_credentials
    (produced by `python selfmanaged_aws_e2e.py --launch`).
    """
    cfg = Config(
        control_plane_url=control_plane_url,
        cluster_name=cluster_name,
        aws_region=aws_region,
        skip_teardown=skip_teardown,
        encrypted_credentials=encrypted_credentials,
    )
    _decrypt_and_export_credentials(cfg)

    debug_dir = os.path.join(
        os.path.dirname(__file__),
        ".debug",
        time.strftime("%Y%m%d-%H%M%S"),
    )

    state = InfraState(debug_dir=debug_dir)
    try:
        # Phase 1: Interactive / credential setup
        print("\n--- Phase 1: Interactive / Credential Setup ---")
        state = provision_dataplane(cfg)
        state.debug_dir = debug_dir

        # Phase 2: Infrastructure
        print("\n--- Phase 2: Infrastructure Setup ---")
        state = create_eks_cluster(cfg, state)
        state = create_s3_buckets(cfg, state)
        state = create_ecr_repo(cfg, state)
        state = create_iam_role(cfg, state)

        # Phase 3: Deploy
        print("\n--- Phase 3: Dataplane Deployment ---")
        state = patch_and_install(cfg, state)

        # Phase 4: Verify
        print("\n--- Phase 4: Verification ---")
        wait_for_healthy(cfg)
        run_example_workflow(cfg)

        print("\n=== E2E test PASSED ===")
        result = "PASSED"

    except Exception as e:
        print(f"\n=== E2E test FAILED: {e} ===")
        _collect_debug_dumps(cfg, debug_dir)
        result = f"FAILED: {e}"
        if not cfg.skip_teardown:
            teardown(cfg, state)
        raise

    # Teardown
    teardown_result = teardown(cfg, state)
    return f"{result} | {teardown_result}"


# =============================================================================
# Key setup and remote launch — run these locally
# =============================================================================

# Minimal local-only env (no image, no secrets — these run on your machine)
_local_env = flyte.TaskEnvironment(name="e2e-local")


@_local_env.task
def setup_keys() -> str:
    """Generate RSA key pair and push private key as a Flyte secret.

    Run once:  flyte run --local selfmanaged_aws_e2e.py setup_keys
    """
    _generate_key_pair()

    print(f"\nPushing private key as Flyte secret '{_FLYTE_SECRET_NAME}'...")
    import flyte.remote as remote

    flyte.init_from_config()
    remote.Secret.create(
        name=_FLYTE_SECRET_NAME,
        value=_PRIVATE_KEY_PATH.read_bytes(),
        type="regular",
    )
    print(f"Secret '{_FLYTE_SECRET_NAME}' created.")

    return f"Key pair in {_KEYS_DIR}/, secret '{_FLYTE_SECRET_NAME}' created."


@_local_env.task
def launch(
    control_plane_url: str = "",
    cluster_name: str = "",
    aws_region: str = "us-east-2",
    skip_teardown: bool = False,
) -> str:
    """Encrypt local credentials and launch e2e_test remotely.

    Usage:
      flyte run --local selfmanaged_aws_e2e.py launch \\
        --control_plane_url https://myorg.union.ai \\
        --cluster_name my-test-cluster
    """
    print("Encrypting local credentials...")
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
    print(f"Launched remote run: {run.name}")
    print(f"  URL: {run.url}")
    return run.url
