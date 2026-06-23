---
title: Debug a run
weight: 15
variants: -flyte +union
---

# Debug a run

When an action behaves unexpectedly, {{< key product_name >}} lets you drop into a live debugging
session for that action — inspecting its environment, filesystem, and code from the inside instead
of guessing from logs alone.

There are two ways to debug:

- **From the UI** — open a debugging session for any action with a single click.
- **SSH into the task** (Beta) — attach your local terminal or VS Code directly to a running task
  pod, using the `flyteplugins-union` plugin.

## Debug from the UI

Open the run in the UI and select the action you want to debug from the action list. In the action
details view, click **Debug action** (the button in the top-right of the summary panel).

This opens an interactive debugging session for that action, where you can explore the action's
state directly. Debugging is scoped to the individual action, so you can debug a single nested
action without affecting the rest of the run.

## SSH into the task (Beta)

> [!WARNING] Beta feature
> SSH-into-task debugging is a Beta feature delivered through the `flyteplugins-union` plugin. Its
> commands and APIs may change in future releases.

This mode launches your run with an in-pod SSH server fronted by a small WebSocket bridge, then
gives you a ready-to-paste `~/.ssh/config` block so you can attach your **local** `ssh` client or
**VS Code Remote-SSH** straight into the task pod. The SSH keypair is auto-managed — you never run
`ssh-keygen`.

### Requirements

- `flyte` (SDK) version **greater than 2.5.3**
- `flyteplugins-union` version **greater than 0.5.0**
- `openssh-server` available in the task image (bake it in for a fast cold start; otherwise it is
  installed on the pod at startup)

Install the plugin:

```bash
uv pip install flyteplugins-union
```

### Debug from the CLI

`flyte debug <run-name>` does everything in one shot: it relaunches an existing run with ssh-debug
enabled (fetching that run's code and inputs), waits for the pod's ssh route to come up, and prints
a ready-to-paste `~/.ssh/config` block.

```bash
# Relaunch a run in debug mode and connect to its root action (a0)
flyte debug <run-name>

# Name the session, use an API key for auth, and write the Host block into ~/.ssh/config
flyte debug <run-name> --name my-dbg --api-key --write-config

# Fire-and-forget: relaunch and return immediately, without waiting for the pod to come up
flyte debug <run-name> --no-wait
```

Only `RUN_NAME` is required; the action name defaults to the root action `a0`. Pass an action name
as a second argument to source the task and inputs from a nested action instead.

The debug run uses a **deterministic name** derived from the source run (or from `--name`), so
re-running `flyte debug <run-name>` **reconnects to the live debug session instead of spawning a
duplicate**. To start a fresh debug run (for example if the previous one died), pass a new `--name`.

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

### Debug programmatically

The `debug()` convenience function mirrors `flyte.run()` / `flyte.rerun()`, with the ssh-debug
environment injected so the new run comes up with `sshd`. After it returns, resolve the connection
with `SSHDebug.connect()`:

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

To bake `openssh-server` into the task image for a fast cold start:

```python
env = flyte.TaskEnvironment(
    name="ssh_debug",
    image=flyte.Image.from_debian_base(name="ssh-debug").with_apt_packages("openssh-server"),
    resources=flyte.Resources(cpu=1, memory="1000Mi"),
)
```

### Attach your editor

Once the `Host` block is in place (use `--write-config`, or paste the printed block into
`~/.ssh/config`), connect with either:

```bash
ssh flyte-debug
```

or, in **VS Code**: **Remote-SSH → Connect to Host → `flyte-debug`** (use the session name you chose
with `--name`).

> [!NOTE]
> Tokens expire. If you get a `401` on reconnect, just re-run the same `flyte debug` command — it
> reconnects and refreshes the token in place (no `--write-config` needed). For multi-day sessions,
> use `--api-key`.

## Related

- [Re-run a run](./rerun-runs) — launch a new run from a previous one.
- [Interact with runs and actions](./interacting-with-runs) — retrieve, monitor, and inspect runs and actions.
