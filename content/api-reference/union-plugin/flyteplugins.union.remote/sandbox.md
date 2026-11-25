---
title: Sandbox
description: "A sandbox session, as the platform has it."
icon: braces
version: 0.26.2
variants: -flyte +union
layout: py_api
---

# Sandbox

**Package:** `flyteplugins.union.remote`

A sandbox session, as the platform has it.



## Parameters

```python
class Sandbox(
    pb2: pb.Sandbox,
    already_exists: bool = False,
    started: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `pb.Sandbox` | |
| `already_exists` | `bool` | |
| `started` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `address` | `Any` | Where its worker serves it (an ``ActionAddress``), once it is ready. Only a watch's answer carries it (`watch`, `current`). |
| `created_at` | `Optional[datetime]` |  |
| `domain` | `str` |  |
| `error` | `Optional[str]` | Why it failed, if it did. |
| `generation` | `int` | Which of the sandbox's runs `run` is: 0 for the first, one more for each resume that started one. |
| `is_ended` | `bool` | Whether its run has ended: as its state says it, where it has one (a watch's, a resume's answer), else as its run's phase says it (``succeeded``, ``failed``, ``aborted``, ``timed_out``). |
| `is_ready` | `bool` | Whether it is reachable. Only a watch says so (`watch`, `current`): never true of a get, list or create answer. |
| `name` | `str` |  |
| `org` | `str` |  |
| `phase` | `str` | The phase of the run that backs it: ``running``, ``succeeded``, ``aborted``, ... |
| `project` | `str` |  |
| `resumable` | `bool` | Whether a resume can start the sandbox again once its run has ended. |
| `run` | `str` | The run that is the sandbox now, which the data proxy routes by: its own name for its first run, and one derived from it for each run a resume starts. Its name where the service doesn't say. |
| `state` | `str` | ``pending`` (no address yet), ``ready`` (reachable) or ``ended``, as a watch (`watch`, `current`) says it. A get, list or create answer carries no state: it is ``ended`` if its run's phase is one that ended, and ``""`` (not known) otherwise. |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Starts a sandbox named ``name`` (a run name: unique in its project and domain) that runs ``task_spec``, a session's task as the platform takes it. |
| [`current()`](#current) | The sandbox named ``name`` as it is now, with its state and, while it is ready, its address: a watch's first answer, the watch closed once it has given it. |
| [`delete()`](#delete) | Ends the sandbox named ``name``: its run is aborted, with ``reason``. |
| [`get()`](#get) | The sandbox named ``name``, as the platform records it now: its run, that run's phase (`is_ended`) and its error. |
| [`listall()`](#listall) | The sandboxes of the project and domain, ``limit`` at most, a page of the service's at a time. |
| [`resume()`](#resume) | Brings the sandbox named ``name`` back: one whose run has not ended is returned as it is (it may be suspended, which the session's own API resumes); one that ended, and was created ``resumable``, is started again as its next run (`generation`), from what its last run kept, with `started` set. |
| [`runs()`](#runs) | Every run the sandbox named ``name`` has had, one per generation, oldest first (``ListSandboxRuns``). |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`watch()`](#watch) | The sandbox named ``name`` each time it changes, from as it is now: its state (``pending``, ``ready``, ``ended``), its address while it is ready, and its run's phase. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.create.aio()`.
```python
def create(
    cls,
    name: str,
    task_spec: Any,
    queue: str = '',
    labels: Optional[Mapping[str, str]] = None,
    resumable: bool = False,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
) -> Sandbox
```
Starts a sandbox named ``name`` (a run name: unique in its project
and domain) that runs ``task_spec``, a session's task as the platform
takes it. It is pending until its worker reports its address:
`watch` it (the answer carries no state nor address).

A sandbox of that name that exists already is returned as it is, with
`already_exists` set: nothing is started, and ``task_spec`` is
not used. ``resumable`` has the service keep the sandbox's disk when
each of its runs ends, published as the artifact named after it, for
`resume`: ``task_spec`` must then keep a disk that can be
committed (not a scratch one) and name the artifact's type.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_spec` | `Any` | |
| `queue` | `str` | |
| `labels` | `Optional[Mapping[str, str]]` | |
| `resumable` | `bool` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

### current()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.current.aio()`.
```python
def current(
    cls,
    name: str,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
) -> Sandbox
```
The sandbox named ``name`` as it is now, with its state and, while
it is ready, its address: a watch's first answer, the watch closed
once it has given it. Pending for one not created (yet).


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.delete.aio()`.
```python
def delete(
    cls,
    name: str,
    reason: str = '',
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
)
```
Ends the sandbox named ``name``: its run is aborted, with ``reason``.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `reason` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.get.aio()`.
```python
def get(
    cls,
    name: str,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
) -> Sandbox
```
The sandbox named ``name``, as the platform records it now: its
run, that run's phase (`is_ended`) and its error. Whether it is
ready, and its address, are not part of it: `current` or
`watch` say those.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.listall.aio()`.
```python
def listall(
    cls,
    limit: int = 100,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
) -> AsyncIterator[Sandbox]
```
The sandboxes of the project and domain, ``limit`` at most, a page
of the service's at a time. As `get` has them: no state nor
address.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

### resume()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.resume.aio()`.
```python
def resume(
    cls,
    name: str,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
) -> Sandbox
```
Brings the sandbox named ``name`` back: one whose run has not ended
is returned as it is (it may be suspended, which the session's own
API resumes); one that ended, and was created ``resumable``, is
started again as its next run (`generation`), from what its
last run kept, with `started` set. `watch` it for its
address.

The service's errors are raised as they are: NOT_FOUND (never
created), FAILED_PRECONDITION (deleted, not resumable, or its last
run failed, was aborted or kept nothing) and UNAVAILABLE (its last
run ended moments ago and its disk is not recorded yet: try again).
A control plane without ``ResumeSandbox`` (UNIMPLEMENTED) raises
`SandboxNotSupported`.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

### runs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.runs.aio()`.
```python
def runs(
    cls,
    name: str,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
) -> List[SandboxRun]
```
Every run the sandbox named ``name`` has had, one per generation,
oldest first (``ListSandboxRuns``). From a control plane without it
(UNIMPLEMENTED), its current run alone, as `get` has it.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

### watch()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Sandbox.watch.aio()`.
```python
def watch(
    cls,
    name: str,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    org: Optional[str] = None,
) -> AsyncIterator[Sandbox]
```
The sandbox named ``name`` each time it changes, from as it is now:
its state (``pending``, ``ready``, ``ended``), its address while it is
ready, and its run's phase. It may be watched before it is created: it
is pending until it is. The watch ends once it has ended.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `org` | `Optional[str]` | |

