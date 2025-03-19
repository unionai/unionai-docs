---
title: flytekit.models.core.workflow
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.core.workflow

## Directory

### Classes

| Class | Description |
|-|-|
| [`Alias`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowalias) | None. |
| [`ApproveCondition`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowapprovecondition) | None. |
| [`ArrayNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowarraynode) | None. |
| [`BoolValue`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowboolvalue) | A ProtocolMessage. |
| [`BranchNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowbranchnode) | None. |
| [`GateNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowgatenode) | None. |
| [`IfBlock`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowifblock) | None. |
| [`IfElseBlock`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowifelseblock) | None. |
| [`K8sObjectMetadata`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowk8sobjectmetadata) | None. |
| [`Node`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflownode) | None. |
| [`NodeMetadata`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflownodemetadata) | None. |
| [`PodTemplate`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowpodtemplate) | Custom PodTemplate specification for a Task. |
| [`Resources`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowresources) | None. |
| [`SignalCondition`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowsignalcondition) | None. |
| [`SleepCondition`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowsleepcondition) | None. |
| [`TaskNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknode) | None. |
| [`TaskNodeOverrides`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknodeoverrides) | None. |
| [`WorkflowMetadata`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadata) | None. |
| [`WorkflowMetadataDefaults`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadatadefaults) | None. |
| [`WorkflowNode`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflownode) | None. |
| [`WorkflowTemplate`](.././flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowtemplate) | None. |

## flytekit.models.core.workflow.Alias

```python
def Alias(
    var,
    alias,
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| alias |  |  |
| is_empty |  |  |
| var |  |  |

## flytekit.models.core.workflow.ApproveCondition

```python
def ApproveCondition(
    signal_id: str,
):
```
Represents a dependency on an signal from a user.



| Parameter | Type |
|-|-|
| `signal_id` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.ApproveCondition,
):
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
| is_empty |  |  |
| signal_id |  |  |

## flytekit.models.core.workflow.ArrayNode

```python
def ArrayNode(
    node: Node,
    parallelism,
    min_successes,
    min_success_ratio,
    execution_mode,
    is_original_sub_node_interface,
    data_mode,
    bound_inputs,
):
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| is_empty |  |  |
| node |  |  |

## flytekit.models.core.workflow.BoolValue

A ProtocolMessage


## flytekit.models.core.workflow.BranchNode

```python
def BranchNode(
    if_else: flytekit.models.core.workflow.IfElseBlock,
):
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type |
|-|-|
| `if_else` | `flytekit.models.core.workflow.IfElseBlock` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
):
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
| if_else |  |  |
| is_empty |  |  |

## flytekit.models.core.workflow.GateNode

```python
def GateNode(
    signal: typing.Optional[flytekit.models.core.workflow.SignalCondition],
    sleep: typing.Optional[flytekit.models.core.workflow.SleepCondition],
    approve: typing.Optional[flytekit.models.core.workflow.ApproveCondition],
):
```
| Parameter | Type |
|-|-|
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SleepCondition]` |
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.GateNode,
):
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
| approve |  |  |
| condition |  |  |
| is_empty |  |  |
| signal |  |  |
| sleep |  |  |

## flytekit.models.core.workflow.IfBlock

```python
def IfBlock(
    condition,
    then_node,
):
```
Defines a condition and the execution unit that should be executed if the condition is satisfied.



| Parameter | Type |
|-|-|
| `condition` |  |
| `then_node` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| condition |  |  |
| is_empty |  |  |
| then_node |  |  |

## flytekit.models.core.workflow.IfElseBlock

```python
def IfElseBlock(
    case,
    other,
    else_node,
    error,
):
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| case |  |  |
| else_node |  |  |
| error |  |  |
| is_empty |  |  |
| other |  |  |

## flytekit.models.core.workflow.K8sObjectMetadata

```python
def K8sObjectMetadata(
    labels: typing.Dict[str, str],
    annotations: typing.Dict[str, str],
):
```
This defines additional metadata for building a kubernetes pod.


| Parameter | Type |
|-|-|
| `labels` | `typing.Dict[str, str]` |
| `annotations` | `typing.Dict[str, str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sObjectMetadata,
):
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
| annotations |  |  |
| is_empty |  |  |
| labels |  |  |

