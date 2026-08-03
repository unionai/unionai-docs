# deploy-selfmanaged

A Claude Code skill that walks a user through deploying a Union
self-managed (BYOC) data plane end-to-end on AWS, GCP, Azure, OCI,
CoreWeave, or generic Kubernetes.

## Files in this directory

| File | Audience | Purpose |
|---|---|---|
| `SKILL.md` | model | Routing, intent capture, universal prereqs, operating rules. Always loaded. |
| `aws.md` / `gcp.md` | model | Drives the existing `scripts/selfmanaged_{aws,gcp}_e2e.py` flyte e2e scripts. |
| `azure.md` / `oci.md` / `coreweave.md` / `generic.md` | model | Guided walkthrough of the corresponding `content/deployment/selfmanaged/<cloud>/` docs. |
| `README.md` | humans | This file. UX overview + how to invoke. |

The cloud-specific files are loaded on demand — Claude only reads the
one matching the user's chosen cloud. Keeps the loaded context small.

## How a user invokes it

Either trigger by intent — say something like "deploy a self-managed
Union cluster on AWS" and the skill auto-engages from its description —
or use the slash command:

```
/deploy-selfmanaged              # asks cloud + mode
/deploy-selfmanaged aws          # mode defaults to deploy
/deploy-selfmanaged gcp teardown # explicit
```

## What the user experience looks like

The skill is **intuitive, guiding, deterministic**. A typical AWS
deploy session goes through six phases:

### 1. Trigger

User says "deploy a self-managed cluster on AWS" *or* runs the slash
command. Claude loads `SKILL.md` and routes by cloud.

### 2. Intent capture

Claude asks two button-pick questions via `AskUserQuestion`:

- **Cloud** — `aws | gcp | azure | oci | coreweave | generic`
- **Mode** — `deploy | teardown | smoke-only`

Then prompts in plain text for the three free-form fields:

- Control plane URL (e.g. `https://myorg.union.ai`)
- Cluster name
- Region

Skipped if the user already volunteered the answer. Echoes a `Plan:`
block back for sanity-checking:

```
Plan:
  cloud:             aws
  mode:              deploy
  control plane:     https://myorg.union.ai
  cluster name:      my-test-cluster
  region:            us-east-2
```

### 3. Prereq verification

Claude runs prereq checks as a single batch and reports a pass/fail
table:

| Check | Result |
|---|---|
| `helm version --short` | ✅ v4.1.1 |
| `kubectl version --client` | ✅ v1.35.1 |
| `uctl version` | ✅ v0.1.20 |
| `uv` | ✅ installed |
| `aws --version` | ✅ aws-cli/2.31.10 |
| `eksctl version` | ✅ 0.225.0 |
| `aws sts get-caller-identity` | ✅ account 479…192 |
| `AWS_ACCESS_KEY_ID` env var | ❌ **not set** |
| `scripts/.venv` | ✅ exists, flyte 2.2.2 importable |

**Any failure halts the flow** with the exact remediation command — no
silent workarounds. SSO-authenticated users specifically: the skill
catches the gap between `aws sts get-caller-identity` succeeding (via
SSO) and the e2e script needing `AWS_ACCESS_KEY_ID` in `os.environ`,
and points them at `aws configure export-credentials --format env`.

### 4. Deploy command — shown before run

Claude composes the exact command, displays it, and asks for explicit
`yes` before running anything cloud-mutating. For AWS/GCP, the deploy
is long-running (~25–40 min) so the recommendation is to run in the
user's own terminal with `--tui`:

```bash
cd scripts && source .venv/bin/activate && \
flyte run --local --tui selfmanaged_aws_e2e.py main \
    --control_plane_url https://myorg.union.ai \
    --cluster_name my-test-cluster \
    --aws_region us-east-2
```

The user sees Phase 1/4 → 2/4 → 3/4 → (4/4 teardown) in a live TUI
tree with timings, logs, and per-resource links. For
Azure/OCI/CoreWeave/generic, Claude walks the cloud's `prepare-infra.md`
→ `deploy-dataplane.md` step by step, **asking before each
cloud-mutating command** and showing the values-file diff before saving.

### 5. Verify

Once helm install completes:

- `kubectl get pods -n union` — every pod must reach Running/Completed
- `kubectl get events -n union --sort-by=.lastTimestamp | tail -20`
- AWS/GCP: smoke suite ran in Phase 3 — Claude reports the TUI summary
- Other clouds: optional `python -m smoke_tests` against the new cluster

### 6. Teardown is first-class

`mode=teardown` is a real entry point, not an afterthought. AWS/GCP
invoke the script's `teardown_cluster` task (resolves account/project
from ambient identity, deletes everything `cluster_name` implied).
Manual clouds get a reverse-order delete with **per-resource
confirmation** — the skill never bulk-deletes a resource group,
project, or subscription.

## Operating rules the skill enforces

These appear at the top of `SKILL.md` and govern every cloud path:

1. **Never run a cloud-mutating command without showing it first and
   getting explicit "yes."** Read-only commands run without prompting.
2. **Never invent values.** Missing `cluster_name`, region, or
   credentials → ask, don't guess.
3. **Failed prereq → halt with the fix command.** No silent workarounds.
4. **One cluster, one run.** No batching across clusters in a single
   skill invocation.
5. **Re-runnable end to end** — scripts are idempotent, manual paths
   note "skip if already created."

## Updating the skill

When the underlying `scripts/selfmanaged_*_e2e.py` scripts change their
flags, default regions, or four-phase shape, `aws.md` / `gcp.md` need
to be updated to match. When the docs under
`content/deployment/selfmanaged/<cloud>/` change, the corresponding
walkthrough file (`azure.md`, etc.) needs the same.

The skill is intentionally thin — it routes and verifies, but defers
to the canonical scripts and docs as sources of truth. Resist the urge
to inline command sequences here; they will rot.
