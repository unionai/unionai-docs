---
title: AppHandle
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AppHandle

**Package:** `flyte`

Protocol defining the common interface between local and remote app handles.

Both ``_LocalApp`` (local serving) and ``App`` (remote serving) satisfy this
protocol, enabling calling code to work uniformly regardless of the serving mode.


```python
protocol AppHandle()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |
| `name` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`activate()`](#activate) |  |
| [`deactivate()`](#deactivate) |  |
| [`ephemeral_ctx()`](#ephemeral_ctx) |  |
| [`ephemeral_ctx_sync()`](#ephemeral_ctx_sync) |  |
| [`is_active()`](#is_active) |  |
| [`is_deactivated()`](#is_deactivated) |  |


### activate()

```python
def activate(
    wait: bool,
) -> AppHandle
```
| Parameter | Type | Description |
|-|-|-|
| `wait` | `bool` | |

### deactivate()

```python
def deactivate(
    wait: bool,
) -> AppHandle
```
| Parameter | Type | Description |
|-|-|-|
| `wait` | `bool` | |

### ephemeral_ctx()

```python
def ephemeral_ctx()
```
### ephemeral_ctx_sync()

```python
def ephemeral_ctx_sync()
```
### is_active()

```python
def is_active()
```
### is_deactivated()

```python
def is_deactivated()
```
