---
title: SSHDebug
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# SSHDebug

**Package:** `flyteplugins.union.remote`

Resolved SSH-into-task connect info for a running debug action.


## Parameters

```python
class SSHDebug(
    run_name: str,
    action_name: str,
    wss_url: str,
    ssh_config: str,
    host_alias: str,
    headers_file: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `run_name` | `str` | |
| `action_name` | `str` | |
| `wss_url` | `str` | |
| `ssh_config` | `str` | |
| `host_alias` | `str` | |
| `headers_file` | `Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`connect()`](#connect) | Resolve connect info for a running ssh-debug action. |
| [`ensure_api_key()`](#ensure_api_key) | Ensure a dedicated, long-lived API key (client credentials) exists; return it encoded. |
| [`ensure_keypair()`](#ensure_keypair) | Ensure the auto-managed debug keypair exists; return (private_key_path, public_key). |
| [`launch_env()`](#launch_env) | Env vars to enable ssh-debug on a run, with the debug pubkey auto-injected. |


### connect()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await SSHDebug.connect.aio()`.
```python
def connect(
    cls,
    run_name: str,
    action_name: str,
    user: str,
    identity_file: Optional[str],
    host_alias: str,
    use_api_key: bool,
    refresh_token: bool,
    headers_file: Optional[str],
    timeout: float,
    poll_interval: float,
) -> 'SSHDebug'
```
Resolve connect info for a running ssh-debug action.

Polls the action until its ``:6060`` IDE route is ready (or *timeout*),
mints (or reuses a cached) Bearer token for the ingress, writes the
headers file, and renders the ssh-config block. *identity_file* defaults
to the auto-managed ``~/.flyte/ssh-debug/id_ed25519`` (created on launch).



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `run_name` | `str` | |
| `action_name` | `str` | |
| `user` | `str` | |
| `identity_file` | `Optional[str]` | |
| `host_alias` | `str` | |
| `use_api_key` | `bool` | |
| `refresh_token` | `bool` | |
| `headers_file` | `Optional[str]` | |
| `timeout` | `float` | |
| `poll_interval` | `float` | |

**Raises**

| Exception | Description |
|-|-|
| `TimeoutError` | if the debug route never becomes ready. |

### ensure_api_key()

```python
def ensure_api_key(
    name: str,
) -> str
```
Ensure a dedicated, long-lived API key (client credentials) exists; return it encoded.

Reuses the locally-stored key if it still exists server-side (verified with
``ApiKey.get`` — the "api-key get to check for existence" path). Otherwise
creates a fresh one and stores it 0600. Use this for headless, reusable auth
that doesn't expire mid-session like an interactive user JWT.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

### ensure_keypair()

```python
def ensure_keypair()
```
Ensure the auto-managed debug keypair exists; return (private_key_path, public_key).

Generates an ed25519 keypair at ``~/.flyte/ssh-debug/id_ed25519`` the first
time, then reuses it. The public key is what gets injected into the run
(``_F_SSH_PK``); the private key is what ``flyte connect ssh`` authenticates
with. Idempotent.


### launch_env()

```python
def launch_env(
    extra: Optional[dict],
) -> dict
```
Env vars to enable ssh-debug on a run, with the debug pubkey auto-injected.

Use with the run launcher so users don't manage keys or env vars::

    run = flyte.with_runcontext(env_vars=SSHDebug.launch_env()).run(task)
    info = SSHDebug.connect(run.name)   # uses the same auto-managed key


| Parameter | Type | Description |
|-|-|-|
| `extra` | `Optional[dict]` | |

