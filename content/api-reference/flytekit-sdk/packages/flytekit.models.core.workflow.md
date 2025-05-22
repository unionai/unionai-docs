---
title: flytekit.models.core.workflow
version: 0.1.dev2192+g7c539c3.d20250403
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



| Parameter | Type |
|-|-|
| `var` |  |
| `alias` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> n: Alias
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `alias` |  | {{< multiline >}}A workflow-level unique alias that downstream nodes can refer to in their input.

:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `var` |  | {{< multiline >}}Must match one of the output variable names on a node.

:rtype: Text
{{< /multiline >}} |

## flytekit.models.core.workflow.ApproveCondition

```python
class ApproveCondition(
    signal_id: str,
)
```
Represents a dependency on an signal from a user.



| Parameter | Type |
|-|-|
| `signal_id` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.ApproveCondition,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.ApproveCondition` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `signal_id` |  |  |

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


| Parameter | Type |
|-|-|
| `node` | `Node` |
| `parallelism` |  |
| `min_successes` |  |
| `min_success_ratio` |  |
| `execution_mode` |  |
| `is_original_sub_node_interface` |  |
| `data_mode` |  |
| `bound_inputs` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ArrayNode
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `node` |  |  |

## flytekit.models.core.workflow.BranchNode

```python
class BranchNode(
    if_else: flytekit.models.core.workflow.IfElseBlock,
)
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type |
|-|-|
| `if_else` | `flytekit.models.core.workflow.IfElseBlock` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
)
```
| Parameter | Type |
|-|-|
| `pb2_objct` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `if_else` |  | {{< multiline >}}:rtype: IfElseBlock
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.core.workflow.GateNode

```python
class GateNode(
    signal: typing.Optional[flytekit.models.core.workflow.SignalCondition],
    sleep: typing.Optional[flytekit.models.core.workflow.SleepCondition],
    approve: typing.Optional[flytekit.models.core.workflow.ApproveCondition],
)
```
| Parameter | Type |
|-|-|
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SleepCondition]` |
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.GateNode,
) -> GateNode
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.GateNode` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `approve` |  |  |
| `condition` |  |  |
| `is_empty` |  |  |
| `signal` |  |  |
| `sleep` |  |  |

## flytekit.models.core.workflow.IfBlock

```python
class IfBlock(
    condition,
    then_node,
)
```
Defines a condition and the execution unit that should be executed if the condition is satisfied.



| Parameter | Type |
|-|-|
| `condition` |  |
| `then_node` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `condition` |  | {{< multiline >}}:rtype: flytekit.models.core.condition.BooleanExpression
{{< /multiline >}} |
| `is_empty` |  |  |
| `then_node` |  | {{< multiline >}}:rtype: Node
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `case` |  |
| `other` |  |
| `else_node` |  |
| `error` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `case` |  | {{< multiline >}}First condition to evaluate.

:rtype: IfBlock
{{< /multiline >}} |
| `else_node` |  | {{< multiline >}}The node to execute in case none of the branches were taken.

:rtype: Node
{{< /multiline >}} |
| `error` |  | {{< multiline >}}An error to throw in case none of the branches were taken.

:rtype: flytekit.models.types.Error
{{< /multiline >}} |
| `is_empty` |  |  |
| `other` |  | {{< multiline >}}Additional branches to evaluate.

:rtype: list[IfBlock]
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `id` |  |
| `metadata` |  |
| `inputs` |  |
| `upstream_node_ids` |  |
| `output_aliases` |  |
| `task_node` |  |
| `workflow_node` |  |
| `branch_node` |  |
| `gate_node` | `typing.Optional[flytekit.models.core.workflow.GateNode]` |
| `array_node` | `typing.Optional[flytekit.models.core.workflow.ArrayNode]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Node
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `array_node` |  |  |
| `branch_node` |  | {{< multiline >}}[Optional] Information about the branch node to evaluate in this node.

:rtype: BranchNode
{{< /multiline >}} |
| `gate_node` |  |  |
| `id` |  | {{< multiline >}}A workflow-level unique identifier that identifies this node in the workflow. "inputs" and
"outputs" are reserved node ids that cannot be used by other nodes.

:rtype: Text
{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}Specifies how to bind the underlying interface's inputs.  All required inputs specified
in the underlying interface must be fulfilled.

:rtype: list[flytekit.models.literals.Binding]
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}Extra metadata about the node.

