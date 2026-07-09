---
title: Debug a run
weight: 15
variants: -flyte +union
---

# Debug a run

When an action behaves unexpectedly, {{< key product_name >}} lets you drop into a live debugging
session for that action — inspecting its environment, filesystem, and code from the inside instead
of guessing from logs alone.

There are three ways to debug:

- **From the UI** — open a debugging session for any action with a single click.
- **From the SDK or CLI** — launch a run in debug mode (`debug=True` / `--debug`) to start a
  browser-based VS Code session on the task pod and step through your code line-by-line.
- **SSH into the task** (Beta) — attach your local terminal or VS Code directly to a running task
  pod, using the `flyteplugins-union` plugin.

## Debug from the UI

Open the run in the UI and select the action you want to debug from the action list. In the action
details view, click **Debug action** (the button in the top-right of the summary panel).

This opens an interactive debugging session for that action, where you can explore the action's
state directly. Debugging is scoped to the individual action, so you can debug a single nested
action without affecting the rest of the run.

## Debug from the SDK or CLI

Launching a run in **debug mode** starts a browser-based VS Code session (a `code-server`) inside
the task pod. You connect to it from the UI and step through your task code line-by-line on the
same infrastructure the run uses — against the same data, images, and dependencies. This is
especially valuable when a task behaves differently remotely than it does locally, where the inputs,
models, or environment often differ and reproducing the problem on your laptop is impractical.

