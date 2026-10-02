---
title: Software development lifecycle
description: Use Flyte as the automation substrate for your own development process — event-driven runs, review and release gates, human approvals, and evaluation gates for systems whose behavior depends on data and models.
icon: arrow-repeat
weight: 11
variants: +flyte +union
sidebar_expanded: false
---

# Software development lifecycle

The rest of the user guide is about running your workloads on Flyte. This section is about something narrower and easier to miss: **the process around those workloads is itself a workload**, and Flyte is unusually good at running it.

Triage when an issue is filed. Rebuild a dataset when a schema changes. Run an evaluation suite before a model is promoted. Ask a human to approve a release and wait — possibly for days — without anything held open. Post the result where the team will see it. These are ordinary software-lifecycle chores, and they are all typed, retried, observable, and auditable when they are Flyte runs, and none of those things when they are a shell script in a CI job.

## Why this needs its own section

A conventional SDLC has one moving part that matters: **code**. Everything downstream of a commit is reproducible from that commit, which is why CI works the way it does — a pull request is a complete description of a change, and a green build is a complete answer about it.

A data or AI system has four moving parts — code, data, models, and prompts — and **three of them change without a commit.** That breaks the assumptions CI is built on:

| Assumption CI makes | How it fails for a data/AI system |
|---|---|
| A change arrives as a diff | A retrained model, a drifted upstream table, and a provider's silent model update arrive as none |
| The same input gives the same output | Generative steps are non-deterministic by construction; two runs of one suite legitimately disagree |
| Tests are pass/fail | Quality is a distribution. The question is not "did it pass" but "is it worse than what is live, by more than the noise" |
| A build takes minutes and is cheap to repeat | An evaluation can need GPUs, paid API calls, and an hour |
| The artifact under test is in the repo | A 40 GB checkpoint is not, and the thing you need to compare against is whatever is in production right now |

Which means the interesting gate is rarely "do the tests pass". It is "did this model get better on the slice we care about, measured against the one currently serving, and is that difference bigger than the run-to-run variance". That is not a CI check. It is a pipeline — fan-out over a dataset, GPU resources, caching so the expensive half is not repeated, retries so a flaky provider does not fail the gate, a report somebody can read, and a human decision at the end.

So: the same orchestrator runs production *and* the checks on production. One system, one set of credentials, one place to look when something is wrong.

## What Flyte brings to it

Nothing here is a special lifecycle feature. It is the ordinary runtime, pointed at a different kind of work.

