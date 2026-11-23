---
title: flyteplugins.union.sandbox
description: "Sandboxes for agents and other tasks that run untrusted code."
icon: box-seam
version: 0.26.0
variants: -flyte +union
layout: py_api
---

# flyteplugins.union.sandbox

Sandboxes for agents and other tasks that run untrusted code.

.. warning::

   **Alpha.** This API can change, or be removed, in any release.

   Sandboxes need microVM nodes, which are off by default. Ask your Union.ai
   solutions team to turn them on for your dataplane.

What a sandbox is
-----------------

A sandbox is a small, isolated computer: a Firecracker microVM (or a gVisor
sandbox, with ``runtime_class="gvisor"``). Your code runs commands in it and
reads and writes its files. Whatever runs inside can't reach your task, your
cluster or your secrets, only what you give it.

A new sandbox is ready in well under a second. One started from another's
disk or from a snapshot takes about two seconds.

There are two ways to get one:

- ``env.session(name)`` is **ephemeral**: a new sandbox for one ``async
  with`` block, closed when the block ends. ``name`` says what it is for.
- ``env.connect(name)`` is **durable**: the sandbox with exactly that name,
  created if there is none. It is the same sandbox every time, from any
  process, and it outlives the block (see "Reconnecting by name").

Everything you need is in this module:

```python
from flyteplugins.union import sandbox
```

Quick start
-----------

Describe the sandbox once with `SandboxEnvironment`, then open one
with ``env.session(name)`` inside ``async with``. It closes when the block
ends:

```python
import flyte
from flyteplugins.union import sandbox

code_runner = sandbox.SandboxEnvironment(
    name="code-runner",
    secrets=[flyte.Secret(key="openai", as_env_var="OPENAI_API_KEY")],
    network=sandbox.Network.internet(),
)
agent_env = flyte.TaskEnvironment(name="agent")

@agent_env.task
async def agent() -> str:
    async with code_runner.session("hello") as sb:
        await sb.fs.write_text("main.py", "print(6 * 7)")  # relative paths are under /work
        r = await sb.run("python main.py")  # raises SandboxCommandFailed on a nonzero exit
        return r.stdout  # "42
```
"

What do you want to do?
-----------------------

==============================================  ===============================================
You want to                                     Call
==============================================  ===============================================
Get a sandbox for one block of code             ``async with env.session(name) as sb``
Get the same sandbox again later, by name       ``async with env.connect(name) as sb``
Run a command and wait for it                   ``await sb.run("pytest -q")``
Stream a long command's output                  ``p = await sb.start(cmd)``; ``async for line in p.stdout``
Read or write files                             ``sb.fs.read_text``, ``sb.fs.write_text``, ``sb.fs.upload``
Save the disk                                   ``disk = await sb.commit()``
Start a new sandbox from a saved disk           ``env.session(name, volume=disk)``
Save disk, memory and running processes         ``snap = await sb.snapshot()``
Pause now and carry on later                    ``snap = await sb.suspend()``
Carry on from a pause or a snapshot             ``env.session(name, snapshot=snap)``
Try something on a copy                         ``async with sb.fork("try-1") as child``
Mount data or a checkpoint folder               ``env.session(name, volumes={"/data": vol})``
==============================================  ===============================================

Running commands
----------------

- ``sb.run(command)`` runs a command to the end and returns a
  `CommandResult` (``exit_code``, ``stdout``, ``stderr``).

  - A string runs in a shell; a list runs the program directly.
  - A nonzero exit raises `SandboxCommandFailed`. Pass
    ``check=False`` to get the result instead.
  - Cancelling the call kills the command.
  - ``sb.run(command, input=...)`` feeds it input.

