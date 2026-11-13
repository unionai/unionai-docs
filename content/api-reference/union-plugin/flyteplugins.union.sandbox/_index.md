---
title: flyteplugins.union.sandbox
description: "Interactive sandbox sessions for agents and other tasks that run untrusted code."
icon: box-seam
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# flyteplugins.union.sandbox

Interactive sandbox sessions for agents and other tasks that run untrusted code.

.. warning::

   **Alpha.** This module is not yet stable: its API can change, or be
   removed, in any release.

   It does not work on your dataplane as it is: sessions need microVM
   nodes, which are not enabled by default. Talk to your Union.ai
   solutions team to enable them.

Declare a sandbox once as a `SandboxEnvironment` (secrets, env vars,
cpu and memory, network, lifetime). A task then starts sessions from it: each
is a Firecracker microVM, a child action on a microVM worker with no pod,
torn down when the block exits. A new session is usable in well under a
second; one forked from another's disk, or restored from a snapshot, in about
two (measured on dogfood-gcp):

```python
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
        r = await sb.run("python main.py")  # raises SandboxCommandFailed if it exits nonzero
        return r.stdout
```

The whole surface:

- ``sb.run(command)`` runs a command to the end and returns a
  `CommandResult` (``exit_code``, ``stdout``, ``stderr``); a string is a
  shell command line, a list runs without a shell. A nonzero exit raises
  `SandboxCommandFailed` unless ``check=False``. The command lives as
  long as the call: cancelling it kills it.
- ``sb.start(command)`` starts one to stream its output:
  ``async for line in p.stdout``, then ``await p.wait()`` for its result. The
  sandbox keeps it running across a broken connection, a snapshot or a
  suspend.
- A started command can be given input and a terminal.
  ``sb.start(command, stdin=True)`` gives it a stdin, ``p.stdin``:
  ``async with p.stdin as stdin: await stdin.write(...)`` writes to it and
  ends its input when the block is left. ``sb.start("bash", tty=sandbox.Tty(30, 120))``
  runs it on a terminal, as in a terminal window: what it prints is read as
  it comes (``async for chunk in p.stdout.chunks()``), what is written is what
  would be typed (``p.stdin.write(b"\x03")`` is Ctrl-C), and
  ``p.resize(rows, cols)`` follows the window. ``p.signal(signal.SIGTERM)``
  signals either.
  ``sb.run(command, input=...)`` runs one to the end on that input.
- ``sb.fs`` reads, writes, lists and removes files, and copies local files
  and directories in and out (at most 512 MiB a file). Writes create missing
  parent directories.
- Leaving the block closes the session (``sb.close()``): its commands get
  SIGTERM, then SIGKILL after ``grace`` (at most 60 s). The block's exit
  waits for the sandbox to close, not for the session's end;
  ``sb.close(wait=True)`` waits for that too. ``sb.cancel()`` aborts it.
- Every session is named for what it is for: ``env.session("build")``,
  ``sb.fork("try-fix-1")``. The name is its action's, so a run's sessions
  read in order as what happened.
- ``sb.startup`` says how long starting it took; ``sb.endpoint`` and
  ``sb.address`` say where it is served.
- ``sb.commit()`` returns its disk as a `SandboxVolume`, which
  ``env.session(name, volume=v)`` starts a session on a copy of, on any
  node; ``sb.fork(name)`` does both.
- ``SandboxEnvironment(publish=True)`` has each session's disk committed
  when the session ends and published as an artifact named as the session
  (``publish="name"`` names it): ``await SandboxVolume.from_artifact(name)``
  is that disk, to start another session on, in any run. A cancelled or
  failed session publishes nothing. ``snapshot_every=`` writes a running
  session's disk out to storage that often, committing nothing, so its
  commit at the end has less to write.
- ``sb.snapshot()`` returns its disk, memory and processes at one instant
  as a `SandboxSnapshot`, which ``env.session(name, snapshot=s)``
  restores a new session from. ``sb.snapshot(wait=False)`` returns as soon
  as the VM runs on again (its disk writes wait until the commit), with a
  `SnapshotFuture`: ``await fut.wait()`` for the snapshot.
- ``sb.suspend()`` pauses it where it is and returns its snapshot;
  ``env.session(snapshot=s)`` resumes it, processes and all, within its
  ``keep``, and otherwise restores a new session from it (as
  ``sb.fork(memory=True)`` does). Its processes see the pause as a stall:
  their clock jumps, and network connections are gone.

