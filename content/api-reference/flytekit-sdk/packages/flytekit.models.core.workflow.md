---
title: flytekit.models.core.workflow
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.core.workflow

## Directory

### Classes

| Class | Description |
|-|-|
| [`Alias`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowalias) |  |
| [`ApproveCondition`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowapprovecondition) |  |
| [`ArrayNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowarraynode) |  |
| [`BranchNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowbranchnode) |  |
| [`GateNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowgatenode) |  |
| [`IfBlock`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowifblock) |  |
| [`IfElseBlock`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowifelseblock) |  |
| [`Node`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflownode) |  |
| [`NodeMetadata`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflownodemetadata) |  |
| [`SignalCondition`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowsignalcondition) |  |
| [`SleepCondition`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowsleepcondition) |  |
| [`TaskNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknode) |  |
| [`TaskNodeOverrides`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknodeoverrides) |  |
| [`WorkflowMetadata`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadata) |  |
| [`WorkflowMetadataDefaults`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadatadefaults) |  |
| [`WorkflowNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflownode) |  |
| [`WorkflowTemplate`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowtemplate) |  |

## flytekit.models.core.workflow.Alias

```python
class Alias(
    var,
    alias,
)
```
Links a variable to an alias.



| Parameter | Type | Description |
|-|-|-|
| `var` |  | |
| `alias` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `alias` | `None` | A workflow-level unique alias that downstream nodes can refer to in their input.  :rtype: Text |
| `is_empty` | `None` |  |
| `var` | `None` | Must match one of the output variable names on a node.  :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.Alias


## flytekit.models.core.workflow.ApproveCondition

```python
class ApproveCondition(
    signal_id: str,
)
```
Represents a dependency on an signal from a user.



| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The node id of the signal, also the signal name. |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `signal_id` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.ApproveCondition,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.ApproveCondition` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.core.workflow.ArrayNode

```python
class ArrayNode(
    node: Node,
    parallelism,
    min_successes,
    min_success_ratio,
    execution_mode,
    is_original_sub_node_interface,
    data_mode,
    bound_inputs,
)
```
TODO: docstring


| Parameter | Type | Description |
|-|-|-|
| `node` | `Node` | |
| `parallelism` |  | |
| `min_successes` |  | |
| `min_success_ratio` |  | |
| `execution_mode` |  | |
| `is_original_sub_node_interface` |  | |
| `data_mode` |  | |
| `bound_inputs` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `node` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ArrayNode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.core.workflow.BranchNode

```python
class BranchNode(
    if_else: flytekit.models.core.workflow.IfElseBlock,
)
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type | Description |
|-|-|-|
| `if_else` | `flytekit.models.core.workflow.IfElseBlock` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `if_else` | `None` | :rtype: IfElseBlock |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_objct` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.BranchNode


## flytekit.models.core.workflow.GateNode

```python
class GateNode(
    signal: typing.Optional[flytekit.models.core.workflow.SignalCondition],
    sleep: typing.Optional[flytekit.models.core.workflow.SleepCondition],
    approve: typing.Optional[flytekit.models.core.workflow.ApproveCondition],
)
```
| Parameter | Type | Description |
|-|-|-|
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` | |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SleepCondition]` | |
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `approve` | `None` |  |
| `condition` | `None` |  |
| `is_empty` | `None` |  |
| `signal` | `None` |  |
| `sleep` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.GateNode,
) -> GateNode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.GateNode` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.core.workflow.IfBlock

```python
class IfBlock(
    condition,
    then_node,
)
```
Defines a condition and the execution unit that should be executed if the condition is satisfied.



| Parameter | Type | Description |
|-|-|-|
| `condition` |  | |
| `then_node` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `condition` | `None` | :rtype: flytekit.models.core.condition.BooleanExpression |
| `is_empty` | `None` |  |
| `then_node` | `None` | :rtype: Node |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.IfBlock


## flytekit.models.core.workflow.IfElseBlock

```python
class IfElseBlock(
    case,
    other,
    else_node,
    error,
)
```
Defines a series of if/else blocks. The first branch whose condition evaluates to true is the one to execute.
If no conditions were satisfied, the else_node or the error will execute.



| Parameter | Type | Description |
|-|-|-|
| `case` |  | |
| `other` |  | |
| `else_node` |  | |
| `error` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `case` | `None` | First condition to evaluate.  :rtype: IfBlock |
| `else_node` | `None` | The node to execute in case none of the branches were taken.  :rtype: Node |
| `error` | `None` | An error to throw in case none of the branches were taken.  :rtype: flytekit.models.types.Error |
| `is_empty` | `None` |  |
| `other` | `None` | Additional branches to evaluate.  :rtype: list[IfBlock] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.IfElseBlock


## flytekit.models.core.workflow.Node

```python
class Node(
    id,
    metadata,
    inputs,
    upstream_node_ids,
    output_aliases,
    task_node,
    workflow_node,
    branch_node,
    gate_node: typing.Optional[flytekit.models.core.workflow.GateNode],
    array_node: typing.Optional[flytekit.models.core.workflow.ArrayNode],
)
```
A Workflow graph Node. One unit of execution in the graph. Each node can be linked to a Task,
a Workflow or a branch node.  One of the nodes must be specified.



| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `metadata` |  | |
| `inputs` |  | |
| `upstream_node_ids` |  | |
| `output_aliases` |  | |
| `task_node` |  | |
| `workflow_node` |  | |
| `branch_node` |  | |
| `gate_node` | `typing.Optional[flytekit.models.core.workflow.GateNode]` | |
| `array_node` | `typing.Optional[flytekit.models.core.workflow.ArrayNode]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `array_node` | `None` |  |
| `branch_node` | `None` | [Optional] Information about the branch node to evaluate in this node.  :rtype: BranchNode |
| `gate_node` | `None` |  |
| `id` | `None` | A workflow-level unique identifier that identifies this node in the workflow. "inputs" and "outputs" are reserved node ids that cannot be used by other nodes.  :rtype: Text |
| `inputs` | `None` | Specifies how to bind the underlying interface's inputs.  All required inputs specified in the underlying interface must be fulfilled.  :rtype: list[flytekit.models.literals.Binding] |
| `is_empty` | `None` |  |
| `metadata` | `None` | Extra metadata about the node.  :rtype: NodeMetadata |
| `output_aliases` | `None` | [Optional] A node can define aliases for a subset of its outputs. This is particularly useful if different nodes need to conform to the same interface (e.g. all branches in a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.  :rtype: list[Alias] |
| `target` | `None` | :rtype: T |
| `task_node` | `None` | [Optional] Information about the Task to execute in this node.  :rtype: TaskNode |
| `upstream_node_ids` | `None` | [Optional] Specifies execution dependency for this node ensuring it will only get scheduled to run after all its upstream nodes have completed. This node will have an implicit dependency on any node that appears in inputs field.  :rtype: list[Text] |
| `workflow_node` | `None` | [Optional] Information about the Workflow to execute in this mode.  :rtype: WorkflowNode |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.Node


## flytekit.models.core.workflow.NodeMetadata

```python
class NodeMetadata(
    name,
    timeout,
    retries,
    interruptible: typing.Optional[bool],
    cacheable: typing.Optional[bool],
    cache_version: typing.Optional[str],
    cache_serializable: typing.Optional[bool],
)
```
Defines extra information about the Node.



| Parameter | Type | Description |
|-|-|-|
| `name` |  | |
| `timeout` |  | |
| `retries` |  | |
| `interruptible` | `typing.Optional[bool]` | |
| `cacheable` | `typing.Optional[bool]` | Indicates that cache operations on this node should be serialized. |
| `cache_version` | `typing.Optional[str]` | The version of the cached data. |
| `cache_serializable` | `typing.Optional[bool]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cache_serializable` | `None` |  |
| `cache_version` | `None` |  |
| `cacheable` | `None` |  |
| `interruptible` | `None` |  |
| `is_empty` | `None` |  |
| `name` | `None` | :rtype: Text |
| `retries` | `None` | :rtype: flytekit.models.literals.RetryStrategy |
| `timeout` | `None` | :rtype: datetime.timedelta |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.NodeMetadata


## flytekit.models.core.workflow.SignalCondition

```python
class SignalCondition(
    signal_id: str,
    type: flytekit.models.types.LiteralType,
    output_variable_name: str,
)
```
Represents a dependency on an signal from a user.



| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The node id of the signal, also the signal name. |
| `type` | `flytekit.models.types.LiteralType` | |
| `output_variable_name` | `str` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `output_variable_name` | `None` |  |
| `signal_id` | `None` |  |
| `type` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.SignalCondition` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.core.workflow.SleepCondition

```python
class SleepCondition(
    duration: datetime.timedelta,
)
```
A sleep condition.


| Parameter | Type | Description |
|-|-|-|
| `duration` | `datetime.timedelta` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `duration` | `None` |  |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
) -> SleepCondition
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.SignalCondition` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.core.workflow.TaskNode

```python
class TaskNode(
    reference_id,
    overrides: typing.Optional[flytekit.models.core.workflow.TaskNodeOverrides],
)
```
Refers to the task that the Node is to execute.
This is currently a oneof in protobuf, but there's only one option currently.
This code should be updated when more options are available.



| Parameter | Type | Description |
|-|-|-|
| `reference_id` |  | |
| `overrides` | `typing.Optional[flytekit.models.core.workflow.TaskNodeOverrides]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `overrides` | `None` |  |
| `reference_id` | `None` | A globally unique identifier for the task. This should map to the identifier in Flyte Admin.  :rtype: flytekit.models.core.identifier.Identifier |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.TaskNode


## flytekit.models.core.workflow.TaskNodeOverrides

```python
class TaskNodeOverrides(
    resources: typing.Optional[flytekit.models.task.Resources],
    extended_resources: typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources],
    container_image: typing.Optional[str],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
)
```
| Parameter | Type | Description |
|-|-|-|
| `resources` | `typing.Optional[flytekit.models.task.Resources]` | |
| `extended_resources` | `typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]` | |
| `container_image` | `typing.Optional[str]` | |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` | `None` |  |
| `extended_resources` | `None` |  |
| `is_empty` | `None` |  |
| `pod_template` | `None` |  |
| `resources` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.core.workflow.WorkflowMetadata

