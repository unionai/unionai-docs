---
title: flytekit.models.filters
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.filters

## Directory

### Classes

| Class | Description |
|-|-|
| [`Contains`](.././flytekit.models.filters#flytekitmodelsfilterscontains) |  |
| [`Equal`](.././flytekit.models.filters#flytekitmodelsfiltersequal) |  |
| [`Filter`](.././flytekit.models.filters#flytekitmodelsfiltersfilter) |  |
| [`FilterList`](.././flytekit.models.filters#flytekitmodelsfiltersfilterlist) |  |
| [`GreaterThan`](.././flytekit.models.filters#flytekitmodelsfiltersgreaterthan) |  |
| [`GreaterThanOrEqual`](.././flytekit.models.filters#flytekitmodelsfiltersgreaterthanorequal) |  |
| [`LessThan`](.././flytekit.models.filters#flytekitmodelsfilterslessthan) |  |
| [`LessThanOrEqual`](.././flytekit.models.filters#flytekitmodelsfilterslessthanorequal) |  |
| [`NotEqual`](.././flytekit.models.filters#flytekitmodelsfiltersnotequal) |  |
| [`SetFilter`](.././flytekit.models.filters#flytekitmodelsfilterssetfilter) |  |
| [`ValueIn`](.././flytekit.models.filters#flytekitmodelsfiltersvaluein) |  |
| [`ValueNotIn`](.././flytekit.models.filters#flytekitmodelsfiltersvaluenotin) |  |

## flytekit.models.filters.Contains

### Parameters

```python
class Contains(
    key,
    values,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `values` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.Equal

### Parameters

```python
class Equal(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.Filter

### Parameters

```python
class Filter(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.FilterList

### Parameters

```python
class FilterList(
    filter_list,
)
```
| Parameter | Type | Description |
|-|-|-|
| `filter_list` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.GreaterThan

### Parameters

```python
class GreaterThan(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.GreaterThanOrEqual

### Parameters

```python
class GreaterThanOrEqual(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.LessThan

### Parameters

```python
class LessThan(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.LessThanOrEqual

### Parameters

```python
class LessThanOrEqual(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.NotEqual

### Parameters

```python
class NotEqual(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.SetFilter

### Parameters

```python
class SetFilter(
    key,
    values,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `values` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.ValueIn

### Parameters

```python
class ValueIn(
    key,
    values,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `values` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

## flytekit.models.filters.ValueNotIn

### Parameters

```python
class ValueNotIn(
    key,
    values,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `values` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

**Returns:** Filter

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


**Returns:** Text

