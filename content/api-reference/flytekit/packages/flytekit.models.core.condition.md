---
title: flytekit.models.core.condition
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.core.condition

## Directory

### Classes

| Class | Description |
|-|-|
| [`BooleanExpression`](.././flytekit.models.core.condition#flytekitmodelscoreconditionbooleanexpression) | None. |
| [`ComparisonExpression`](.././flytekit.models.core.condition#flytekitmodelscoreconditioncomparisonexpression) | None. |
| [`ConjunctionExpression`](.././flytekit.models.core.condition#flytekitmodelscoreconditionconjunctionexpression) | None. |
| [`Operand`](.././flytekit.models.core.condition#flytekitmodelscoreconditionoperand) | None. |

## flytekit.models.core.condition.BooleanExpression

```python
def BooleanExpression(
    conjunction,
    comparison,
):
```
Defines a boolean expression tree. It can be a simple or a conjunction expression.
Multiple expressions can be combined using a conjunction or a disjunction to result in a final boolean result.



| Parameter | Type |
|-|-|
| `conjunction` |  |
| `comparison` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| comparison |  |  |
| conjunction |  |  |
| is_empty |  |  |

## flytekit.models.core.condition.ComparisonExpression

```python
def ComparisonExpression(
    operator,
    left_value,
    right_value,
):
```
Defines a 2-level tree where the root is a comparison operator and Operands are primitives or known variables.
Each expression results in a boolean result.



| Parameter | Type |
|-|-|
| `operator` |  |
| `left_value` |  |
| `right_value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| left_value |  |  |
| operator |  |  |
| right_value |  |  |

## flytekit.models.core.condition.ConjunctionExpression

```python
def ConjunctionExpression(
    operator,
    left_expression,
    right_expression,
):
```
Defines a conjunction expression of two boolean expressions.


| Parameter | Type |
|-|-|
| `operator` |  |
| `left_expression` |  |
| `right_expression` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| left_expression |  |  |
| operator |  |  |
| right_expression |  |  |

## flytekit.models.core.condition.Operand

```python
def Operand(
    primitive,
    var,
    scalar,
):
```
Defines an operand to a comparison expression.


| Parameter | Type |
|-|-|
| `primitive` |  |
| `var` |  |
| `scalar` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| primitive |  |  |
| scalar |  |  |
| var |  |  |

