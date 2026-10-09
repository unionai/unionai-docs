---
title: dbt
icon: book
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# dbt



## Directory

### Classes

| Class | Description |
|-|-|
| [`DbtNodeResult`](./dbtnoderesult) | Small serializable summary of one dbt node result. |
| [`DbtTask`](./dbttask) | A Flyte task that maps one dbtRunner.invoke(...) call to one task. |
| [`DbtTaskResolver`](./dbttaskresolver) | Reconstructs a DbtTask in the remote task container. |

### Errors

| Exception | Description |
|-|-|
| [`DbtInvocationError`](./dbtinvocationerror) | Raised when dbt finishes cleanly but reports failed node results. |

### Methods

| Method | Description |
|-|-|
| [`invoke_dbt()`](#invoke_dbt) | Run exactly one dbtRunner invocation and return a serializable summary. |


## Methods

#### invoke_dbt()

```python
def invoke_dbt(
    cli_args: list[str],
    callbacks: Sequence[DbtEventCallback | str] | None = None,
) -> list[DbtNodeResult]
```
Run exactly one dbtRunner invocation and return a serializable summary.


| Parameter | Type | Description |
|-|-|-|
| `cli_args` | `list[str]` | |
| `callbacks` | `Sequence[DbtEventCallback \| str] \| None` | |

