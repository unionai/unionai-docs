---
title: Agent memory
weight: 4
variants: +flyte +serverless +union
mermaid: true
---

# Agent memory

By default, an [`Agent`](./flyte-agents) is stateless: each `run` starts from a blank conversation. `MemoryStore` gives an agent continuity across runs by persisting both the conversation transcript and arbitrary path-addressed artifacts to a `flyte.io.Dir`. This is what lets a scheduled or webhook-driven agent remember what it did last time.

Use cases:

- An "inbox triage" agent that recalls which threads it has already responded to.
- A research agent that builds up a scratchpad over many days.
- Any sleep/wake pattern where the agent wakes on a schedule and resumes prior context.

## What a `MemoryStore` holds

A `MemoryStore` combines two complementary stores backed by a working directory:

- **`messages`** — the live LLM conversation transcript, managed by the agent. Mutate it only via `append()` / `extend()`.
- **Path-addressed files** — arbitrary named blobs under the working root. Read and write them with `read_text` / `write_text` / `read_json` / `write_json` / `list_paths`.

The on-disk layout under the root looks like:

```
<root>/messages.json                           # transcript
<root>/<your/path>.{txt,json,…}                # path-addressed entries
<root>/meta/<encoded_path>.json                # per-entry metadata (sha, actor, ts)
<root>/audit/log.jsonl                         # opt-in audit trail
<root>/versions/<encoded_path>/<ts>_<sha>.txt  # opt-in version history
```

## Sync vs async

The path-addressed I/O methods (`read_text`, `read_json`, `write_text`, `write_json`, `get_meta`, `current_sha`) and the lifecycle methods (`create`, `get_or_create`, `save`) are sync-by-default with an `.aio(...)` companion. Inside `async def` tasks, use the `.aio` form.

## Keyed stores: the easy path

For durable agent memory, use a **keyed store**. `MemoryStore.get_or_create(key=...)` loads an existing store if present, otherwise creates a new one, saving to a deterministic blob-store namespace under the active {{< key product_name >}} raw-data root:

```
{storage_root}/agents/memory-store/v0/{org}/{project}/{domain}/{key}
```

Reuse the same `key` across runs to keep continuity. The chat task below picks up where the previous run left off (see the [full example](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/build-agent/agent-memory/agent_with_memory.py) for the `agent` and `TaskEnvironment` setup):

{{< code file="/unionai-examples/v2/user-guide/build-agent/agent-memory/agent_with_memory.py" fragment="chat" lang="python" >}}

The first run records facts; a later run with the same `memory_key` recalls them — no extra plumbing required.

## Path-addressed artifacts

Beyond the transcript, tools can persist structured artifacts. Every write is recorded in a metadata sidecar (sha256, actor, timestamp) and, by default, appended to an audit log. The tools below read and write a `notes/notes.json` artifact, using optimistic concurrency (covered next) to avoid lost updates:

{{< code file="/unionai-examples/v2/user-guide/build-agent/agent-memory/agent_with_memory.py" fragment="tools" lang="python" >}}

## Optimistic concurrency

When several tasks or agents share one keyed store (e.g. parallel tool calls, or a sleep/wake pattern), guard against lost updates by passing `expected_sha=`. The write succeeds only if the current content still matches; otherwise it raises `ConcurrencyError`:

```python
from flyte.ai.agents import ConcurrencyError

notes = await memory.read_json.aio("notes/notes.json", default=[])
sha = await memory.current_sha.aio("notes/notes.json")
notes.append(note)
try:
    await memory.write_json.aio("notes/notes.json", notes, expected_sha=sha, reason="agent note")
except ConcurrencyError:
    # Another writer updated the file between our read and write.
    return "Memory changed while saving the note; please retry."
```

## Optional capabilities

`MemoryStore` (and `create` / `get_or_create`) accept a few flags:

| Option | Default | What it does |
|--------|---------|--------------|
| `audit` | `True` | Append every successful write to `audit/log.jsonl`. Inspect with `audit_tail(n)`. |
| `keep_versions` | `False` | Snapshot every write under `versions/` for full history (≈ 2× storage per write). |
| `read_only_prefixes` | `()` | Reject direct writes into the given prefixes (e.g. `("memory/",)`), so the agent must stage proposals elsewhere and a trusted pipeline promotes them. |

The internal `audit/`, `meta/`, and `versions/` prefixes and `messages.json` are reserved — writes to them are rejected, and they're excluded from `list_paths`.

## Lower-level usage (without a key)

You can also construct a `MemoryStore` directly against a working `root` and call `save(remote_destination=...)` yourself. This is useful for one-off persistence or when you manage the destination path. When omitted, a temporary working directory is created and cleaned up automatically.

## Next steps

- [The Flyte Agent harness](./flyte-agents): how the agent loop uses `memory`.
- [Deploy an agent as a service](./deploy-agent-as-service): schedule a memory-backed agent so it resumes context on each wakeup.
