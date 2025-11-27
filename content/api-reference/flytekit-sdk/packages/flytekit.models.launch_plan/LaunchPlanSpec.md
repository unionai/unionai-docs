---
title: LaunchPlanSpec
version: 1.16.10
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


## Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  | {{< multiline >}}The annotations to execute the workflow with
:rtype: flytekit.models.common.Annotations
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}The authorization method with which to execute the workflow.
:rtype: flytekit.models.common.AuthRole
{{< /multiline >}} |
| `concurrency_policy` |  | {{< multiline >}}Concurrency settings for the launch plan.
:rtype: flytekit.models.concurrency.ConcurrencyPolicy
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

