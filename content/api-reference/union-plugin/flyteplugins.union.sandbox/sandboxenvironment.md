---
title: SandboxEnvironment
description: "A sandbox definition: secrets, env vars, resources, network and lifetime."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SandboxEnvironment

**Package:** `flyteplugins.union.sandbox`

A sandbox definition: secrets, env vars, resources, network and lifetime.

Sessions start from a task with `session` and run the platform's
Python base. ``resources`` sizes the VM by cpu and memory (default 1 vCPU,
1 GiB). Custom images, other resources and pod settings are not supported
yet and raise; see "Not supported yet" in `flyteplugins.union.sandbox`.


## Parameters

```python
class SandboxEnvironment(
    name: str,
    depends_on: List[Environment] = <factory>,
    pod_template: Optional[Union[str, PodTemplate]] = None,
    description: Optional[str] = None,
    secrets: Optional[SecretRequest] = None,
    env_vars: Optional[Dict[str, str]] = None,
    resources: Optional[Resources] = None,
    interruptible: bool = False,
    image: Any = None,
    include: Tuple[str, ...] = <factory>,
    service_account: Optional[str] = None,
    network: Network = <factory>,
    max_duration: Union[int, timedelta] = 3600,
    queue: str = '',
    expiry: Optional[Union[int, timedelta]] = None,
    publish: Union[bool, str] = False,
    snapshot_every: Optional[Union[int, timedelta]] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `depends_on` | `List[Environment]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `resources` | `Optional[Resources]` | |
| `interruptible` | `bool` | |
| `image` | `Any` | |
| `include` | `Tuple[str, ...]` | |
| `service_account` | `Optional[str]` | |
| `network` | `Network` | |
| `max_duration` | `Union[int, timedelta]` | |
| `queue` | `str` | |
| `expiry` | `Optional[Union[int, timedelta]]` | |
| `publish` | `Union[bool, str]` | |
| `snapshot_every` | `Optional[Union[int, timedelta]]` | |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`attach()`](#attach) | Yields the `Sandbox` of a session that is already running, by its `Sandbox.name`: one started outside a task by another replica of an app, or by this app before it restarted. |
| [`clone_with()`](#clone_with) |  |
| [`session()`](#session) | Starts a session and yields its `Sandbox`. |


### add_dependency()

```python
def add_dependency(
    *env: Environment,
)
```
Add one or more environment dependencies so they are deployed together.

When you deploy this environment, any environments added via
`add_dependency` will also be deployed. This is an alternative to
passing `depends_on=[...]` at construction time, useful when the
dependency is defined after the environment is created.

Duplicate dependencies are silently ignored. An environment cannot
depend on itself.



| Parameter | Type | Description |
|-|-|-|
| `*env` | `Environment` | One or more `Environment` instances to add as dependencies. |

### attach()

```python
def attach(
    name: str,
    ready_timeout: Union[int, timedelta] = 120,
) -> AsyncIterator[Sandbox]
```
Yields the `Sandbox` of a session that is already running,
by its `Sandbox.name`: one started outside a task by another
replica of an app, or by this app before it restarted.

The session is not this block's: leaving the block only disconnects
from it, and it runs on until whoever started it closes it, or its
``max_duration``. `Sandbox.close` and `Sandbox.cancel`
still end it, for the caller that means to. Waits up to
``ready_timeout`` for a session that is still starting; fails with
`SandboxSessionError` if there is none of that name, or it has
ended.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `ready_timeout` | `Union[int, timedelta]` | |

### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]] = None,
    resources: Optional[Resources] = None,
    env_vars: Optional[Dict[str, str]] = None,
    secrets: Optional[SecretRequest] = None,
    depends_on: Optional[List[Environment]] = None,
    description: Optional[str] = None,
    **kwargs: Any,
) -> Environment
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` | |
| `resources` | `Optional[Resources]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `depends_on` | `Optional[List[Environment]]` | |
| `description` | `Optional[str]` | |
| `**kwargs` | `Any` | |

### session()

```python
def session(
    name: str,
    volume: SessionVolume = None,
    snapshot: Optional[Union[SandboxSnapshot, SnapshotFuture]] = None,
    ready_timeout: Union[int, timedelta] = 120,
) -> AsyncIterator[Sandbox]
```
Starts a session and yields its `Sandbox`.

Inside a task the session is a child action of the task. Outside one,
in an app or a script, it is a sandbox of its own, started through the
platform (flyte must be initialised with a project and a domain, as
``flyte.init_in_cluster`` does in an app): its `Sandbox.name` is
then unique in the project and domain, and `attach` reaches it
from another process by that name.

``name`` says what the session is for (``"build"``, ``"snapshot-1"``,
``"resume-1"``): it names the session's action, so a run's sessions
read in order as what happened. Resuming a suspended session in place
keeps the name it had.

The session is a child action of the task, run by a sandbox worker with
no pod. It is yielded once it answers, and ends when the block
exits: closed gracefully (`Sandbox.close`, awaited), so it
succeeds. Fails
with `SandboxSessionError` if it isn't ready within
``ready_timeout`` (seconds, or a ``timedelta``).

Its disk is ``volume``: by default a new, empty one, which
`Sandbox.commit` and `Sandbox.fork` copy. A
`SandboxVolume` (from a commit, in this task or another) starts
it on a copy of that disk, leaving the volume as it is.
``ScratchVolume()`` keeps the disk on the node: it can't be committed.

``snapshot`` (a `SandboxSnapshot`, instead of ``volume``)
continues a session from it, its memory and processes as they were.
If it is a session `Sandbox.suspend` paused through this same
``SandboxEnvironment`` object, still within its ``keep``, that session
is resumed where it is. Otherwise a
new session's VM is restored from the snapshot, as many times as it
is asked: each runs on apart, on a copy of its disk. A restored
session needs the snapshot's cpu and memory, and a node like the one
it was taken on; its processes see the time between as a stall, and
their network connections are gone. ``volume=snapshot`` instead
starts a session on its disk alone.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `volume` | `SessionVolume` | |
| `snapshot` | `Optional[Union[SandboxSnapshot, SnapshotFuture]]` | |
| `ready_timeout` | `Union[int, timedelta]` | |

