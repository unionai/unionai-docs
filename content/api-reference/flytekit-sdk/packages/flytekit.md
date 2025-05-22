---
title: flytekit
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit


This package contains all of the most common abstractions you'll need to write Flyte workflows and extend Flytekit.

## Basic Authoring


These are the essentials needed to get started writing tasks and workflows.

- task
- workflow
- kwtypes
- current_context
- ExecutionParameters
- FlyteContext
- map_task
- ImperativeWorkflow
- create_node
- NodeOutput
- FlyteContextManager

> [!NOTE]
> **Local Execution**
>
> Tasks and Workflows can both be locally run, assuming the relevant tasks are capable of local execution.
> This is useful for unit testing.


### Branching and Conditionals


Branches and conditionals can be expressed explicitly in Flyte. These conditions are evaluated
in the flyte engine and hence should be used for control flow. "dynamic workflows" can be used to perform custom conditional logic not supported by flytekit.


### Customizing Tasks & Workflows

- TaskMetadata - Wrapper object that allows users to specify Task
- Resources - Things like CPUs/Memory, etc.
- WorkflowFailurePolicy - Customizes what happens when a workflow fails.
- PodTemplate - Custom PodTemplate for a task.

#### Dynamic and Nested Workflows

See the Dynamic module for more information.


##### Signaling

- approve
- sleep
- wait_for_input

Scheduling

- CronSchedule
- FixedRate

##### Notifications

- Email
- PagerDuty
- Slack

##### Reference Entities

- get_reference_entity
- LaunchPlanReference
- TaskReference
- WorkflowReference
- reference_task
- reference_workflow
- reference_launch_plan

##### Core Task Types

- SQLTask
- ContainerTask
- PythonFunctionTask
- PythonInstanceTask
- LaunchPlan

##### Secrets and SecurityContext

- Secret
- SecurityContext


##### Common Flyte IDL Objects

- AuthRole
- Labels
- Annotations
- WorkflowExecutionPhase
- Blob
- BlobMetadata
- Literal
- Scalar
- LiteralType
- BlobType


## Directory

### Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | Use this method to get a handle of specific parameters available in a flyte task. |
| [`load_implicit_plugins()`](#load_implicit_plugins) | This method allows loading all plugins that have the entrypoint specification. |
| [`new_context()`](#new_context) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `LOGGING_RICH_FMT_ENV_VAR` | `str` |  |

## Methods

#### current_context()

```python
def current_context()
```
Use this method to get a handle of specific parameters available in a flyte task.

Usage

```python
flytekit.current_context().logging.info(...)
```

Available params are documented in {{< py_class_ref flytekit.core.context_manager.ExecutionParams >}}.
There are some special params, that should be available


#### load_implicit_plugins()

```python
def load_implicit_plugins()
```
This method allows loading all plugins that have the entrypoint specification. This uses the plugin loading
behavior.

This is an opt in system and plugins that have an implicit loading requirement should add the implicit loading
entrypoint specification to their setup.py. The following example shows how we can autoload a module called fsspec
(whose init files contains the necessary plugin registration step)


> [!NOTE]
> The group is always ``flytekit.plugins``


```python
setup(
    ...
    entry_points={'flytekit.plugins': 'fsspec=flytekitplugins.fsspec'},
    ...
)
```
This works as long as the fsspec module has

> [!NOTE]
> For data persistence plugins:

```python
DataPersistencePlugins.register_plugin(f"{k}://", FSSpecPersistence, force=True)
```
OR for type plugins:

```python
TypeEngine.register(PanderaTransformer())
# etc
```


#### new_context()

```python
def new_context()
```
