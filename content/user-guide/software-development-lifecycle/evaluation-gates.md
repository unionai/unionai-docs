---
title: Evaluation gates
description: Promote on measured quality instead of a green checkmark, comparing against what is live with enough samples to tell a real change from noise.
icon: clipboard-check
weight: 4
variants: +flyte +union
---

# Evaluation gates

An evaluation gate decides whether a model, prompt, or dataset change may proceed by scoring it against what is currently live. Use one wherever a test suite can't answer the question: the system under test is non-deterministic, quality is a distribution, and a run costs GPUs or paid API calls.

## Build the gate

The gate scores every case against both the candidate and the baseline, several times each, and then compares the two sets of scores:

```python
import asyncio

import flyte

env = flyte.TaskEnvironment(
    name="eval-gate",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-mlflow"),
    resources=flyte.Resources(cpu=4, memory="8Gi"),
)


@env.task(cache="auto", retries=3)
async def score_one(model_uri: str, case: dict, repeat: int) -> float:
    """Score one case against one model. `repeat` makes each sample a separate cache entry."""
    ...


@env.task
async def score_all(model_uri: str, cases: list[dict], repeats: int = 3) -> list[float]:
    """Score every case `repeats` times."""
    samples = [(case, r) for case in cases for r in range(repeats)]
    return [
        score
        async for score in flyte.map.aio(
            score_one,
            [model_uri] * len(samples),
            [case for case, _ in samples],
            [r for _, r in samples],
            return_exceptions=False,
        )
    ]


def decide(candidate: list[float], baseline: list[float]) -> bool:
    """Your comparison rule. See "Compare honestly" below."""
    ...


@env.task(report=True)
async def gate(candidate_uri: str, baseline_uri: str, cases: list[dict]) -> bool:
    candidate, baseline = await asyncio.gather(
        score_all(candidate_uri, cases),
        score_all(baseline_uri, cases),
    )
    passed = decide(candidate, baseline)
    await flyte.report.replace.aio(
        f"<h2>{'Pass' if passed else 'Fail'}</h2>"
        f"<p>Candidate mean: {sum(candidate) / len(candidate):.3f} ({candidate_uri})</p>"
        f"<p>Baseline mean: {sum(baseline) / len(baseline):.3f} ({baseline_uri})</p>",
        do_flush=True,
    )
    return passed
```

Three settings do most of the work:

- `cache="auto"` on `score_one`. The baseline's scores are the same for every candidate you test against it, so after the first gate they come from the cache. `repeat` is an input, so each repeat is a separate sample rather than a cache hit on the first one.
- `retries=3` on `score_one`, not on `gate`. A transient provider error retries one case. A retry on `gate` would re-run every case.
- `flyte.map.aio` for the fan-out. Each case is its own action, so a failure at case 900 doesn't lose the first 899.

The cache key is the task's code plus its inputs, so cached scores are only valid while `model_uri` names exactly one model. Pass an immutable identifier, such as a registry version or a provider's dated model snapshot, never an alias like `latest`. If anything else that affects scoring changes, such as a judge model or a dependency, add it as an input to `score_one` so both sides are rescored.

`flyte.map` passes the lists to `score_one` position by position, like Python's built-in `map`. `return_exceptions=False` makes a case that exhausts its retries fail the gate instead of appearing as an exception in the score list.

Don't measure the noise floor by passing the same model URI to both sides of `gate`. Both sides have identical inputs, so they read the same cached scores and the measured noise is zero. Instead, run `score_all` on the baseline with `repeats=6` and compare repeats 0–2 of each case with repeats 3–5.

## Why a test suite doesn't fit

| A unit test | An evaluation |
|---|---|
| Deterministic | Non-deterministic, for anything generative |
| Pass or fail | A distribution of scores |
| Milliseconds, free | Minutes to hours, with GPUs and paid API calls |
| Asserts against a fixed expectation | Compares against what is currently live |
| A failure means the code is wrong | A failure can mean the data moved, the provider changed a model, or chance |

Two common shapes fail:

- **A hard threshold.** `assert accuracy > 0.9` goes permanently red when the data shifts, or stays green and stops carrying information.
- **A single comparison run.** One run per side measures noise. A difference between them is not evidence of a change.

