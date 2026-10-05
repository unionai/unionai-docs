---
title: Review and release gates
description: Gate a change on its way from pull request to production, including changes to a model or dataset that never appear as a diff.
icon: shield-check
weight: 2
variants: +flyte +union
---

# Review and release gates

A gate is a check that must pass before a change can proceed. CI handles cheap checks well. Use Flyte for the checks that need real data, real compute, or a person, and for changes that never appear as a diff.

## Match the gate to the change

| The change is | It arrives as | Gate it with |
|---|---|---|
| Code | A commit | Lint, type checks, and unit tests, in CI |
| Code that changes behavior | A commit | An [evaluation run](./evaluation-gates) on real data |
| A model, prompt, or dataset | No commit: a training run finished, or an upstream table changed | An evaluation run against what is currently live |

For the third kind of change there is no pull request to attach a check to. The gate has to start when the new model or dataset appears, and it has to record its verdict somewhere other than a PR status.

{{< variant union >}}
{{< markdown >}}
Register the model or dataset as an artifact, and use an [artifact trigger](../triggers/artifact-triggers) to start the evaluation when a new version is published.
{{< /markdown >}}
{{< /variant >}}

## Gate a pull request

The [GitHub integration](../../integrations/software-development-tools/github) receives the pull request event and launches a task. The receiver is the one shown in [Event-driven automation](./event-driven-automation#launch-once-per-event). The launched task does the work and writes the result back to the pull request. This one labels the pull request by size:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=task lang=python >}}

To make the result a required status, have the task publish a check run through the GitHub API (for example, `Repository.create_check_run` in PyGithub), and require that check in branch protection. GitHub accepts check runs only from a GitHub App, so authenticate with an [installation token](#gate-agent-pull-requests) rather than a personal access token.

Running the gate as a Flyte task instead of a CI job lets it:

- Hold a GPU for only the step that needs it, with per-task [resources](../tasks/task-configuration/resources).
- Skip the expensive work on a re-run, with [caching](../tasks/task-configuration/caching).
- Run a thousand-case suite in parallel, with [fan-out](../tasks/task-programming/fanout).
- Absorb a provider's transient 503 with [retries](../tasks/task-configuration/retries-and-timeouts), instead of failing the build.

## Gate on a person's review

`review_pr` pauses a run on a condition that carries the pull request's metadata, waits for a person to answer in the {{< key product_name >}} UI, and returns a typed verdict:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=review-gate lang=python >}}

See [Human gates and approvals](./human-gates-and-approvals) for timeouts, who may answer, and how long a run can wait.

## Promote the same version

Treat a release as a promotion: the same versioned code moves between domains as it passes each gate, instead of being rebuilt for each environment.

1. On every merge, deploy to `development` pinned to the commit, with `flyte deploy --version ${{ github.sha }}`. See [CI/CD deployments](../project-patterns/cicd).
2. Run the gate there, against real data.
3. If it passes, promote the same version to `staging`, then to `production`.

Deploying the same commit twice produces the same version, and tasks already registered at that version are not registered again. Every run traces back to its commit. If you rebuild for each environment, you can no longer show that what you tested is what you shipped.

## Gate agent pull requests

When an agent opens pull requests, change two things.

**Credentials.** Authenticate the agent as a GitHub App. It mints a short-lived installation token for each operation instead of holding a personal access token:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=app-token lang=python >}}

Installation tokens expire after one hour. That is long enough for a clone or a `gh pr create`, and a leaked token stops working soon after.

**Review load.** An agent can open more pull requests than reviewers can read carefully. To keep review meaningful:

- Make an automated gate the only gate for mechanical changes, and reserve human review for changes that alter behavior.
- Test generated code before review. The [code generation integration](../../integrations/codegen/_index) runs it in a sandbox first.

[Agent frameworks](../../integrations/agents/_index) covers running agent SDKs as durable tasks, and [Agents](../agents/_index) covers Flyte's own agent harness.

## Gate a dataset change

Gate a dataset change like a model change, and add a schema check in front of it. [Pandera](../../integrations/pandera/_index) validates dataframes at task boundaries, so a changed column type or an unexpected null fails at the step that introduced it. See [Evaluation gates](./evaluation-gates#gate-the-input) for input checks on model output.

## Gates to avoid

A gate that people work around gives false assurance. Avoid these:

- **A non-deterministic gate with no tolerance.** If it fails one run in five, people re-run it until it passes.
- **An absolute threshold.** "Accuracy above 0.9" turns permanently red when the data shifts, or permanently passes. Compare against what is live instead. See [Evaluation gates](./evaluation-gates).
- **A slow gate in front of a fast loop.** A 40-minute gate belongs after merge, with the ability to roll back.

## See also

- [Evaluation gates](./evaluation-gates) for measuring quality well enough to gate on it.
- [Human gates and approvals](./human-gates-and-approvals) for putting a person in the loop.
- [CI/CD deployments](../project-patterns/cicd) for deployment from CI.
