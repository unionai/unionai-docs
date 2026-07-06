---
title: flyteplugins.union
version: 0.5.1
variants: +flyte +union
layout: py_api
---

# flyteplugins.union

Union SDK - Proprietary extensions for Flyte.

This package provides Union-specific functionality on top of the open-source Flyte SDK.
## Directory

### Methods

| Method | Description |
|-|-|
| [`debug()`](#debug) | Launch a task, or relaunch an existing run, with ssh-into-task debug enabled. |
| [`with_debugcontext()`](#with_debugcontext) | Like `flyte. |


## Methods

#### debug()

```python
def debug(
    target: 'str | TaskTemplate',
    args: *args,
    action_name: str,
    name: Optional[str],
    ssh_host_name: Optional[str],
    custom_context: Optional[Dict[str, str]],
    task_template: 'Optional[TaskTemplate]',
    inputs: Optional[Dict[str, Any]],
    env_vars: Optional[Dict[str, str]],
    kwargs: **kwargs,
) -> 'Run'
```
Launch a task, or relaunch an existing run, with ssh-into-task debug enabled. Returns the `Run`.

Two forms (mirroring `flyte.run` / `flyte.rerun`), both with the ssh-debug env injected so the new
run comes up with sshd:

- **`debug(task, x=1)`** — run ``task`` in debug mode (= `with_debugcontext().run(task, x=1)`).
- **`debug("run-name")`** — relaunch an existing run in debug mode, fetching its code + inputs
  (= `with_debugcontext().rerun("run-name")`). Pass ``inputs={...}`` to change parameters or
  ``task_template=`` to substitute code.

Then connect with `SSHDebug.connect(run.name)` (or use the `flyte debug &lt;run&gt;` CLI, which relaunches
**and** connects in one shot).



| Parameter | Type | Description |
|-|-|-|
| `target` | `'str \| TaskTemplate'` | a `TaskTemplate` to launch, or a prior run name (str) to relaunch. |
| `args` | `*args` | |
| `action_name` | `str` | action to source the task + inputs from (default ``a0``). |
| `name` | `Optional[str]` | explicit name for the new run; omit to let the platform assign one. A fixed name makes the launch idempotent — relaunching with the same name re-uses the existing run. |
| `ssh_host_name` | `Optional[str]` | record the intended ssh Host alias on the run's custom_context (``ssh-host-name``); record/propagation only (see `with_debugcontext`). |
| `custom_context` | `Optional[Dict[str, str]]` | extra custom-context key/values to attach to the run (merged with ``ssh-host-name`` when *ssh_host_name* is given). |
| `task_template` | `'Optional[TaskTemplate]'` | substitute task to run instead of the prior run's code. |
| `inputs` | `Optional[Dict[str, Any]]` | native input overrides; omit to reuse the prior run's inputs. |
| `env_vars` | `Optional[Dict[str, str]]` | extra env vars to set on the run (merged with the ssh-debug env). |
| `kwargs` | `**kwargs` | |

**Returns:** the new ssh-debug Run.

#### with_debugcontext()

```python
def with_debugcontext(
    mode: Any,
    env_vars: Optional[Dict[str, str]],
    ssh_host_name: Optional[str],
    custom_context: Optional[Dict[str, str]],
    kwargs,
)
```
Like `flyte.with_runcontext`, but preconfigured for ssh-into-task debug.

Ensures the auto-managed debug keypair exists and merges the ssh-debug env
(``_F_E_SSH`` / ``_F_SSH_PK`` / ``_F_E_VS``) into *env_vars*; all other
arguments are forwarded unchanged. Returns the same runner as
`with_runcontext`, so call ``.run(task, ...)`` / ``.rerun(run, ...)`` on it.

*ssh_host_name* records the intended ssh Host alias on the run's *custom_context*
(under ``ssh-host-name``); it is propagation/record only — the alias used to build
the local ssh-config is the one threaded directly to `SSHDebug.connect`.


| Parameter | Type | Description |
|-|-|-|
| `mode` | `Any` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `ssh_host_name` | `Optional[str]` | |
| `custom_context` | `Optional[Dict[str, str]]` | |
| `kwargs` | `**kwargs` | |

