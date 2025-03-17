---
title: FlyteTaskExecution
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FlyteTaskExecution

**Package:** `flytekit.remote`

A class encapsulating a task execution being run on a Flyte remote backend.


```python
def FlyteTaskExecution(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
):
```
| Parameter | Type |
|-|-|
| `proto` |  |
### promote_from_model()

```python
def promote_from_model(
    base_model: admin_task_execution_models.TaskExecution,
):
```
| Parameter | Type |
|-|-|
| `base_model` | `admin_task_execution_models.TaskExecution` |
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
