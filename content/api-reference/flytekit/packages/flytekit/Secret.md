---
title: Secret
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Secret

**Package:** `flytekit`

See :std:ref:`cookbook:secrets` for usage examples.



```python
def Secret(
    group: typing.Optional[str],
    key: typing.Optional[str],
    group_version: typing.Optional[str],
    mount_requirement: <enum 'MountType'>,
    env_var: typing.Optional[str],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `group` | `typing.Optional[str]` |
| `key` | `typing.Optional[str]` |
| `group_version` | `typing.Optional[str]` |
| `mount_requirement` | `<enum 'MountType'>` |
| `env_var` | `typing.Optional[str]` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.Secret,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.Secret` |
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
