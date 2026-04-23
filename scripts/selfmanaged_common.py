"""
Shared utilities for selfmanaged E2E tests.

Contains base configuration, encryption, shell helpers, debug collection,
Docker image construction, Helm chart management, and verification logic
that is reused across cloud providers (AWS, GCP, etc.).
"""

from __future__ import annotations

import base64
import json
import logging
import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)s - %(message)s",
)
logger = logging.getLogger("flyte.e2e")

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
    helm_values_override: str = ""  # extra values file (e.g. "values-legacy.yaml" from the chart)

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
    """Fields shared across all cloud providers.

    values_file_content carries the YAML text produced by
    `uctl selfserve provision-dataplane-resources` so downstream tasks don't
    rely on the generating task's local filesystem. Writing it to a temp file
    is the responsibility of the consumer (helm install, yq patching).
    """

    values_file_content: str = ""
    debug_dir: str = ""


# =============================================================================
# Shell helpers
# =============================================================================


def _sh(cmd: str, check: bool = True, capture: bool = True) -> str:
    """Run a shell command, return stdout."""
    logger.info(f"  $ {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=capture,
        text=True,
    )
    if capture and result.stdout:
        logger.info(result.stdout.rstrip())
    if capture and result.stderr:
        logger.warning(result.stderr.rstrip())
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
    logger.info(f"Generated key pair in {_KEYS_DIR}/")
    logger.info(f"  Public key:  {_PUBLIC_KEY_PATH}")
    logger.info(f"  Private key: {_PRIVATE_KEY_PATH}")


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
            logger.info(f"  Found private key at {secret_path}")
            break

    if private_key_pem is None and os.environ.get(_FLYTE_SECRET_NAME):
        private_key_pem = os.environ[_FLYTE_SECRET_NAME].encode()
        logger.info(f"  Found private key in ${_FLYTE_SECRET_NAME} env var")

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
            logger.info(f"  Decrypted {env_var} ({len(os.environ[env_var])} chars)")


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
            logger.info(f"  Encrypted {key} ({len(value)} chars -> {len(encrypted[key])} chars)")
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
        logger.warning("No cluster access — skipping debug dump.")
        return debug_dir

    os.makedirs(debug_dir, exist_ok=True)
    logger.info(f"Collecting debug dumps to {debug_dir}...")

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

    logger.info(f"Debug dumps written to {debug_dir}")
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
        # flyte + flyteplugins-union give us Python access to the control plane
        # (ApiKey, Cluster, Project) so we can avoid shelling out to uctl for
        # those operations. uctl is still installed below for the few
        # selfserve/clusterpool commands we haven't ported yet.
        .with_pip_packages("cryptography", "flyte", "flyteplugins-union")
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
    """Run `uctl selfserve provision-dataplane-resources`.

    TODO: once flyteplugins-union exposes a Dataplane/Selfserve API that can
    generate this values YAML via gRPC, drop the uctl subprocess. For now we
    shell out; the generated YAML is read from disk and returned as content so
    downstream tasks do not depend on this container's filesystem.

    Side effects: may also populate cfg.org_name from the uctl output table.
    """
    assert cfg.control_plane_url, "control_plane_url is required"
    assert cfg.cluster_name, "cluster_name is required"

    import glob
    import tempfile

    state = BaseInfraState()

    work_dir = tempfile.mkdtemp(prefix="union-e2e-provision-")
    logger.info(f"  Provisioning in temp dir: {work_dir}")

    # config init may open a browser for OAuth when running locally. In a
    # Flyte task container, UNION_API_KEY should already be set (via
    # decrypt_and_export_credentials), so uctl can pick it up non-interactively.
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

    # Read content into state so downstream tasks (possibly in different
    # containers) don't depend on this container's filesystem.
    with open(values_file) as _f:
        state.values_file_content = _f.read()
    logger.info(f"Generated values file: {values_file} ({len(state.values_file_content)} chars)")

    # Also persist a copy to the workspace for local debugging / reruns. This
    # is best-effort; remote tasks may not have a writable workspace dir.
    try:
        import shutil

        workspace = os.path.join(os.path.dirname(__file__), ".e2e-workspace")
        os.makedirs(workspace, exist_ok=True)
        dest = os.path.join(workspace, os.path.basename(values_file))
        shutil.copy2(values_file, dest)
        logger.info(f"  Copied to workspace: {dest}")
    except Exception as e:
        logger.info(f"  Skipped workspace copy: {e}")

    # Parse org name from the uctl output table
    if not cfg.org_name:
        for line in output.splitlines():
            if cfg.cluster_name in line and "|" in line:
                fields = [f.strip() for f in line.split("|")]
                if len(fields) >= 3 and fields[1]:
                    cfg.org_name = fields[1]
                    logger.info(f"  Parsed org name: {cfg.org_name}")
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
    """Run helm upgrade --install and create EAGER_API_KEY.

    values_file is a path on the current container's filesystem (helm needs a
    real file). Callers that carry YAML content via state should write a temp
    file before invoking this.
    """
    # If helm_values_override is a relative path and the chart was cloned locally,
    # resolve it relative to the chart directory.
    override_flag = ""
    if cfg.helm_values_override:
        override_path = cfg.helm_values_override
        if not os.path.isabs(override_path) and "/" not in override_path:
            # Might be a file inside the chart (e.g. "values-legacy.yaml")
            candidate = os.path.join(chart_ref, override_path) if os.path.isdir(chart_ref) else ""
            if candidate and os.path.exists(candidate):
                override_path = candidate
        override_flag = f'-f "{override_path}" '
        logger.info(f"  Using values override: {override_path}")

    _sh(
        f"helm upgrade --install {cfg.helm_release_name} {chart_ref} "
        f"{override_flag}"
        f'-f "{values_file}" '
        f"-n {cfg.helm_namespace} --create-namespace --wait --timeout 10m "
        f"--force-conflicts"
    )
    logger.info("Helm chart installed.")

    # Replaces: `uctl create apikey --keyName EAGER_API_KEY`.
    # ApiKey.create talks to the control plane directly; no uctl config state
    # required. Org is taken from the initialized flyte client.
    from flyteplugins.union.remote import ApiKey

    try:
        ApiKey.create(name="EAGER_API_KEY")
        logger.info("EAGER_API_KEY created.")
    except Exception as e:
        # Typically AlreadyExists on reruns — safe to proceed.
        logger.info(f"EAGER_API_KEY not created (likely exists): {e}")


