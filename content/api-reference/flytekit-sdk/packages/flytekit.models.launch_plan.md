---
title: flytekit.models.launch_plan
version: 0.1.dev2192+g7c539c3.d20250403
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


| Parameter | Type |
|-|-|
| `assumable_iam_role` |  |
| `kubernetes_service_account` |  |

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
) -> e: Auth
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
:rtype: flyteidl.admin.launch_plan_pb2.Auth


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `assumable_iam_role` |  | {{< multiline >}}The IAM role to execute the workflow with
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `kubernetes_service_account` |  | {{< multiline >}}The kubernetes service account to execute the workflow with
:rtype: Text
{{< /multiline >}} |

## flytekit.models.launch_plan.LaunchPlan

```python
class LaunchPlan(
    id,
    spec,
    closure,
    auto_activate,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `spec` |  |
| `closure` |  |
| `auto_activate` |  |

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
) -> e: LaunchPlan
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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlan


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: LaunchPlanClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `should_auto_activate` |  |  |
| `spec` |  | {{< multiline >}}:rtype: LaunchPlanSpec
{{< /multiline >}} |

## flytekit.models.launch_plan.LaunchPlanClosure

```python
class LaunchPlanClosure(
    state,
    expected_inputs,
    expected_outputs,
)
```
| Parameter | Type |
|-|-|
| `state` |  |
| `expected_inputs` |  |
| `expected_outputs` |  |

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
) -> e: LaunchPlanClosure
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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanClosure


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `expected_inputs` |  | {{< multiline >}}:rtype: flytekit.models.interface.ParameterMap
{{< /multiline >}} |
| `expected_outputs` |  | {{< multiline >}}:rtype: flytekit.models.interface.VariableMap
{{< /multiline >}} |
| `is_empty` |  |  |
| `state` |  | {{< multiline >}}:rtype: LaunchPlanState
{{< /multiline >}} |

## flytekit.models.launch_plan.LaunchPlanMetadata

```python
class LaunchPlanMetadata(
    schedule,
    notifications,
    launch_conditions,
)
```
| Parameter | Type |
|-|-|
| `schedule` |  |
| `notifications` |  |
| `launch_conditions` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | List of notifications based on Execution status transitions. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: LaunchPlanMetadata
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
List of notifications based on Execution status transitions
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanMetadata


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `launch_conditions` |  |  |
| `notifications` |  | {{< multiline >}}List of notifications based on Execution status transitions
:rtype: list[flytekit.models.common.Notification]
{{< /multiline >}} |
| `schedule` |  | {{< multiline >}}Schedule to execute the Launch Plan
:rtype: flytekit.models.schedule.Schedule
{{< /multiline >}} |

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
)
```
The spec for a Launch Plan.



| Parameter | Type |
|-|-|
| `workflow_id` |  |
| `entity_metadata` |  |
| `default_inputs` |  |
| `fixed_inputs` |  |
| `labels` | `flytekit.models.common.Labels` |
| `annotations` | `flytekit.models.common.Annotations` |
| `auth_role` | `flytekit.models.common.AuthRole` |
| `raw_output_data_config` | `flytekit.models.common.RawOutputDataConfig` |
| `max_parallelism` | `typing.Optional[int]` |
| `security_context` | `typing.Optional[flytekit.models.security.SecurityContext]` |
| `overwrite_cache` | `typing.Optional[bool]` |

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
    pb2,
) -> e: LaunchPlanSpec
```
| Parameter | Type |
|-|-|
| `pb2` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  | {{< multiline >}}The annotations to execute the workflow with
:rtype: flytekit.models.common.Annotations
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}The authorization method with which to execute the workflow.
:rtype: flytekit.models.common.AuthRole
{{< /multiline >}} |
| `default_inputs` |  | {{< multiline >}}Input values to be passed for the execution
:rtype: flytekit.models.interface.ParameterMap
{{< /multiline >}} |
| `entity_metadata` |  | {{< multiline >}}:rtype: LaunchPlanMetadata
{{< /multiline >}} |
| `fixed_inputs` |  | {{< multiline >}}Fixed, non-overridable inputs for the Launch Plan
:rtype: flytekit.models.literals.LiteralMap
{{< /multiline >}} |
| `is_empty` |  |  |
| `labels` |  | {{< multiline >}}The labels to execute the workflow with
:rtype: flytekit.models.common.Labels
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `overwrite_cache` |  |  |
| `raw_output_data_config` |  | {{< multiline >}}Where to store offloaded data like Blobs and Schemas
:rtype: flytekit.models.common.RawOutputDataConfig
{{< /multiline >}} |
| `security_context` |  |  |
| `workflow_id` |  | {{< multiline >}}Unique identifier for the workflow in question
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |

## flytekit.models.launch_plan.LaunchPlanState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    val,
) -> e: Text
```
| Parameter | Type |
|-|-|
| `val` |  |

