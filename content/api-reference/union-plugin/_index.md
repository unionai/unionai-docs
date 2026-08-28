---
title: Union plugin
version: 0.8.2
variants: -flyte +union
layout: py_api
weight: 5
---

# Union plugin



Union SDK - Proprietary extensions for Flyte.

This package provides Union-specific functionality on top of the open-source Flyte SDK.
## Directory

### Methods

| Method | Description |
|-|-|
| [`debug()`](#debug) | Launch a task, or relaunch an existing run, with ssh-into-task debug enabled. |
| [`fork()`](#fork) | Fork run *run_name*, replaying it with new code and/or inputs. |
| [`with_debugcontext()`](#with_debugcontext) | Like `flyte.with_runcontext`, but preconfigured for ssh-into-task debug. |
| [`with_forkcontext()`](#with_forkcontext) | Like `flyte.with_runcontext`, but the returned runner can also `fork(run_name, ...)`. |


## Methods

#### debug()

```python
def debug(
    target: 'str | TaskTemplate',
    *args: Any,
    action_name: str = 'a0',
    name: Optional[str] = None,
    ssh_host_name: Optional[str] = None,
    custom_context: Optional[Dict[str, str]] = None,
    task_template: 'Optional[TaskTemplate]' = None,
    inputs: Optional[Dict[str, Any]] = None,
    env_vars: Optional[Dict[str, str]] = None,
    **kwargs: Any,
) -> 'Run'
```
Launch a task, or relaunch an existing run, with ssh-into-task debug enabled. Returns the `Run`.

Two forms (mirroring `flyte.run` / `flyte.rerun`), both with the ssh-debug env injected so the new
run comes up with sshd:

- **`debug(task, x=1)`** — run ``task`` in debug mode (= `with_debugcontext().run(task, x=1)`).
- **`debug("run-name")`** — relaunch an existing run in debug mode, fetching its code + inputs
  (= `with_debugcontext().rerun("run-name")`). Pass ``inputs={...}`` to change parameters or
  ``task_template=`` to substitute code.

Then connect with `SSHDebug.connect(run.name)` (or use the `flyte debug <run>` CLI, which relaunches
**and** connects in one shot).



| Parameter | Type | Description |
|-|-|-|
| `target` | `'str \| TaskTemplate'` | a `TaskTemplate` to launch, or a prior run name (str) to relaunch. |
| `*args` | `Any` | |
| `action_name` | `str` | action to source the task + inputs from (default ``a0``). |
| `name` | `Optional[str]` | explicit name for the new run; omit to let the platform assign one. A fixed name makes the launch idempotent — relaunching with the same name re-uses the existing run. |
| `ssh_host_name` | `Optional[str]` | record the intended ssh Host alias on the run's custom_context (``ssh-host-name``); record/propagation only (see `with_debugcontext`). |
| `custom_context` | `Optional[Dict[str, str]]` | extra custom-context key/values to attach to the run (merged with ``ssh-host-name`` when *ssh_host_name* is given). |
| `task_template` | `'Optional[TaskTemplate]'` | substitute task to run instead of the prior run's code. |
| `inputs` | `Optional[Dict[str, Any]]` | native input overrides; omit to reuse the prior run's inputs. |
| `env_vars` | `Optional[Dict[str, str]]` | extra env vars to set on the run (merged with the ssh-debug env). |
| `**kwargs` | `Any` | |

**Returns:** the new ssh-debug Run.

#### fork()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await fork.aio()`.
```python
def fork(
    run_name: str,
    task_template: TaskTemplate | None = None,
    force_rerun_actions: Sequence[str] | None = None,
    allow_missing_source_outputs: bool = False,
    **inputs: Any,
) -> Run
```
Fork run *run_name*, replaying it with new code and/or inputs. Returns a `Run`.

Its succeeded actions are reused; the ones whose code you edited re-execute, along with
anything downstream of them. Pass keyword inputs to change the root action's parameters
(`fork("r1", task_template=fixed, x=2)`); inputs left out keep the source run's values. Use
`with_forkcontext(...)` to apply run-context overrides (name, env vars, ...).



| Parameter | Type | Description |
|-|-|-|
| `run_name` | `str` | Name of the run to fork. |
| `task_template` | `TaskTemplate \| None` | Substitute task to run instead of the source run's code. |
| `force_rerun_actions` | `Sequence[str] \| None` | Names of actions that must re-execute even though they succeeded in the source run. A listed parent re-enqueues its children — list them too to force the whole subtree. Unknown names are ignored. |
| `allow_missing_source_outputs` | `bool` | Proceed when the source run's outputs were cleaned up from storage, using its inputs URI directly. |
| `**inputs` | `Any` | Native keyword inputs to change the root action's parameters; omit an input to keep the source run's value. |

**Returns:** the new Run.

#### with_debugcontext()

```python
def with_debugcontext(
    mode: Any = None,
    env_vars: Optional[Dict[str, str]] = None,
    ssh_host_name: Optional[str] = None,
    custom_context: Optional[Dict[str, str]] = None,
    **kwargs,
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
| `**kwargs` |  | |

#### with_forkcontext()

```python
def with_forkcontext(
    mode: Any = None,
    **kwargs: Any,
) -> _ForkRunner
```
Like `flyte.with_runcontext`, but the returned runner can also `fork(run_name, ...)`.

**The keyword arguments are `flyte.with_runcontext`'s, one for one.** They are forwarded
unchanged to the same underlying runner, so anything you can set on a run you can set on
a fork — `name`, `project`, `domain`, `env_vars`, `labels`, `annotations`, `queue`,
`service_account`, `interruptible`, `copy_style`, `raw_data_path`, `overwrite_cache`,
`cache_lookup_scope`, `max_action_concurrency`, `notifications`, `custom_context`,
`log_level`, `debug`, and the rest. `flyte.with_runcontext`
is the authoritative reference for what each one does; this function deliberately does not
restate or restrict the list, so options added to the SDK work here the day they land.

They are taken as `**kwargs` rather than spelled out, which is what keeps the two in
lockstep — at the cost of no signature help in an editor. `test_fork.py` asserts every
`with_runcontext` parameter is still accepted here, so the claim above stays true.

What to fork — the run name, substitute code, replay actions — belongs to `fork()`, not
here, exactly as the run itself belongs to `run()` / `rerun()`.

```python
run = with_forkcontext(
    name="fix-1",                     # any with_runcontext option
    env_vars={"LOG_LEVEL": "debug"},
    queue="gpu",
).fork("ul56wcvgqrb9vzhzz5l2", task_template=my_task)
```



| Parameter | Type | Description |
|-|-|-|
| `mode` | `Any` | Run mode, as `flyte.with_runcontext`'s first argument. Forking is remote-only, so a non-remote mode is rejected by `fork()` at launch. |
| `**kwargs` | `Any` | Any keyword argument `flyte.with_runcontext` accepts, forwarded unchanged. |

**Returns:** a runner that behaves like `with_runcontext`'s, plus `fork()`.

