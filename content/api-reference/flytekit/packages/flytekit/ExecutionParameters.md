---
title: ExecutionParameters
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# ExecutionParameters

**Package:** `flytekit`

This is a run-time user-centric context object that is accessible to every @task method. It can be accessed using

.. code-block:: python

flytekit.current_context()

This object provides the following
* a statsd handler
* a logging handler
* the execution ID as an :py:class:`flytekit.models.core.identifier.WorkflowExecutionIdentifier` object
* a working directory for the user to write arbitrary files to

Please do not confuse this object with the :py:class:`flytekit.FlyteContext` object.


```python
def ExecutionParameters(
    execution_date,
    tmp_dir,
    stats,
    execution_id: typing.Optional[_identifier.WorkflowExecutionIdentifier],
    logging,
    raw_output_prefix,
    output_metadata_prefix,
    checkpoint,
    decks,
    task_id: typing.Optional[_identifier.Identifier],
    enable_deck: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `execution_date` |  |
| `tmp_dir` |  |
| `stats` |  |
| `execution_id` | `typing.Optional[_identifier.WorkflowExecutionIdentifier]` |
| `logging` |  |
| `raw_output_prefix` |  |
| `output_metadata_prefix` |  |
| `checkpoint` |  |
| `decks` |  |
| `task_id` | `typing.Optional[_identifier.Identifier]` |
| `enable_deck` | `bool` |
| `kwargs` | ``**kwargs`` |
## Methods

### builder()

```python
def builder()
```
No parameters
### get()

```python
def get(
    key: str,
):
```
Returns task specific context if present else raise an error. The returned context will match the key


| Parameter | Type |
|-|-|
| `key` | `str` |
### has_attr()

```python
def has_attr(
    attr_name: str,
):
```
| Parameter | Type |
|-|-|
| `attr_name` | `str` |
### new_builder()

```python
def new_builder(
    current: Optional[ExecutionParameters],
):
```
| Parameter | Type |
|-|-|
| `current` | `Optional[ExecutionParameters]` |
### with_enable_deck()

```python
def with_enable_deck(
    enable_deck: bool,
):
```
| Parameter | Type |
|-|-|
| `enable_deck` | `bool` |
### with_task_sandbox()

```python
def with_task_sandbox()
```
No parameters
