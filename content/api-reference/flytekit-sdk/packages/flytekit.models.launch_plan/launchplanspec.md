---
title: LaunchPlanSpec
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LaunchPlanSpec

**Package:** `flytekit.models.launch_plan`

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

## Properties

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

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanSpec


