---
title: FlyteNodeExecution
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FlyteNodeExecution

**Package:** `flytekit.remote`

A class encapsulating a node execution being run on a Flyte remote backend.


```python
def FlyteNodeExecution(
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
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
):
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` |
### promote_from_model()

```python
def promote_from_model(
    base_model: node_execution_models.NodeExecution,
):
```
| Parameter | Type |
|-|-|
| `base_model` | `node_execution_models.NodeExecution` |
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