def helm_uninstall(cfg: BaseConfig) -> list[str]:
    """Uninstall Helm release. Returns list of errors (empty = success)."""
    errors: list[str] = []
    if _sh_ok(f"helm status {cfg.helm_release_name} -n {cfg.helm_namespace}"):
        logger.info(f"Uninstalling Helm release {cfg.helm_release_name}...")
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

    NOTE: cluster-pool / cluster-pool-assignment / cluster-pool-attributes
    still shell out to uctl. Only Project has a usable Python API today;
    when the pool APIs land in flyteplugins-union, port them in and the need
    for uctl auth state in this task body disappears entirely.
    """
    import tempfile

    from flyte.remote import Project

    pool_name = cfg.cluster_name  # one pool per cluster, named after it
    org_flag = f"--org {cfg.org_name}" if cfg.org_name else ""

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
    logger.info(f"Cluster pool '{pool_name}' created/verified.")

    # Assign this cluster to the pool
    _sh(
        f"uctl create clusterpoolassignment "
        f"--poolName {pool_name} --clusterName {cfg.cluster_name} {org_flag}",
        check=False,  # may already be assigned
    )
    logger.info(f"Cluster '{cfg.cluster_name}' assigned to pool '{pool_name}'.")

    # 2. Create project via flyte.remote (no uctl needed).
    try:
        Project.create(
            id=cfg.test_project,
            name=cfg.test_project,
            description=f"E2E test project for cluster {cfg.cluster_name}",
        )
        logger.info(f"Project '{cfg.test_project}' created.")
    except Exception as e:
        # AlreadyExists on reruns — safe.
        logger.info(f"Project '{cfg.test_project}' not created (likely exists): {e}")

    # 3. Route the project to the cluster pool for all domains (uctl).
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
    logger.info(f"Cluster pool attributes set: {cfg.test_project} -> {pool_name}")


# =============================================================================
# Verification (Phase 4) — fully cloud-agnostic
# =============================================================================


def wait_for_healthy(cfg: BaseConfig) -> bool:
    """Poll the control plane until the cluster is enabled and healthy."""
    from flyteplugins.union.remote import Cluster

    deadline = time.time() + cfg.cluster_healthy_timeout
    while time.time() < deadline:
        try:
            cluster = Cluster.get(name=cfg.cluster_name)
        except Exception as e:
            # Cluster may not yet be registered with the control plane — keep polling.
            logger.info(f"  Cluster lookup failed ({e}); waiting...")
            time.sleep(15)
            continue

        if cluster.state == "enabled" and cluster.health == "healthy":
            logger.info(f"Cluster {cfg.cluster_name} is enabled and healthy.")
            # Opportunistically remember the org so later calls that need it
            # (e.g. _detect_org_name) don't have to re-fetch.
            if not cfg.org_name and cluster.organization:
                cfg.org_name = cluster.organization
            return True

        logger.info(f"  state={cluster.state} health={cluster.health}, waiting...")
        time.sleep(15)

    raise RuntimeError(
        f"Cluster {cfg.cluster_name} did not become healthy within {cfg.cluster_healthy_timeout}s"
    )


def _clean_workspace(name: str) -> str:
    """Create (or recreate) a clean workspace directory, removing stale .pyc files."""
    import shutil

    workspace = os.path.join(os.path.dirname(__file__), "e2e_workspace", name)
    if os.path.exists(workspace):
        shutil.rmtree(workspace)
    os.makedirs(workspace, exist_ok=True)
    return workspace


def run_example_workflow(cfg: BaseConfig) -> str:
    """Run a simple workflow with a unique input to avoid cache hits.

    Returns the run name on success.
    """
    import uuid

    workspace = _clean_workspace("hello_test")

    # Generate a script with a unique nonce input so cache never matches
    nonce = str(uuid.uuid4())
    script_path = os.path.join(workspace, "hello_e2e.py")
    with open(script_path, "w") as f:
        f.write('''\
import logging
import flyte

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flyte.e2e.hello")

env = flyte.TaskEnvironment(name="hello-e2e", cache="disable")

@env.task
async def say_hello(nonce: str) -> str:
    logger.info(f"Hello from e2e test! nonce={nonce}")
    return f"hello-{nonce}"

@env.task
async def main(nonce: str) -> str:
    result = await say_hello(nonce=nonce)
    logger.info(f"Workflow completed: {result}")
    return result
''')

    logger.info(f"Running hello workflow (nonce={nonce})")
    run_result = subprocess.run(
        f"flyte run "
        f"--project {cfg.test_project} "
        f"--domain development "
        f"--follow "
        f"{script_path} main --nonce {nonce}",
        shell=True,
        capture_output=True,
        text=True,
    )

    logger.info(run_result.stdout)
    if run_result.stderr:
        logger.info(run_result.stderr)

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
        logger.warning(f"flyte run exited with code {run_result.returncode} (workflow_failed={workflow_failed})")
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
    logger.info(f"Example workflow SUCCEEDED (run: {run_name})")
    return run_name


def _detect_org_name(cfg: BaseConfig) -> str:
    """Fetch the cluster's org from the control plane and cache it on cfg."""
    from flyteplugins.union.remote import Cluster

    try:
        cluster = Cluster.get(name=cfg.cluster_name)
    except Exception as e:
        logger.info(f"  Cluster.get failed in _detect_org_name: {e}")
        return ""
    if cluster.organization:
        cfg.org_name = cluster.organization
        return cluster.organization
    return ""