An evaluation gate has to do four things:

1. Hold the evaluation set fixed, and version it so scores are comparable across weeks.
2. Score the candidate and the baseline under the same conditions: same set, same prompts, same scoring code.
3. Take more than one sample per side, so it can tell a real difference from noise.
4. Produce a report a person can read, because the final decision is often a judgment the number informs.

{{< variant union >}}
{{< markdown >}}
To version the evaluation set, register it as an [artifact](../artifacts/_index).
{{< /markdown >}}
{{< /variant >}}

## Compare honestly

- **Repeat both sides.** If the system is non-deterministic, score each case several times on each side and compare distributions.
- **Pair by case.** Compare the candidate and baseline scores for the same case. Case difficulty is usually the largest source of variance, and pairing cancels it.
- **Set the threshold in units of noise.** Measure run-to-run variance on the baseline first, as described above. A difference smaller than that is not a result. A threshold below the noise floor makes the gate fire at random.
- **Slice before aggregating.** An overall mean can improve while the slice you care about gets worse. Gate on each slice as well as the total.
- **Define "worse" per metric.** Latency and cost usually have hard ceilings, and quality usually has a tolerance. "No regression on any slice beyond noise, and no latency increase beyond 10%" is a gate. "Better on average" is not.

## Record the result

[MLflow](../../integrations/mlflow/_index) and [Weights & Biases](../../integrations/wandb/_index) both log from inside a task, so the recorded metrics trace back to the run that produced them.

For the readable half, `report=True` gives the gate a task report, which the example fills with `flyte.report.replace.aio`. Add per-slice scores and the worst-scoring cases there. If the reviewer needs plots and tables, [Papermill](../../integrations/papermill/_index) runs a parameterized notebook as a task, so the notebook is the gate's output.

## Gate the input

Validating inputs catches a problem before any scoring compute is spent:

- [Pandera](../../integrations/pandera/_index) validates dataframes at task boundaries. A column that changed type, or an unexpected null, fails at the step that introduced it instead of surfacing later as a regression.
- [TypeSafe AI](../../integrations/typesafe-ai/_index) returns typed, confidence-scored answers from a model, which you can check directly instead of parsing free text. [System one types](../system-one-types/_index) covers the pattern.

## Scale the compute

- [`flyte.map`](../tasks/task-programming/fanout) for per-case fan-out. This is usually enough.
- [Ray](../../integrations/ray/_index), [Spark](../../integrations/spark/_index), or [Dask](../../integrations/dask/_index) when scoring needs a cluster rather than many independent tasks.
- Per-task [resources](../tasks/task-configuration/resources), so only the step that needs a GPU holds one.
- [Snowflake](../../integrations/snowflake/_index), [BigQuery](../../integrations/bigquery/_index), or [Databricks](../../integrations/databricks/_index) when the evaluation set is in a warehouse.
- [Polars](../../integrations/polars/_index), [Lance](../../integrations/lance/_index), [JSONL](../../integrations/jsonl/_index), or [Hugging Face](../../integrations/huggingface/_index) to pass scored data between steps without writing your own serialization.

## Record the configuration

A score is only comparable if you know how it was produced. [Hydra](../../integrations/hydra/_index) and [OmegaConf](../../integrations/omegaconf/_index) pass structured configuration between tasks as typed inputs, so the configuration is recorded with the run instead of living in environment variables.

## Evaluate agents

An agent's output is a trajectory, not a single value. A correct answer reached by a wasteful or unsafe path is not equivalent to the same answer reached directly, so score more than the final output:

- Task completion, on a fixed set of scenarios.
- Tool-call correctness: the right tools, with the right arguments, in a sensible order.
- Cost and turn count. These often regress first when a prompt changes.
- Safety behaviors, on cases chosen to provoke them.

[Agent plugins](../../integrations/agents/_index) run each tool call as a child action and record each model turn, so the trajectory is already in the run. Completed turns replay on retry instead of calling the model again.

## See also

- [Review and release gates](./review-and-release-gates) for wiring the verdict into a promotion.
- [Human gates and approvals](./human-gates-and-approvals) for the decision the number informs.
- [Notifications and observability](./notifications-and-observability) for catching in production what the gate missed.
