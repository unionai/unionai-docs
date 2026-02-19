---
title: flytekit.core.gate
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.gate

## Directory

### Classes

| Class | Description |
|-|-|
| [`Gate`](../flytekit.core.gate/gate) | A node type that waits for user input before proceeding with a workflow. |

### Methods

| Method | Description |
|-|-|
| [`approve()`](#approve) | Create a Gate object for binary approval. |
| [`sleep()`](#sleep) | Create a sleep Gate object. |
| [`wait_for_input()`](#wait_for_input) | Create a Gate object that waits for user input of the specified type. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_TIMEOUT` | `timedelta` |  |

## Methods

#### approve()

```python
def approve(
    upstream_item: Union[Tuple[Promise], Promise, VoidPromise],
    name: str,
    timeout: datetime.timedelta,
)
```
Create a Gate object for binary approval.

Create a Gate object. This object will function like a task. Note that unlike a task,
each time this function is called, a new Python object is created. If a workflow
calls a subworkflow twice, and the subworkflow has a signal, then two Gate
objects are created. This shouldn't be a problem as long as the objects are identical.



| Parameter | Type | Description |
|-|-|-|
| `upstream_item` | `Union[Tuple[Promise], Promise, VoidPromise]` | This should be the output, one output, of a previous task, that you want to gate execution on. This is the value that you want a human to check before moving on. |
| `name` | `str` | The name of the gate node. |
| `timeout` | `datetime.timedelta` | How long to wait before Flyte fails the workflow. :return: |

#### sleep()

```python
def sleep(
    duration: datetime.timedelta,
)
```
Create a sleep Gate object.



| Parameter | Type | Description |
|-|-|-|
| `duration` | `datetime.timedelta` | How long to sleep for :return: |

#### wait_for_input()

```python
def wait_for_input(
    name: str,
    timeout: datetime.timedelta,
    expected_type: typing.Type,
)
```
Create a Gate object that waits for user input of the specified type.

Create a Gate object. This object will function like a task. Note that unlike a task,
each time this function is called, a new Python object is created. If a workflow
calls a subworkflow twice, and the subworkflow has a signal, then two Gate
objects are created. This shouldn't be a problem as long as the objects are identical.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the gate node. |
| `timeout` | `datetime.timedelta` | How long to wait for before Flyte fails the workflow. |
| `expected_type` | `typing.Type` | What is the type that the user will be inputting? :return: |

