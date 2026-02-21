---
title: flytekit.core.options
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.options

## Directory

### Classes

| Class | Description |
|-|-|
| [`Options`](.././flytekit.core.options#flytekitcoreoptionsoptions) | These are options that can be configured for a launchplan during registration or overridden during an execution. |

## flytekit.core.options.Options

These are options that can be configured for a launchplan during registration or overridden during an execution.
For instance two people may want to run the same workflow but have the offloaded data stored in two different
buckets. Or you may want labels or annotations to be different. This object is used when launching an execution
in a Flyte backend, and also when registering launch plans.



```python
class Options(
    labels: typing.Optional[flytekit.models.common.Labels],
    annotations: typing.Optional[flytekit.models.common.Annotations],
    raw_output_data_config: typing.Optional[flytekit.models.common.RawOutputDataConfig],
    security_context: typing.Optional[flytekit.models.security.SecurityContext],
    max_parallelism: typing.Optional[int],
    notifications: typing.Optional[typing.List[flytekit.models.common.Notification]],
    disable_notifications: typing.Optional[bool],
    overwrite_cache: typing.Optional[bool],
)
```
| Parameter | Type | Description |
|-|-|-|
| `labels` | `typing.Optional[flytekit.models.common.Labels]` | Custom labels to be applied to the execution resource |
| `annotations` | `typing.Optional[flytekit.models.common.Annotations]` | Custom annotations to be applied to the execution resource |
| `raw_output_data_config` | `typing.Optional[flytekit.models.common.RawOutputDataConfig]` | Optional location of offloaded data for things like S3, etc. remote prefix for storage location of the form ``s3://&lt;bucket&gt;/key...`` or ``gcs://...`` or ``file://...``. If not specified will use the platform configured default. This is where the data for offloaded types is stored. |
| `security_context` | `typing.Optional[flytekit.models.security.SecurityContext]` | Indicates security context for permissions triggered with this launch plan |
| `max_parallelism` | `typing.Optional[int]` | Controls the maximum number of tasknodes that can be run in parallel for the entire workflow. |
| `notifications` | `typing.Optional[typing.List[flytekit.models.common.Notification]]` | List of notifications for this execution. |
| `disable_notifications` | `typing.Optional[bool]` | This should be set to true if all notifications are intended to be disabled for this execution. |
| `overwrite_cache` | `typing.Optional[bool]` | |

### Methods

| Method | Description |
|-|-|
| [`default_from()`](#default_from) |  |


#### default_from()

```python
def default_from(
    k8s_service_account: typing.Optional[str],
    raw_data_prefix: typing.Optional[str],
) -> Options
```
| Parameter | Type | Description |
|-|-|-|
| `k8s_service_account` | `typing.Optional[str]` | |
| `raw_data_prefix` | `typing.Optional[str]` | |

