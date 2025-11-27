---
title: WorkflowBase
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowBase

**Package:** `flytekit.core.workflow`

```python
class WorkflowBase(
    name: str,
    workflow_metadata: WorkflowMetadata,
    workflow_metadata_defaults: WorkflowMetadataDefaults,
    python_interface: Interface,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    default_options: Optional[Options],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `workflow_metadata` | `WorkflowMetadata` | |
| `workflow_metadata_defaults` | `WorkflowMetadataDefaults` | |
| `python_interface` | `Interface` | |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` | |
| `docs` | `Optional[Documentation]` | |
| `default_options` | `Optional[Options]` | |
| `kwargs` | `**kwargs` | |

## Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


### compile()

```python
def compile(
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
### execute()

```python
def execute(
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `interface` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

