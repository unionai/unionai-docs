# Union selfmanaged E2E scripts

End-to-end test harness for a Union selfmanaged (BYOC) dataplane on AWS.
Provisions the underlying cloud infra, deploys the Union helm chart, wires
up cluster-pool routing for a test project, and (optionally) runs a smoke
+ verification suite.

## Layout

```
scripts/
├── selfmanaged_common.py   # shared dataclasses, helpers, control-plane calls
├── selfmanaged_aws_e2e.py  # AWS tasks + main / teardown_cluster entrypoints
├── smoke_tests.py          # post-deploy verification suite (SDK-only)
├── _smoke_hello.py         # isolated hello task — kept small so flyte.run
│                           # bundles just this file for remote submission
├── selfmanaged_gcp_e2e.py  # (stub — GCP port is a follow-up)
└── pyproject.toml
```

## Prerequisites

Local tools:

```bash
brew install awscli eksctl helm kubectl uv
brew upgrade uctl        # >= 0.1.20, needs `selfserve` subcommand
```

Python env (3.13+):

```bash
cd scripts
uv venv --python 3.13 .venv
source .venv/bin/activate
uv pip install -e .
```

AWS + Union auth:

```bash
# Fresh STS session each time (expires in 12h):
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...
# Union control plane (PKCE is auto-initialized from your keyring):
uctl config init --host=<your-control-plane-url>
```

## Deploy a dataplane

```bash
flyte run --local --tui \
    selfmanaged_aws_e2e.py main \
    --control_plane_url https://myorg.union.ai \
    --cluster_name my-test-cluster
```

`--tui` opens a live tree of tasks/traces with timings, logs and a link to
each running resource — strongly recommended. If you omit `--tui` the output
goes straight to stdout instead.

Useful flags on `main`:

| flag | default | purpose |
|---|---|---|
| `--skip_teardown` | off | leave AWS infra in place after the run (for iteration) |
| `--skip_smoke_tests` | off | skip Phase 3's run_smoke_suite (handy while debugging deploy) |
| `--aws_region` | `us-east-2` | EKS region |
| `--helm_values_override` | `""` | extra `-f` file to layer on top of the generated values.yaml |

The four phases are:

1. **Infrastructure** — `asyncio.gather` over provision_dataplane, EKS,
   S3×2, ECR; then IAM role with IRSA trust policy.
2. **Deploy** — patch values.yaml in Python (pyyaml, no yq), `helm upgrade
   --install --wait --take-ownership`; a live `[pods]` watcher prints the
   namespace's pods every 15s while helm blocks.
3. **Verify** — wait cluster healthy, create project + cluster-pool
   routing, `run_smoke_suite` (hello + 7 verifications, all submitted via
   `flyte.run.aio`).
4. **Teardown** — reverse-order delete; runs in `finally` unless
   `--skip_teardown`.

## Tear down only

If a run failed mid-way and you just want the infra gone:

```bash
flyte run --local --tui \
    selfmanaged_aws_e2e.py teardown_cluster \
    --control_plane_url https://myorg.union.ai \
    --cluster_name my-test-cluster
```

This short-circuits Phases 1–3, resolves the AWS account id from the
ambient identity, and deletes everything `cluster_name` implied (EKS, S3,
ECR, IAM role + policies, helm release).

## Running smoke tests standalone

`smoke_tests.py` is importable from `main` but also runs standalone — for
poking at an already-deployed cluster without re-deploying:

```bash
python -m smoke_tests \
    --control_plane_url https://myorg.union.ai \
    --cluster_name my-test-cluster
```

Covers: hello smoke + logs, I/O, CORS, image builder, image cache,
reusable containers, app deployment (FastAPI).

## Remote execution (advanced)

When the user machine can't reach the dataplane directly, submit `main` as
a remote run. The bootstrap flow stashes your local AWS creds as a Flyte
Secret; the remote task reads them via env-var injection.

```bash
# One-time per STS rotation:
flyte run --local --tui selfmanaged_common.py stash_credentials

# Kick off remote:
flyte run --local --tui selfmanaged_aws_e2e.py launch_remote \
    --control_plane_url https://myorg.union.ai \
    --cluster_name my-test-cluster
```

## Troubleshooting

- **`SelectCluster failed ... Not Found`** during code-bundle upload —
  cluster-pool-attributes aren't set for (project, domain). Check your
  identity has `action_view_flyte_inventory` on projects in the org; `uctl
  update cluster-pool-attributes` silently fails on the pre-fetch
  otherwise. Workaround: `--skip_smoke_tests`.
- **`PermissionDenied [action_view_flyte_inventory]`** — same as above.
- **`Identity is not permitted to perform action on resource`** at helm
  install — your EKS kubeconfig isn't pointing at the new cluster. The
  `create_eks` task runs `aws eks update-kubeconfig` but a stale
  `~/.kube/config` can shadow it; re-run or check `kubectl config
  current-context`.
- **`no nodegroups found`** — `create_eks` adopts an existing EKS control
  plane but expects a managed nodegroup; will create one automatically if
  missing. Takes ~5–10 min.
- **Cached replays** — flyte local-persistence may replay a prior task
  output. `cache="disable"` is set on `main` and `teardown_cluster`. To
  force a fully fresh run: `rm -rf /tmp/flyte/metadata /tmp/flyte/raw_data
  ~/.flyte/local-cache/cache.db`.
