---
title: flytekit.core.node
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.node

## Directory

### Classes

| Class | Description |
|-|-|
| [`Node`](../flytekit.core.node/node) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |

### Methods

| Method | Description |
|-|-|
| [`assert_no_promises_in_resources()`](#assert_no_promises_in_resources) | This function will raise an exception if any of the resources have promises in them. |
| [`assert_not_promise()`](#assert_not_promise) | This function will raise an exception if the value is a promise. |


## Methods

#### assert_no_promises_in_resources()

```python
def assert_no_promises_in_resources(
    resources: _resources_model,
)
```
This function will raise an exception if any of the resources have promises in them. This is because we don't
support promises in resources / runtime overriding of resources through input values.


| Parameter | Type | Description |
|-|-|-|
| `resources` | `_resources_model` | |

#### assert_not_promise()

```python
def assert_not_promise(
    v: Any,
    location: str,
)
```
This function will raise an exception if the value is a promise. This should be used to ensure that we don't
accidentally use a promise in a place where we don't support it.


| Parameter | Type | Description |
|-|-|-|
| `v` | `Any` | |
| `location` | `str` | |