@dataclass
class TestResult:
    """Tracks the result of a single verification test."""
    name: str
    passed: bool = False
    error: str = ""


@dataclass
class E2EResult:
    """Full result of an E2E test run."""
    overall: str = ""  # "PASSED" or "FAILED"
    error: str = ""  # top-level error message if failed
    example_run_name: str = ""
    teardown_result: str = ""
    test_results: list[TestResult] = None

    def __post_init__(self):
        if self.test_results is None:
            self.test_results = []

    @property
    def passed(self) -> bool:
        return self.overall == "PASSED"

    @property
    def tests_passed(self) -> int:
        return sum(1 for t in self.test_results if t.passed)

    @property
    def tests_total(self) -> int:
        return len(self.test_results)

    def summary(self) -> str:
        lines = [f"E2E Result: {self.overall}"]
        if self.error:
            lines.append(f"  Error: {self.error}")
        if self.example_run_name:
            lines.append(f"  Example run: {self.example_run_name}")
        if self.test_results:
            lines.append(f"  Verification: {self.tests_passed}/{self.tests_total} passed")
            for t in self.test_results:
                status = "PASSED" if t.passed else "FAILED"
                line = f"    {t.name:<40} {status}"
                if t.error:
                    line += f"  {t.error[:80]}"
                lines.append(line)
        if self.teardown_result:
            lines.append(f"  Teardown: {self.teardown_result}")
        return "\n".join(lines)


