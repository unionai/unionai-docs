---
title: FlyteTaskNode
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FlyteTaskNode

**Package:** `flytekit.remote`

A class encapsulating a task that a Flyte node needs to execute.


```python
def FlyteTaskNode(
    flyte_task: FlyteTask,
):
```
Refers to the task that the Node is to execute.
This is currently a oneof in protobuf, but there's only one option currently.
This code should be updated when more options are available.



| Parameter | Type |
|-|-|
| `flyte_task` | `FlyteTask` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |
### promote_from_model()

```python
def promote_from_model(
    task: FlyteTask,
):
```
Takes the idl wrapper for a TaskNode,
and returns the hydrated Flytekit object for it by fetching it with the FlyteTask control plane.


| Parameter | Type |
|-|-|
| `task` | `FlyteTask` |
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
