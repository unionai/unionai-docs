---
title: BindingData
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BindingData

**Package:** `flytekit.models.literals`

```python
class BindingData(
    scalar,
    collection,
    promise,
    map,
)
```
Specifies either a simple value or a reference to another output. Only one of the input arguments may be
specified.



| Parameter | Type | Description |
|-|-|-|
| `scalar` |  | |
| `collection` |  | |
| `promise` |  | |
| `map` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`to_literal_model()`](#to_literal_model) | Converts current binding data into a Literal asserting that there are no promises in the bindings. |


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
:rtype: flyteidl.core.literals_pb2.BindingData


### to_literal_model()

```python
def to_literal_model()
```
Converts current binding data into a Literal asserting that there are no promises in the bindings.
:rtype: Literal


## Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}[Optional] A collection of binding data. This allows nesting of binding data to any number of levels.
:rtype: BindingDataCollection
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}[Optional] A map of bindings. The key is always a string.
:rtype: BindingDataMap
{{< /multiline >}} |
| `promise` |  | {{< multiline >}}[Optional] References an output promised by another node.
:rtype: flytekit.models.types.OutputReference
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}A simple scalar value.
:rtype: Scalar
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns whichever value is set
:rtype: T
{{< /multiline >}} |

