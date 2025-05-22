---
title: flytekit.models.filters
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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

```python
class Contains(
    key,
    values,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.Equal

```python
class Equal(
    key,
    value,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.Filter

```python
class Filter(
    key,
    value,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.FilterList

```python
class FilterList(
    filter_list,
)
```
| Parameter | Type |
|-|-|
| `filter_list` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.GreaterThan

```python
class GreaterThan(
    key,
    value,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.GreaterThanOrEqual

```python
class GreaterThanOrEqual(
    key,
    value,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.LessThan

```python
class LessThan(
    key,
    value,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.LessThanOrEqual

```python
class LessThanOrEqual(
    key,
    value,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.NotEqual

```python
class NotEqual(
    key,
    value,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.SetFilter

```python
class SetFilter(
    key,
    values,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.ValueIn

```python
class ValueIn(
    key,
    values,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.filters.ValueNotIn

```python
class ValueNotIn(
    key,
    values,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Filter
```
| Parameter | Type |
|-|-|
| `string` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

