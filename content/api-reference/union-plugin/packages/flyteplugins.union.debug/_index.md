---
title: flyteplugins.union.debug
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# flyteplugins.union.debug

SSH-into-task debug helpers.

`with_debugcontext(...)` is `flyte.with_runcontext(...)` preconfigured for
ssh-into-task debug: it creates/uses the auto-managed debug keypair and sets the
``_F_E_SSH`` / ``_F_SSH_PK`` / ``_F_E_VS`` env vars, then forwards everything
else to `flyte.with_runcontext`. After the run starts, resolve the connection
with `SSHDebug.connect(run.name)` (or the `flyte connect ssh <run>` CLI).

Example:
```python
import flyte
from flyteplugins.union.debug import with_debugcontext, SSHDebug

flyte.init_from_config()
run = with_debugcontext().run(my_task, x=1)
print(SSHDebug.connect(run.name).ssh_config)   # paste into ~/.ssh/config, then `ssh flyte-debug`
```
## Directory

### Classes

| Class | Description |
|-|-|
| [`SSHDebug`](../flyteplugins.union.debug/sshdebug) | Resolved SSH-into-task connect info for a running debug action. |

### Methods

| Method | Description |
|-|-|
| [`with_debugcontext()`](#with_debugcontext) | Like `flyte. |


## Methods

#### with_debugcontext()

```python
def with_debugcontext(
    mode: Any,
    env_vars: Optional[Dict[str, str]],
    kwargs,
)
```
Like `flyte.with_runcontext`, but preconfigured for ssh-into-task debug.

Ensures the auto-managed debug keypair exists and merges the ssh-debug env
(``_F_E_SSH`` / ``_F_SSH_PK`` / ``_F_E_VS``) into *env_vars*; all other
arguments are forwarded unchanged. Returns the same runner as
`with_runcontext`, so call ``.run(task, ...)`` on it.


| Parameter | Type | Description |
|-|-|-|
| `mode` | `Any` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `kwargs` | `**kwargs` | |

