---
title: SecurityContext
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# SecurityContext

**Package:** `flytekit`

This is a higher level wrapper object that for the most part users shouldn't have to worry about. You should
be able to just use :py:class:`flytekit.Secret` instead.


```python
def SecurityContext(
    run_as: typing.Optional[flytekit.models.security.Identity],
    secrets: typing.Optional[typing.List[flytekit.models.security.Secret]],
    tokens: typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `run_as` | `typing.Optional[flytekit.models.security.Identity]` |
| `secrets` | `typing.Optional[typing.List[flytekit.models.security.Secret]]` |
| `tokens` | `typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]]` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.SecurityContext,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.SecurityContext` |
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
