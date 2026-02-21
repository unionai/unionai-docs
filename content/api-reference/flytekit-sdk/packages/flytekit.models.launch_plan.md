---
title: flytekit.models.launch_plan
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.launch_plan

## Directory

### Classes

| Class | Description |
|-|-|
| [`Auth`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planauth) |  |
| [`LaunchPlan`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplan) |  |
| [`LaunchPlanClosure`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanclosure) |  |
| [`LaunchPlanMetadata`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanmetadata) |  |
| [`LaunchPlanSpec`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanspec) |  |
| [`LaunchPlanState`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanstate) |  |

## flytekit.models.launch_plan.Auth

```python
class Auth(
    assumable_iam_role,
    kubernetes_service_account,
)
```
DEPRECATED. Do not use. Use flytekit.models.common.AuthRole instead
At most one of assumable_iam_role or kubernetes_service_account can be set.


| Parameter | Type | Description |
|-|-|-|
| `assumable_iam_role` |  | |
| `kubernetes_service_account` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `assumable_iam_role` | `None` | The IAM role to execute the workflow with :rtype: Text |
| `is_empty` | `None` |  |
| `kubernetes_service_account` | `None` | The kubernetes service account to execute the workflow with :rtype: Text |

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
:rtype: flyteidl.admin.launch_plan_pb2.Auth


## flytekit.models.launch_plan.LaunchPlan

```python
class LaunchPlan(
    id,
    spec,
    closure,
    auto_activate,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `spec` |  | |
| `closure` |  | |
| `auto_activate` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: LaunchPlanClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `is_empty` | `None` |  |
| `should_auto_activate` | `None` |  |
| `spec` | `None` | :rtype: LaunchPlanSpec |

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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlan


## flytekit.models.launch_plan.LaunchPlanClosure

```python
class LaunchPlanClosure(
    state,
    expected_inputs,
    expected_outputs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `state` |  | |
| `expected_inputs` |  | |
| `expected_outputs` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `expected_inputs` | `None` | :rtype: flytekit.models.interface.ParameterMap |
| `expected_outputs` | `None` | :rtype: flytekit.models.interface.VariableMap |
| `is_empty` | `None` |  |
| `state` | `None` | :rtype: LaunchPlanState |

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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanClosure


## flytekit.models.launch_plan.LaunchPlanMetadata

```python
class LaunchPlanMetadata(
    schedule,
    notifications,
    launch_conditions,
)
```
| Parameter | Type | Description |
|-|-|-|
| `schedule` |  | |
| `notifications` |  | |
| `launch_conditions` |  | Additional metadata for launching |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `launch_conditions` | `None` |  |
| `notifications` | `None` | List of notifications based on Execution status transitions :rtype: list[flytekit.models.common.Notification] |
| `schedule` | `None` | Schedule to execute the Launch Plan :rtype: flytekit.models.schedule.Schedule |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | List of notifications based on Execution status transitions. |


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
List of notifications based on Execution status transitions
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanMetadata


## flytekit.models.launch_plan.LaunchPlanSpec

```python
class LaunchPlanSpec(
    workflow_id,
    entity_metadata,
    default_inputs,
    fixed_inputs,
    labels: flytekit.models.common.Labels,
    annotations: flytekit.models.common.Annotations,
    auth_role: flytekit.models.common.AuthRole,
    raw_output_data_config: flytekit.models.common.RawOutputDataConfig,
    max_parallelism: typing.Optional[int],
    security_context: typing.Optional[flytekit.models.security.SecurityContext],
    overwrite_cache: typing.Optional[bool],
    concurrency_policy: typing.Optional[flytekit.models.concurrency.ConcurrencyPolicy],
)
```
The spec for a Launch Plan.



| Parameter | Type | Description |
|-|-|-|
| `workflow_id` |  | |
| `entity_metadata` |  | |
| `default_inputs` |  | |
| `fixed_inputs` |  | |
| `labels` | `flytekit.models.common.Labels` | |
| `annotations` | `flytekit.models.common.Annotations` | |
| `auth_role` | `flytekit.models.common.AuthRole` | |
| `raw_output_data_config` | `flytekit.models.common.RawOutputDataConfig` | |
| `max_parallelism` | `typing.Optional[int]` | |
| `security_context` | `typing.Optional[flytekit.models.security.SecurityContext]` | This can be used to add security information to a LaunchPlan, which will be used by every execution |
| `overwrite_cache` | `typing.Optional[bool]` | |
| `concurrency_policy` | `typing.Optional[flytekit.models.concurrency.ConcurrencyPolicy]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` | `None` | The annotations to execute the workflow with :rtype: flytekit.models.common.Annotations |
| `auth_role` | `None` | The authorization method with which to execute the workflow. :rtype: flytekit.models.common.AuthRole |
| `concurrency_policy` | `None` | Concurrency settings for the launch plan. :rtype: flytekit.models.concurrency.ConcurrencyPolicy |
| `default_inputs` | `None` | Input values to be passed for the execution :rtype: flytekit.models.interface.ParameterMap |
| `entity_metadata` | `None` | :rtype: LaunchPlanMetadata |
| `fixed_inputs` | `None` | Fixed, non-overridable inputs for the Launch Plan :rtype: flytekit.models.literals.LiteralMap |
| `is_empty` | `None` |  |
| `labels` | `None` | The labels to execute the workflow with :rtype: flytekit.models.common.Labels |
| `max_parallelism` | `None` |  |
| `overwrite_cache` | `None` |  |
| `raw_output_data_config` | `None` | Where to store offloaded data like Blobs and Schemas :rtype: flytekit.models.common.RawOutputDataConfig |
| `security_context` | `None` |  |
| `workflow_id` | `None` | Unique identifier for the workflow in question :rtype: flytekit.models.core.identifier.Identifier |

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
    pb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` |  | |

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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanSpec


## flytekit.models.launch_plan.LaunchPlanState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

