---
title: flytekit.models.core.condition
version: 1.16.16
variants: +flyte +union
layout: py_api
---

# flytekit.models.core.condition

## Directory

### Classes

| Class | Description |
|-|-|
| [`BooleanExpression`](.././flytekit.models.core.condition#flytekitmodelscoreconditionbooleanexpression) |  |
| [`ComparisonExpression`](.././flytekit.models.core.condition#flytekitmodelscoreconditioncomparisonexpression) |  |
| [`ConjunctionExpression`](.././flytekit.models.core.condition#flytekitmodelscoreconditionconjunctionexpression) |  |
| [`Operand`](.././flytekit.models.core.condition#flytekitmodelscoreconditionoperand) |  |

## flytekit.models.core.condition.BooleanExpression

### Parameters

```python
class BooleanExpression(
    conjunction,
    comparison,
)
```
Defines a boolean expression tree. It can be a simple or a conjunction expression.
Multiple expressions can be combined using a conjunction or a disjunction to result in a final boolean result.



| Parameter | Type | Description |
|-|-|-|
| `conjunction` |  | |
| `comparison` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `comparison` | `None` | Comparison expression or None if not set. |
| `conjunction` | `None` | Conjunction expression or None if not set. |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
**Returns:** flyteidl.core.condition_pb2.BooleanExpression

## flytekit.models.core.condition.ComparisonExpression

### Parameters

```python
class ComparisonExpression(
    operator,
    left_value,
    right_value,
)
```
Defines a 2-level tree where the root is a comparison operator and Operands are primitives or known variables.
Each expression results in a boolean result.



| Parameter | Type | Description |
|-|-|-|
| `operator` |  | |
| `left_value` |  | |
| `right_value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `left_value` | `None` | Gets the left value for the comparison expression. |
| `operator` | `None` | Gets the operator representing this comparison expression. |
| `right_value` | `None` | Gets the right value for the comparison expression. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
**Returns:** flyteidl.core.condition_pb2.ComparisonExpression

## flytekit.models.core.condition.ConjunctionExpression

### Parameters

```python
class ConjunctionExpression(
    operator,
    left_expression,
    right_expression,
)
```
Defines a conjunction expression of two boolean expressions.


| Parameter | Type | Description |
|-|-|-|
| `operator` |  | |
| `left_expression` |  | |
| `right_expression` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `left_expression` | `None` | Gets the left value for the conjunction expression. |
| `operator` | `None` | Gets the operator representing this conjunction expression. |
| `right_expression` | `None` | Gets the right value for the conjunction expression. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
**Returns:** flyteidl.core.condition_pb2.ConjunctionExpression

## flytekit.models.core.condition.Operand

### Parameters

```python
class Operand(
    primitive,
    var,
    scalar,
)
```
Defines an operand to a comparison expression.


| Parameter | Type | Description |
|-|-|-|
| `primitive` |  | |
| `var` |  | |
| `scalar` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `primitive` | `None` |  |
| `scalar` | `None` |  |
| `var` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
**Returns:** flyteidl.core.condition_pb2.Operand

