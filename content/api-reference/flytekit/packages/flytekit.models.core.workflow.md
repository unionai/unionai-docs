---
title: flytekit.models.core.workflow
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| [`BoolValue`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowboolvalue) | A ProtocolMessage. |
| [`BranchNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowbranchnode) |  |
| [`GateNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowgatenode) |  |
| [`IfBlock`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowifblock) |  |
| [`IfElseBlock`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowifelseblock) |  |
| [`K8sObjectMetadata`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowk8sobjectmetadata) |  |
| [`Node`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflownode) |  |
| [`NodeMetadata`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflownodemetadata) |  |
| [`PodTemplate`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowpodtemplate) | Custom PodTemplate specification for a Task. |
| [`Resources`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowresources) |  |
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `alias` |  | {{< multiline >}}A workflow-level unique alias that downstream nodes can refer to in their input.

{{< /multiline >}} |
| `is_empty` |  |  |
| `var` |  | {{< multiline >}}Must match one of the output variable names on a node.

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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `node` |  |  |

## flytekit.models.core.workflow.BoolValue

A ProtocolMessage


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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `if_else` |  |  |
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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `condition` |  |  |
| `is_empty` |  |  |
| `then_node` |  |  |

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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `case` |  | {{< multiline >}}First condition to evaluate.

{{< /multiline >}} |
| `else_node` |  | {{< multiline >}}The node to execute in case none of the branches were taken.

{{< /multiline >}} |
| `error` |  | {{< multiline >}}An error to throw in case none of the branches were taken.

{{< /multiline >}} |
| `is_empty` |  |  |
| `other` |  | {{< multiline >}}Additional branches to evaluate.

{{< /multiline >}} |

## flytekit.models.core.workflow.K8sObjectMetadata

```python
class K8sObjectMetadata(
    labels: typing.Dict[str, str],
    annotations: typing.Dict[str, str],
)
```
This defines additional metadata for building a kubernetes pod.


| Parameter | Type |
|-|-|
| `labels` | `typing.Dict[str, str]` |
| `annotations` | `typing.Dict[str, str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sObjectMetadata,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sObjectMetadata` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `is_empty` |  |  |
| `labels` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Node
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `array_node` |  |  |
| `branch_node` |  | {{< multiline >}}[Optional] Information about the branch node to evaluate in this node.

{{< /multiline >}} |
| `gate_node` |  |  |
| `id` |  | {{< multiline >}}A workflow-level unique identifier that identifies this node in the workflow. "inputs" and
"outputs" are reserved node ids that cannot be used by other nodes.

{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}Specifies how to bind the underlying interface's inputs.  All required inputs specified
in the underlying interface must be fulfilled.

{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}Extra metadata about the node.

{{< /multiline >}} |
| `output_aliases` |  | {{< multiline >}}[Optional] A node can define aliases for a subset of its outputs. This
is particularly useful if different nodes need to conform to the same interface (e.g. all branches in
a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.

{{< /multiline >}} |
| `target` |  |  |
| `task_node` |  | {{< multiline >}}[Optional] Information about the Task to execute in this node.

{{< /multiline >}} |
| `upstream_node_ids` |  | {{< multiline >}}[Optional] Specifies execution dependency for this node ensuring it will
only get scheduled to run after all its upstream nodes have completed. This node will have
an implicit dependency on any node that appears in inputs field.

{{< /multiline >}} |
| `workflow_node` |  | {{< multiline >}}[Optional] Information about the Workflow to execute in this mode.

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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `cache_serializable` |  |  |
| `cache_version` |  |  |
| `cacheable` |  |  |
| `interruptible` |  |  |
| `is_empty` |  |  |
| `name` |  |  |
| `retries` |  |  |
| `timeout` |  |  |

## flytekit.models.core.workflow.PodTemplate

Custom PodTemplate specification for a Task.


```python
class PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
)
```
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

## flytekit.models.core.workflow.Resources

```python
class Resources(
    requests,
    limits,
)
```
| Parameter | Type |
|-|-|
| `requests` |  |
| `limits` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Resources
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `limits` |  | {{< multiline >}}These are the limits required.  These are guaranteed to be satisfied.
{{< /multiline >}} |
| `requests` |  | {{< multiline >}}The desired resources for execution.  This is given on a best effort basis.
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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskNode
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `overrides` |  |  |
| `reference_id` |  | {{< multiline >}}A globally unique identifier for the task. This should map to the identifier in Flyte Admin.

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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowMetadata
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `on_failure` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowMetadata
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowNode
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `launchplan_ref` |  | {{< multiline >}}[Optional] A globally unique identifier for the launch plan.  Should map to Admin.

{{< /multiline >}} |
| `reference` |  |  |
| `sub_workflow_ref` |  | {{< multiline >}}[Optional] Reference to a subworkflow, that should be defined with the compiler context.

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowTemplate
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `failure_node` |  | {{< multiline >}}Node failure_node: A catch-all node. This node is executed whenever the execution engine determines the
workflow has failed. The interface of this node must match the Workflow interface with an additional input
named "error" of type pb.lyft.flyte.core.Error.

{{< /multiline >}} |
| `id` |  | {{< multiline >}}This is an autogenerated id by the system. The id is globally unique across Flyte.

{{< /multiline >}} |
| `interface` |  | {{< multiline >}}Defines a strongly typed interface for the Workflow (inputs, outputs). This can include some optional
parameters.

{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}This contains information on how to run the workflow.

{{< /multiline >}} |
| `metadata_defaults` |  | {{< multiline >}}This contains information on how to run the workflow.

{{< /multiline >}} |
| `nodes` |  | {{< multiline >}}A list of nodes. In addition, "globals" is a special reserved node id that can be used to consume
workflow inputs.

{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}A list of output bindings that specify how to construct workflow outputs. Bindings can
pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound
in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes
to execute successfully in order to bind final outputs.

{{< /multiline >}} |

