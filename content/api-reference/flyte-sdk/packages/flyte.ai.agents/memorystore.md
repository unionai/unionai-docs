---
title: MemoryStore
version: 2.5.2
variants: +flyte +union
layout: py_api
---

# MemoryStore

**Package:** `flyte.ai.agents`

Conversation transcript + path-addressed artifact memory backed by :class:`flyte.io.Dir`.

The construct combines two complementary stores:

- ``messages``: the live LLM conversation transcript (managed by
  :class:`~flyte.ai.agents.Agent`; mutate via :meth:`append` /
  :meth:`extend` only).
- **Path-addressed files** under a working directory ``root``. Use
  :meth:`write_text` / :meth:`read_text` / :meth:`write_json` /
  :meth:`read_json` / :meth:`list_paths` for arbitrary named blobs that
  should round-trip through Flyte object storage.

Persistence is :class:`flyte.io.Dir`-backed. Obtain a store via
:meth:`create` or :meth:`get_or_create`; it saves to a deterministic
blob-store namespace under the active Flyte raw-data bucket, derived from
its ``key``. :meth:`save` always targets that deterministic
:attr:`remote_path`. :meth:`create`, :meth:`get_or_create`, and
:meth:`save` are sync-by-default (``MemoryStore.create(...)``) with an
``.aio(...)`` companion for async call sites, mirroring the rest of the
Flyte SDK.

The on-disk layout under ``root`` looks like::

    &lt;root&gt;/messages.json                           # transcript
    &lt;root&gt;/&lt;your/path&gt;.{txt,json,…}                # path-addressed entries
    &lt;root&gt;/meta/&lt;encoded_path&gt;.json                # per-entry metadata
    &lt;root&gt;/audit/log.jsonl                         # opt-in audit trail
    &lt;root&gt;/versions/&lt;encoded_path&gt;/&lt;ts&gt;_&lt;sha&gt;.txt  # opt-in version history

Optional capabilities (off-by-default unless noted):

- ``read_only_prefixes``: block direct writes into one or more prefixes
  (e.g. ``("memory/",)``). Useful when the agent must stage proposals
  under ``user/`` and a separate trusted pipeline (sleep cycle, reviewer)
  promotes them.
- ``audit`` *(default: True)*: append every successful write to
  ``audit/log.jsonl``. Cheap and easy to disable.
- ``keep_versions``: snapshot every successful write under
  ``versions/&lt;encoded_path&gt;/&lt;ts&gt;_&lt;sha&gt;.txt`` for full history (≈ 2x
  storage on every mutation).

Optimistic concurrency is supported via the ``expected_sha=`` argument on
:meth:`write_text` / :meth:`write_json`; mismatches raise
:class:`ConcurrencyError`.

Public I/O methods are async by default. Each one has a ``*_sync``
companion that runs the same logic on the calling thread; the async
version simply dispatches the sync version to a background thread via
:func:`asyncio.to_thread`.

Every :class:`MemoryStore` is **keyed**: it is bound to a deterministic
blob-store namespace derived from its ``key``. Obtain one via
:meth:`create` or :meth:`get_or_create` (the recommended entry points);
direct construction is supported for serialization / advanced use but still
requires a ``key``. There is no such thing as an unkeyed / ephemeral store.

Parameters
----------
key:
    Deterministic memory key (a single path segment). Determines the
    durable :attr:`remote_path` under the active raw-data root.
messages:
    Pre-existing conversation transcript. Defaults to empty.
root:
    Local working directory backing the store. When omitted, a fresh
    temporary directory is created (and automatically cleaned up when
    the :class:`MemoryStore` is garbage-collected). When pointing at an
    existing directory that contains ``messages.json``, the transcript
    is auto-loaded. This is an internal staging directory; callers
    normally never set it.
remote_path:
    Durable destination for :meth:`save`. Usually resolved from ``key``
    (and the Flyte context) by :meth:`create` / :meth:`get_or_create`;
    when omitted it is resolved lazily on first :meth:`save` / hydration.
read_only_prefixes:
    Prefixes that direct writes are not permitted to target.
audit:
    Enable the append-only audit log.
keep_versions:
    Snapshot every successful write under ``versions/``.


## Parameters

