# GCP path

Source of truth: `scripts/selfmanaged_gcp_e2e.py` and
`content/deployment/selfmanaged/selfmanaged-gcp/`.

The script is the deterministic deploy. It provisions GKE, two GCS
buckets, an Artifact Registry repo, Workload Identity bindings, then
runs the helm install and smoke suite — same four-phase shape as AWS.

## Cloud-specific prereqs

```bash
gcloud --version            # google-cloud-sdk; any modern version
gcloud components list --filter='id:gke-gcloud-auth-plugin AND state:Installed' \
  --format='value(id)'      # must print 'gke-gcloud-auth-plugin'
```

Install missing tools:

```bash
brew install --cask google-cloud-sdk
gcloud components install gke-gcloud-auth-plugin
```

## Auth verification

```bash
gcloud auth application-default print-access-token >/dev/null && echo OK
```

If this fails, the user needs application-default credentials:

```bash
gcloud auth application-default login
```

Confirm the active project matches what the user provided:

```bash
gcloud config get-value project
```

If the user didn't pin a `project_id` at intent capture, ask now —
**don't pick the gcloud-default**. The script accepts an empty
`project_id` and resolves from gcloud, but the skill should make the
choice explicit so the user can't be surprised.

## Union API key

GCP local runs need `UNION_API_KEY` exported (the AWS path uses STS env
vars instead). Verify:

```bash
test -n "$UNION_API_KEY" && echo "set" || echo "missing"
```

If missing, the user creates one in the Union console under "API keys"
for their org and exports it:

```bash
export UNION_API_KEY=<the-key>
```

## Python venv

Same as AWS — see `aws.md` "Python venv" section. The same `scripts/.venv`
is used for both clouds.

## Deploy

```bash
flyte run --local --tui \
    selfmanaged_gcp_e2e.py main \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME> \
    --project_id <GCP_PROJECT_ID> \
    --region <GCP_REGION>
```

Defaults: `region=us-central1`. Confirm both with the user — don't
assume.

Optional flags (same semantics as AWS):

| Flag | When to use |
|---|---|
| `--skip_teardown` | Keep infra after run for iteration. |
| `--skip_smoke_tests` | Skip Phase 3 verification. |
| `--helm_values_override <file>` | Custom values overlay. |
| `--dataplane_image_sha <sha>` | Pin dataplane image. |
| `--helm_chart_branch <branch>` | Test WIP `unionai/helm-charts` branch. |

Phases are identical to AWS (infra → deploy → verify → teardown). The
infra phase fans out: provision dataplane, GKE, GCS metadata, GCS
fast-registration, Artifact Registry — then sets up Workload Identity
bindings.

## Smoke-only mode

```bash
source scripts/.venv/bin/activate
cd scripts
python -m smoke_tests \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME>
```

(`smoke_tests.py` is cloud-agnostic — same module the AWS path uses.)

## Teardown

```bash
flyte run --local --tui \
    selfmanaged_gcp_e2e.py teardown_cluster \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME> \
    --project_id <GCP_PROJECT_ID> \
    --region <GCP_REGION>
```

Resolves the project from the config and deletes GKE, both GCS buckets,
the Artifact Registry repo, Workload Identity bindings, and the helm
release.

## GCP-specific gotchas

- **Remote runs are not yet supported.** The script's docstring is
  explicit: shared `stash_credentials` only carries AWS STS today.
  GCP runs must stay `--local`. If the user's machine can't reach the
  GKE control plane, walk them through opening the cluster's authorized
  networks rather than trying remote execution.
- **`gke-gcloud-auth-plugin` missing** silently produces "executable not
  found" from kubectl after cluster creation. The prereq check above
  catches this — don't skip it.
- **Project-level Artifact Registry** — the script creates a regional
  AR repo. If the user wants a multi-region or differently-named repo,
  use `--helm_values_override` rather than editing the script.
- **Cached replays** — same as AWS: `rm -rf /tmp/flyte/metadata
  /tmp/flyte/raw_data ~/.flyte/local-cache/cache.db`.
