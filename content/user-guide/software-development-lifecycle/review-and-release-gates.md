---
title: Review and release gates
description: Move a change from pull request to production — and handle the case where the change is a model or a dataset rather than a diff.
icon: shield-check
weight: 2
variants: +flyte +union
---

# Review and release gates

A gate is a question asked before a change is allowed to proceed, where a "no" stops it. Ordinary CI answers cheap questions well. This page is about the ones it answers badly: questions needing real data, real compute, or a person — and questions about changes that never appear as a diff.

## Three kinds of change, and what can gate them

| The change is | It arrives as | A useful gate |
|---|---|---|
| Code | A commit | Lint, types, unit tests — keep these in CI |
| Code with a behavioral effect | A commit | An [evaluation run](./evaluation-gates) on real data |
| A model, prompt, or dataset | **Nothing.** A training run finished, or an upstream table changed | An evaluation run comparing it against what is currently live |

The third row is the one that breaks conventional pipelines, and it is worth being blunt about why: **there is no pull request to attach a check to.** Nobody opened anything. A gate for that change has to be triggered by the artifact appearing, not by a commit, and its verdict has to be recorded somewhere that is not a PR status.

{{< variant union >}}
{{< markdown >}}
[Artifact triggers](../triggers/artifact-triggers) are how the first half works: register the model or dataset as an artifact, and the evaluation starts when a new version lands.
{{< /markdown >}}
{{< /variant >}}

## Gating a pull request

The [GitHub integration](../../integrations/software-development-tools/github) gives you both halves — the event, and a place to put the verdict.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=handler lang=python >}}

The launched task does the work and writes back. A check run is the usual destination, because it is what branch protection can require:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=task lang=python >}}

Two things this buys over doing the same in a CI job:

- **The gate can be expensive.** Per-task [resources](../tasks/task-configuration/resources) mean the gate can hold a GPU for the one step that needs it. [Caching](../tasks/task-configuration/caching) means a re-run after an unrelated push does not repeat the expensive half. [Fan-out](../tasks/task-programming/fanout) means a thousand-case suite runs in parallel.
- **The gate can be flaky without being wrong.** [Retries](../tasks/task-configuration/retries-and-timeouts) absorb a provider's 503. In CI, that 503 is a red build and somebody clicking "re-run jobs".

## Gating on a human decision

Some gates are judgment, not measurement. `review_pr` parks a run on a durable condition carrying the pull request's metadata, waits for a person to answer in the Flyte UI, and returns a typed verdict:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=review-gate lang=python >}}

The run survives restarts while it waits, because the condition is state on the backend rather than a held-open process. A gate can wait days.

See [Human gates and approvals](./human-gates-and-approvals) for the design questions — timeouts, who may answer, and how not to create a run that is stuck forever.

## Promotion, not deployment

The useful mental model for a release here is **promotion**: the same versioned thing moves between domains as evidence accumulates, rather than being rebuilt per environment.

1. Deploy to `development` on every merge, pinned to the commit: `flyte deploy --version ${{ github.sha }}`. See [CI/CD deployments](../project-patterns/cicd).
2. Run the gate there, against real data.
3. On a pass, promote the **same version** to `staging`, then `production`.

Pinning the version is what makes this work, and it is cheap. Re-running the same commit produces the same version identifier, tasks already registered at that version are no-ops, and every run traces back to a commit without anyone having to maintain a mapping.

Rebuilding per environment breaks the chain: what you tested is no longer demonstrably what you shipped.

## Agents that open pull requests

When the thing proposing a change is an agent rather than a person, two things change.

**Credentials.** An agent that clones, pushes, and opens PRs should authenticate as a GitHub App, minting a short-lived installation token per operation rather than holding a long-lived personal token:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=app-token lang=python >}}

Tokens live one hour — enough for a clone or a `gh pr create`, useless to anyone who later finds one in a log. A stored PAT has neither property.

**Review burden.** An agent can open more pull requests than anyone will read carefully, which quietly converts review from a gate into a rubber stamp. Two things help:

- Make the automated gate *the* gate for mechanical changes, and reserve human review for changes that alter behavior.
- Test generated code before trusting it. The [code generation integration](../../integrations/codegen/_index) runs it in a sandbox first, which is the difference between "the model says this works" and "this works".

If agents are a significant part of your workflow, [Agent frameworks](../../integrations/agents/_index) covers running them as durable tasks, and [Agents](../agents/_index) covers Flyte's own harness.

## Gating a dataset change

A dataset change is the same shape as a model change, with a cheaper gate available: a schema contract catches most real breakage immediately and costs nothing.

[Pandera](../../integrations/pandera/_index) validates dataframes at task boundaries and produces a report in the UI. A column that silently changed type, a null that should not exist, a range that moved — these fail at the boundary where they were introduced, rather than three stages downstream as a confusing model regression.

Where the question is about meaning rather than shape, [TypeSafe AI](../../integrations/typesafe-ai/_index) supplies typed, confidence-scored answers usable as a guard. [System one types](../system-one-types/_index) covers the pattern.

## What not to gate

Gates have a cost beyond compute: a gate people route around is worse than no gate, because it is a false assurance.

- **Do not gate on something non-deterministic without a tolerance.** A suite that fails one run in five teaches people to re-run until green, which disables the gate while leaving it in place.
- **Do not gate on an absolute threshold that drifts.** "Accuracy above 0.9" becomes either permanently red or permanently meaningless. Compare against what is live — see [Evaluation gates](./evaluation-gates).
- **Do not put a slow gate in front of a fast loop.** If it takes forty minutes, it belongs after merge with the ability to roll back, not before.

## Next

- [Evaluation gates](./evaluation-gates) — measuring quality well enough to gate on it.
- [Human gates and approvals](./human-gates-and-approvals) — people in the loop.
- [CI/CD deployments](../project-patterns/cicd) — the deploy mechanics this page assumes.
