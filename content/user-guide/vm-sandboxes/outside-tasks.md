---
title: Use sandboxes outside a task
description: Open VM sandboxes from a laptop, a script, or an app, reconnect to them by name, and manage them with the remote API.
weight: 9
variants: -flyte +union
---

# Use sandboxes outside a task

Your RL driver runs on a workstation next to your trainer. Your product's backend is a FastAPI app that runs user code on demand. Neither is a Flyte task, and both need sandboxes. `env.session()` works the same way from a script, a laptop, or an app: the code you write in a task runs unchanged.

```python
import asyncio

import flyte
from flyteplugins.union import sandbox

code_runner = sandbox.SandboxEnvironment(name="code-runner", labels={"job": "eval-1115"})


async def main() -> None:
    async with code_runner.session("eval") as sb:
        print((await sb.run("python -c 'print(6 * 7)'")).stdout)


flyte.init_from_config(project="<your-project>", domain="development")
asyncio.run(main())
```

## How a session outside a task differs

| | In a task | Outside a task |
| --- | --- | --- |
| What the session is | A child action of the task's run | A run of its own, created through the platform's sandbox service |
| Project and domain | The task's | The ones you initialize `flyte` with. `flyte.init_in_cluster()` sets them in an app. |
| Name | The name you pass | The name you pass, made unique in the project and domain. Read it from `sb.name`. |
| Labels | The run's | `SandboxEnvironment(labels=...)` |
| Can be reached from another process | No | Yes, by name, with `env.connect(name, create=False)` |

## From a laptop or a script

Initialize `flyte` with a project and a domain before you open a session. Sessions are created there, as runs of their own.

From outside your cluster, every call to a session goes through the Union.ai data proxy, signed in as you, the same sign-in `flyte.init_from_config()` uses. Commands, files, ports, commits, and snapshots all work as they do in a task.

> [!NOTE] Calls from outside the cluster are slower
> Each call from outside the cluster makes a round trip through the data proxy, so commands take noticeably longer than the few milliseconds they take from a task or an app. Union.ai is working to reduce this overhead. For high-volume workloads, such as many parallel RL rollouts, run the driver as a task or an app in your cluster.

For runs with nobody at the keyboard, sign in with an API key. A browser sign-in that expires in the middle of a run waits for you to sign in again.

```bash
flyte create api-key --name sandbox-driver
export FLYTE_API_KEY=<the key it printed>
```

## From an app

An app can open sessions with no task in between. Initialize `flyte` with `flyte.init_in_cluster()` at startup to set the project and domain. Sessions outlive the request that started them, and any replica of the app can reach one by name:

```python
import contextlib

import flyte
from fastapi import FastAPI, HTTPException
from flyte.app.extras import FastAPIAppEnvironment
from pydantic import BaseModel

from flyteplugins.union import sandbox

vm = sandbox.SandboxEnvironment(name="app-vm", max_duration=1800)

# Sessions this replica started, kept open until they are deleted.
_open: dict[str, contextlib.AsyncExitStack] = {}


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await flyte.init_in_cluster.aio()  # sets the project and domain sessions are created in
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/sandboxes")
async def create() -> dict:
    stack = contextlib.AsyncExitStack()
    sb = await stack.enter_async_context(vm.session("chat"))
    _open[sb.name] = stack
    return {"name": sb.name}


class Command(BaseModel):
    command: str


@app.post("/sandboxes/{name}/run")
async def run(name: str, req: Command) -> dict:
    try:
        async with vm.connect(name, create=False) as sb:  # only finds it; it stays open after the block
            r = await sb.run(req.command, check=False)
    except sandbox.SandboxSessionError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    return {"exit_code": r.exit_code, "stdout": r.stdout, "stderr": r.stderr}


@app.delete("/sandboxes/{name}")
async def delete(name: str) -> dict:
    stack = _open.pop(name, None)
    if stack is not None:
        await stack.aclose()  # this replica started it: leaving its block closes it
        return {"closed": name}
    try:
        async with vm.connect(name, create=False) as sb:  # another replica's: close it from here
            await sb.close()
    except sandbox.SandboxSessionError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    return {"closed": name}


app_env = FastAPIAppEnvironment(
    name="sandbox-api",
    app=app,
    image=flyte.Image.from_debian_base().with_pip_packages(
        "flyteplugins-union>=0.23.0", "fastapi", "uvicorn"
    ),
)
```

Deploy it with `flyte deploy`. See [Apps](../apps/_index).

## Reconnect to a session

A session started outside a task can be reached from another process by its `sb.name`. `env.connect(name, create=False)` finds it: a session another replica started, or one this process started before it restarted.

```python
async with vm.connect(name, create=False) as sb:
    await sb.run("ls")
```

It waits up to `ready_timeout` for a session that is still starting, and resumes one that is suspended. It never creates a session: it raises `SandboxSessionError` if there is none of that name or it has ended.

Leaving the block only disconnects. The session keeps running until whoever started it closes it, or it reaches `max_duration`. Call `sb.close()` or `sb.cancel()` inside the block to end it.

To reach a sandbox by a name you choose, create it if it is missing, and start it again after it has ended, use `env.connect(name)` without `create=False`. See [Keep a sandbox and come back to it](./reconnect).

A session that a task started belongs to that task. You cannot connect to it from outside the cluster.

## Manage sessions with the remote API

`flyteplugins.union.remote.Sandbox` exposes the platform's sandbox service, like the other objects in `flyteplugins.union.remote`. Use it to look up or clean up sessions without connecting to them:

```python
from flyteplugins.union.remote import Sandbox

s = await Sandbox.current.aio("chat-1a2b3c4d")
print(s.state, s.phase, s.address, s.error)  # state is pending, ready, or ended
await Sandbox.delete.aio("chat-1a2b3c4d")
```

| Call | What it does |
| --- | --- |
| `Sandbox.current(name)` | The sandbox as it is now: its state and, while it is ready, its address. |
| `Sandbox.watch(name)` | The same, again each time the sandbox changes, until it ends. |
| `Sandbox.get(name)` | The platform's record of the sandbox: its run, that run's phase, and its error. It does not say whether the sandbox is ready, and has no address. |
| `Sandbox.listall()` | The sandboxes in a project and domain, as `get` has them. |
| `Sandbox.runs(name)` | The runs a sandbox has had, oldest first, one for each time it was started again. |
| `Sandbox.delete(name)` | Ends the sandbox by aborting its run. |

Each has an `.aio` form.

## Find a job's sessions

Outside a task, every session is a run of its own. Put one label on all the sessions of a job and list them together:

```bash
flyte get run --with-label job=eval-1115
```

## Choose how sessions are reached

By default, a caller running in a Kubernetes cluster calls a session's address directly, and any other caller goes through the data proxy. Set `UNION_SANDBOX_ROUTE=proxy` or `UNION_SANDBOX_ROUTE=direct` to force one or the other.