:rtype: NodeMetadata
{{< /multiline >}} |
| `output_aliases` |  | {{< multiline >}}[Optional] A node can define aliases for a subset of its outputs. This
is particularly useful if different nodes need to conform to the same interface (e.g. all branches in
a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.

:rtype: list[Alias]
{{< /multiline >}} |
| `target` |  | {{< multiline >}}:rtype: T
{{< /multiline >}} |
| `task_node` |  | {{< multiline >}}[Optional] Information about the Task to execute in this node.

:rtype: TaskNode
{{< /multiline >}} |
| `upstream_node_ids` |  | {{< multiline >}}[Optional] Specifies execution dependency for this node ensuring it will
only get scheduled to run after all its upstream nodes have completed. This node will have
an implicit dependency on any node that appears in inputs field.

:rtype: list[Text]
{{< /multiline >}} |
| `workflow_node` |  | {{< multiline >}}[Optional] Information about the Workflow to execute in this mode.

:rtype: WorkflowNode
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `name` |  |
| `timeout` |  |
| `retries` |  |
| `interruptible` | `typing.Optional[bool]` |
| `cacheable` | `typing.Optional[bool]` |
| `cache_version` | `typing.Optional[str]` |
| `cache_serializable` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `cache_serializable` |  |  |
| `cache_version` |  |  |
| `cacheable` |  |  |
| `interruptible` |  |  |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `retries` |  | {{< multiline >}}:rtype: flytekit.models.literals.RetryStrategy
{{< /multiline >}} |
| `timeout` |  | {{< multiline >}}:rtype: datetime.timedelta
{{< /multiline >}} |

## flytekit.models.core.workflow.SignalCondition

```python
class SignalCondition(
    signal_id: str,
    type: flytekit.models.types.LiteralType,
    output_variable_name: str,
)
```
Represents a dependency on an signal from a user.



| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `type` | `flytekit.models.types.LiteralType` |
| `output_variable_name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.SignalCondition` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `output_variable_name` |  |  |
| `signal_id` |  |  |
| `type` |  |  |

## flytekit.models.core.workflow.SleepCondition

```python
class SleepCondition(
    duration: datetime.timedelta,
)
```
A sleep condition.


| Parameter | Type |
|-|-|
| `duration` | `datetime.timedelta` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
) -> SleepCondition
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.SignalCondition` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `duration` |  |  |
| `is_empty` |  |  |

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



| Parameter | Type |
|-|-|
| `reference_id` |  |
| `overrides` | `typing.Optional[flytekit.models.core.workflow.TaskNodeOverrides]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskNode
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `overrides` |  |  |
| `reference_id` |  | {{< multiline >}}A globally unique identifier for the task. This should map to the identifier in Flyte Admin.

:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |

## flytekit.models.core.workflow.TaskNodeOverrides

```python
class TaskNodeOverrides(
    resources: typing.Optional[flytekit.models.task.Resources],
    extended_resources: typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources],
    container_image: typing.Optional[str],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
)
```
| Parameter | Type |
|-|-|
| `resources` | `typing.Optional[flytekit.models.task.Resources]` |
| `extended_resources` | `typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]` |
| `container_image` | `typing.Optional[str]` |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` |  |  |
| `extended_resources` |  |  |
| `is_empty` |  |  |
| `pod_template` |  |  |
| `resources` |  |  |

## flytekit.models.core.workflow.WorkflowMetadata

```python
class WorkflowMetadata(
    on_failure,
)
```
Metadata for the workflow.



| Parameter | Type |
|-|-|
| `on_failure` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowMetadata
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `on_failure` |  | {{< multiline >}}:rtype: flytekit.models.core.workflow.WorkflowMetadata.OnFailurePolicy
{{< /multiline >}} |

## flytekit.models.core.workflow.WorkflowMetadataDefaults

```python
class WorkflowMetadataDefaults(
    interruptible,
)
```
Metadata Defaults for the workflow.


| Parameter | Type |
|-|-|
| `interruptible` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowMetadata
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `interruptible` |  |  |
| `is_empty` |  |  |

## flytekit.models.core.workflow.WorkflowNode

```python
class WorkflowNode(
    launchplan_ref,
    sub_workflow_ref,
)
```
Refers to a the workflow the node is to execute. One of the references must be supplied.



| Parameter | Type |
|-|-|
| `launchplan_ref` |  |
| `sub_workflow_ref` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowNode
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `launchplan_ref` |  | {{< multiline >}}[Optional] A globally unique identifier for the launch plan.  Should map to Admin.

:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `reference` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `sub_workflow_ref` |  | {{< multiline >}}[Optional] Reference to a subworkflow, that should be defined with the compiler context.

:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `id` |  |
| `metadata` |  |
| `metadata_defaults` |  |
| `interface` |  |
| `nodes` |  |
| `outputs` |  |
| `failure_node` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowTemplate
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `failure_node` |  | {{< multiline >}}Node failure_node: A catch-all node. This node is executed whenever the execution engine determines the
workflow has failed. The interface of this node must match the Workflow interface with an additional input
named "error" of type pb.lyft.flyte.core.Error.

:rtype: Node
{{< /multiline >}} |
| `id` |  | {{< multiline >}}This is an autogenerated id by the system. The id is globally unique across Flyte.

:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `interface` |  | {{< multiline >}}Defines a strongly typed interface for the Workflow (inputs, outputs). This can include some optional
parameters.

:rtype: flytekit.models.interface.TypedInterface
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}This contains information on how to run the workflow.

:rtype: WorkflowMetadata
{{< /multiline >}} |
| `metadata_defaults` |  | {{< multiline >}}This contains information on how to run the workflow.

:rtype: WorkflowMetadataDefaults
{{< /multiline >}} |
| `nodes` |  | {{< multiline >}}A list of nodes. In addition, "globals" is a special reserved node id that can be used to consume
workflow inputs.

:rtype: list[Node]
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}A list of output bindings that specify how to construct workflow outputs. Bindings can
pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound
in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes
to execute successfully in order to bind final outputs.

:rtype: list[flytekit.models.literals.Binding]
{{< /multiline >}} |

