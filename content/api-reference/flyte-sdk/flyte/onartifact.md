---
title: OnArtifact
description: "Artifact-based automation for use with `Trigger`: fire a run whenever a new version of the named artifact is created."
icon: braces
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# OnArtifact

**Package:** `flyte`

Artifact-based automation for use with `Trigger`: fire a run whenever a new
version of the named artifact is created.

Bind the triggering artifact to a task input with the `flyte.TriggeredArtifact`
sentinel in the trigger's `inputs` (analogous to `flyte.TriggerTime` for
schedules), and a partition value of it with `flyte.TriggeredPartition("date")`.
Other inputs may carry regular default values.

```python
retrain = flyte.Trigger(
    name="retrain_on_new_model",
    automation=flyte.OnArtifact(name="customer_model"),
    inputs={"model": flyte.TriggeredArtifact, "threshold": 0.5},
)

@env.task(triggers=[retrain])
async def validate(model: File, threshold: float) -> str:
    ...

# Fire per partition: only US versions, passing the day being published.
daily = flyte.Trigger(
    name="clean_us",
    automation=flyte.OnArtifact("raw_events", region="us"),
    inputs={"raw": flyte.TriggeredArtifact, "day": flyte.TriggeredPartition("date")},
)
```



## Parameters

```python
class OnArtifact(
    name: str,
    version: str | None = None,
    partitions: Mapping[str, str] | None = None,
    **partition_kwargs: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the artifact to watch, scoped to the task's project/domain (required). |
| `version` | `str \| None` | Optional exact version pin — fire only when precisely this version is created. Default `None` fires on any new version. |
| `partitions` | `Mapping[str, str] \| None` | Fire only for versions whose string partitions carry every one of these key/value pairs, e.g. `{"region": "us"}`. Also accepted as keyword arguments: `OnArtifact("raw_events", region="us")`. |
| `**partition_kwargs` | `str` | |

