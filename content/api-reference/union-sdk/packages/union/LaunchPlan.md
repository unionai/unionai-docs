---
title: LaunchPlan
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# LaunchPlan

**Package:** `union`

Launch Plans are one of the core constructs of Flyte. Please take a look at the discussion in the
:std:ref:`core concepts <flyte:divedeep-launchplans>` if you are unfamiliar with them.

Every workflow is registered with a default launch plan, which is just a launch plan with none of the additional
attributes set - no default values, fixed values, schedules, etc. Assuming you have the following workflow

```python
@workflow
def wf(a: int, c: str) -> str:
        ...
```
Create the default launch plan with

```python
LaunchPlan.get_or_create(workflow=my_wf)
```
If you specify additional parameters, you'll also have to give the launch plan a unique name. Default and
fixed inputs can be expressed as Python native values like so:

Additionally, a launch plan can be configured to run on a schedule and emit notifications.


Please see the relevant Schedule and Notification objects as well.

To configure the remaining parameters, you'll need to import the relevant model objects as well.

```python
from flytekit.models.common import Annotations, AuthRole, Labels, RawOutputDataConfig
```
Then use as follows:


```python
class LaunchPlan(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    parameters: _interface_models.ParameterMap,
    fixed_inputs: _literal_models.LiteralMap,
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
    concurrency: Optional[ConcurrencyPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `workflow` | `_annotated_workflow.WorkflowBase` | |
| `parameters` | `_interface_models.ParameterMap` | |
| `fixed_inputs` | `_literal_models.LiteralMap` | |
| `schedule` | `Optional[_schedule_model.Schedule]` | |
| `notifications` | `Optional[List[_common_models.Notification]]` | |
| `labels` | `Optional[_common_models.Labels]` | |
| `annotations` | `Optional[_common_models.Annotations]` | |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` | |
| `max_parallelism` | `Optional[int]` | |
| `security_context` | `Optional[security.SecurityContext]` | |
| `trigger` | `Optional[LaunchPlanTriggerBase]` | |
| `overwrite_cache` | `Optional[bool]` | |
| `auto_activate` | `bool` | |
| `concurrency` | `Optional[ConcurrencyPolicy]` | |

## Methods

