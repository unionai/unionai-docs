---
title: RunPolicy
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RunPolicy

**Package:** `flyteplugins.pytorch.task`

RunPolicy describes some policy to apply to the execution of a kubeflow job.



```python
class RunPolicy(
    clean_pod_policy: typing.Optional[typing.Literal['None', 'all', 'Running']],
    ttl_seconds_after_finished: typing.Optional[int],
    active_deadline_seconds: typing.Optional[int],
    backoff_limit: typing.Optional[int],
)
```
| Parameter | Type | Description |
|-|-|-|
| `clean_pod_policy` | `typing.Optional[typing.Literal['None', 'all', 'Running']]` | Policy for cleaning up pods after the PyTorchJob completes. Allowed values are "None", "all", or "Running". Defaults to None. |
| `ttl_seconds_after_finished` | `typing.Optional[int]` | Defines the TTL (in seconds) for cleaning up finished PyTorchJobs. Defaults to None. |
| `active_deadline_seconds` | `typing.Optional[int]` | Specifies the duration (in seconds) since startTime during which the job can remain active before it is terminated. Must be a positive integer. Applies only to pods where restartPolicy is OnFailure or Always. Defaults to None. |
| `backoff_limit` | `typing.Optional[int]` | Number of retries before marking this job as failed. Defaults to None. |

