---
title: Primitive
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Primitive

**Package:** `flytekit.models.literals`

```python
class Primitive(
    integer: typing.Optional[int],
    float_value: typing.Optional[float],
    string_value: typing.Optional[str],
    boolean: typing.Optional[bool],
    datetime: typing.Optional[datetime.datetime],
    duration: typing.Optional[datetime.timedelta],
)
```
This object proxies the primitives supported by the Flyte IDL system.  Only one value can be set.


| Parameter | Type | Description |
|-|-|-|
| `integer` | `typing.Optional[int]` | |
| `float_value` | `typing.Optional[float]` | |
| `string_value` | `typing.Optional[str]` | |
| `boolean` | `typing.Optional[bool]` | |
| `datetime` | `typing.Optional[datetime.datetime]` | |
| `duration` | `typing.Optional[datetime.timedelta]` | |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.core.literals_pb2.Primitive


## Properties

| Property | Type | Description |
|-|-|-|
| `boolean` |  | {{< multiline >}}:rtype: bool
{{< /multiline >}} |
| `datetime` |  | {{< multiline >}}:rtype: datetime.datetime
{{< /multiline >}} |
| `duration` |  | {{< multiline >}}:rtype: datetime.timedelta
{{< /multiline >}} |
| `float_value` |  | {{< multiline >}}:rtype: float
{{< /multiline >}} |
| `integer` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `is_empty` |  |  |
| `string_value` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `value` |  | {{< multiline >}}This returns whichever field is set.
:rtype: T
{{< /multiline >}} |

