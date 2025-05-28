---
title: flytekit.clients.helpers
version: 0.1.dev2192+g7c539c3.d20250403
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
    unique_parent_id,
) -> e: Iterator[flytekit.models.node_execution.NodeExecution]
```
This returns a generator for node executions.


| Parameter | Type |
|-|-|
| `client` |  |
| `workflow_execution_identifier` |  |
| `task_execution_identifier` |  |
| `limit` |  |
| `filters` |  |
| `unique_parent_id` |  |

#### iterate_task_executions()

```python
def iterate_task_executions(
    client,
    node_execution_identifier,
    limit,
    filters,
) -> e: Iterator[flytekit.models.admin.task_execution.TaskExecution]
```
This returns a generator for task executions, given a node execution identifier


| Parameter | Type |
|-|-|
| `client` |  |
| `node_execution_identifier` |  |
| `limit` |  |
| `filters` |  |

