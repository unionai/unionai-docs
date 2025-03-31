---
title: flytekit.models.filters
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.filters

## Directory

### Classes

| Class | Description |
|-|-|
| [`Contains`](.././flytekit.models.filters#flytekitmodelsfilterscontains) | None. |
| [`Equal`](.././flytekit.models.filters#flytekitmodelsfiltersequal) | None. |
| [`Filter`](.././flytekit.models.filters#flytekitmodelsfiltersfilter) | None. |
| [`FilterList`](.././flytekit.models.filters#flytekitmodelsfiltersfilterlist) | None. |
| [`GreaterThan`](.././flytekit.models.filters#flytekitmodelsfiltersgreaterthan) | None. |
| [`GreaterThanOrEqual`](.././flytekit.models.filters#flytekitmodelsfiltersgreaterthanorequal) | None. |
| [`LessThan`](.././flytekit.models.filters#flytekitmodelsfilterslessthan) | None. |
| [`LessThanOrEqual`](.././flytekit.models.filters#flytekitmodelsfilterslessthanorequal) | None. |
| [`NotEqual`](.././flytekit.models.filters#flytekitmodelsfiltersnotequal) | None. |
| [`SetFilter`](.././flytekit.models.filters#flytekitmodelsfilterssetfilter) | None. |
| [`ValueIn`](.././flytekit.models.filters#flytekitmodelsfiltersvaluein) | None. |
| [`ValueNotIn`](.././flytekit.models.filters#flytekitmodelsfiltersvaluenotin) | None. |

## flytekit.models.filters.Contains

```python
def Contains(
    key,
    values,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.Equal

```python
def Equal(
    key,
    value,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.Filter

```python
def Filter(
    key,
    value,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.FilterList

```python
def FilterList(
    filter_list,
):
```
| Parameter | Type |
|-|-|
| `filter_list` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.GreaterThan

```python
def GreaterThan(
    key,
    value,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.GreaterThanOrEqual

```python
def GreaterThanOrEqual(
    key,
    value,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.LessThan

```python
def LessThan(
    key,
    value,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.LessThanOrEqual

```python
def LessThanOrEqual(
    key,
    value,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.NotEqual

```python
def NotEqual(
    key,
    value,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.SetFilter

```python
def SetFilter(
    key,
    values,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.ValueIn

```python
def ValueIn(
    key,
    values,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.models.filters.ValueNotIn

```python
def ValueNotIn(
    key,
    values,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl()
```
#### from_python_std()

```python
def from_python_std(
    string,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