```python
class WorkflowMetadata(
    on_failure,
)
```
Metadata for the workflow.



| Parameter | Type | Description |
|-|-|-|
| `on_failure` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `on_failure` | `None` | :rtype: flytekit.models.core.workflow.WorkflowMetadata.OnFailurePolicy |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.WorkflowMetadata


## flytekit.models.core.workflow.WorkflowMetadataDefaults

```python
class WorkflowMetadataDefaults(
    interruptible,
)
```
Metadata Defaults for the workflow.


| Parameter | Type | Description |
|-|-|-|
| `interruptible` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `interruptible` | `None` |  |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.WorkflowMetadataDefaults


## flytekit.models.core.workflow.WorkflowNode

```python
class WorkflowNode(
    launchplan_ref,
    sub_workflow_ref,
)
```
Refers to a the workflow the node is to execute. One of the references must be supplied.



| Parameter | Type | Description |
|-|-|-|
| `launchplan_ref` |  | |
| `sub_workflow_ref` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `launchplan_ref` | `None` | [Optional] A globally unique identifier for the launch plan.  Should map to Admin.  :rtype: flytekit.models.core.identifier.Identifier |
| `reference` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `sub_workflow_ref` | `None` | [Optional] Reference to a subworkflow, that should be defined with the compiler context.  :rtype: flytekit.models.core.identifier.Identifier |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.WorkflowNode


