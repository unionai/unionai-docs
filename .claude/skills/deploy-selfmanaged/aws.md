# AWS path

Source of truth: `scripts/selfmanaged_aws_e2e.py` and
`content/deployment/selfmanaged/selfmanaged-aws/`.

The script is the deterministic deploy — do not hand-roll the helm
sequence on AWS unless the user explicitly asks (in which case point
them at `content/deployment/selfmanaged/selfmanaged-aws/deploy-dataplane.md`).

## Cloud-specific prereqs

Run as a batch:

```bash
aws --version           # AWS CLI v2
eksctl version          # >= 0.190 (script targets 0.204)
```

Install missing tools:

```bash
brew install awscli eksctl
```

## Auth verification

Two checks — both required:

```bash
# 1. AWS CLI can authenticate (covers SSO, profiles, env vars):
aws sts get-caller-identity

# 2. STS env vars are exported (the e2e script reads these directly,
#    not the AWS config file or SSO cache):
test -n "$AWS_ACCESS_KEY_ID" && test -n "$AWS_SECRET_ACCESS_KEY" \
  && echo "STS env vars set" \
  || echo "MISSING — export STS env vars"
```

Both must pass. The first proves the user is authenticated to AWS at
all; the second proves the e2e script (`selfmanaged_common.py:310`,
`hydrate_credentials`) can read creds from `os.environ`.

**If the user is SSO-authenticated** (Identity Center / federated
roles), check #1 will succeed but check #2 will fail. They need to
materialize STS creds into env vars. Common patterns:

- Use the `Get credentials` button in the AWS access portal and copy
  the "Set credentials in your terminal" block.
- `aws configure export-credentials --profile <sso-profile> --format env`
  then `eval` the output.

After exporting, re-run check #2 to confirm.

**Token expiry.** STS session tokens expire (~1–12h depending on the
issuer). If a re-run the next day fails mid-deploy with `ExpiredToken`,
re-export and resume. The script is idempotent — already-created
resources will be detected and skipped.

## Python venv (one-time per checkout)

The flyte e2e script runs in a 3.13 venv under `scripts/.venv`. Check
first:

```bash
test -d scripts/.venv && echo "venv exists" || echo "needs bootstrap"
```

If missing, bootstrap:

```bash
cd scripts
uv venv --python 3.13 .venv
source .venv/bin/activate
uv pip install -e .
```

Confirm `flyte` is importable:

```bash
source scripts/.venv/bin/activate && python -c "import flyte; print(flyte.__version__)"
```

## Deploy

Show this command, get confirmation, then run from `scripts/` with the
venv activated:

```bash
flyte run --local --tui \
    selfmanaged_aws_e2e.py main \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME> \
    --aws_region <AWS_REGION>
```

`--tui` is strongly recommended — it shows a live tree of tasks with
timings, logs, and links. Without `--tui`, output streams to stdout.

Optional flags (offer if relevant; do not enable by default):

| Flag | When to use |
|---|---|
| `--skip_teardown` | User wants to keep infra after the run for iteration. |
| `--skip_smoke_tests` | Smoke suite is hitting the cluster-pool-attributes permission issue, or user only wants infra+deploy validated. |
| `--helm_values_override <file>` | User has a custom values file to layer on top. |
| `--dataplane_image_sha <sha>` | Pin a specific dataplane image. |
| `--helm_chart_branch <branch>` | Test a WIP branch of `unionai/helm-charts`. |

The four phases the user will see in the TUI:

1. **Infrastructure** — provision dataplane (control-plane call), create
   EKS, two S3 buckets, ECR repo, IAM role with IRSA trust policy. Runs
   in parallel via `asyncio.gather`.
2. **Deploy** — patch `values.yaml` in Python, `helm upgrade --install
   --wait --take-ownership`. A live `[pods]` watcher prints namespace
   pods every 15s while helm blocks.
3. **Verify** — wait cluster healthy, create test project + cluster-pool
   routing, run the smoke suite (hello + 7 verifications, all submitted
   via `flyte.run.aio`).
4. **Teardown** — reverse-order delete in `finally`, unless
   `--skip_teardown`.

## Smoke-only mode

For a cluster that's already deployed (e.g. iterating on platform
features without re-running infra):

```bash
source scripts/.venv/bin/activate
cd scripts
python -m smoke_tests \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME>
```

Covers: hello smoke + logs, I/O, CORS, image builder, image cache,
reusable containers, app deployment (FastAPI).

## Teardown

```bash
flyte run --local --tui \
    selfmanaged_aws_e2e.py teardown_cluster \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME> \
    --aws_region <AWS_REGION>
```

Resolves account id from ambient AWS identity and deletes everything
`cluster_name` implied: EKS cluster + nodegroup, both S3 buckets, ECR
repo, IAM role + attached policies, helm release.

Show the command, confirm, then run.

## AWS-specific gotchas

- **Stale kubeconfig** can mask helm-install permission errors. The
  `create_eks` task runs `aws eks update-kubeconfig` but a pre-existing
  `~/.kube/config` entry can shadow it. If helm install fails with
  permission errors, run `kubectl config current-context` — it should
  point at the new EKS cluster.
- **Adopting an existing EKS cluster**: `create_eks` adopts an existing
  control plane but expects a managed nodegroup. If missing, it creates
  one (~5–10 min). Don't interrupt this.
- **Cached replays** — flyte's local-persistence may replay a prior task
  output even with `cache="disable"` set. To force a fully fresh run:
  `rm -rf /tmp/flyte/metadata /tmp/flyte/raw_data ~/.flyte/local-cache/cache.db`.

## Remote execution (advanced; only if user asks)

If the user's machine can't reach the dataplane directly, submit `main`
as a remote run. Stash AWS creds as a Flyte Secret, then launch:

```bash
flyte run --local --tui selfmanaged_common.py stash_credentials
flyte run --local --tui selfmanaged_aws_e2e.py launch_remote \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME>
```

Re-stash on every STS rotation.
