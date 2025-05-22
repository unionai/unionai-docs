---
title: flytekit.models.core.condition
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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

```python
class BooleanExpression(
    conjunction,
    comparison,
)
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.condition_pb2.BooleanExpression


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `comparison` |  | {{< multiline >}}Comparison expression or None if not set.
:rtype: ComparisonExpression
{{< /multiline >}} |
| `conjunction` |  | {{< multiline >}}Conjunction expression or None if not set.
:rtype: ConjunctionExpression
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.core.condition.ComparisonExpression

```python
class ComparisonExpression(
    operator,
    left_value,
    right_value,
)
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.condition_pb2.ComparisonExpression


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `left_value` |  | {{< multiline >}}Gets the left value for the comparison expression.
:rtype: Operand
{{< /multiline >}} |
| `operator` |  | {{< multiline >}}Gets the operator representing this comparison expression.
:rtype: ComparisonExpression.Operator
{{< /multiline >}} |
| `right_value` |  | {{< multiline >}}Gets the right value for the comparison expression.
:rtype: Operand
{{< /multiline >}} |

## flytekit.models.core.condition.ConjunctionExpression

```python
class ConjunctionExpression(
    operator,
    left_expression,
    right_expression,
)
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.condition_pb2.ConjunctionExpression


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `left_expression` |  | {{< multiline >}}Gets the left value for the conjunction expression.
:rtype: Operand
{{< /multiline >}} |
| `operator` |  | {{< multiline >}}Gets the operator representing this conjunction expression.
:rtype: ConjunctionExpression.LogicalOperator
{{< /multiline >}} |
| `right_expression` |  | {{< multiline >}}Gets the right value for the conjunction expression.
:rtype: Operand
{{< /multiline >}} |

## flytekit.models.core.condition.Operand

```python
class Operand(
    primitive,
    var,
    scalar,
)
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.condition_pb2.Operand


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `primitive` |  | {{< multiline >}}:rtype: flytekit.models.literals.Primitive
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}:rtype: flytekit.models.literals.Scalar
{{< /multiline >}} |
| `var` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