## flytekit.models.core.workflow.WorkflowTemplate

```python
class WorkflowTemplate(
    id,
    metadata,
    metadata_defaults,
    interface,
    nodes,
    outputs,
    failure_node,
)
```
A workflow template encapsulates all the task, branch, and subworkflow nodes to run a statically analyzable,
directed acyclic graph. It contains also metadata that tells the system how to execute the workflow (i.e.
the AWS IAM role to run with).



| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `metadata` |  | |
| `metadata_defaults` |  | |
| `interface` |  | |
| `nodes` |  | |
| `outputs` |  | |
| `failure_node` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `failure_node` | `None` | Node failure_node: A catch-all node. This node is executed whenever the execution engine determines the workflow has failed. The interface of this node must match the Workflow interface with an additional input named "error" of type pb.lyft.flyte.core.Error.  :rtype: Node |
| `id` | `None` | This is an autogenerated id by the system. The id is globally unique across Flyte.  :rtype: flytekit.models.core.identifier.Identifier |
| `interface` | `None` | Defines a strongly typed interface for the Workflow (inputs, outputs). This can include some optional parameters.  :rtype: flytekit.models.interface.TypedInterface |
| `is_empty` | `None` |  |
| `metadata` | `None` | This contains information on how to run the workflow.  :rtype: WorkflowMetadata |
| `metadata_defaults` | `None` | This contains information on how to run the workflow.  :rtype: WorkflowMetadataDefaults |
| `nodes` | `None` | A list of nodes. In addition, "globals" is a special reserved node id that can be used to consume workflow inputs.  :rtype: list[Node] |
| `outputs` | `None` | A list of output bindings that specify how to construct workflow outputs. Bindings can pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes to execute successfully in order to bind final outputs.  :rtype: list[flytekit.models.literals.Binding] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.WorkflowTemplate


