---
title: Custom Context
weight: 100
variants: +flyte +serverless +byoc +selfmanaged
---

# Custom context

Custom context provides a mechanism for implicitly passing configuration and metadata through your entire task execution hierarchy without adding parameters to every task. It is ideal for cross-cutting concerns such as tracing, environment metadata, or experiment identifiers.

Think of custom context as **execution-scoped metadata** that automatically flows from parent to child tasks.

## Overview

Custom context is an implicit key–value configuration map that is automatically available in every Flyte task during execution. It is accessed via:

```python
flyte.ctx().custom_context
```

Custom context is fundamentally different from standard task inputs. Task inputs are explicit, strongly typed parameters that you declare as part of a task’s signature. They directly influence the task’s computation and therefore participate in Flyte’s caching and reproducibility guarantees.

Custom context, on the other hand, is implicit metadata. It consists only of string key/value pairs, is not part of the task signature, and does not affect task caching. Because it is injected by the Flyte runtime rather than passed as a formal input, it should be used only for environmental or contextual information, not for data that changes the logical output of a task.

## When to use it and when not to

Custom Context is perfect when you need metadata, not domain data, to flow through your tasks.

Good use cases:

- Tracing IDs, span IDs
- Experiment or run metadata
- Environment region, cluster ID
- Logging correlation keys
- Feature flags
- Session IDs for 3rd-party APIs (e.g., an LLM session)

Avoid using for:

- Business/domain data
- Inputs that change task outputs
- Anything affecting caching or reproducibility
- Large blobs of data (keep it small)

It is the cleanest mechanism when you need something available everywhere, but not logically an input to the computation.

## Setting custom context

There are two ways to set custom context for a Flyte run:

1. Set it once for the entire run when you launch (`with_runcontext`) — this establishes the base context for the execution
2. Set or override it inside task code using `flyte.custom_context(...)` context manager — this changes the active context for that task block and any nested tasks called from it

Both are legitimate and complementary. The important behavioral rules to understand are:

- `with_runcontext(...)` sets the run-level base. Values provided here are available everywhere unless overridden later. Use this for metadata that should apply to most or all tasks in the run (experiment name, top-level trace id, run id, etc.).
- `flyte.custom_context(...)` is used inside task code to set or override values for that scope. It does affect nested tasks invoked while that context is active. In practice this means you can override run-level entries, add new keys for downstream tasks, or both.
- Merging & precedence: contexts are merged; when the same key appears in multiple places the most recent/innermost value wins (i.e., values set by `flyte.custom_context(...)` override the run-level values from `with_runcontext(...)` for the duration of that block).

### Run-level context

Set base metadata once when starting the run:

```python
import flyte

env = flyte.TaskEnvironment("hello_world")

@env.task
async def leaf_task():
    # Reads run-level context
    print("leaf sees:", flyte.ctx().custom_context)
    return flyte.ctx().custom_context.get("trace_id")

@env.task
async def root():
    return await leaf_task()

if __name__ == "__main__":
    flyte.init_from_config()
    # Base context for the entire run
    flyte.with_runcontext(custom_context={"trace_id": "root-abc", "experiment": "v1"}).run(root)
```

Output (every task sees the base keys unless overridden):

```bash
leaf sees: {"trace_id": "root-abc", "experiment": "v1"}
```

### Overriding inside a task (local override that affects nested tasks)

Use `flyte.custom_context(...)` inside a task to override or add keys for downstream calls:

```python
@env.task
async def downstream():
    print("downstream sees:", flyte.ctx().custom_context)
    return flyte.ctx().custom_context.get("trace_id")

@env.task
async def parent():
    print("parent initial:", flyte.ctx().custom_context)

    # Override the trace_id for the nested call(s)
    with flyte.custom_context(trace_id="child-override"):
        val = await downstream()     # downstream sees trace_id="child-override"

    # After the context block, run-level values are back
    print("parent after:", flyte.ctx().custom_context)
    return val
```

If the run was started with `{"trace_id": "root-abc"}`, this prints:

```bash
parent initial: {"trace_id": "root-abc"}
downstream sees: {"trace_id": "child-override"}
parent after: {"trace_id": "root-abc"}
```

Note that the override affected the nested downstream task because it was invoked while the `flyte.custom_context` block was active.

### Adding new keys for nested tasks

You can add keys (not just override):

```python
with flyte.custom_context(experiment="exp-blue", run_group="g-7"):
    await some_task()   # some_task sees both base keys + the new keys
```

## Accessing custom context

Always via the Flyte runtime:

```python
ctx = flyte.ctx().custom_context
value = ctx.get("key")
```

You can access the custom context using either `flyte.ctx().custom_context` or the shorthand `flyte.get_custom_context()`, which returns the same dictionary of key/value pairs.

Values are always strings, so parse as needed:

```python
timeout = int(ctx["timeout_seconds"])
```