```python
class MemoryStore(
    key: str,
    messages: list[dict[str, Any]],
    root: pathlib.Path | str | None,
    remote_path: str | None,
    read_only_prefixes: tuple[str, ...],
    audit: bool,
    keep_versions: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | |
| `messages` | `list[dict[str, Any]]` | |
| `root` | `pathlib.Path \| str \| None` | |
| `remote_path` | `str \| None` | |
| `read_only_prefixes` | `tuple[str, ...]` | |
| `audit` | `bool` | |
| `keep_versions` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`append()`](#append) | Append a single message to the conversation transcript. |
| [`audit_tail()`](#audit_tail) | Return the last ``n`` audit events (most recent last). |
| [`audit_tail_sync()`](#audit_tail_sync) | Synchronous variant of :meth:`audit_tail`. |
| [`create()`](#create) | Create a new keyed memory store at its deterministic remote path. |
| [`current_sha()`](#current_sha) | Return the sha256 of ``rel_path`` (empty string if it does not exist). |
| [`exists()`](#exists) |  |
| [`extend()`](#extend) | Append a sequence of messages to the conversation transcript. |
| [`flush_messages()`](#flush_messages) | Persist the live transcript to ``messages. |
| [`flush_messages_sync()`](#flush_messages_sync) | Synchronous variant of :meth:`flush_messages`. |
| [`get_meta()`](#get_meta) | Return the :class:`MemoryMeta` sidecar for ``rel_path`` if present. |
| [`get_or_create()`](#get_or_create) | Load a keyed memory store if present, otherwise create it. |
| [`list_paths()`](#list_paths) | List memory file paths under ``prefix`` (POSIX-relative, sorted). |
| [`read_json()`](#read_json) | Return the JSON-decoded contents of ``rel_path`` (or ``default`` if empty/missing). |
| [`read_text()`](#read_text) | Return the UTF-8 contents of ``rel_path`` (or ``default`` if missing). |
| [`remote_path_for_key()`](#remote_path_for_key) | Return the deterministic blob-store path for a keyed memory store. |
| [`save()`](#save) | Serialize this memory to its deterministic keyed remote path. |
| [`write_json()`](#write_json) | JSON-encode ``obj`` and write it via :meth:`write_text`. |
| [`write_text()`](#write_text) | Write ``content`` to ``rel_path`` with optional concurrency + audit + versioning. |


### append()

```python
def append(
    message: dict[str, Any],
)
```
Append a single message to the conversation transcript.


| Parameter | Type | Description |
|-|-|-|
| `message` | `dict[str, Any]` | |

### audit_tail()

```python
def audit_tail(
    n: int,
) -> list[dict[str, Any]]
```
Return the last ``n`` audit events (most recent last).

Returns an empty list when auditing is disabled or the log does not
exist yet.


| Parameter | Type | Description |
|-|-|-|
| `n` | `int` | |

### audit_tail_sync()

```python
def audit_tail_sync(
    n: int,
) -> list[dict[str, Any]]
```
Synchronous variant of :meth:`audit_tail`.


| Parameter | Type | Description |
|-|-|-|
| `n` | `int` | |

### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await MemoryStore.create.aio()`.
```python
def create(
    cls,
    key: str,
    org: str | None,
    project: str | None,
    domain: str | None,
    read_only_prefixes: tuple[str, ...],
    audit: bool,
    keep_versions: bool,
) -> 'MemoryStore'
```
Create a new keyed memory store at its deterministic remote path.

Call synchronously via ``MemoryStore.create(...)``; in async contexts use
``MemoryStore.create.aio(...)``.

Raises :class:`MemoryStoreError` if the keyed blob-store path already
exists. This preserves the explicit "create means new" contract while
keeping subsequent saves deterministic via :meth:`save`.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `key` | `str` | |
| `org` | `str \| None` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `read_only_prefixes` | `tuple[str, ...]` | |
| `audit` | `bool` | |
| `keep_versions` | `bool` | |

### current_sha()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <MemoryStore instance>.current_sha.aio()`.
```python
def current_sha(
    rel_path: str,
) -> str
```
Return the sha256 of ``rel_path`` (empty string if it does not exist).

Sync-by-default (``memory.current_sha(...)``) with an ``.aio(...)`` companion.


| Parameter | Type | Description |
|-|-|-|
| `rel_path` | `str` | |

### exists()

```python
def exists(
    key: str,
    org: str | None,
    project: str | None,
    domain: str | None,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | |
| `org` | `str \| None` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |

### extend()

```python
def extend(
    messages: Sequence[dict[str, Any]],
)
```
Append a sequence of messages to the conversation transcript.


| Parameter | Type | Description |
|-|-|-|
| `messages` | `Sequence[dict[str, Any]]` | |

### flush_messages()

```python
def flush_messages()
```
Persist the live transcript to ``messages.json`` under the working root.


### flush_messages_sync()

```python
def flush_messages_sync()
```
Synchronous variant of :meth:`flush_messages`.


### get_meta()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <MemoryStore instance>.get_meta.aio()`.
```python
def get_meta(
    rel_path: str,
) -> MemoryMeta | None
```
Return the :class:`MemoryMeta` sidecar for ``rel_path`` if present.

Sync-by-default (``memory.get_meta(...)``) with an ``.aio(...)`` companion.


| Parameter | Type | Description |
|-|-|-|
| `rel_path` | `str` | |