Durations (``max_duration``, ``ready_timeout``, a command's ``timeout``) are
seconds or a ``timedelta``.

Outside a task
--------------

``env.session(name)`` also works in an app or a script, where there is no
task for the session to be a child of. The session is then a sandbox of its
own, started through the platform's ``SandboxService``, and flyte must be
initialised with a project and a domain (``flyte.init_in_cluster`` in an
app). Its address arrives as soon as its worker reports it, with no task or
pod started for it.

Such a session can be reached from another process by its ``sb.name``, which
is unique in the project and domain:

```python
async with vm.attach(name) as sb:   # another replica, or after a restart
    await sb.run("ls")
```

``attach`` only connects: leaving its block leaves the session running, for
whoever started it to close.

From a laptop, or anywhere else outside the cluster, the session is reached
through the platform's data proxy, as your own Union sign-in (what
``flyte.init_from_config`` uses): commands, files, ports, commits and
snapshots all work as they do in a task, and nothing on the way holds the
session's token but the platform. A process in a Kubernetes cluster calls the
session's address directly; ``UNION_SANDBOX_ROUTE=proxy`` or ``=direct``
forces either. Calling it takes permission to create executions in the
project, as starting it does. ``sb.port_url(port)`` is then the data proxy's
URL of that port, which takes your Union credentials too.

It needs a dataplane with microVM nodes enabled by your Union.ai solutions
team (see the warning above), an actions service that supports
``ActionAddress``, and a flyte release with ``flyte.extend.new_session``
(inside a task) or whose ``flyteidl2`` has ``ActionAddress`` (outside one).
Reaching a session from outside the cluster needs a control plane whose data
proxy routes to a session's API.

Not supported yet
-----------------

Each of these raises a ``ValueError`` that points here, rather than being
silently ignored:

- **Custom images** (``image=``). A session runs the platform's Python base.
  Install what it needs at runtime, e.g. ``await sb.run("pip install
  pandas")``, with a network that reaches PyPI (``Network.pypi()``).
- **GPU, disk and shm resources.** A session's VM is sized by ``cpu`` and
  ``memory`` alone (default 1 vCPU, 1 GiB).
- **Pod settings** (``pod_template``, ``service_account``, ``interruptible``,
  ``include``). A session is a microVM, not a pod.

Not offered at all yet:

- **An idle timeout.** A session lives until its block exits, or for
  ``max_duration`` seconds.
- **Moving** ``flyte.io.File`` **/** ``Dir`` **in and out through the
  platform.** Copy through ``sb.fs`` (``upload``, ``download``,
  ``upload_dir``, ``download_dir``), which goes through the calling task.
- **Reaching a session in a task from outside the cluster.** A session a
  task started is the task's to use; a script outside the cluster reaches
  the sessions it starts, or attaches to, itself.

Secrets are supported, but only on a worker started with ``--secrets-dir``;
on one without it, a session that declares a secret fails with
``SecretNotFound``.
## Directory

### Classes

| Class | Description |
|-|-|
| [`CommandResult`](../flyteplugins.union.sandbox/commandresult) | A finished command: what `Sandbox.run` returns. |
| [`FileEntry`](../flyteplugins.union.sandbox/fileentry) | One entry from `FileSystem.ls` or `FileSystem.stat`. |
| [`FileSystem`](../flyteplugins.union.sandbox/filesystem) | File access inside a sandbox (``sb.fs``). |
| [`Network`](../flyteplugins.union.sandbox/network) | Outbound network for a sandbox. |
| [`Process`](../flyteplugins.union.sandbox/process) | A running command, from `Sandbox.start`. |
| [`Sandbox`](../flyteplugins.union.sandbox/sandbox) | A running sandbox session, from ``async with env.session("build") as sb``. |
| [`SandboxEnvironment`](../flyteplugins.union.sandbox/sandboxenvironment) | A sandbox definition: secrets, env vars, resources, network and lifetime. |
| [`SandboxSnapshot`](../flyteplugins.union.sandbox/sandboxsnapshot) | A sandbox session's disk, memory and processes at one instant (``sb.snapshot()``, ``sb.suspend()``). |
| [`SandboxVolume`](../flyteplugins.union.sandbox/sandboxvolume) | A sandbox session's disk at a commit (``sb.commit()``, ``sb.fork_close()``). |
| [`ScratchVolume`](../flyteplugins.union.sandbox/scratchvolume) | A session's disk that stays on the node and ends with the session: ``env.session(volume=ScratchVolume())``. |
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
| [`SandboxSessionEnded`](../flyteplugins.union.sandbox/sandboxsessionended) | A call into a sandbox failed because its session has ended: its microVM was lost (e.g. its node restarted), it ran past its maximum duration, or it was aborted. |
| [`SandboxSessionError`](../flyteplugins.union.sandbox/sandboxsessionerror) | A sandbox session could not be started, or ended before it was ready. |
| [`SandboxUsageError`](../flyteplugins.union.sandbox/sandboxusageerror) | A sandbox session was used in a way that can't work: started outside a task, with a flyte that has no sessions, or used after its ``async with`` block ended. |

