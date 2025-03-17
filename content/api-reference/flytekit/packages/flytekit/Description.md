---
title: Description
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Description

**Package:** `flytekit`

Full user description with formatting preserved. This can be rendered
by clients, such as the console or command line tools with in-tact
formatting.


```python
def Description(
    value: typing.Optional[str],
    uri: typing.Optional[str],
    icon_link: typing.Optional[str],
    format: <enum 'DescriptionFormat'>,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `value` | `typing.Optional[str]` |
| `uri` | `typing.Optional[str]` |
| `icon_link` | `typing.Optional[str]` |
| `format` | `<enum 'DescriptionFormat'>` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.Description,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.Description` |
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