## flytekit.models.core.workflow.Node

```python
def Node(
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
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| array_node |  |  |
| branch_node |  |  |
| gate_node |  |  |
| id |  |  |
| inputs |  |  |
| is_empty |  |  |
| metadata |  |  |
| output_aliases |  |  |
| target |  |  |
| task_node |  |  |
| upstream_node_ids |  |  |
| workflow_node |  |  |

## flytekit.models.core.workflow.NodeMetadata

```python
def NodeMetadata(
    name,
    timeout,
    retries,
    interruptible: typing.Optional[bool],
    cacheable: typing.Optional[bool],
    cache_version: typing.Optional[str],
    cache_serializable: typing.Optional[bool],
):
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| cache_serializable |  |  |
| cache_version |  |  |
| cacheable |  |  |
| interruptible |  |  |
| is_empty |  |  |
| name |  |  |
| retries |  |  |
| timeout |  |  |

## flytekit.models.core.workflow.PodTemplate

Custom PodTemplate specification for a Task.


```python
def PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
):
```
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

## flytekit.models.core.workflow.Resources

```python
def Resources(
    requests,
    limits,
):
```
| Parameter | Type |
|-|-|
| `requests` |  |
| `limits` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| is_empty |  |  |
| limits |  |  |
| requests |  |  |

## flytekit.models.core.workflow.SignalCondition

```python
def SignalCondition(
    signal_id: str,
    type: flytekit.models.types.LiteralType,
    output_variable_name: str,
):
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
):
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
| is_empty |  |  |
| output_variable_name |  |  |
| signal_id |  |  |
| type |  |  |

## flytekit.models.core.workflow.SleepCondition

```python
def SleepCondition(
    duration: datetime.timedelta,
):
```
A sleep condition.


| Parameter | Type |
|-|-|
| `duration` | `datetime.timedelta` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
):
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
| duration |  |  |
| is_empty |  |  |

## flytekit.models.core.workflow.TaskNode

```python
def TaskNode(
    reference_id,
    overrides: typing.Optional[flytekit.models.core.workflow.TaskNodeOverrides],
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| is_empty |  |  |
| overrides |  |  |
| reference_id |  |  |

## flytekit.models.core.workflow.TaskNodeOverrides

```python
def TaskNodeOverrides(
    resources: typing.Optional[flytekit.models.task.Resources],
    extended_resources: typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources],
    container_image: typing.Optional[str],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
):
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| container_image |  |  |
| extended_resources |  |  |
| is_empty |  |  |
| pod_template |  |  |
| resources |  |  |

## flytekit.models.core.workflow.WorkflowMetadata

```python
def WorkflowMetadata(
    on_failure,
):
```
Metadata for the workflow.



| Parameter | Type |
|-|-|
| `on_failure` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| is_empty |  |  |
| on_failure |  |  |

## flytekit.models.core.workflow.WorkflowMetadataDefaults

```python
def WorkflowMetadataDefaults(
    interruptible,
):
```
Metadata Defaults for the workflow.


| Parameter | Type |
|-|-|
| `interruptible` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| interruptible |  |  |
| is_empty |  |  |

## flytekit.models.core.workflow.WorkflowNode

```python
def WorkflowNode(
    launchplan_ref,
    sub_workflow_ref,
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| is_empty |  |  |
| launchplan_ref |  |  |
| reference |  |  |
| sub_workflow_ref |  |  |

## flytekit.models.core.workflow.WorkflowTemplate

```python
def WorkflowTemplate(
    id,
    metadata,
    metadata_defaults,
    interface,
    nodes,
    outputs,
    failure_node,
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| failure_node |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| metadata |  |  |
| metadata_defaults |  |  |
| nodes |  |  |
| outputs |  |  |

