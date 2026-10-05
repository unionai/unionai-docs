---
title: Software development lifecycle
description: Automate your own development process with Flyte, using event-driven runs, review and release gates, human approvals, and evaluation gates for systems whose behavior depends on data and models.
icon: arrow-repeat
weight: 11
variants: +flyte +union
sidebar_expanded: false
---

# Software development lifecycle

The process around your workloads can run on Flyte too. Triage an issue when it is filed, rebuild a dataset when a schema changes, evaluate a model before it is promoted, or wait days for a person to approve a release. As Flyte runs, these chores are typed, retried, observable, and auditable.

## Why data and AI systems need more than CI

A conventional software project has one input that changes: code. Everything downstream of a commit is reproducible from that commit, so a pull request fully describes a change and a green build fully answers whether it is safe.

A data or AI system has four inputs that change: code, data, models, and prompts. Three of them change without a commit, which breaks the assumptions CI is built on:

| CI assumes | For a data or AI system |
|---|---|
| A change arrives as a diff | A retrained model, a drifted upstream table, or a provider's model update arrives with no diff |
| The same input gives the same output | Generative steps are non-deterministic, so two runs of one suite can disagree |
| Tests pass or fail | Quality is a distribution. The question is whether the change is worse than what is live by more than the noise |
| A build takes minutes and is cheap to repeat | An evaluation can need GPUs, paid API calls, and an hour |
| The artifact under test is in the repository | A 40 GB checkpoint is not, and the comparison point is whatever is in production |

So the useful gate is rarely "do the tests pass". It is "is this model better than the one serving, on the slice that matters, by more than the run-to-run variance". Answering that takes a pipeline: fan-out over a dataset, GPUs, caching, retries, a readable report, and often a human decision. Running that pipeline on the same orchestrator as production gives you one system, one set of credentials, and one place to look when something goes wrong.

## What Flyte provides

The section uses no special lifecycle features. Each need maps to an ordinary part of Flyte:

| Need | Use |
|---|---|
| Start a run from GitHub, Slack, Linear, ClickUp, or Jira | [Software development tools](../../integrations/software-development-tools/_index) |
| Start a run on a schedule | [Triggers](../triggers/_index) |
| Launch once per event, even when the event is delivered twice | `run_once`, keyed on the event |
| Wait for a person, possibly for days | [External conditions](../tasks/task-programming/conditions) |
| Keep an expensive gate fast | [Caching](../tasks/task-configuration/caching), [fan-out](../tasks/task-programming/fanout), and per-task [resources](../tasks/task-configuration/resources) |
| Survive a flaky provider | [Retries and timeouts](../tasks/task-configuration/retries-and-timeouts) |
| Trace an output back to its inputs and commit | Run history, task reports, and [lineage](./notifications-and-observability#track-what-produced-an-output) |
| Tell a person the result | [Notifications](../tasks/task-deployment/run-with-notifications), or a Slack message from inside the run |

{{< variant union >}}
{{< markdown >}}
[Artifacts](../artifacts/_index) add data and model versions to the picture: lineage across runs, and [artifact triggers](../triggers/artifact-triggers) that start the next stage when a new version is published.
{{< /markdown >}}
{{< /variant >}}

## Integrations by stage

Most teams use a handful of these. None is required.

| Stage | Integrations |
|---|---|
| Trigger a run from an event | [GitHub](../../integrations/software-development-tools/github), [Slack](../../integrations/software-development-tools/slack), [Linear](../../integrations/software-development-tools/linear), [ClickUp](../../integrations/software-development-tools/clickup), [Jira](../../integrations/software-development-tools/jira) |
| Configure the run | [Hydra](../../integrations/hydra/_index), [OmegaConf](../../integrations/omegaconf/_index) |
| Validate inputs | [Pandera](../../integrations/pandera/_index) for dataframe contracts, [TypeSafe AI](../../integrations/typesafe-ai/_index) for typed, confidence-scored model answers |
| Test generated code | [Code generation](../../integrations/codegen/_index), which runs generated code in a sandbox |
| Compute | [Ray](../../integrations/ray/_index), [Spark](../../integrations/spark/_index), [Dask](../../integrations/dask/_index), [PyTorch](../../integrations/pytorch/_index) |
| Read from a warehouse | [Snowflake](../../integrations/snowflake/_index), [BigQuery](../../integrations/bigquery/_index), [Databricks](../../integrations/databricks/_index) |
| Move data between steps | [Polars](../../integrations/polars/_index), [Lance](../../integrations/lance/_index), [JSONL](../../integrations/jsonl/_index), [Hugging Face](../../integrations/huggingface/_index) |
| Record results | [MLflow](../../integrations/mlflow/_index), [Weights & Biases](../../integrations/wandb/_index) |
| Report to a reviewer | [Papermill](../../integrations/papermill/_index), for a parameterized notebook as the gate's output |
| Run agents | [Agent frameworks](../../integrations/agents/_index), with ten SDKs that run as durable tasks |
| Observe production | [OpenTelemetry](../../integrations/opentelemetry/_index), [Grafana Agent](../../integrations/grafana-agent-observability/_index) |

## Scope of this section

- **Deploying from CI** is covered in [CI/CD deployments](../project-patterns/cicd): API keys, `flyte deploy`, and commit-pinned versions. This section assumes you have that in place.
- **Your CI system stays.** Keep linting, unit tests, and type checking in CI. They are fast and need no cluster. Use Flyte for checks that need real data, real compute, retries, or a person.

{{< subpage-cards >}}
