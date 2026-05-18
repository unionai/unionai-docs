---
description: Deploy a Union self-managed (BYOC) data plane on AWS, GCP, Azure, OCI, CoreWeave, or generic Kubernetes — guided, deterministic, with prereq verification.
argument-hint: "[cloud] [mode]   # e.g. 'aws deploy' or 'gcp teardown' (both optional)"
---

Invoke the `deploy-selfmanaged` skill at
`.claude/skills/deploy-selfmanaged/SKILL.md`.

Arguments (both optional, free-form):

- `$1` — cloud: one of `aws`, `gcp`, `azure`, `oci`, `coreweave`, `generic`.
  If omitted, ask the user via `AskUserQuestion`.
- `$2` — mode: one of `deploy`, `teardown`, `smoke-only`. Default `deploy`.

Provided arguments: `$ARGUMENTS`

Follow `SKILL.md` from Step 1 (capture intent — fill in any missing
fields from the arguments above) through Step 5 (or Step 4 for deploy
mode). Honor every "Operating rule" in the skill — never run a
cloud-mutating command without showing it and getting explicit
confirmation, never invent values, halt on failed prereqs.
