---
title: TriggeredPartition
description: "Bind one partition value of the triggering artifact version to a task input of an artifact trigger: `inputs={\"day\": flyte.TriggeredPartition(\"date\")}` supplies the new version's `date` partition (a datetime for the time partition, a string for a string partition)."
icon: braces
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# TriggeredPartition

**Package:** `flyte`

Bind one partition value of the triggering artifact version to a task input of
an artifact trigger: `inputs={"day": flyte.TriggeredPartition("date")}` supplies
the new version's `date` partition (a datetime for the time partition, a string
for a string partition).


## Parameters

```python
class TriggeredPartition(
    key: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | |

