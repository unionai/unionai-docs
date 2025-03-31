---
title: flytekit.models.launch_plan
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.launch_plan

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planany) | A ProtocolMessage. |
| [`Auth`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planauth) | None. |
| [`LaunchPlan`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplan) | None. |
| [`LaunchPlanClosure`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanclosure) | None. |
| [`LaunchPlanMetadata`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanmetadata) | None. |
| [`LaunchPlanSpec`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanspec) | None. |
| [`LaunchPlanState`](.././flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanstate) | None. |

## flytekit.models.launch_plan.Any

A ProtocolMessage


### Methods

| Method | Description |
|-|-|
| [`Is()`](#is) | Checks if this Any represents the given protobuf type |
| [`Pack()`](#pack) | Packs the specified message into current Any message |
| [`TypeName()`](#typename) | Returns the protobuf type name of the inner message |
| [`Unpack()`](#unpack) | Unpacks the current Any message into specified message |


#### Is()

```python
def Is(
    descriptor,
):
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
):
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
):
```
Unpacks the current Any message into specified message.


| Parameter | Type |
|-|-|
| `msg` |  |

## flytekit.models.launch_plan.Auth

```python
def Auth(
    assumable_iam_role,
    kubernetes_service_account,
):
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
| assumable_iam_role |  |  |
| is_empty |  |  |
| kubernetes_service_account |  |  |

## flytekit.models.launch_plan.LaunchPlan

```python
def LaunchPlan(
    id,
    spec,
    closure,
    auto_activate,
):
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
| closure |  |  |
| id |  |  |
| is_empty |  |  |
| should_auto_activate |  |  |
| spec |  |  |

## flytekit.models.launch_plan.LaunchPlanClosure

```python
def LaunchPlanClosure(
    state,
    expected_inputs,
    expected_outputs,
):
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
| expected_inputs |  |  |
| expected_outputs |  |  |
| is_empty |  |  |
| state |  |  |

## flytekit.models.launch_plan.LaunchPlanMetadata

```python
def LaunchPlanMetadata(
    schedule,
    notifications,
    launch_conditions,
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | List of notifications based on Execution status transitions |
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
List of notifications based on Execution status transitions


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| launch_conditions |  |  |
| notifications |  |  |
| schedule |  |  |

## flytekit.models.launch_plan.LaunchPlanSpec

```python
def LaunchPlanSpec(
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
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
):
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
| annotations |  |  |
| auth_role |  |  |
| default_inputs |  |  |
| entity_metadata |  |  |
| fixed_inputs |  |  |
| is_empty |  |  |
| labels |  |  |
| max_parallelism |  |  |
| overwrite_cache |  |  |
| raw_output_data_config |  |  |
| security_context |  |  |
| workflow_id |  |  |

## flytekit.models.launch_plan.LaunchPlanState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    val,
):
```
| Parameter | Type |
|-|-|
| `val` |  |

