---
title: Evaluation gates
description: Promote on measured quality instead of a green checkmark — comparing against what is live, with enough runs to tell a real change from noise.
icon: clipboard-check
weight: 4
variants: +flyte +union
---

# Evaluation gates

This is the page the rest of the section exists for. In a conventional pipeline the gate is a test suite: deterministic, cheap, pass or fail. For a system whose behavior depends on data and models, none of those three hold — and an evaluation gate is what you build instead.

## Why a test suite is the wrong shape

| A unit test | An evaluation |
|---|---|
| Deterministic | Non-deterministic by construction, for anything generative |
| Pass or fail | A distribution of scores |
| Milliseconds, free | Minutes to hours; GPUs and paid API calls |
| Asserts against a fixed expectation | Compares against **what is currently live** |
| A failure means the code is wrong | A failure might mean the data moved, the provider changed a model, or you got unlucky |

Treating an evaluation as a test suite produces one of two failure modes, and most teams hit both:

- **A hard threshold.** `assert accuracy > 0.9` is permanently red the day the data shifts, or permanently green and meaningless. Either way the gate stops carrying information.
- **A single comparison run.** One run of the candidate against one run of the baseline, scores differ, ship it. That is measuring noise and calling it progress.

## What an evaluation gate actually has to do

Four things, and Flyte supplies the awkward parts of each:

1. **Hold the evaluation set still** while everything else moves. Version it, so a score is comparable across weeks. {{< variant union >}}{{< markdown >}}Register it as an [artifact](../artifacts/_index).{{< /markdown >}}{{< /variant >}}
2. **Score the candidate and the baseline under the same conditions.** Same set, same prompts, same scoring code, same version of all three.
3. **Decide whether the difference is real** — which needs more than one sample per side when the thing under test is non-deterministic.
4. **Produce something a human can read**, because the eventual decision is usually a judgment informed by the number, not the number alone.

## The shape

```python
import flyte

env = flyte.TaskEnvironment(
    name="eval-gate",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-mlflow"),
    resources=flyte.Resources(cpu=4, memory="8Gi"),
)


@env.task(cache="auto", retries=3)
async def score_one(model_uri: str, case: dict) -> float:
    """One case against one model.

    `cache="auto"` is doing real work here: the baseline's scores do not
    change between candidates, so they are computed once and replayed. That
    is usually most of the bill.

    `retries=3` matters because a provider's 503 is not a quality signal.
    """
    ...


@env.task
async def score_all(model_uri: str, cases: list[dict], repeats: int = 3) -> list[float]:
    """Every case, repeated — so variance is measured rather than assumed."""
    return await flyte.map.aio(
        score_one,
        [(model_uri, c) for c in cases for _ in range(repeats)],
    )


@env.task(report=True)
async def gate(candidate_uri: str, baseline_uri: str, cases: list[dict]) -> bool:
    """Compare the two, and decide."""
    candidate, baseline = await score_all(candidate_uri, cases), await score_all(baseline_uri, cases)
    return decide(candidate, baseline)
```

Three details carry most of the value:

- **`cache="auto"` on the per-case task.** The baseline's scores are identical across every candidate you ever test against it. Caching them turns a repeated full evaluation into a partial one.
- **`retries=` on the per-case task, not the gate.** A transient provider failure retries one case. Put the retry on the gate instead and a single 503 re-runs everything.
- **`flyte.map` for the fan-out.** A thousand cases is a thousand cheap parallel actions, not a loop in one long-running process that loses everything when it dies at case 900.

## Comparing honestly

The statistics matter more than the orchestration, and are easier to get wrong.

**Repeat both sides.** If the system is non-deterministic, one run per side tells you nothing about whether a difference is real. Repeat each case on each side and compare distributions.

**Compare paired, by case.** The same case scored on both models is a pair; differences per case have far less variance than the difference of two means, because case difficulty — usually the dominant term — cancels.

**Set the threshold in units of noise.** Measure run-to-run variance with the *same* model on both sides first. That number is your floor: a difference smaller than it is not a result. A gate whose threshold is below its own noise floor fires at random, and people learn to re-run it.