- ``sb.start(command)`` starts a command and returns a `Process` right
  away. Read ``async for line in p.stdout``, then ``await p.wait()`` for the
  result. The command keeps running if the connection breaks, or across a
  snapshot or a suspend.

  - ``sb.start(command, stdin=True)`` gives it input:
    ``async with p.stdin as stdin: await stdin.write(...)``. Leaving the
    block ends its input.
  - ``sb.start("bash", tty=sandbox.Tty(30, 120))`` runs it on a terminal.
    Read output as it comes (``async for chunk in p.stdout.chunks()``),
    type into it (``p.stdin.write(b"")`` is Ctrl-C), and call
    ``p.resize(rows, cols)`` when the window changes.
  - ``p.signal(signal.SIGTERM)`` sends a signal.

Times (``max_duration``, ``ready_timeout``, a command's ``timeout``) are
seconds, or a ``timedelta``.

Files
-----

``sb.fs`` reads, writes, lists and removes files, and copies local files and
folders in and out (up to 512 MiB a file). Relative paths are under
``/work``. Writing a file creates its missing parent folders.

Names
-----

Every sandbox is named for what it does: ``env.session("build")``,
``sb.fork("try-fix-1")``. The name is also its action's name, so a run's
sandboxes read in order as what happened.

Closing
-------

Leaving the ``async with`` block closes the sandbox (``sb.close()``). Its
commands get SIGTERM, then SIGKILL after ``grace`` (at most 60 s).

- The block waits for the sandbox to close, not for its action to finish;
  ``sb.close(wait=True)`` waits for both.
- ``sb.cancel()`` stops it at once.
- ``sb.startup`` says how long starting took; ``sb.endpoint`` and
  ``sb.address`` say where it runs.

Saving and restoring
--------------------

Three ways to keep what a sandbox has, from least to most:

1. **Its disk:** ``disk = await sb.commit()`` returns a
   `SandboxVolume`. ``env.session(name, volume=disk)`` starts a new
   sandbox on a copy of it, on any node. ``sb.close(commit=True)`` closes and
   commits in one step.
2. **Its disk, memory and processes:** ``snap = await sb.snapshot()`` returns
   a `SandboxSnapshot`. ``env.session(name, snapshot=snap)`` starts a
   new sandbox exactly as it was.
3. **A pause:** ``snap = await sb.suspend()`` pauses the sandbox where it is
   and returns its snapshot. ``env.session(name, snapshot=snap)`` resumes it,
   processes and all, within ``keep``. After ``keep`` it starts a new sandbox
   from the snapshot instead. Processes see the pause as a stall: their
   clock jumps and network connections are gone.

Faster versions:

- ``sb.suspend(wait=False)`` returns as soon as the VM is paused, with a
  `SnapshotFuture`. ``env.session(name, snapshot=fut)`` resumes it in
  place without waiting for the save to finish. This is the fast way to pause
  and carry on.
- ``sb.snapshot(wait=False)`` returns as soon as the VM runs again. ``await
  fut.wait()`` gives the snapshot once it is saved.

Copies:

- ``sb.fork(name)`` commits the disk and starts a new sandbox on it.
- ``sb.fork(name, memory=True)`` copies memory and processes too.

Saving every disk automatically:
``SandboxEnvironment(publish_on_exit=True)`` commits each sandbox's disk when
it ends and publishes it as an artifact with the sandbox's name
(``publish_on_exit="other-name"`` picks the name). ``await
SandboxVolume.from_artifact(name)`` gets it back, in any run. A sandbox that
is cancelled or fails publishes nothing.

Mounting volumes
----------------

A sandbox can mount block volumes next to its disk, each at its own path.
Name them when it starts, with ``volumes=`` (with an "s"; ``volume=`` is the
sandbox's own disk):

```python
async with env.session("train", volumes={
    "/data": dataset,                         # an ROBlockVolume: read-only
    "/ckpt": sandbox.Mount(ckpt, mode="rw"),  # read-write
}) as sb:
    await sb.run("python train.py --data /data --out /ckpt")
    new_ckpt = await sb.volumes["/ckpt"].commit()  # a new ROBlockVolume
```

The rules:

- Each mount is a private copy. The volume you passed never changes.
- Read-only is the default.
- At most six, each a committed block volume (from ``BlockVolume.commit()``,
  or returned by a task). They work on microVM and gVisor sandboxes alike.
- From a terminal: ``flyte connect sandbox NAME --with-volume PATH=VOLUME``
  mounts one read-only.

Two things to know:

- **Only a commit keeps what is written to a volume.**
  ``sb.volumes[path].commit()`` saves the copy as a new version, and the
  sandbox keeps running. When a sandbox closes, is cancelled or fails, what it
  wrote since the last commit is dropped. Nothing is committed for you.

  - ``sb.commit()`` saves the sandbox's own disk only, never its volumes.
  - A sandbox started from a disk (``volume=``) mounts only the ``volumes=``
    you name for it.
  - A snapshot, a suspend, a fork and a connected sandbox's next run do
    carry the volumes: they save the disk and every volume at the same
    instant and mount them again where the sandbox continues.
    ``sb.fork(name, volumes=...)`` mounts other volumes instead.
  - When you continue from a snapshot (``env.session(name, snapshot=...)``),
    ``volumes=`` may only list paths the sandbox already mounts, each in the
    same mode. Anything else raises `SandboxUsageError`.
  - ``sb.volumes`` lists what a sandbox mounts.

- **A volume written by untrusted code can attack whoever mounts it.** A
  volume committed read-write from a sandbox holds an ext4 filesystem the
  sandbox's code wrote. The next kernel that mounts it reads that
  filesystem, and it may be crafted to attack that kernel. For code you don't
  trust, mount volumes read-only (or not at all), and don't mount what it
  committed anywhere you trust.

Reconnecting by name
--------------------

``env.connect(name)`` reaches a sandbox by a name you pick, and creates it if
there is none. It is the same sandbox every time, from this process or any
other. An agent that stops (it restarted, it moved, it chose to pause)
connects again with the same name and carries on:

```python
async with env.connect("agent-7", on_exit="suspend", keep=timedelta(minutes=30)) as sb:
    print(sb.connected, sb.generation)  # "created", 0 the first time
    await sb.run("git clone ... /work/repo")

# Later, anywhere:
async with env.connect("agent-7") as sb:  # "resumed": its processes as they were
    await sb.run("cd /work/repo && make test")
```

What it finds, it uses:

- a sandbox that is starting is waited for;
- one that is running is joined (``sb.connected == "attached"``);
- one that is suspended is resumed (``"resumed"``).

A sandbox that already exists keeps its own settings: the environment only
says how to create one. Leaving the block does ``on_exit``:

- ``"detach"`` (the default) leaves it running;
- ``"suspend"`` pauses it for ``keep`` (at most an hour);
- ``"close"`` ends it.

Each run still ends at ``max_duration``.

``env.connect(name, create=False)`` only finds a sandbox. It raises
`SandboxNotFound` if there is none with that name, and
`SandboxSessionError` if it has ended.

A connected sandbox always publishes its disk when its run ends, as an
artifact named after it, so it can't use a ``ScratchVolume``. A later run
starts from that disk. When the platform supports sandbox resume, connecting
to a sandbox whose run ended (suspended past ``keep``, closed, or past
``max_duration``) starts its next run (``sb.generation`` goes up by one) from
its disk, and from its memory too if it ended suspended (``"restored"``).
Until then that connect raises `SandboxSessionError`; connect to a new
name instead.

A failed connect deletes only a sandbox it created itself, never one that
already existed.

From a terminal: ``flyte connect sandbox NAME`` opens a shell in it,
``flyte suspend sandbox NAME`` pauses it, ``flyte get sandbox [NAME]`` lists
sandboxes and their runs, and ``flyte delete sandbox NAME`` ends it.

Outside a task
--------------

``env.session(name)`` and ``env.connect(name)`` also work in an app or a
script. There is no task for the sandbox to belong to, so it is a sandbox of
its own, started through the platform's ``SandboxService``. Initialise flyte
with a project and a domain first (``flyte.init_in_cluster`` in an app).

- ``sb.address`` is where it runs, as soon as its worker reports it.
- To look a sandbox up without connecting, use
  ``flyteplugins.union.remote.Sandbox``: ``Sandbox.current(name)`` is how it
  is now (state and address), ``Sandbox.watch(name)`` follows it, and
  ``Sandbox.get(name)`` reads its record (its run's phase, but not its
  address).
- Another process reaches it by its ``sb.name``, which is unique in the
  project and domain:

  ```python
  async with env.connect(name, create=False) as sb:  # another replica, or after a restart
      await sb.run("ls")
  ```

  Leaving that block leaves the sandbox running, for whoever started it to
  close.

From a laptop, or anywhere outside the cluster, the sandbox is reached
through the platform's data proxy, as you (the sign-in
``flyte.init_from_config`` uses). Commands, files, ports, commits and
snapshots all work as in a task. A process inside a Kubernetes cluster calls
the sandbox directly. Set ``UNION_SANDBOX_ROUTE=proxy`` or ``=direct`` to
force either. Using a sandbox takes permission to create executions in its
project, as starting one does. ``sb.port_url(port)`` is a port's URL through
the data proxy, which also takes your Union sign-in.

This needs: microVM nodes on your dataplane (see the warning above), an
actions service that supports ``ActionAddress``, and a flyte release with
``flyte.extend.new_session`` (inside a task) or whose ``flyteidl2`` has
``ActionAddress`` (outside one). Reaching a sandbox from outside the cluster
needs a control plane whose data proxy routes to a sandbox's API.

Errors
------

All errors are in this module (and in ``flyteplugins.union.errors``):

- `SandboxUsageError`: the call can't work as written (a bad
  argument, a closed sandbox, the wrong ``volumes=``). Fix the code.
