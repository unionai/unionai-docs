---
name: deploy-selfmanaged
description: |
  Deploy a Union self-managed (BYOC) data plane to a customer Kubernetes
  cluster on AWS, GCP, Azure, OCI, CoreWeave, or generic Kubernetes. Walks
  the user through prereqs, verifies each one before continuing, then runs
  the deterministic deploy path for their cloud (e2e script for AWS/GCP,
  guided helm walkthrough for the rest). Also handles teardown and
  smoke-only modes.

  Trigger when the user says "deploy a self-managed cluster", "set up a
  BYOC dataplane", "spin up Union on <cloud>", "tear down my self-managed
  cluster", or asks for help with anything under
  content/deployment/selfmanaged/.
---

# deploy-selfmanaged

Self-managed (BYOC) deployments stand up a Union data plane on a customer's
own Kubernetes cluster. Two paths exist depending on cloud:

| Cloud | Path | Source of truth |
|---|---|---|
| AWS | flyte e2e script | `scripts/selfmanaged_aws_e2e.py` |
| GCP | flyte e2e script | `scripts/selfmanaged_gcp_e2e.py` |
| Azure | guided walkthrough | `content/deployment/selfmanaged/selfmanaged-azure/` |
| OCI | guided walkthrough | `content/deployment/selfmanaged/selfmanaged-oci/` |
| CoreWeave | guided walkthrough | `content/deployment/selfmanaged/selfmanaged-coreweave/` |
| Generic K8s | guided walkthrough | `content/deployment/selfmanaged/selfmanaged-generic/` |

Architecture and cluster sizing context lives at
`content/deployment/selfmanaged/architecture/` and
`content/deployment/selfmanaged/cluster-recommendations.md`. Read those if
the user asks "what am I about to install" before running anything.

---

## Operating rules (read every time)

These rules apply to every cloud path. Do not relax them.

1. **Never run a cloud-mutating command without showing it first and
   getting explicit "yes" from the user.** This includes `eksctl create`,
   `gcloud container clusters create`, `az aks create`, `helm install`,
   any `aws|gcloud|az|oci ... delete`, and the e2e `main` / `teardown_cluster`
   tasks. Read-only commands (`aws sts get-caller-identity`,
   `kubectl get nodes`, `helm list`, etc.) may run without confirmation.
2. **Never invent values.** If the user has not given you
   `control_plane_url`, `cluster_name`, region/project/subscription, or
   credentials, ask. Do not pick a default cluster name or region.
3. **Failed prereq → halt.** If a verification step fails, stop and tell
   the user the exact command to fix it. Never try to "work around" a
   missing tool, expired token, or unauthenticated CLI.
4. **One cluster, one run.** Don't loop or batch across multiple clusters
   in a single skill invocation. If the user wants two clusters, run the
   skill twice.
5. **Re-runnability.** Both e2e scripts are idempotent and the manual
   walkthroughs note "skip if already created" at each step. If a step
   appears already done, confirm with the user and skip — don't re-create.

---

## Step 1 — Capture intent

All five fields are required before doing anything except read-only doc
lookups.

Use **`AskUserQuestion`** for the two enums (cloud + mode) — they're
multiple-choice and benefit from a UI. Then **prompt in plain text** for
the free-form values (URL, cluster name, region) in the same response,
since AskUserQuestion is multi-choice only and forcing free-form fields
into "Other" is awkward.

If the user already supplied any of these in their initial message, skip
asking that one.

1. **Cloud** — one of: `aws`, `gcp`, `azure`, `oci`, `coreweave`, `generic`.
   *(AskUserQuestion)*
2. **Mode** — one of:
   - `deploy` — full prepare-infra + deploy-dataplane + smoke (default).
   - `teardown` — remove a previously deployed cluster.
   - `smoke-only` — re-run the smoke suite against an already-deployed
     cluster (AWS/GCP only — see `aws.md` / `gcp.md` for invocation).
   *(AskUserQuestion)*
3. **Control plane URL** — e.g. `https://myorg.union.ai`. Ask the user
   if unsure; do not guess from `git remote` or memory. *(free-form)*
4. **Cluster name** — the name registered with the Union control plane.
   Coordinate with Union if the user doesn't have one. *(free-form)*