### get_or_create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await MemoryStore.get_or_create.aio()`.
```python
def get_or_create(
    cls,
    key: str,
    org: str | None,
    project: str | None,
    domain: str | None,
    read_only_prefixes: tuple[str, ...],
    audit: bool,
    keep_versions: bool,
) -> 'MemoryStore'
```
Load a keyed memory store if present, otherwise create it.

Call synchronously via ``MemoryStore.get_or_create(...)``; in async contexts
use ``MemoryStore.get_or_create.aio(...)``.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `key` | `str` | |
| `org` | `str \| None` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `read_only_prefixes` | `tuple[str, ...]` | |
| `audit` | `bool` | |
| `keep_versions` | `bool` | |

### list_paths()

```python
def list_paths(
    prefix: str,
) -> list[str]
```
List memory file paths under ``prefix`` (POSIX-relative, sorted).

Internal bookkeeping (``audit/``, ``meta/``, ``versions/``) and the
conversation transcript (``messages.json``) are excluded. Symlinked
files are also skipped — both for safety (they can point outside
the root) and to keep the listing deterministic.


| Parameter | Type | Description |
|-|-|-|
| `prefix` | `str` | |

### read_json()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <MemoryStore instance>.read_json.aio()`.
```python
def read_json(
    rel_path: str,
    default: Any,
) -> Any
```
Return the JSON-decoded contents of ``rel_path`` (or ``default`` if empty/missing).

Sync-by-default (``memory.read_json(...)``) with an ``.aio(...)`` companion.


| Parameter | Type | Description |
|-|-|-|
| `rel_path` | `str` | |
| `default` | `Any` | |

### read_text()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <MemoryStore instance>.read_text.aio()`.
```python
def read_text(
    rel_path: str,
    default: str,
) -> str
```
Return the UTF-8 contents of ``rel_path`` (or ``default`` if missing).

Sync-by-default (``memory.read_text(...)``) with an ``.aio(...)`` companion.


| Parameter | Type | Description |
|-|-|-|
| `rel_path` | `str` | |
| `default` | `str` | |

### remote_path_for_key()

```python
def remote_path_for_key(
    key: str,
    org: str | None,
    project: str | None,
    domain: str | None,
) -> str
```
Return the deterministic blob-store path for a keyed memory store.

The path is rooted at the active raw-data bucket/storage root, excluding
bucket-internal sharding and run-specific prefixes::

    {storage_root}/agents/memory-store/v0/{org}/{project}/{domain}/{key}

The ``agents/memory-store`` prefix and ``v0`` version come from
:data:`_MEMORY_NAMESPACE` / :data:`_MEMORY_SCHEMA_VERSION`.


| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | |
| `org` | `str \| None` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |

### save()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <MemoryStore instance>.save.aio()`.
```python
def save()
```
Serialize this memory to its deterministic keyed remote path.

Call synchronously via ``memory.save(...)``; in async contexts use
``memory.save.aio(...)``.

Flushes the conversation transcript to ``messages.json`` under the working
root, then uploads the whole root (live files plus audit log, metadata
sidecars, and any version snapshots) to :attr:`remote_path` (resolved
from :attr:`key` if not already set).


### write_json()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <MemoryStore instance>.write_json.aio()`.
```python
def write_json(
    rel_path: str,
    obj: Any,
    actor: str,
    reason: str,
    expected_sha: str | None,
) -> MemoryMeta
```
JSON-encode ``obj`` and write it via :meth:`write_text`.

Sync-by-default (``memory.write_json(...)``) with an ``.aio(...)`` companion.


| Parameter | Type | Description |
|-|-|-|
| `rel_path` | `str` | |
| `obj` | `Any` | |
| `actor` | `str` | |
| `reason` | `str` | |
| `expected_sha` | `str \| None` | |

### write_text()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <MemoryStore instance>.write_text.aio()`.
```python
def write_text(
    rel_path: str,
    content: str,
    actor: str,
    reason: str,
    expected_sha: str | None,
) -> MemoryMeta
```
Write ``content`` to ``rel_path`` with optional concurrency + audit + versioning.

Sync-by-default (``memory.write_text(...)``) with an ``.aio(...)`` companion.



| Parameter | Type | Description |
|-|-|-|
| `rel_path` | `str` | Destination path, relative to the memory root. Must not escape the root and must not target a reserved or read-only prefix. |
| `content` | `str` | UTF-8 string to write. |
| `actor` | `str` | Free-form identifier of the writer (typically the tool or agent name). Recorded in the audit log + metadata sidecar. |
| `reason` | `str` | Optional human-readable explanation. |
| `expected_sha` | `str \| None` | When provided, the write succeeds only if the current sha256 of ``rel_path`` matches. Mismatches raise :class:`ConcurrencyError`. |

**Returns:** The :class:`MemoryMeta` describing the new content.

