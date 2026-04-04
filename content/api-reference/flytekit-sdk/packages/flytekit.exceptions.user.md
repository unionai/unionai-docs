---
title: flytekit.exceptions.user
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.exceptions.user

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteAssertion`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteassertion) |  |
| [`FlyteAuthenticationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteauthenticationexception) |  |
| [`FlyteCompilationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytecompilationexception) |  |
| [`FlyteDataNotFoundException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytedatanotfoundexception) |  |
| [`FlyteDisapprovalException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytedisapprovalexception) |  |
| [`FlyteEntityAlreadyExistsException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentityalreadyexistsexception) |  |
| [`FlyteEntityNotExistException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotexistexception) |  |
| [`FlyteEntityNotFoundException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotfoundexception) |  |
| [`FlyteFailureNodeInputMismatchException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytefailurenodeinputmismatchexception) |  |
| [`FlyteInvalidInputException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteinvalidinputexception) |  |
| [`FlyteMissingReturnValueException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytemissingreturnvalueexception) |  |
| [`FlyteMissingTypeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytemissingtypeexception) |  |
| [`FlytePromiseAttributeResolveException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytepromiseattributeresolveexception) |  |
| [`FlyteRecoverableException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyterecoverableexception) |  |
| [`FlyteTimeout`](.././flytekit.exceptions.user#flytekitexceptionsuserflytetimeout) |  |
| [`FlyteTypeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytetypeexception) |  |
| [`FlyteUserException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteuserexception) |  |
| [`FlyteUserRuntimeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteuserruntimeexception) |  |
| [`FlyteValidationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytevalidationexception) |  |
| [`FlyteValueException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytevalueexception) |  |

## flytekit.exceptions.user.FlyteAssertion

### Parameters

```python
class FlyteAssertion(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteAuthenticationException

### Parameters

```python
class FlyteAuthenticationException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteCompilationException

### Parameters

```python
class FlyteCompilationException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `fn` | `typing.Callable` | |
| `param_name` | `typing.Optional[str]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteDataNotFoundException

### Parameters

```python
class FlyteDataNotFoundException(
    path: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteDisapprovalException

### Parameters

```python
class FlyteDisapprovalException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteEntityAlreadyExistsException

### Parameters

```python
class FlyteEntityAlreadyExistsException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteEntityNotExistException

### Parameters

```python
class FlyteEntityNotExistException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteEntityNotFoundException

### Parameters

```python
class FlyteEntityNotFoundException(
    module_name: str,
    entity_name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `module_name` | `str` | |
| `entity_name` | `str` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteFailureNodeInputMismatchException

### Parameters

```python
class FlyteFailureNodeInputMismatchException(
    failure_node_node: typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')],
    workflow: WorkflowBase,
)
```
| Parameter | Type | Description |
|-|-|-|
| `failure_node_node` | `typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')]` | |
| `workflow` | `WorkflowBase` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteInvalidInputException

### Parameters

```python
class FlyteInvalidInputException(
    request: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` | `typing.Any` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteMissingReturnValueException

### Parameters

```python
class FlyteMissingReturnValueException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `fn` | `typing.Callable` | |
| `param_name` | `typing.Optional[str]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteMissingTypeException

### Parameters

```python
class FlyteMissingTypeException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `fn` | `typing.Callable` | |
| `param_name` | `typing.Optional[str]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlytePromiseAttributeResolveException

### Parameters

```python
class FlytePromiseAttributeResolveException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteRecoverableException

### Parameters

```python
class FlyteRecoverableException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteTimeout

### Parameters

```python
class FlyteTimeout(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteTypeException

### Parameters

```python
class FlyteTypeException(
    received_type,
    expected_type,
    additional_msg,
    received_value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `received_type` |  | |
| `expected_type` |  | |
| `additional_msg` |  | |
| `received_value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteUserException

### Parameters

```python
class FlyteUserException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteUserRuntimeException

### Parameters

```python
class FlyteUserRuntimeException(
    exc_value: Exception,
    timestamp: typing.Optional[float],
)
```
FlyteUserRuntimeException is thrown when a user code raises an exception.



| Parameter | Type | Description |
|-|-|-|
| `exc_value` | `Exception` | The exception that was raised from user code. |
| `timestamp` | `typing.Optional[float]` | The timestamp as fractional seconds since epoch when the exception was raised. |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |
| `value` | `None` |  |

## flytekit.exceptions.user.FlyteValidationException

### Parameters

```python
class FlyteValidationException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.user.FlyteValueException

### Parameters

```python
class FlyteValueException(
    received_value,
    error_message,
)
```
| Parameter | Type | Description |
|-|-|-|
| `received_value` |  | |
| `error_message` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