def run_verification_tests(cfg: BaseConfig, run_name: str) -> list[TestResult]:
    """Run all post-workflow verification tests and return results."""
    tests = [
        ("Live & Persistent Logs", verify_logs),
        ("Inputs/Outputs", verify_io),
        ("Code Bundle Download & CORS", verify_code_bundle_cors),
        ("Remote Image Builder", verify_image_builder),
        ("Image Cache (No Rebuild)", verify_image_cache),
        ("Reusable Containers", verify_reusable_containers),
        ("App Deployment", verify_app_deployment),
    ]
    results: list[TestResult] = []
    for test_name, test_fn in tests:
        result = TestResult(name=test_name)
        try:
            test_fn(cfg, run_name)
            result.passed = True
        except Exception as e:
            result.error = str(e)[:200]
            logger.info(f"  TEST FAILED: {test_name}: {result.error}")
        results.append(result)

    # Print summary table
    logger.info("\n" + "=" * 70)
    logger.info(f"  {'Test':<40} {'Result':<10} {'Error'}")
    logger.info("-" * 70)
    for r in results:
        status = "PASSED" if r.passed else "FAILED"
        error_msg = "" if r.passed else r.error[:60]
        logger.info(f"  {r.name:<40} {status:<10} {error_msg}")
    logger.info("=" * 70)

    passed = sum(1 for r in results if r.passed)
    total = len(results)
    logger.info(f"  {passed}/{total} tests passed\n")

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
            logger.info(f"  Run metadata ready (attempt {attempt + 1})")
            return
        wait = 5 * (attempt + 1)
        logger.info(f"  Run metadata not ready yet, waiting {wait}s (attempt {attempt + 1}/6)...")
        time.sleep(wait)
    # Don't fail here — let the caller decide


def verify_logs(cfg: BaseConfig, run_name: str) -> None:
    """Live & Persistent Logs test: get logs, delete pods, get logs again."""
    logger.info(f"\n--- Test: Live & Persistent Logs (run={run_name}) ---")
    domain = "development"

    # Wait for run metadata to be available
    _wait_for_run_metadata(cfg, run_name, domain)

    # 1. Get logs while pods are still around
    logger.info("Getting logs (live)...")
    output1 = _sh(
        f"flyte get logs {run_name} --project {cfg.test_project} --domain {domain}",
        check=False,
    )
    if not output1.strip() or "NOT FOUND" in output1 or "NOT_FOUND" in output1:
        raise RuntimeError(f"No logs returned for run {run_name} (live)")
    logger.info("  Live logs: OK")

    # 2. Delete the pods for this run
    logger.info("Deleting run pods...")
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
    logger.info("Getting logs (persistent, after pod deletion)...")
    output2 = _sh(
        f"flyte get logs {run_name} --project {cfg.test_project} --domain {domain}",
        check=False,
    )
    if not output2.strip():
        raise RuntimeError(f"No logs returned for run {run_name} after pod deletion (persistent logs missing)")
    logger.info("  Persistent logs: OK")
    logger.info("--- Live & Persistent Logs: PASSED ---")


