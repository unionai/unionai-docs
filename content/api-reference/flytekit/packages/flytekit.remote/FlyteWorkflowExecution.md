---
title: FlyteWorkflowExecution
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FlyteWorkflowExecution

**Package:** `flytekit.remote`

A class encapsulating a workflow execution being run on a Flyte remote backend.


```python
def FlyteWorkflowExecution(
    type_hints: Optional[Dict[str, typing.Type]],
    remote: Optional['FlyteRemote'],
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `type_hints` | `Optional[Dict[str, typing.Type]]` |
| `remote` | `Optional['FlyteRemote']` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
):
```
| Parameter | Type |
|-|-|
| `pb` |  |
### promote_from_model()

```python
def promote_from_model(
    base_model: execution_models.Execution,
    remote: Optional['FlyteRemote'],
    type_hints: Optional[Dict[str, typing.Type]],
):
```
| Parameter | Type |
|-|-|
| `base_model` | `execution_models.Execution` |
| `remote` | `Optional['FlyteRemote']` |
| `type_hints` | `Optional[Dict[str, typing.Type]]` |
### serialize_to_string()

```python
def serialize_to_string()
```
No parameters
### short_string()

```python
def short_string()
```
No parameters
### sync()

```python
def sync(
    sync_nodes: bool,
):
```
Sync the state of the current execution and returns a new object with the updated state.


| Parameter | Type |
|-|-|
| `sync_nodes` | `bool` |
### to_flyte_idl()

```python
def to_flyte_idl()
```
No parameters
### verbose_string()

```python
def verbose_string()
```
No parameters
### wait()

```python
def wait(
    timeout: Optional[Union[timedelta, int]],
    poll_interval: Optional[Union[timedelta, int]],
    sync_nodes: bool,
):
```
Wait for the execution to complete. This is a blocking call.



| Parameter | Type |
|-|-|
| `timeout` | `Optional[Union[timedelta, int]]` |
| `poll_interval` | `Optional[Union[timedelta, int]]` |
| `sync_nodes` | `bool` |
