---
title: flyte.ai.agents.memory
version: 2.5.1
variants: +flyte +union
layout: py_api
---

# flyte.ai.agents.memory

Dir-backed memory for :class:`flyte.ai.agents.Agent`.

This module implements :class:`MemoryStore`, a directory-backed store that
combines a managed conversation transcript with path-addressed artifact files,
plus optional auditing, read-only prefixes, version snapshots, and optimistic
concurrency. It is intentionally decoupled from the agent loop so non-agent
code (sleep cycles, promotion tasks, dashboards) can use the same store with
the same enforcement.

Design influences include the Claude-style "many small files addressed by
path, with audit + version history" pattern.

The path-addressed I/O methods (``read_text``, ``read_json``, ``get_meta``,
``current_sha``, ``write_text``, ``write_json``) — like the keyed-store methods
``create`` / ``get_or_create`` / ``save`` — are :func:`~flyte.syncify.syncify`-wrapped:
call them synchronously (``memory.read_text(...)``) or await the ``.aio(...)``
companion in async code. The remaining helpers (``flush_messages``, ``audit_tail``)
stay async-by-default with explicit ``*_sync`` companions, and ``list_paths`` is
synchronous.
## Directory

### Classes

| Class | Description |
|-|-|
| [`MemoryMeta`](../flyte.ai.agents.memory/memorymeta) | Per-file metadata sidecar (sha256, actor, timestamp, …) for a memory entry. |
| [`MemoryStore`](../flyte.ai.agents.memory/memorystore) | Conversation transcript + path-addressed artifact memory backed by :class:`flyte. |

### Errors

| Exception | Description |
|-|-|
| [`AccessDenied`](../flyte.ai.agents.memory/accessdenied) | Raised when a write targets a read-only or reserved prefix. |
| [`ConcurrencyError`](../flyte.ai.agents.memory/concurrencyerror) | Raised when an ``expected_sha`` precondition does not match the current state. |
| [`MemoryStoreError`](../flyte.ai.agents.memory/memorystoreerror) | Base class for :class:`MemoryStore` errors. |

### Variables

| Property | Type | Description |
|-|-|-|
| `MESSAGES_PATH` | `str` |  |

