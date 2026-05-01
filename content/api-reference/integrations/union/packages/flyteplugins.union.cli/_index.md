---
title: flyteplugins.union.cli
version: 0.2.2
variants: +flyte +union
layout: py_api
---

# flyteplugins.union.cli

## Directory

### Methods

| Method | Description |
|-|-|
| [`edit_with_retry()`](#edit_with_retry) | Open an editor and retry or save to file on failure. |


## Methods

#### edit_with_retry()

```python
def edit_with_retry(
    yaml_text: str,
    apply_fn,
    console,
    noun: str,
)
```
Open an editor and retry or save to file on failure.



| Parameter | Type | Description |
|-|-|-|
| `yaml_text` | `str` | Initial YAML content to edit. |
| `apply_fn` |  | Callable that takes the edited YAML string and applies it. Should raise on failure. |
| `console` |  | Rich console for output. |
| `noun` | `str` | Name of the resource for messages (e.g. "role", "policy"). |

**Returns:** The result of apply_fn on success, or None if cancelled.

