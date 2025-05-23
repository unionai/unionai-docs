---
title: flytekit.exceptions.user
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.exceptions.user

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteAssertion`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteassertion) | Assertion failed. |
| [`FlyteAuthenticationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteauthenticationexception) | Assertion failed. |
| [`FlyteCompilationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytecompilationexception) | Common base class for all non-exit exceptions. |
| [`FlyteDataNotFoundException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytedatanotfoundexception) | Inappropriate argument value (of correct type). |
| [`FlyteDisapprovalException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytedisapprovalexception) | Assertion failed. |
| [`FlyteEntityAlreadyExistsException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentityalreadyexistsexception) | Assertion failed. |
| [`FlyteEntityNotExistException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotexistexception) | Assertion failed. |
| [`FlyteEntityNotFoundException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotfoundexception) | Inappropriate argument value (of correct type). |
| [`FlyteFailureNodeInputMismatchException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytefailurenodeinputmismatchexception) | Assertion failed. |
| [`FlyteInvalidInputException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteinvalidinputexception) | Common base class for all non-exit exceptions. |
| [`FlyteMissingReturnValueException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytemissingreturnvalueexception) | Common base class for all non-exit exceptions. |
| [`FlyteMissingTypeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytemissingtypeexception) | Common base class for all non-exit exceptions. |
| [`FlytePromiseAttributeResolveException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytepromiseattributeresolveexception) | Assertion failed. |
| [`FlyteRecoverableException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyterecoverableexception) | Common base class for all non-exit exceptions. |
| [`FlyteTimeout`](.././flytekit.exceptions.user#flytekitexceptionsuserflytetimeout) | Assertion failed. |
| [`FlyteTypeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytetypeexception) | Inappropriate argument type. |
| [`FlyteUserException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteuserexception) | Common base class for all non-exit exceptions. |
| [`FlyteUserRuntimeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteuserruntimeexception) | Common base class for all non-exit exceptions. |
| [`FlyteValidationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytevalidationexception) | Assertion failed. |
| [`FlyteValueException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytevalueexception) | Inappropriate argument value (of correct type). |

## flytekit.exceptions.user.FlyteAssertion

Assertion failed.


```python
class FlyteAssertion(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteAuthenticationException

Assertion failed.


```python
class FlyteAuthenticationException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteCompilationException

Common base class for all non-exit exceptions.


```python
class FlyteCompilationException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteDataNotFoundException

Inappropriate argument value (of correct type).


```python
class FlyteDataNotFoundException(
    path: str,
)
```
| Parameter | Type |
|-|-|
| `path` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteDisapprovalException

Assertion failed.


```python
class FlyteDisapprovalException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteEntityAlreadyExistsException

Assertion failed.


```python
class FlyteEntityAlreadyExistsException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteEntityNotExistException

Assertion failed.


```python
class FlyteEntityNotExistException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteEntityNotFoundException

Inappropriate argument value (of correct type).


```python
class FlyteEntityNotFoundException(
    module_name: str,
    entity_name: str,
)
```
| Parameter | Type |
|-|-|
| `module_name` | `str` |
| `entity_name` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteFailureNodeInputMismatchException

Assertion failed.


```python
class FlyteFailureNodeInputMismatchException(
    failure_node_node: typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')],
    workflow: WorkflowBase,
)
```
| Parameter | Type |
|-|-|
| `failure_node_node` | `typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')]` |
| `workflow` | `WorkflowBase` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteInvalidInputException

Common base class for all non-exit exceptions.


```python
class FlyteInvalidInputException(
    request: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `request` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteMissingReturnValueException

Common base class for all non-exit exceptions.


```python
class FlyteMissingReturnValueException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteMissingTypeException

Common base class for all non-exit exceptions.


```python
class FlyteMissingTypeException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlytePromiseAttributeResolveException

Assertion failed.


```python
class FlytePromiseAttributeResolveException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteRecoverableException

Common base class for all non-exit exceptions.


```python
class FlyteRecoverableException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteTimeout

Assertion failed.


```python
class FlyteTimeout(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteTypeException

Inappropriate argument type.


```python
class FlyteTypeException(
    received_type,
    expected_type,
    additional_msg,
    received_value,
)
```
| Parameter | Type |
|-|-|
| `received_type` |  |
| `expected_type` |  |
| `additional_msg` |  |
| `received_value` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteUserException

Common base class for all non-exit exceptions.


```python
class FlyteUserException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteUserRuntimeException

Common base class for all non-exit exceptions.


```python
class FlyteUserRuntimeException(
    exc_value: Exception,
    timestamp: typing.Optional[float],
)
```
FlyteUserRuntimeException is thrown when a user code raises an exception.



| Parameter | Type |
|-|-|
| `exc_value` | `Exception` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |
| `value` |  |  |

## flytekit.exceptions.user.FlyteValidationException

Assertion failed.


```python
class FlyteValidationException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.user.FlyteValueException

Inappropriate argument value (of correct type).


```python
class FlyteValueException(
    received_value,
    error_message,
)
```
| Parameter | Type |
|-|-|
| `received_value` |  |
| `error_message` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

