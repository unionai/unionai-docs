---
title: Auth
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Auth

**Package:** `flytekit.models.launch_plan`

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
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.launch_plan_pb2.Auth


## Properties

| Property | Type | Description |
|-|-|-|
| `assumable_iam_role` |  | {{< multiline >}}The IAM role to execute the workflow with
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `kubernetes_service_account` |  | {{< multiline >}}The kubernetes service account to execute the workflow with
:rtype: Text
{{< /multiline >}} |

