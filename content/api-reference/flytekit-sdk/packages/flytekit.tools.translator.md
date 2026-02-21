---
title: flytekit.tools.translator
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.translator

## Directory

### Methods

| Method | Description |
|-|-|
| [`gather_dependent_entities()`](#gather_dependent_entities) | The ``get_serializable`` function above takes in an ``OrderedDict`` that helps keep track of dependent entities. |
| [`get_command_prefix_for_fast_execute()`](#get_command_prefix_for_fast_execute) |  |
| [`get_reference_spec()`](#get_reference_spec) |  |
| [`get_serializable()`](#get_serializable) | The flytekit authoring code produces objects representing Flyte entities (tasks, workflows, etc. |
| [`get_serializable_array_node()`](#get_serializable_array_node) |  |
| [`get_serializable_array_node_map_task()`](#get_serializable_array_node_map_task) |  |
| [`get_serializable_branch_node()`](#get_serializable_branch_node) |  |
| [`get_serializable_flyte_task()`](#get_serializable_flyte_task) | TODO replace with deep copy. |
| [`get_serializable_flyte_workflow()`](#get_serializable_flyte_workflow) | TODO replace with deep copy. |
| [`get_serializable_launch_plan()`](#get_serializable_launch_plan) |  |
| [`get_serializable_node()`](#get_serializable_node) |  |
| [`get_serializable_task()`](#get_serializable_task) |  |
| [`get_serializable_workflow()`](#get_serializable_workflow) |  |
| [`prefix_with_fast_execute()`](#prefix_with_fast_execute) |  |
| [`to_serializable_case()`](#to_serializable_case) |  |
| [`to_serializable_cases()`](#to_serializable_cases) |  |


## Methods

#### gather_dependent_entities()

```python
def gather_dependent_entities(
    serialized: collections.OrderedDict,
) -> typing.Tuple[typing.Dict[flytekit.models.core.identifier.Identifier, flytekit.models.task.TaskTemplate], typing.Dict[flytekit.models.core.identifier.Identifier, flytekit.models.admin.workflow.WorkflowSpec], typing.Dict[flytekit.models.core.identifier.Identifier, flytekit.models.launch_plan.LaunchPlanSpec]]
```
The ``get_serializable`` function above takes in an ``OrderedDict`` that helps keep track of dependent entities.
For example, when serializing a workflow, all its tasks are also serialized. The ordered dict will also contain
serialized entities that aren't as useful though, like nodes and branches. This is just a small helper function
that will pull out the serialized tasks, workflows, and launch plans. This function is primarily used for testing.



| Parameter | Type | Description |
|-|-|-|
| `serialized` | `collections.OrderedDict` | This should be the filled in OrderedDict used in the get_serializable function above. :return: |

#### get_command_prefix_for_fast_execute()

```python
def get_command_prefix_for_fast_execute(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_reference_spec()

```python
def get_reference_spec(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: flytekit.core.reference_entity.ReferenceEntity,
) -> flytekit.core.reference_entity.ReferenceSpec
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `entity` | `flytekit.core.reference_entity.ReferenceEntity` | |

#### get_serializable()

```python
def get_serializable(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode],
    options: typing.Optional[flytekit.core.options.Options],
) -> typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]
```
The flytekit authoring code produces objects representing Flyte entities (tasks, workflows, etc.). In order to
register these, they need to be converted into objects that Flyte Admin understands (the IDL objects basically, but
this function currently translates to the layer above (e.g. SdkTask) - this will be changed to the IDL objects
directly in the future).



| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | This is an ordered dict that will be mutated in place. The reason this argument exists is because there is a natural ordering to the entities at registration time. That is, underlying tasks have to be registered before the workflows that use them. The recursive search done by this function and the functions above form a natural topological sort, finding the dependent entities and adding them to this parameter before the parent entity this function is called with. |
| `settings` | `flytekit.configuration.SerializationSettings` | used to pick up project/domain/name - to be deprecated. |
| `entity` | `typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode]` | The local flyte entity to try to convert (along with its dependencies) |
| `options` | `typing.Optional[flytekit.core.options.Options]` | Optionally pass in a set of options that can be used to add additional metadata for Launchplans :return: The resulting control plane entity, in addition to being added to the mutable entity_mapping parameter is also returned. |

#### get_serializable_array_node()

```python
def get_serializable_array_node(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    node: typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode],
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.core.workflow.ArrayNode
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `node` | `typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode]` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### get_serializable_array_node_map_task()

```python
def get_serializable_array_node_map_task(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    node: flytekit.core.node.Node,
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.core.workflow.ArrayNode
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `node` | `flytekit.core.node.Node` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### get_serializable_branch_node()

```python
def get_serializable_branch_node(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode],
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.core.workflow.BranchNode
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `entity` | `typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode]` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### get_serializable_flyte_task()

```python
def get_serializable_flyte_task(
    entity: FlyteTask,
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]
```
TODO replace with deep copy


| Parameter | Type | Description |
|-|-|-|
| `entity` | `FlyteTask` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_serializable_flyte_workflow()

```python
def get_serializable_flyte_workflow(
    entity: FlyteWorkflow,
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]
```
TODO replace with deep copy


| Parameter | Type | Description |
|-|-|-|
| `entity` | `FlyteWorkflow` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_serializable_launch_plan()

```python
def get_serializable_launch_plan(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: flytekit.core.launch_plan.LaunchPlan,
    recurse_downstream: bool,
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.launch_plan.LaunchPlan
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `entity` | `flytekit.core.launch_plan.LaunchPlan` | |
| `recurse_downstream` | `bool` | This boolean indicate is wf for the entity should also be recursed to :return: |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### get_serializable_node()

```python
def get_serializable_node(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: flytekit.core.node.Node,
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.core.workflow.Node
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `entity` | `flytekit.core.node.Node` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### get_serializable_task()

```python
def get_serializable_task(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode],
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.task.TaskSpec
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `entity` | `typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode]` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### get_serializable_workflow()

```python
def get_serializable_workflow(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: flytekit.core.workflow.WorkflowBase,
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.admin.workflow.WorkflowSpec
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `entity` | `flytekit.core.workflow.WorkflowBase` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### prefix_with_fast_execute()

```python
def prefix_with_fast_execute(
    settings: flytekit.configuration.SerializationSettings,
    cmd: typing.List[str],
) -> typing.List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `cmd` | `typing.List[str]` | |

#### to_serializable_case()

```python
def to_serializable_case(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    c: flytekit.models.core.workflow.IfBlock,
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.core.workflow.IfBlock
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `c` | `flytekit.models.core.workflow.IfBlock` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

#### to_serializable_cases()

```python
def to_serializable_cases(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    cases: typing.List[flytekit.models.core.workflow.IfBlock],
    options: typing.Optional[flytekit.core.options.Options],
) -> typing.Optional[typing.List[flytekit.models.core.workflow.IfBlock]]
```
| Parameter | Type | Description |
|-|-|-|
| `entity_mapping` | `collections.OrderedDict` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `cases` | `typing.List[flytekit.models.core.workflow.IfBlock]` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

