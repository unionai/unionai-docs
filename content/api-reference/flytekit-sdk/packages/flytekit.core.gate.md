---
title: flytekit.core.gate
version: 1.16.10
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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `input_type` | `typing.Optional[typing.Type]` | |
| `upstream_item` | `typing.Optional[typing.Any]` | |
| `sleep_duration` | `typing.Optional[datetime.timedelta]` | |
| `timeout` | `typing.Optional[datetime.timedelta]` | |

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
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `kwargs` | `**kwargs` | |

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

