---
title: flytekit.clients.helpers
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.helpers

## Directory

### Methods

| Method | Description |
|-|-|
| [`iterate_node_executions()`](#iterate_node_executions) | This returns a generator for node executions. |
| [`iterate_task_executions()`](#iterate_task_executions) | This returns a generator for task executions, given a node execution identifier. |


## Methods

#### iterate_node_executions()

```python
def iterate_node_executions(
    client,
    workflow_execution_identifier,
    task_execution_identifier,
    limit,
    filters,
    sort_by,
    unique_parent_id,
)
```
This returns a generator for node executions.


| Parameter | Type | Description |
|-|-|-|
| `client` |  | |
| `workflow_execution_identifier` |  | |
| `task_execution_identifier` |  | |
| `limit` |  | |
| `filters` |  | |
| `sort_by` |  | |
| `unique_parent_id` |  | |

#### iterate_task_executions()

```python
def iterate_task_executions(
    client,
    node_execution_identifier,
    limit,
    filters,
    sort_by,
)
```
This returns a generator for task executions, given a node execution identifier


| Parameter | Type | Description |
|-|-|-|
| `client` |  | |
| `node_execution_identifier` |  | |
| `limit` |  | |
| `filters` |  | |
| `sort_by` |  | |

