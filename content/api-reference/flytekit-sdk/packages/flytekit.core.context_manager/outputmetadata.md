---
title: OutputMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OutputMetadata

**Package:** `flytekit.core.context_manager`

```python
class OutputMetadata(
    artifact: 'Artifact',
    dynamic_partitions: Optional[typing.Dict[str, str]],
    time_partition: Optional[datetime],
    additional_items: Optional[typing.List[SerializableToString]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `artifact` | `'Artifact'` | |
| `dynamic_partitions` | `Optional[typing.Dict[str, str]]` | |
| `time_partition` | `Optional[datetime]` | |
| `additional_items` | `Optional[typing.List[SerializableToString]]` | |