Unlike **[Debug from the UI](#debug-from-the-ui)**, which you open on an action after it has
started, debug mode is requested at **launch time** — from your own code or from the CLI.

### From the SDK

Pass `debug=True` to `flyte.with_runcontext()`, then call `.run(...)` as usual. After the run
starts, `run.get_debug_url()` returns the URL of the VS Code session:

```python
import flyte

env = flyte.TaskEnvironment(name="debug_example")


@env.task
def say_hello(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting


if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.with_runcontext(debug=True).run(say_hello, name="World")
    print("Run URL:", run.url)
    print("Debug URL:", run.get_debug_url())
```

`run.get_debug_url()` waits for the VS Code Debugger entry to appear in the run's action details,
then returns its URL. It returns `None` if the entry never appears — check the task logs if so. The
same URL is also available in the UI on the action's details view.

### From the CLI

Pass `--debug` to `flyte run`:

```bash
flyte run --debug debug.py say_hello --name World
```

The run starts with a `code-server` attached. Once the session is ready, the CLI prints a **Debug**
panel containing the VS Code Debugger URL — open it to connect to the interactive session. If the
URL doesn't appear, the panel points you to the task logs.

> [!NOTE]
> The debug session runs on the remote task pod and stays alive while you use it, shutting down
> automatically after a period of inactivity. Because the session runs inside the task container,
> it has the run's real inputs, image, and dependencies available for interactive inspection.

## SSH into the task (Beta)

> [!WARNING] Beta feature
> SSH-into-task debugging is a Beta feature delivered through the `flyteplugins-union` plugin. Its
> commands and APIs may change in future releases.

This mode launches your run with an in-pod SSH server fronted by a small WebSocket bridge, then
gives you a ready-to-paste `~/.ssh/config` block so you can attach your **local** `ssh` client or
**VS Code Remote-SSH** straight into the task pod. The SSH keypair is auto-managed — you never run
`ssh-keygen`.

### Requirements

- `flyte` (SDK) version **2.5.8 or newer**
- `flyteplugins-union` version **greater than 0.5.0**

The in-pod SSH server is pure Python (`asyncssh`, bundled with `flyte`), so **no extra packages are
needed in the task image** — there is no `openssh-server` install and nothing to bake in.

Install the plugin:

```bash
uv pip install flyteplugins-union
```

### Debug from the CLI

`flyte debug <run-name>` does everything in one shot: it relaunches an existing run with ssh-debug
enabled (fetching that run's code and inputs), waits for the pod's ssh route to come up, and prints
a ready-to-paste `~/.ssh/config` block.

The canonical flow is to write the `Host` block straight into `~/.ssh/config`, then `ssh` to it:

```bash
flyte debug <run-name> --write-config
ssh flyte-debug
```

`--write-config` adds a `Host flyte-debug` block to your `~/.ssh/config`, so `ssh flyte-debug` (or
**VS Code → Remote-SSH → `flyte-debug`**) connects straight into the task pod. Only `<run-name>` is
required; the action name defaults to the root action `a0` — pass an action name as a second
argument to source the task and inputs from a nested action instead.

#### Naming a session

Pass `--name` to name the debug session. The name is used as **both** the remote debug run name and
the `~/.ssh/config` Host alias, so you then `ssh <name>`:

```bash
flyte debug <run-name> --name my-dbg --write-config
ssh my-dbg
```

Naming lets you keep several debug sessions side by side. The debug run uses a **deterministic
name** (derived from the source run, or from `--name`), so re-running the same command
**reconnects to the live debug session instead of spawning a duplicate**. To start a fresh debug
run (for example if the previous one died), pass a new `--name`.

For a long-lived tunnel that survives re-logins, add `--api-key`; to relaunch without blocking on
the pod coming up, add `--no-wait`:

```bash
flyte debug <run-name> --name my-dbg --api-key --write-config
```

Useful options:

| Option | Description |
|---|---|
| `--user` | SSH login user inside the pod (default `root`). |
| `--identity-file` | Private key to authenticate with. Defaults to the auto-managed `~/.flyte/ssh-debug/id_ed25519`. |
| `--name` | Name for this debug session — used as **both** the `~/.ssh/config` Host alias and the remote debug run name. Re-running with the same name reconnects; a new name starts a fresh debug run. |
| `--api-key` | Authenticate the tunnel with a dedicated, long-lived API key instead of your interactive session token. |
| `--refresh-token` | Force a fresh token instead of reusing the cached one (use if you hit auth errors). |
| `--write-config` | Write the `Host` block into `~/.ssh/config`, replacing any prior block of the same name. |
| `--wait` / `--no-wait` | Wait for the route to become ready and print the ssh-config (default), or relaunch and return immediately. |
| `--timeout` | Seconds to wait for the debug route to become ready (default `300`). |

> [!NOTE]
> Tokens expire. If you get a `401` on reconnect, just re-run the same `flyte debug` command — it
> reconnects and refreshes the token in place (no `--write-config` needed). For multi-day sessions,
> use `--api-key`.

### Debug programmatically

The `debug()` convenience function mirrors `flyte.run()` / `flyte.rerun()`, with the ssh-debug
environment injected so the new run comes up with an in-pod SSH server. After it returns, resolve the
connection with `SSHDebug.connect()`:

```python
import flyte
from flyteplugins.union import debug
from flyteplugins.union.remote import SSHDebug

flyte.init_from_config()

# Launch a NEW task in debug mode...
run = debug(my_task, x=1)

# ...or relaunch an EXISTING run in debug mode (fetches its code + inputs):
run = debug("some-prior-run")

# Print a ready-to-paste ~/.ssh/config block for the run's root action (a0).
print(SSHDebug.connect(run.name).ssh_config)
```

For the run-name form, pass `inputs={...}` to change parameters or `task_template=...` to substitute
code. For finer control over launch settings, use `with_debugcontext()` — it is
`flyte.with_runcontext()` preconfigured for ssh-into-task debug (it creates the auto-managed keypair
and sets the SSH-debug environment variables), so you call `.run(...)` or `.rerun(...)` on it:

```python
from flyteplugins.union import with_debugcontext

run = with_debugcontext(env_vars={"LOG_LEVEL": "20"}).run(my_task, x=1)
```

## Related

- [Run context](./run-context) — set `debug` and other invocation-time parameters with `flyte.with_runcontext()`.
- [Re-run a run](./rerun-runs) — launch a new run from a previous one.
- [Interact with runs and actions](./interacting-with-runs) — retrieve, monitor, and inspect runs and actions.