def verify_io(cfg: BaseConfig, run_name: str) -> None:
    """Inputs/Outputs test: verify flyte get io returns data."""
    logger.info(f"\n--- Test: Inputs/Outputs (run={run_name}) ---")
    domain = "development"

    output = _sh(
        f"flyte get io {run_name} --project {cfg.test_project} --domain {domain}",
        check=False,
    )
    if not output.strip():
        raise RuntimeError(f"No I/O data returned for run {run_name}")
    logger.info(f"  I/O data returned ({len(output)} chars)")
    logger.info("--- Inputs/Outputs: PASSED ---")


def verify_code_bundle_cors(cfg: BaseConfig, run_name: str) -> None:
    """Code bundle download & CORS test.

    1. Get an access token from keyring
    2. POST to CreateDownloadLinkV2 to get a presigned URL for the code bundle
    3. Verify the presigned URL is downloadable and has correct CORS headers
    """
    import re
    import urllib.parse
    import urllib.request

    logger.info(f"\n--- Test: Code Bundle Download & CORS (run={run_name}) ---")
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
    logger.info(f"  Access token: found ({len(token)} chars)")

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
    logger.info(f"  Presigned URL obtained ({len(signed_url)} chars)")

    # 4. HEAD request with Origin header to verify CORS
    cors_origin = cp_base
    # 4. GET the file with Origin header — verifies both download and CORS
    logger.info(f"  Using cors_origin ({cors_origin})")
    get_req = urllib.request.Request(
        signed_url,
        headers={"Origin": cors_origin},
        method="GET",
    )
    try:
        with urllib.request.urlopen(get_req) as resp:
            data = resp.read()
            cors_header = resp.getheader("Access-Control-Allow-Origin", "")
            content_length = resp.getheader("Content-Length", str(len(data)))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GET on presigned URL failed ({e.code})")

    logger.info(f"  GET response: {len(data)} bytes, CORS={cors_header}")
    if len(data) == 0:
        raise RuntimeError("Code bundle is empty")
    if not cors_header:
        raise RuntimeError(
            f"No Access-Control-Allow-Origin header on presigned URL. "
            f"CORS may not be configured on the storage bucket."
        )
    logger.info(f"  CORS header: {cors_header} — OK")

    logger.info("--- Code Bundle Download & CORS: PASSED ---")


# =============================================================================
# Image builder & reusable container tests
# =============================================================================


