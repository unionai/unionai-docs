---
title: ExecutionSpec
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ExecutionSpec

**Package:** `flytekit.models.execution`

```python
class ExecutionSpec(
    launch_plan,
    metadata,
    notifications,
    disable_all,
    labels,
    annotations,
    auth_role,
    raw_output_data_config,
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    overwrite_cache: Optional[bool],
    interruptible: Optional[bool],
    envs: Optional[_common_models.Envs],
    tags: Optional[typing.List[str]],
    cluster_assignment: Optional[ClusterAssignment],
    execution_cluster_label: Optional[ExecutionClusterLabel],
)
```
| Parameter | Type | Description |
|-|-|-|
| `launch_plan` |  | |
| `metadata` |  | |
| `notifications` |  | |
| `disable_all` |  | |
| `labels` |  | |
| `annotations` |  | |
| `auth_role` |  | |
| `raw_output_data_config` |  | Optional location of offloaded data for things like S3, etc. |
| `max_parallelism` | `Optional[int]` | |
| `security_context` | `Optional[security.SecurityContext]` | Optional security context to use for this execution. |
| `overwrite_cache` | `Optional[bool]` | Optional flag to overwrite the cache for this execution. |
| `interruptible` | `Optional[bool]` | Optional flag to override the default interruptible flag of the executed entity. |
| `envs` | `Optional[_common_models.Envs]` | flytekit.models.common.Envs environment variables to set for this execution. |
| `tags` | `Optional[typing.List[str]]` | Optional list of tags to apply to the execution. |
| `cluster_assignment` | `Optional[ClusterAssignment]` | |
| `execution_cluster_label` | `Optional[ExecutionClusterLabel]` | Optional execution cluster label to use for this execution. |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.execution_pb2.ExecutionSpec


## Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  | {{< multiline >}}:rtype: flytekit.models.common.Annotations
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}:rtype: flytekit.models.common.AuthRole
{{< /multiline >}} |
| `cluster_assignment` |  |  |
| `disable_all` |  | {{< multiline >}}:rtype: Optional[bool]
{{< /multiline >}} |
| `envs` |  |  |
| `execution_cluster_label` |  |  |
| `interruptible` |  |  |
| `is_empty` |  |  |
| `labels` |  | {{< multiline >}}:rtype: flytekit.models.common.Labels
{{< /multiline >}} |
| `launch_plan` |  | {{< multiline >}}If the values were too large, this is the URI where the values were offloaded.
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `metadata` |  | {{< multiline >}}:rtype: ExecutionMetadata
{{< /multiline >}} |
| `notifications` |  | {{< multiline >}}:rtype: Optional[NotificationList]
{{< /multiline >}} |
| `overwrite_cache` |  |  |
| `raw_output_data_config` |  | {{< multiline >}}:rtype: flytekit.models.common.RawOutputDataConfig
{{< /multiline >}} |
| `security_context` |  |  |
| `tags` |  |  |

