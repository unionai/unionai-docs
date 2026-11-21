---
title: SandboxEnvironment
description: "A sandbox definition: secrets, env vars, resources, network and lifetime."
icon: braces
version: 0.24.0
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
    labels: Optional[Dict[str, str]] = None,
    publish_on_exit: Union[bool, str] = False,
    snapshot_interval: Optional[Union[int, timedelta]] = None,
    runtime_class: RuntimeClass = 'microvm',
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
| `labels` | `Optional[Dict[str, str]]` | |
| `publish_on_exit` | `Union[bool, str]` | |
| `snapshot_interval` | `Optional[Union[int, timedelta]]` | |
| `runtime_class` | `RuntimeClass` | |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) |  |
| [`connect()`](#connect) | Yields the `Sandbox` named ``name``, creating it if there is none: the same sandbox every time, from this process or any other, for as long as it lasts. |
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

### connect()

```python
def connect(
    name: str,
    create: bool = True,
    volume: SessionVolume = None,
    ready_timeout: Union[int, timedelta] = 120,
    on_exit: OnExit = 'detach',
    keep: Union[int, timedelta] = datetime.timedelta(seconds=600),
    on_phase: Optional[Callable[[_session.ConnectPhase], None]] = None,
) -> AsyncIterator[Sandbox]
```
Yields the `Sandbox` named ``name``, creating it if there is
none: the same sandbox every time, from this process or any other, for
as long as it lasts. An agent that disconnects (it restarted, its
laptop slept, it chose to stop for now) connects again by the same
name and carries on where it was, its files, and its processes if the
sandbox was suspended or kept running.

``name`` is used exactly as given (1 to 30 letters, digits, '.', '_'
and '-'), in the project and domain flyte was initialised with. The
sandbox is found in whichever state it is in:

- none of that name: it is created from this environment (and
  ``volume``, a `SandboxVolume` to start its disk from);
  ``sb.connected == "created"``;
- starting: it is waited for;
- running: it is connected to as it is (``"attached"``);
- suspended (``on_exit="suspend"``, or `Sandbox.suspend`): it
  is resumed where it was paused, its processes as they were
  (``"resumed"``);
- suspended for longer than its ``keep``, or past its
  ``max_duration``: its run has ended. A platform with sandbox resume
  starts it again as its next run (``sb.generation`` one more) from
  the disk its last run published, and its memory too where that run
  ended suspended (``"restored"``); one without raises
  `SandboxSessionError` saying so.

A sandbox that exists already is used as it is: this environment's
resources, network and the rest are only for creating one, and an
existing sandbox with others keeps its own.

A sandbox connected to is always kept resumable: its disk is
published when its run ends, as the artifact named ``name``
(whatever the environment's ``publish_on_exit`` says), which
is what a later run starts from. So its disk can't be a
`ScratchVolume`.

``create=False`` only finds it: a sandbox started elsewhere (by
another replica of an app, by this app before it restarted, or by
`session` outside a task, by its `Sandbox.name`). It never
creates one and never starts one whose run has ended again: it fails
with `SandboxSessionError` if there is none of that name, or
it has ended. ``volume`` is then not taken.

Leaving the block does ``on_exit`` to it: ``"detach"`` (the default)
leaves it running, for the next connect; ``"suspend"`` pauses it for
``keep`` (seconds or a ``timedelta``, at most an hour; 0 ends it once
its snapshot is committed), for a connect within that to resume in
milliseconds; ``"close"`` ends it, its disk
published. A sandbox the block closed, suspended or cancelled itself
is left as it is. A suspend that fails leaves it running rather than
losing it. ``max_duration`` bounds each run however often it is
connected to.

Waits up to ``ready_timeout`` (seconds, or a ``timedelta``) for all of
it; fails with `SandboxSessionError` past it. Only a sandbox
this call created is ever deleted on a failure: one that existed is
never stopped here.

``on_phase``, if given, is called with a `ConnectPhase` each
time what the connect is doing changes (finding the sandbox, waiting
for a node to start it, starting it again, connecting), and when it
deletes a sandbox it created and gave up on: for a caller that shows
progress, since the wait for a node can be long. It is called on the
connect's own loop, and should return at once.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `create` | `bool` | |
| `volume` | `SessionVolume` | |
| `ready_timeout` | `Union[int, timedelta]` | |
| `on_exit` | `OnExit` | |
| `keep` | `Union[int, timedelta]` | |
| `on_phase` | `Optional[Callable[[_session.ConnectPhase], None]]` | |

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
then unique in the project and domain, and `connect` (``create=False``) reaches it
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