def _run_flyte_script(
    cfg: BaseConfig, script_path: str, entrypoint: str = "main", timeout: int = 600,
) -> str:
    """Run a flyte script remotely and return the run name. Raises on failure.

    Args:
        timeout: Maximum seconds to wait for the run to complete (default 10 min).
    """
    import re

    try:
        result = subprocess.run(
            f"flyte run "
            f"--project {cfg.test_project} "
            f"--domain development "
            f"--follow "
            f"{script_path} {entrypoint}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        combined = (e.stdout or b"").decode(errors="replace") + (e.stderr or b"").decode(errors="replace")
        logger.info(combined[:5000])
        raise RuntimeError(f"Script timed out after {timeout}s:\n{combined[-500:]}")
    combined = (result.stdout or "") + (result.stderr or "")
    logger.info(combined[:5000])

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
    logger.info("\n--- Test: Remote Image Builder ---")
    import uuid

    # Use a path without dots — Python treats dotted dirs as relative imports
    workspace = _clean_workspace("image_builder_test")

    # Write a file with a random string so the image hash changes every run
    unique_marker = str(uuid.uuid4())
    marker_file = os.path.join(workspace, "build_marker.txt")
    with open(marker_file, "w") as f:
        f.write(unique_marker)

    # Write the test script
    script_path = os.path.join(workspace, "image_build_test.py")
    with open(script_path, "w") as f:
        f.write(f'''\
import logging
from pathlib import Path
import flyte

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flyte.e2e.image_build")

image = (
    flyte.Image.from_debian_base()
    .with_pip_packages("requests")
    .with_source_file(Path("{marker_file}"))
)

env = flyte.TaskEnvironment(name="image-builder-e2e", image=image, cache="disable")

@env.task
async def main(nonce: str) -> str:
    marker = Path("build_marker.txt").read_text()
    logger.info(f"Built with marker: {{marker}}, nonce: {{nonce}}")
    return f"Built with marker: {{marker}}"
''')

    logger.info(f"  Marker: {unique_marker}")
    logger.info("  Running with unique source file (should trigger image build)...")
    run_name = _run_flyte_script(cfg, script_path, entrypoint=f"main --nonce {unique_marker}")

    if not run_name:
        raise RuntimeError("Could not parse run name from image builder test")
    logger.info(f"  Image build test run: {run_name}")
    logger.info("--- Remote Image Builder: PASSED ---")


def verify_image_cache(cfg: BaseConfig, _run_name: str) -> None:
    """Image Cache test: run the same image twice, second should skip build."""
    logger.info("\n--- Test: Image Cache (No Rebuild) ---")

    import uuid

    workspace = os.path.join(os.path.dirname(__file__), "e2e_workspace", "image_cache_test")
    workspace = _clean_workspace("image_cache_test")

    # Write a script with an image hash that is stable within this E2E run (so run 2
    # hits the image cache from run 1), but different across E2E setups (so stale
    # build cache from a torn-down cluster doesn't interfere). We embed the cluster
    # name as an env var in the image — this changes the image hash per cluster.
    script_path = os.path.join(workspace, "image_cache_test.py")
    with open(script_path, "w") as f:
        f.write(f'''\
import logging
import flyte

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flyte.e2e.image_cache")

image = (
    flyte.Image.from_debian_base()
    .with_pip_packages("requests==2.32.3")
    .with_env_vars({{"E2E_CLUSTER": "{cfg.cluster_name}"}})
)

env = flyte.TaskEnvironment(name="image-cache-e2e", image=image, cache="disable")

@env.task
async def main(nonce: str) -> str:
    import requests
    logger.info(f"requests version: {{requests.__version__}}, nonce: {{nonce}}")
    return f"requests version: {{requests.__version__}}"
''')

    nonce1 = str(uuid.uuid4())
    nonce2 = str(uuid.uuid4())

    # First run — may or may not build the image
    logger.info("  Run 1 (may build)...")
    run1 = _run_flyte_script(cfg, script_path, entrypoint=f"main --nonce {nonce1}")
    logger.info(f"  Run 1 completed: {run1}")

    # Second run — same image, different nonce. Image should be cached.
    logger.info("  Run 2 (should skip build)...")
    result2 = subprocess.run(
        f"flyte run "
        f"--project {cfg.test_project} "
        f"--domain development "
        f"--follow "
        f"{script_path} main --nonce {nonce2}",
        shell=True,
        capture_output=True,
        text=True,
    )
    import re

    combined2 = (result2.stdout or "") + (result2.stderr or "")
    ansi_clean2 = re.sub(r"\x1b\[[0-9;]*m", "", combined2)
    logger.info(ansi_clean2[:5000])

    # Check that the second run skipped the build
    if "already exists, skipping build" in ansi_clean2:
        logger.info("  Image cache hit confirmed: 'already exists, skipping build'")
    elif "Building" not in ansi_clean2:
        logger.info("  No build step detected (image was cached)")
    else:
        logger.info("  WARNING: Second run may have rebuilt the image (check output above)")

    failure_indicators = [
        "FAILED", "exited unsuccessfully", "Traceback (most recent call last)",
        "Filtered traceback (most recent call last)", "RuntimeError:",
        "TypeError:", "ActionPhase.FAILED",
    ]
    if result2.returncode != 0 or any(ind in ansi_clean2 for ind in failure_indicators):
        raise RuntimeError(f"Second run failed (exit {result2.returncode}):\n{ansi_clean2[-500:]}")

    logger.info("--- Image Cache (No Rebuild): PASSED ---")


def verify_reusable_containers(cfg: BaseConfig, _run_name: str) -> None:
    """Reusable Containers test: run the reusable example from flyte-sdk."""
    logger.info("\n--- Test: Reusable Containers ---")

    workspace = os.path.join(os.path.dirname(__file__), ".e2e-workspace")
    sdk_dir = os.path.join(workspace, "flyte-sdk")
    reuse_src = os.path.join(sdk_dir, "examples", "reuse", "reusable.py")

    if not os.path.exists(reuse_src):
        _sh(f"cd {sdk_dir} && git sparse-checkout add examples/reuse", check=False)

    if not os.path.exists(reuse_src):
        raise RuntimeError(f"Reusable example not found: {reuse_src}")

    # Copy to a clean path without dots to avoid Python import issues
    import shutil

    clean_dir = _clean_workspace("reuse_test")
    clean_path = os.path.join(clean_dir, "reusable.py")
    shutil.copy2(reuse_src, clean_path)

    logger.info(f"  Running: {clean_path}")
    import random
    n = random.randint(3, 10)
    run_name = _run_flyte_script(cfg, clean_path, entrypoint=f"main --n {n}")

    if not run_name:
        raise RuntimeError("Could not parse run name from reusable containers test")
    logger.info(f"  Reusable containers run: {run_name}")
    logger.info("--- Reusable Containers: PASSED ---")


def verify_app_deployment(cfg: BaseConfig, _run_name: str) -> None:
    """App Deployment test: deploy a FastAPI app, verify internal + public endpoints."""
    logger.info("\n--- Test: App Deployment ---")
    import re
    import urllib.request

    workspace = _clean_workspace("app_deploy_test")

    # Write a script that deploys a FastAPI app, tests it internally, and prints the public URL
    script_path = os.path.join(workspace, "app_deploy_test.py")
    with open(script_path, "w") as f:
        f.write('''\
import logging
import typing
import fastapi
import flyte
import flyte.app.extras

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flyte.e2e.app_deploy")

app = fastapi.FastAPI()

@app.get("/")
async def root() -> str:
    return "e2e-app-ok"

@app.get("/health")
async def health() -> dict:
    return {"status": "healthy", "source": "e2e-test"}

app_env = flyte.app.extras.FastAPIAppEnvironment(
    name="e2e-app-deploy",
    app=app,
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn", "httpx"),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

task_env = flyte.TaskEnvironment(
    name="e2e-app-deploy-tester",
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn", "httpx"),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    depends_on=[app_env],
)

class AppDeployResult(typing.NamedTuple):
    internal_url: str
    public_url: str

@task_env.task
async def main() -> AppDeployResult:
    import httpx

    await flyte.init_in_cluster.aio()
    deployed = flyte.serve(app_env)
    internal_url = app_env.endpoint
    public_url = deployed.endpoint
    logger.info(f"internal url: {internal_url}. public url: {public_url}")

    try:
        # Test internal endpoints
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{internal_url}/")
            assert resp.status_code == 200, f"Root endpoint [{internal_url}] returned {resp.status_code}: {resp.text}"
            logger.info(f"GET / -> {resp.status_code}")
            assert "e2e-app-ok" in resp.text, f"Unexpected response: {resp.text}"

            resp = await client.get(f"{internal_url}/health")
            assert resp.status_code == 200, f"Health endpoint [{internal_url}/health] returned {resp.status_code}: {resp.text}"
            body = resp.json()
            assert body.get("status") == "healthy", f"Unexpected health response: {body}"
            logger.info(f"GET /health -> {resp.status_code}")
    finally:
        # Always deactivate the app, whether tests pass or fail
        logger.info("Deactivating app...")
        deployed.deactivate(wait=True)
        logger.info("App deactivated.")

    return AppDeployResult(internal_url=internal_url, public_url=public_url)
''')

    logger.info("  Deploying FastAPI app and testing internal endpoints (timeout: 180s)...")
    try:
        result = subprocess.run(
            f"flyte run "
            f"--project {cfg.test_project} "
            f"--domain development "
            f"--follow "
            f"{script_path} main",
            shell=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired as e:
        combined = (e.stdout or b"").decode(errors="replace") + (e.stderr or b"").decode(errors="replace")
        ansi_clean = re.sub(r"\x1b\[[0-9;]*m", "", combined)
        logger.info(ansi_clean[:5000])
        raise RuntimeError(f"App deployment timed out after 180s:\n{ansi_clean[-500:]}")
    combined = (result.stdout or "") + (result.stderr or "")
    ansi_clean = re.sub(r"\x1b\[[0-9;]*m", "", combined)
    logger.info(ansi_clean[:5000])

    failure_indicators = [
        "FAILED", "exited unsuccessfully", "Traceback (most recent call last)",
        "Filtered traceback (most recent call last)", "RuntimeError:",
        "TypeError:", "ActionPhase.FAILED",
    ]
    if result.returncode != 0 or any(ind in ansi_clean for ind in failure_indicators):
        raise RuntimeError(f"App deployment failed:\n{ansi_clean[-500:]}")

    run_match = re.search(r"Created Run:\s+([a-z0-9]+)", ansi_clean)
    run_name = run_match.group(1) if run_match else ""
    logger.info(f"  Internal endpoints verified (run: {run_name})")

    # Get the public URL from the task output via flyte get io
    # The task returns AppDeployResult(internal_url=..., public_url=...)
    public_url = ""
    if run_name:
        _wait_for_run_metadata(cfg, run_name)
        io_output = _sh(
            f"flyte get io {run_name} --project {cfg.test_project} --domain development",
            check=False,
        )
        io_clean = re.sub(r"\x1b\[[0-9;]*m", "", io_output)
        # Look for the public_url field in the output
        url_match = re.search(r"public_url['\"]?\s*[:=]\s*['\"]?(https?://\S+)", io_clean)
        if url_match:
            public_url = url_match.group(1).rstrip("'\")")
        # Fallback: look for any https URL that looks like an app endpoint
        if not public_url:
            url_match = re.search(r"(https?://\S+/apps/\S+)", io_clean)
            if url_match:
                public_url = url_match.group(1).rstrip("'\")")

    if not public_url:
        logger.info("  WARNING: Could not parse public URL — skipping external verification")
        logger.info("--- App Deployment: PASSED (internal only) ---")
        return

    logger.info(f"  Public URL: {public_url}")

    # Test the public URL from outside the cluster (requires auth)
    try:
        import keyring
    except ImportError:
        _sh("pip install keyring", check=False)
        import keyring

    cp_host = cfg.control_plane_url.replace("https://", "").replace("http://", "").rstrip("/")
    token = keyring.get_password(cp_host, "access_token")

    if not token:
        logger.info("  WARNING: No auth token — skipping public URL verification")
        logger.info("--- App Deployment: PASSED (internal only) ---")
        return

    logger.info("  Testing public URL from outside the cluster...")
    req = urllib.request.Request(
        public_url,
        headers={"Authorization": f"Bearer {token}"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
            status = resp.status
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Public URL returned {e.code}: {e.read().decode()[:200]}")
    except Exception as e:
        raise RuntimeError(f"Public URL request failed: {e}")

    if status != 200:
        raise RuntimeError(f"Public URL returned status {status}")
    if "e2e-app-ok" not in body:
        raise RuntimeError(f"Public URL unexpected response: {body[:200]}")

    logger.info(f"  Public URL responded: {status} OK")
    logger.info("--- App Deployment: PASSED (internal + public) ---")


# =============================================================================
# Key setup helper
# =============================================================================


def setup_keys_impl() -> str:
    """Generate RSA key pair and push private key as a Flyte secret."""
    import flyte
    import flyte.remote as remote

    _generate_key_pair()

    logger.info(f"\nPushing private key as Flyte secret '{_FLYTE_SECRET_NAME}'...")
    flyte.init_from_config()
    remote.Secret.create(
        name=_FLYTE_SECRET_NAME,
        value=_PRIVATE_KEY_PATH.read_bytes(),
        type="regular",
    )
    logger.info(f"Secret '{_FLYTE_SECRET_NAME}' created.")

    return f"Key pair in {_KEYS_DIR}/, secret '{_FLYTE_SECRET_NAME}' created."