| Method | Description |
|-|-|
| [`clone_with()`](#clone_with) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create()`](#create) |  |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead. |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans. |


### clone_with()

```python
def clone_with(
    name: str,
    parameters: Optional[_interface_models.ParameterMap],
    fixed_inputs: Optional[_literal_models.LiteralMap],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `parameters` | `Optional[_interface_models.ParameterMap]` | |
| `fixed_inputs` | `Optional[_literal_models.LiteralMap]` | |
| `schedule` | `Optional[_schedule_model.Schedule]` | |
| `notifications` | `Optional[List[_common_models.Notification]]` | |
| `labels` | `Optional[_common_models.Labels]` | |
| `annotations` | `Optional[_common_models.Annotations]` | |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` | |
| `max_parallelism` | `Optional[int]` | |
| `security_context` | `Optional[security.SecurityContext]` | |
| `trigger` | `Optional[LaunchPlanTriggerBase]` | |
| `overwrite_cache` | `Optional[bool]` | |
| `auto_activate` | `bool` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
### create()

```python
def create(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
    concurrency: Optional[ConcurrencyPolicy],
) -> LaunchPlan
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `workflow` | `_annotated_workflow.WorkflowBase` | |
| `default_inputs` | `Optional[Dict[str, Any]]` | |
| `fixed_inputs` | `Optional[Dict[str, Any]]` | |
| `schedule` | `Optional[_schedule_model.Schedule]` | |
| `notifications` | `Optional[List[_common_models.Notification]]` | |
| `labels` | `Optional[_common_models.Labels]` | |
| `annotations` | `Optional[_common_models.Annotations]` | |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` | |
| `max_parallelism` | `Optional[int]` | |
| `security_context` | `Optional[security.SecurityContext]` | |
| `auth_role` | `Optional[_common_models.AuthRole]` | |
| `trigger` | `Optional[LaunchPlanTriggerBase]` | |
| `overwrite_cache` | `Optional[bool]` | |
| `auto_activate` | `bool` | |
| `concurrency` | `Optional[ConcurrencyPolicy]` | |

### get_default_launch_plan()

```python
def get_default_launch_plan(
    ctx: FlyteContext,
    workflow: _annotated_workflow.WorkflowBase,
) -> LaunchPlan
```
Users should probably call the get_or_create function defined below instead. A default launch plan is the one
that will just pick up whatever default values are defined in the workflow function signature (if any) and
use the default auth information supplied during serialization, with no notifications or schedules.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | This is not flytekit.current_context(). This is an internal context object. Users familiar with flytekit should feel free to use this however. |
| `workflow` | `_annotated_workflow.WorkflowBase` | The workflow to create a launch plan for. |

### get_or_create()

```python
def get_or_create(
    workflow: _annotated_workflow.WorkflowBase,
    name: Optional[str],
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
    concurrency: Optional[ConcurrencyPolicy],
) -> LaunchPlan
```
This function offers a friendlier interface for creating launch plans. If the name for the launch plan is not
supplied, this assumes you are looking for the default launch plan for the workflow. If it is specified, it
will be used. If creating the default launch plan, none of the other arguments may be specified.

The resulting launch plan is also cached and if called again with the same name, the
cached version is returned



| Parameter | Type | Description |
|-|-|-|
| `workflow` | `_annotated_workflow.WorkflowBase` | The Workflow to create a launch plan for. |
| `name` | `Optional[str]` | If you supply a name, keep it mind it needs to be unique. That is, project, domain, version, and this name form a primary key. If you do not supply a name, this function will assume you want the default launch plan for the given workflow. |
| `default_inputs` | `Optional[Dict[str, Any]]` | Default inputs, expressed as Python values. |
| `fixed_inputs` | `Optional[Dict[str, Any]]` | Fixed inputs, expressed as Python values. At call time, these cannot be changed. |
| `schedule` | `Optional[_schedule_model.Schedule]` | Optional schedule to run on. |
| `notifications` | `Optional[List[_common_models.Notification]]` | Notifications to send. |
| `labels` | `Optional[_common_models.Labels]` | Optional labels to attach to executions created by this launch plan. |
| `annotations` | `Optional[_common_models.Annotations]` | Optional annotations to attach to executions created by this launch plan. |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` | Optional location of offloaded data for things like S3, etc. |
| `max_parallelism` | `Optional[int]` | Controls the maximum number of tasknodes that can be run in parallel for the entire workflow. This is useful to achieve fairness. Note: MapTasks are regarded as one unit, and parallelism/concurrency of MapTasks is independent from this. |
| `security_context` | `Optional[security.SecurityContext]` | Security context for the execution |
| `auth_role` | `Optional[_common_models.AuthRole]` | Add an auth role if necessary. |
| `trigger` | `Optional[LaunchPlanTriggerBase]` | [alpha] This is a new syntax for specifying schedules. |
| `overwrite_cache` | `Optional[bool]` | If set to True, the execution will always overwrite cache |
| `auto_activate` | `bool` | If set to True, the launch plan will be activated automatically on registration. Default is False. |
| `concurrency` | `Optional[ConcurrencyPolicy]` | Defines execution concurrency limits and policy when limit is reached |

## Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `concurrency` |  |  |
| `fixed_inputs` |  |  |
| `interface` |  |  |
| `labels` |  |  |
| `max_parallelism` |  |  |
| `name` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `parameters` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  |  |
| `saved_inputs` |  |  |
| `schedule` |  |  |
| `security_context` |  |  |
| `should_auto_activate` |  |  |
| `trigger` |  |  |
| `workflow` |  |  |