**Slice before aggregating.** An overall mean that improves while the slice you care about degrades is the single most common way a bad model ships. Gate on the slices, not just the total.

**Say what "worse" means per metric.** Latency and cost usually have hard ceilings; quality usually has a tolerance. "No regression on any slice beyond noise, and no latency increase beyond 10%" is a gate. "Better on average" is not.

## Recording the result

A score nobody can find later is a score you will recompute. [MLflow](../../integrations/mlflow/_index) and [Weights & Biases](../../integrations/wandb/_index) are the usual destinations, and both work from inside a task, so the run and the recorded metrics share a lineage.

For the human-readable half, `report=True` renders into the task report. Where the reviewer wants plots and tables, [Papermill](../../integrations/papermill/_index) runs a parameterized notebook as a task, which makes the notebook the gate's output rather than something someone runs by hand afterwards.

## Gating the input, not just the output

The cheapest evaluation gate is the one that catches a problem before any compute is spent.

- **Schema contracts.** [Pandera](../../integrations/pandera/_index) validates dataframes at task boundaries. A column that changed type or a null that should not exist fails where it was introduced, rather than three stages later as a confusing regression.
- **Typed guards on model I/O.** [TypeSafe AI](../../integrations/typesafe-ai/_index) returns typed, confidence-scored answers in one call, which is a far better gate than parsing free text and hoping. [System one types](../system-one-types/_index) covers the pattern.

A surprising share of "the model got worse" incidents are upstream data problems, and these two catch them at a fraction of the cost.

## Where the compute comes from

Evaluations are embarrassingly parallel, which is the good case.

- [`flyte.map`](../tasks/task-programming/fanout) for per-case fan-out — usually sufficient.
- [Ray](../../integrations/ray/_index), [Spark](../../integrations/spark/_index), or [Dask](../../integrations/dask/_index) when scoring needs a cluster rather than many independent tasks.
- Per-task [resources](../tasks/task-configuration/resources) so the GPU is held by the step that needs it and nothing else.
- [Snowflake](../../integrations/snowflake/_index), [BigQuery](../../integrations/bigquery/_index), or [Databricks](../../integrations/databricks/_index) when the evaluation set lives in the warehouse.

For moving scored data between steps, the [data-type integrations](../../integrations/_index) — [Polars](../../integrations/polars/_index), [Lance](../../integrations/lance/_index), [JSONL](../../integrations/jsonl/_index), [Hugging Face](../../integrations/huggingface/_index) — avoid a serialization step you would otherwise write.

## Keeping the configuration honest

An evaluation is only comparable if you know exactly what was configured. [Hydra](../../integrations/hydra/_index) and [OmegaConf](../../integrations/omegaconf/_index) pass structured configuration between tasks as typed objects, so the configuration is a recorded run input rather than a set of environment variables nobody wrote down.

This is what makes a six-week-old score meaningful. Without it, the honest answer to "why is this number different" is usually "we don't know".

## Evaluating agents

Agents add a difficulty: the output is a trajectory, not a value. A correct answer reached by a wasteful or unsafe path is not equivalent to the same answer reached directly, so scoring only the final output misses most of what you care about.

What tends to be worth gating:

- **Task completion**, on a fixed set of scenarios.
- **Tool-call correctness** — the right tools, with the right arguments, in a sensible order.
- **Cost and turn count**, which regress quietly and are the usual first sign of a prompt change going wrong.
- **Safety behaviors**, on cases chosen to provoke them.

Because [agent plugins](../../integrations/agents/_index) make each tool call a child action and record model turns, the trajectory is in the run already — it does not need separate instrumentation. Completed turns also replay on retry rather than re-billing, which makes a large evaluation affordable enough to run on every change.

## Next

- [Review and release gates](./review-and-release-gates) — wiring the verdict into a promotion.
- [Human gates and approvals](./human-gates-and-approvals) — for the decision the number informs but does not make.
- [Notifications and observability](./notifications-and-observability) — catching in production what the gate missed.