- `SandboxSessionError`: the sandbox couldn't be started or reached.
  `SandboxNotFound` (no sandbox with that name) and
  `SandboxSessionEnded` (it ended: its VM was lost, it ran past
  ``max_duration``, or it was aborted) are kinds of it.
- `SandboxCommandFailed`: a command exited nonzero (``sb.run`` with
  ``check=True``, the default). `SandboxCommandTimedOut`: it ran past
  its ``timeout``.

Not supported yet
-----------------

Each of these raises a ``ValueError`` that points here, rather than being
silently ignored:

- **Custom images** (``image=``). A sandbox runs the platform's Python image.
  Install what you need at runtime, e.g. ``await sb.run("pip install
  pandas")``, with a network that reaches PyPI (``Network.pypi()``).
- **GPU, disk and shm resources.** A sandbox is sized by ``cpu`` and
  ``memory`` only (default 1 vCPU, 1 GiB).
- **Pod settings** (``pod_template``, ``service_account``, ``interruptible``,
  ``include``). A sandbox is a microVM, not a pod.

Not offered at all yet:

- **Deleting volumes by age.** ``SandboxVolume.expires_at`` is reserved;
  nothing sets or enforces it.
- **An idle timeout.** A sandbox lives until its block ends, or for
  ``max_duration``.
- **Moving** ``flyte.io.File`` **/** ``Dir`` **through the platform.** Copy
  with ``sb.fs`` (``upload``, ``download``, ``upload_dir``,
  ``download_dir``), which goes through the calling task.
- **Reaching a task's sandbox from outside the cluster.** A sandbox a task
  started is that task's to use. A script outside the cluster reaches only
  the sandboxes it starts, or connects to, itself.

Advanced
--------

- ``SandboxEnvironment(snapshot_interval=...)`` writes a running sandbox's
  disk to storage that often, without committing, so the commit at the end
  has less to write. Nothing can be started from these writes.
- Secrets work only on a worker started with ``--secrets-dir``. On one
  without it, a sandbox that declares a secret fails with ``SecretNotFound``.
## Directory

### Classes

| Class | Description |
|-|-|
| [`CommandResult`](../flyteplugins.union.sandbox/commandresult) | A finished command: what `Sandbox.run` returns. |
| [`ConnectPhase`](../flyteplugins.union.sandbox/connectphase) | What ``env.connect`` is doing now, for a caller that shows its progress (``on_phase=``). |
| [`FileEntry`](../flyteplugins.union.sandbox/fileentry) | One entry from `FileSystem.ls` or `FileSystem.stat`. |
| [`FileSystem`](../flyteplugins.union.sandbox/filesystem) | File access inside a sandbox (``sb.fs``). |
| [`Mount`](../flyteplugins.union.sandbox/mount) | A block volume a session mounts: ``volumes={"/data": Mount(v, mode="rw")}``. |
| [`MountedVolume`](../flyteplugins.union.sandbox/mountedvolume) | A block volume a session mounts (``sb.volumes["/ckpt"]``): a private copy of `volume`, at `path`, read-only or read-write. |
| [`Network`](../flyteplugins.union.sandbox/network) | Outbound network for a sandbox. |
| [`Process`](../flyteplugins.union.sandbox/process) | A running command, from `Sandbox.start`. |
| [`Sandbox`](../flyteplugins.union.sandbox/sandbox) | A running sandbox session, from ``async with env.session("build") as sb``. |
| [`SandboxEnvironment`](../flyteplugins.union.sandbox/sandboxenvironment) | A sandbox definition: secrets, env vars, resources, network and lifetime. |
| [`SandboxSnapshot`](../flyteplugins.union.sandbox/sandboxsnapshot) | A sandbox session's disk, memory and processes at one instant (``sb.snapshot()``, ``sb.suspend()``). |
| [`SandboxVolume`](../flyteplugins.union.sandbox/sandboxvolume) | A sandbox session's disk at a commit (``sb.commit()``, ``sb.close(commit=True)``). |
| [`ScratchVolume`](../flyteplugins.union.sandbox/scratchvolume) | A session's disk that stays on the node and ends with the session: ``env.session(name, volume=ScratchVolume())``. |
| [`SessionStartup`](../flyteplugins.union.sandbox/sessionstartup) | How long each step of starting a session took, in seconds (``sb.startup``). |
| [`SnapshotFuture`](../flyteplugins.union.sandbox/snapshotfuture) | A snapshot taken, from ``await sb.snapshot(wait=False)``: what it holds is fixed and its session runs on. |
| [`Tty`](../flyteplugins.union.sandbox/tty) | A terminal for a command to run on (``sb.start(command, tty=Tty(30, 120))``). |

### Errors

| Exception | Description |
|-|-|
| [`ProcessError`](../flyteplugins.union.sandbox/processerror) | A command ended abnormally: the session failed or its stream broke. |
| [`ProcessUnsupported`](../flyteplugins.union.sandbox/processunsupported) | The sandbox cannot give a command what was asked for it: its node runs a version from before commands had a stdin or a terminal. |
| [`SandboxCommandFailed`](../flyteplugins.union.sandbox/sandboxcommandfailed) | A command run with ``sb.run(...)`` exited with a nonzero code (``check`` is on by default). |
| [`SandboxCommandTimedOut`](../flyteplugins.union.sandbox/sandboxcommandtimedout) | A command ran past its ``timeout`` and was stopped. |
| [`SandboxNotFound`](../flyteplugins.union.sandbox/sandboxnotfound) | There is no sandbox of that name, and the call (``create=False``) makes none. |
| [`SandboxSessionEnded`](../flyteplugins.union.sandbox/sandboxsessionended) | A call into a sandbox failed because its session has ended: its microVM was lost (e.g. its node restarted), it ran past its maximum duration, or it was aborted. |
| [`SandboxSessionError`](../flyteplugins.union.sandbox/sandboxsessionerror) | A sandbox session could not be started, or ended before it was ready. |
| [`SandboxUsageError`](../flyteplugins.union.sandbox/sandboxusageerror) | A sandbox session was used in a way that can't work: started outside a task, with a flyte that has no sessions, or used after its ``async with`` block ended. |

