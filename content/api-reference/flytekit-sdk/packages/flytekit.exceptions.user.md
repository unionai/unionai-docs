---
title: flytekit.exceptions.user
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.exceptions.user

## Directory

### Classes

No classes in this package.

### Errors

* [`FlyteAssertion`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteassertion)
* [`FlyteAuthenticationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteauthenticationexception)
* [`FlyteCompilationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytecompilationexception)
* [`FlyteDataNotFoundException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytedatanotfoundexception)
* [`FlyteDisapprovalException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytedisapprovalexception)
* [`FlyteEntityAlreadyExistsException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentityalreadyexistsexception)
* [`FlyteEntityNotExistException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotexistexception)
* [`FlyteEntityNotFoundException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotfoundexception)
* [`FlyteFailureNodeInputMismatchException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytefailurenodeinputmismatchexception)
* [`FlyteInvalidInputException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteinvalidinputexception)
* [`FlyteMissingReturnValueException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytemissingreturnvalueexception)
* [`FlyteMissingTypeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytemissingtypeexception)
* [`FlytePromiseAttributeResolveException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytepromiseattributeresolveexception)
* [`FlyteRecoverableException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyterecoverableexception)
* [`FlyteTimeout`](.././flytekit.exceptions.user#flytekitexceptionsuserflytetimeout)
* [`FlyteTypeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytetypeexception)
* [`FlyteUserException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteuserexception)
* [`FlyteUserRuntimeException`](.././flytekit.exceptions.user#flytekitexceptionsuserflyteuserruntimeexception)
* [`FlyteValidationException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytevalidationexception)
* [`FlyteValueException`](.././flytekit.exceptions.user#flytekitexceptionsuserflytevalueexception)

## flytekit.exceptions.user.FlyteAssertion

Assertion failed.


```python
def FlyteAssertion(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteAuthenticationException

Assertion failed.


```python
def FlyteAuthenticationException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteCompilationException

Common base class for all non-exit exceptions.


```python
def FlyteCompilationException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteDataNotFoundException

Inappropriate argument value (of correct type).


```python
def FlyteDataNotFoundException(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteDisapprovalException

Assertion failed.


```python
def FlyteDisapprovalException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteEntityAlreadyExistsException

Assertion failed.


```python
def FlyteEntityAlreadyExistsException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteEntityNotExistException

Assertion failed.


```python
def FlyteEntityNotExistException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteEntityNotFoundException

Inappropriate argument value (of correct type).


```python
def FlyteEntityNotFoundException(
    module_name: str,
    entity_name: str,
):
```
| Parameter | Type |
|-|-|
| `module_name` | `str` |
| `entity_name` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteFailureNodeInputMismatchException

Assertion failed.


```python
def FlyteFailureNodeInputMismatchException(
    failure_node_node: typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')],
    workflow: WorkflowBase,
):
```
| Parameter | Type |
|-|-|
| `failure_node_node` | `typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')]` |
| `workflow` | `WorkflowBase` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteInvalidInputException

Common base class for all non-exit exceptions.


```python
def FlyteInvalidInputException(
    request: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `request` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteMissingReturnValueException

Common base class for all non-exit exceptions.


```python
def FlyteMissingReturnValueException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteMissingTypeException

Common base class for all non-exit exceptions.


```python
def FlyteMissingTypeException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlytePromiseAttributeResolveException

Assertion failed.


```python
def FlytePromiseAttributeResolveException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteRecoverableException

Common base class for all non-exit exceptions.


```python
def FlyteRecoverableException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteTimeout

Assertion failed.


```python
def FlyteTimeout(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteTypeException

Inappropriate argument type.


```python
def FlyteTypeException(
    received_type,
    expected_type,
    additional_msg,
    received_value,
):
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
| timestamp |  |  |

## flytekit.exceptions.user.FlyteUserException

Common base class for all non-exit exceptions.


```python
def FlyteUserException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteUserRuntimeException

Common base class for all non-exit exceptions.


```python
def FlyteUserRuntimeException(
    exc_value: Exception,
    timestamp: typing.Optional[float],
):
```
FlyteUserRuntimeException is thrown when a user code raises an exception.



| Parameter | Type |
|-|-|
| `exc_value` | `Exception` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |
| value |  |  |

## flytekit.exceptions.user.FlyteValidationException

Assertion failed.


```python
def FlyteValidationException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.user.FlyteValueException

Inappropriate argument value (of correct type).


```python
def FlyteValueException(
    received_value,
    error_message,
):
```
| Parameter | Type |
|-|-|
| `received_value` |  |
| `error_message` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

