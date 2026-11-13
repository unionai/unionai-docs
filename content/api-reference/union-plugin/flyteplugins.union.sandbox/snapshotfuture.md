---
title: SnapshotFuture
description: "A snapshot taken, from ``await sb.snapshot(wait=False)``: what it holds is fixed and its session runs on."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SnapshotFuture

**Package:** `flyteplugins.union.sandbox`

A snapshot taken, from ``await sb.snapshot(wait=False)``: what it holds
is fixed and its session runs on. ``await fut.wait()`` returns it as a
`SandboxSnapshot` once committed, which is when it can be restored
anywhere; ``env.session(name, snapshot=fut)`` waits for it too. The node
commits it whether or not anyone waits.


## Parameters

```python
class SnapshotFuture(
    session: str,
    paused_ms: int,
    generation: int,
    committed: Awaitable[SandboxSnapshot],
)
```
| Parameter | Type | Description |
|-|-|-|
| `session` | `str` | |
| `paused_ms` | `int` | |
| `generation` | `int` | |
| `committed` | `Awaitable[SandboxSnapshot]` | |

## Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Whether it is committed (or its commit failed). |
| [`wait()`](#wait) | The snapshot, once committed. |


### done()

```python
def done()
```
Whether it is committed (or its commit failed).


### wait()

```python
def wait()
```
The snapshot, once committed. Raises if its commit failed (the
session runs on, with no snapshot). Waiting again returns the same.


