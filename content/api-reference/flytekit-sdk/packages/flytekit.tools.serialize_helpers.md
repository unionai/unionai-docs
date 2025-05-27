---
title: flytekit.tools.serialize_helpers
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.serialize_helpers

## Directory

### Methods

| Method | Description |
|-|-|
| [`get_registrable_entities()`](#get_registrable_entities) | Returns all entities that can be serialized and should be sent over to Flyte backend. |
| [`persist_registrable_entities()`](#persist_registrable_entities) | For protobuf serializable list of entities, writes a file with the name if the entity and. |


## Methods

#### get_registrable_entities()

```python
def get_registrable_entities(
    ctx: flytekit.core.context_manager.FlyteContext,
    options: typing.Optional[flytekit.core.options.Options],
) -> typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]
```
Returns all entities that can be serialized and should be sent over to Flyte backend. This will filter any entities
that are not known to Admin


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `options` | `typing.Optional[flytekit.core.options.Options]` |

#### persist_registrable_entities()

```python
def persist_registrable_entities(
    entities: typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]],
    folder: str,
)
```
For protobuf serializable list of entities, writes a file with the name if the entity and
enumeration order to the specified folder

This function will write to the folder specified the following protobuf types ::
    flyteidl.admin.launch_plan_pb2.LaunchPlan
    flyteidl.admin.workflow_pb2.WorkflowSpec
    flyteidl.admin.task_pb2.TaskSpec

These can be inspected by calling (in the launch plan case) ::
    flyte-cli parse-proto -f filename.pb -p flyteidl.admin.launch_plan_pb2.LaunchPlan


| Parameter | Type |
|-|-|
| `entities` | `typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]` |
| `folder` | `str` |