5. **Region / project / subscription** — cloud-specific, free-form:
   - aws: `aws_region` (script default `us-east-2` — confirm, don't assume).
   - gcp: `project_id` + `region` (default `us-central1`).
   - azure: `SUBSCRIPTION_ID` + `LOCATION` + `RESOURCE_GROUP`.
   - oci/coreweave/generic: see the cloud's `prepare-infra.md`.

Echo the captured intent back to the user as a single block before moving
to Step 2. Example:

```
Plan:
  cloud:             aws
  mode:              deploy
  control plane:     https://myorg.union.ai
  cluster name:      my-test-cluster
  region:            us-east-2
```

---

## Step 2 — Universal prereqs

Required for every cloud. Run these as a batch and report pass/fail per
tool. **Halt on any failure** with the install command.

```bash
helm version --short        # expect: v3.x or newer
kubectl version --client    # expect: any modern client
uctl version | head -1      # expect: >= 0.1.20  (note: subcommand, not --version)
which uv                    # required only for AWS/GCP (script venv)
```

Remediation:
- `helm` missing → `brew install helm` (or platform equivalent).
- `kubectl` missing → `brew install kubectl`.
- `uctl` missing or `< 0.1.20` → `brew install unionai/tap/uctl` then
  `brew upgrade uctl`. The skill needs `uctl selfserve` which lands in
  ≥ 0.1.20.
- `uv` missing → `brew install uv` (only blocks AWS/GCP paths).

If `uctl config` is unconfigured (no host set), instruct:

```bash
uctl config init --host=<control-plane-url-from-step-1>
```

Verify with `uctl get organization` (read-only).

---

## Step 3 — Cloud-specific prereqs and deploy

Load the file for the chosen cloud and follow it end to end:

- `aws` → read [`aws.md`](aws.md)
- `gcp` → read [`gcp.md`](gcp.md)
- `azure` → read [`azure.md`](azure.md)
- `oci` → read [`oci.md`](oci.md)
- `coreweave` → read [`coreweave.md`](coreweave.md)
- `generic` → read [`generic.md`](generic.md)

Each cloud file documents:
- Cloud CLI install + auth verification commands.
- The exact deploy invocation (script call or helm sequence).
- The teardown invocation.
- Cloud-specific gotchas the user should be warned about up front.

Do not improvise — if a cloud file says "run X", run X verbatim. If the
user wants to deviate, ask why and confirm before changing the command.

---

## Step 4 — Verify

After deploy:

1. `kubectl get pods -n union` — every pod should reach `Running` or
   `Completed`. If any pod is `CrashLoopBackOff`, `ImagePullBackOff`, or
   `Pending` for > 5 min, dump logs and stop.
2. `kubectl get events -n union --sort-by=.lastTimestamp | tail -20`.
3. AWS/GCP: smoke suite ran automatically in Phase 3. Check the TUI
   summary; on failure, the script captures debug dumps under
   `scripts/.debug/<timestamp>/`.
4. Other clouds: run a hello workflow as the smoke check —
   `python -m smoke_tests --control_plane_url <url> --cluster_name <name>`
   from `scripts/` (after the venv is set up; see `aws.md` for venv
   bootstrap).

Report the verification result as a short summary and stop. Do not
proactively trigger additional tests, configuration changes, or
documentation updates unless the user asks.

---

## Step 5 — Teardown (when mode = teardown)

Teardown is a first-class entry point, not an afterthought.

- AWS/GCP: invoke the script's `teardown_cluster` task (see `aws.md` /
  `gcp.md`). It resolves the account/project from ambient identity and
  deletes everything `cluster_name` implied.
- Azure/OCI/CoreWeave/generic: walk the cloud's `prepare-infra.md` in
  reverse, deleting one resource at a time, **asking before each
  delete**. Helm release first (`helm uninstall union -n union`), then
  IAM/identities, then storage, then the cluster, then any networking
  the user created specifically for this dataplane.

Never delete a resource group / project / subscription wholesale — only
the resources the user (or this skill) created for *this* cluster.

---

## When things go wrong

Common failure modes and what to tell the user (do not auto-retry):

- **`SelectCluster failed ... Not Found`** during AWS/GCP smoke — cluster-pool
  attributes aren't set. Either retry with `--skip_smoke_tests` or have an
  org admin grant `action_view_flyte_inventory`.
- **`Identity is not permitted to perform action on resource`** at helm
  install — kubeconfig is pointing at the wrong cluster. Run
  `kubectl config current-context` and switch.
- **STS token expired** (AWS) — re-export `AWS_ACCESS_KEY_ID`,
  `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`.
- **`helm install` hangs** — the e2e scripts watch pods every 15s under
  `[pods]`. For manual paths, open a second terminal and run
  `kubectl get pods -n union -w`. Hangs are almost always image pull
  (check `kubectl describe pod`).
- **Stale local-cache replays** in flyte — `rm -rf /tmp/flyte/metadata
  /tmp/flyte/raw_data ~/.flyte/local-cache/cache.db`.

When in doubt, point the user at the per-cloud `_index.md` under
`content/deployment/selfmanaged/` rather than guessing.
