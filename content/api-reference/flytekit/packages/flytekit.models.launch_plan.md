---
title: flytekit.models.launch_plan
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.launch_plan

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planany) | A ProtocolMessage. |
| [`Auth`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planauth) |  |
| [`LaunchPlan`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplan) |  |
| [`LaunchPlanClosure`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanclosure) |  |
| [`LaunchPlanMetadata`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanmetadata) |  |
| [`LaunchPlanSpec`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanspec) |  |
| [`LaunchPlanState`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanstate) |  |

## flytekit.models.launch_plan.Any

A ProtocolMessage


### Methods

| Method | Description |
|-|-|
| [`Is()`](#is) | Checks if this Any represents the given protobuf type. |
| [`Pack()`](#pack) | Packs the specified message into current Any message. |
| [`TypeName()`](#typename) | Returns the protobuf type name of the inner message. |
| [`Unpack()`](#unpack) | Unpacks the current Any message into specified message. |


#### Is()

```python
def Is(
    descriptor,
)
```
Checks if this Any represents the given protobuf type.


| Parameter | Type |
|-|-|
| `descriptor` |  |

#### Pack()

```python
def Pack(
    msg,
    type_url_prefix,
    deterministic,
)
```
Packs the specified message into current Any message.


| Parameter | Type |
|-|-|
| `msg` |  |
| `type_url_prefix` |  |
| `deterministic` |  |

#### TypeName()

```python
def TypeName()
```
Returns the protobuf type name of the inner message.


#### Unpack()

```python
def Unpack(
    msg,
)
```
Unpacks the current Any message into specified message.


| Parameter | Type |
|-|-|
| `msg` |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Auth
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
| `assumable_iam_role` |  | {{< multiline >}}The IAM role to execute the workflow with
{{< /multiline >}} |
| `is_empty` |  |  |
| `kubernetes_service_account` |  | {{< multiline >}}The kubernetes service account to execute the workflow with
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LaunchPlan
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
| `closure` |  |  |
| `id` |  |  |
| `is_empty` |  |  |
| `should_auto_activate` |  |  |
| `spec` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LaunchPlanClosure
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
| `expected_inputs` |  |  |
| `expected_outputs` |  |  |
| `is_empty` |  |  |
| `state` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | List of notifications based on Execution status transitions. |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LaunchPlanMetadata
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
List of notifications based on Execution status transitions


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `launch_conditions` |  |  |
| `notifications` |  | {{< multiline >}}List of notifications based on Execution status transitions
{{< /multiline >}} |
| `schedule` |  | {{< multiline >}}Schedule to execute the Launch Plan
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
) -> LaunchPlanSpec
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
| `annotations` |  | {{< multiline >}}The annotations to execute the workflow with
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}The authorization method with which to execute the workflow.
{{< /multiline >}} |
| `default_inputs` |  | {{< multiline >}}Input values to be passed for the execution
{{< /multiline >}} |
| `entity_metadata` |  |  |
| `fixed_inputs` |  | {{< multiline >}}Fixed, non-overridable inputs for the Launch Plan
{{< /multiline >}} |
| `is_empty` |  |  |
| `labels` |  | {{< multiline >}}The labels to execute the workflow with
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `overwrite_cache` |  |  |
| `raw_output_data_config` |  | {{< multiline >}}Where to store offloaded data like Blobs and Schemas
{{< /multiline >}} |
| `security_context` |  |  |
| `workflow_id` |  | {{< multiline >}}Unique identifier for the workflow in question
{{< /multiline >}} |

## flytekit.models.launch_plan.LaunchPlanState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    val,
) -> Text
```
| Parameter | Type |
|-|-|
| `val` |  |

