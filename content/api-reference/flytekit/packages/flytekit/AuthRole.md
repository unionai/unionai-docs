---
title: AuthRole
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# AuthRole

**Package:** `flytekit`

```python
def AuthRole(
    assumable_iam_role,
    kubernetes_service_account,
):
```
Auth configuration for IAM or K8s service account.

Either one or both of the assumable IAM role and/or the K8s service account can be set.



| Parameter | Type |
|-|-|
| `assumable_iam_role` |  |
| `kubernetes_service_account` |  |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |
### serialize_to_string()

```python
def serialize_to_string()
```
No parameters
### short_string()

```python
def short_string()
```
No parameters
### to_flyte_idl()

```python
def to_flyte_idl()
```
No parameters
### verbose_string()

```python
def verbose_string()
```
No parameters
