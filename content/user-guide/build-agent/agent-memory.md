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

First, define the agent. Here it's a small research assistant with a single, **stateless** `web_search` tool — its continuity comes from memory, not from the tool:

{{< code file="/unionai-examples/v2/user-guide/build-agent/agent-memory/agent_with_memory.py" fragment="agent" lang="python" >}}

Reuse the same `key` across runs to keep continuity. The chat task below picks up where the previous run left off (see the [full example](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/build-agent/agent-memory/agent_with_memory.py) for the `TaskEnvironment` setup):

{{< code file="/unionai-examples/v2/user-guide/build-agent/agent-memory/agent_with_memory.py" fragment="chat" lang="python" >}}

The agent has no note-taking tools. Continuity comes entirely from the persisted transcript, and it remembers two kinds of things for free: the **facts the user shares** and the **results its tools return**. The first run records both in `messages.json`; a later run with the same `memory_key` reloads and prepends them, so the agent recalls earlier context — and reuses prior `web_search` findings instead of searching again. That is the core value of `MemoryStore` — no extra plumbing required.

## Working with a MemoryStore independently

Beyond the transcript, you can persist structured artifacts under arbitrary paths in the same store. This is optional — most agents get all the continuity they need from the transcript above — but it's useful when you want durable, queryable state (a scratchpad, a dedupe ledger, intermediate results).

A flyte task can commit its own artifact by loading the keyed store, read-modify-writing a path-addressed file, and calling `save()`. Every write is recorded in a metadata sidecar (sha256, actor, timestamp) and, by default, appended to an audit log:

```python
from flyte.ai.agents import MemoryStore

MEMORY_KEY = "my-assistant"
NOTES_PATH = "notes/notes.json"


@env.task
async def add_note(note: str) -> str:
    """A tool that commits its own artifact to the keyed store."""
    memory = await MemoryStore.get_or_create.aio(key=MEMORY_KEY)
    notes = await memory.read_json.aio(NOTES_PATH, default=[])
    notes.append(note)
    await memory.write_json.aio(NOTES_PATH, notes, reason="agent note")
    await memory.save.aio()  # commit the artifact to the keyed remote path
    return f"Noted: {note}"
```

> [!NOTE] Coordinating tool writes with the transcript
> Artifacts live on independent paths (e.g. `notes/notes.json`) from the transcript (`messages.json`), so they never collide. But when a tool writes to the same keyed store that the orchestrator also saves, the orchestrator's working copy goes stale mid-run. Reload the store with `get_or_create` after `agent.run`, carry over the updated transcript (`reloaded.messages = result.memory.messages`), and save once — otherwise the orchestrator's final save re-uploads a stale copy and clobbers the tool's artifact.

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

## Passing memory to the agent

Memory is not attached to the agent — it is passed in per call and returned on the result. `agent.run(message, memory=store)` prepends the store's prior transcript, runs the loop, and appends the new turn back onto the store. Persisting is explicit: `run` never writes on its own, so call `memory.save()` (or `await memory.save.aio()`) yourself afterward.

```python
memory = await MemoryStore.get_or_create.aio(key="my-assistant")
result = await agent.run.aio(message, memory=memory)
await memory.save.aio()  # save() always targets the deterministic keyed path
```

You can also pass a plain `list[dict]` of prior messages as `memory` for a stateless, single-shot history (nothing is persisted in that case).

## Lower-level usage

Every `MemoryStore` is **keyed** — there is no unkeyed/ephemeral store. You normally obtain one via `MemoryStore.create(key=...)` or `MemoryStore.get_or_create(key=...)`, but direct construction is supported for advanced use and serialization (`MemoryStore` is a Flyte I/O type, so it can be passed as a task input/output). `save()` takes no arguments: it always uploads the working root to the deterministic keyed `remote_path`. When `root` is omitted, a temporary working directory is created and cleaned up automatically.

## Next steps

- [The Flyte Agent harness](./flyte-agents): how the agent loop uses `memory`.
- [Deploy an agent as a service](./deploy-agent-as-service): schedule a memory-backed agent so it resumes context on each wakeup.
