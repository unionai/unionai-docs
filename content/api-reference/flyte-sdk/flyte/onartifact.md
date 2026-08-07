---
title: OnArtifact
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# OnArtifact

**Package:** `flyte`

Artifact-based automation for use with `Trigger`: fire a run whenever a new
version of the named artifact is created.

Bind the triggering artifact to a task input with the `flyte.TriggeredArtifact`
sentinel in the trigger's `inputs` (analogous to `flyte.TriggerTime` for
schedules). Other inputs may carry regular default values.

```python
retrain = flyte.Trigger(
    name="retrain_on_new_model",
    automation=flyte.OnArtifact(name="customer_model"),
    inputs={"model": flyte.TriggeredArtifact, "threshold": 0.5},
)

@env.task(triggers=[retrain])
async def validate(model: File, threshold: float) -> str:
    ...
```



## Parameters

```python
class OnArtifact(
    name: str,
    version: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the artifact to watch, scoped to the task's project/domain (required). |
| `version` | `str \| None` | Optional exact version pin — fire only when precisely this version is created. Default `None` fires on any new version. |