| Need | What supplies it |
|---|---|
| Something outside Flyte should start a run | [Software development tools](../../integrations/software-development-tools/_index) — webhooks from GitHub, Slack, Linear, ClickUp, and Jira |
| Time or data should start a run | [Triggers](../triggers/_index) — schedules and artifact events |
| An automation must not double-fire | `run_once`, keyed on the event rather than the delivery |
| A step needs a person | [External conditions](../tasks/task-programming/conditions), including a run that waits days without holding a process open |
| A gate needs to be expensive and still fast enough | [Caching](../tasks/task-configuration/caching), [fan-out](../tasks/task-programming/fanout), per-task [resources](../tasks/task-configuration/resources) |
| A flaky provider must not fail the gate | [Retries and timeouts](../tasks/task-configuration/retries-and-timeouts) |
| Someone must be able to explain what ran, and why | Run history, task reports, and [lineage](#tracking-what-changed) |
| The result has to reach a human | [Notifications](../tasks/task-deployment/run-with-notifications), or a Slack message from the run itself |

## The pages in this section

1. **[Event-driven automation](./event-driven-automation)** — the inbound half. What should start a run, and how to choose between a webhook, a schedule, and an artifact trigger.
2. **[Review and release gates](./review-and-release-gates)** — getting a change from a pull request to production, and what "a change" means when it is a model rather than a diff.
3. **[Human gates and approvals](./human-gates-and-approvals)** — putting a person in the loop without creating a run that is stuck forever.
4. **[Evaluation gates](./evaluation-gates)** — the AI- and data-specific core: promoting on measured quality instead of on a green checkmark.
5. **[Notifications and observability](./notifications-and-observability)** — closing the loop, and what to reach for when production misbehaves.

## Where the plugins fit

A map of the full integration surface onto the lifecycle, so you can find the relevant one without reading all of them. Nothing here is required — most teams use a handful.

| Stage | Integrations |
|---|---|
| **Trigger** — something happened | [GitHub](../../integrations/software-development-tools/github), [Slack](../../integrations/software-development-tools/slack), [Linear](../../integrations/software-development-tools/linear), [ClickUp](../../integrations/software-development-tools/clickup), [Jira](../../integrations/software-development-tools/jira) |
| **Configure** — what exactly are we running | [Hydra](../../integrations/hydra/_index), [OmegaConf](../../integrations/omegaconf/_index) |
| **Validate** — is the input admissible | [Pandera](../../integrations/pandera/_index) for dataframe contracts, [TypeSafe AI](../../integrations/typesafe-ai/_index) for typed, confidence-scored guards on model I/O |
| **Build and test** — including code a model wrote | [Code generation](../../integrations/codegen/_index), which tests generated code in a sandbox before it is trusted |
| **Compute** — the expensive half of a gate | [Ray](../../integrations/ray/_index), [Spark](../../integrations/spark/_index), [Dask](../../integrations/dask/_index), [PyTorch](../../integrations/pytorch/_index) |
| **Read from the warehouse** | [Snowflake](../../integrations/snowflake/_index), [BigQuery](../../integrations/bigquery/_index), [Databricks](../../integrations/databricks/_index) |
| **Move data between steps** | [Polars](../../integrations/polars/_index), [Lance](../../integrations/lance/_index), [JSONL](../../integrations/jsonl/_index), [Hugging Face](../../integrations/huggingface/_index) |
| **Record the result** | [MLflow](../../integrations/mlflow/_index), [Weights & Biases](../../integrations/wandb/_index) |
| **Report for a human reviewer** | [Papermill](../../integrations/papermill/_index), for a parameterized notebook as the gate's readable output |
| **Agentic steps in the loop** | [Agent frameworks](../../integrations/agents/_index) — ten SDKs, each run as durable tasks |
| **Observe** — what is production doing | [OpenTelemetry](../../integrations/opentelemetry/_index), [Grafana Agent](../../integrations/grafana-agent-observability/_index) |

## Tracking what changed

The recurring question in a data or AI lifecycle is not "what code is deployed" — that one is easy — but **"which data and which model produced this output, and what changed since the last time it was right."**

{{< variant union >}}
{{< markdown >}}
[Artifacts](../artifacts/_index) are the direct answer: register a dataset or model as a named, versioned artifact, and you get lineage across runs, plus [artifact triggers](../triggers/artifact-triggers) so the next stage starts when a new version lands rather than on a schedule that hopes it has.
{{< /markdown >}}
{{< /variant >}}

Independently of that, every run records its inputs, outputs, code version, and image. Deploying with `--version <commit-sha>` (see [CI/CD deployments](../project-patterns/cicd)) is what makes a run traceable back to a commit, and it is the cheapest useful thing on this page.

## What this section is not

- **Not how to deploy Flyte code from CI.** That is [CI/CD deployments](../project-patterns/cicd): API keys, `flyte deploy`, commit-pinned versions. This section assumes you have that and asks what to automate *with* it.
- **Not a replacement for your CI system.** Keep linting, unit tests, and type checking where they are — they are fast, cheap, and need no cluster. Reach for Flyte when a check needs real data, real compute, retries, or a human, which is exactly where a CI job starts to hurt.
- **Not a product feature.** Everything here is composed from tasks, conditions, triggers, apps, and plugins that exist for other reasons.

{{< subpage-cards >}}
