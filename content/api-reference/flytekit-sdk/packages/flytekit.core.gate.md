---
title: flytekit.core.gate
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.gate

## Directory

### Classes

| Class | Description |
|-|-|
| [`Gate`](.././flytekit.core.gate#flytekitcoregategate) | A node type that waits for user input before proceeding with a workflow. |

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
) -> n:
```
Create a Gate object for binary approval.

Create a Gate object. This object will function like a task. Note that unlike a task,
each time this function is called, a new Python object is created. If a workflow
calls a subworkflow twice, and the subworkflow has a signal, then two Gate
objects are created. This shouldn't be a problem as long as the objects are identical.



| Parameter | Type |
|-|-|
| `upstream_item` | `Union[Tuple[Promise], Promise, VoidPromise]` |
| `name` | `str` |
| `timeout` | `datetime.timedelta` |

#### sleep()

```python
def sleep(
    duration: datetime.timedelta,
) -> n:
```
Create a sleep Gate object.



| Parameter | Type |
|-|-|
| `duration` | `datetime.timedelta` |

#### wait_for_input()

```python
def wait_for_input(
    name: str,
    timeout: datetime.timedelta,
    expected_type: typing.Type,
) -> n:
```
Create a Gate object that waits for user input of the specified type.

Create a Gate object. This object will function like a task. Note that unlike a task,
each time this function is called, a new Python object is created. If a workflow
calls a subworkflow twice, and the subworkflow has a signal, then two Gate
objects are created. This shouldn't be a problem as long as the objects are identical.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `timeout` | `datetime.timedelta` |
| `expected_type` | `typing.Type` |

## flytekit.core.gate.Gate

A node type that waits for user input before proceeding with a workflow.
A gate is a type of node that behaves like a task, but instead of running code, it either needs to wait
for user input to proceed or wait for a timer to complete running.


```python
class Gate(
    name: str,
    input_type: typing.Optional[typing.Type],
    upstream_item: typing.Optional[typing.Any],
    sleep_duration: typing.Optional[datetime.timedelta],
    timeout: typing.Optional[datetime.timedelta],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `input_type` | `typing.Optional[typing.Type]` |
| `upstream_item` | `typing.Optional[typing.Any]` |
| `sleep_duration` | `typing.Optional[datetime.timedelta]` |
| `timeout` | `typing.Optional[datetime.timedelta]` |

### Methods

| Method | Description |
|-|-|
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `input_type` |  |  |
| `literal_type` |  |  |
| `name` |  |  |
| `python_interface` |  | {{< multiline >}}This will not be valid during local execution
Part of SupportsNodeCreation interface
{{< /multiline >}} |
| `sleep_duration` |  |  |

