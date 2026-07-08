---
title: Error handling
weight: 13
variants: +flyte +union
---

# Error handling

One of the key features of Flyte 2 is the ability to recover from user-level errors in a workflow execution.
This includes out-of-memory errors, timeouts, oversized inline I/O, and other exceptions.

In a distributed system with heterogeneous compute, certain types of errors are expected and even, in a sense, acceptable.
Flyte 2 recognizes this and allows you to handle them gracefully as part of your workflow logic.

This ability is a direct result of the fact that workflows are now written in regular Python,
giving you all the power and flexibility of Python error handling.
When a task fails, Flyte surfaces the failure to the calling task as a typed exception that you can catch with a
standard `try...except` block and respond to however you like—retry with more resources, fall back to a different
code path, or clean up and re-raise.

## How Flyte represents failures

When a downstream task fails, the failure propagates to the awaiting parent task as an exception from the
`flyte.errors` module. Every native exception derives from a small hierarchy of base classes:

- `flyte.errors.BaseRuntimeError` — the root of all Flyte runtime errors.
- `flyte.errors.RuntimeUserError` — the failure was caused by your code (a bug, an exception you raised, an
  out-of-memory condition, and so on). An exception you raise inside a task—say a `ValueError`—is wrapped and
  surfaces to the parent as a `flyte.errors.RuntimeUserError`.
- `flyte.errors.RuntimeSystemError` — the failure was caused by the platform rather than your code.

Every concrete error carries a `code` attribute (a stable string identifier such as `"OOMError"`) that you can
inspect when logging or branching. Because the errors form a hierarchy, you can catch broadly
(`except flyte.errors.RuntimeUserError`) or narrowly (`except flyte.errors.OOMError`), depending on how specific
your recovery logic needs to be.

## Catching and recovering from errors

The most common pattern is to catch a specific exception and re-run the failing task with a different
configuration. The following example intentionally triggers an out-of-memory error, catches the
`flyte.errors.OOMError`, and retries the task with more memory:

{{< code file="/unionai-examples/v2/user-guide/task-programming/error-handling/error_handling.py" lang="python" >}}

In this code, we do the following:

* Import the necessary modules, including `flyte.errors`.
* Set up the task environment with a modest resource allocation of 1 CPU and 250 MiB of memory.
* Define two tasks: `oomer`, which allocates a large list and is likely to run out of memory, and
  `always_succeeds`, which always returns cleanly.
* Define the `main` task (the top-level workflow task) that contains the failure-recovery logic.

The `try...except` block in `main` runs `oomer`. If it exhausts memory, `main` catches the
`flyte.errors.OOMError` and retries by calling `oomer.override(resources=...)` with a larger memory allocation.
If the retry also runs out of memory, `main` gives up and re-raises the error. The `finally` block runs
`always_succeeds` regardless of the outcome.

This type of dynamic error handling lets you gracefully recover from user-level errors in your workflows using
patterns you already know from ordinary Python. For a complete, self-tuning version of this pattern that caches
the optimal memory setting across runs, see the
[`resource_tuner` example](https://github.com/flyteorg/flyte-sdk/blob/main/examples/advanced/resource_tuner.py).

> [!NOTE] Programmatic recovery vs. automatic retries
> Catching an exception and re-running a task is *programmatic* recovery—you decide what to do differently on
> the next attempt. This is distinct from Flyte's *automatic* retries (`retries=N` on a task), which simply
> re-run the same attempt unchanged. The two compose: automatic retries handle transient failures, while a
> `try...except` handles failures you want to respond to deliberately. See
> [Retries and timeouts](../task-configuration/retries-and-timeouts).

## Limiting inline I/O

Small task inputs and outputs are passed *inline*—embedded directly in the task's metadata—rather than offloaded
to blob storage. This is fast, but very large inline values are undesirable, so each task has a ceiling on the
size of its inline I/O. You set this ceiling with the `max_inline_io_bytes` parameter on `@env.task`, and Flyte
raises a `flyte.errors.InlineIOMaxBytesBreached` when an input or output exceeds it:

```python
import flyte
import flyte.errors

env = flyte.TaskEnvironment(
    name="large_inline_io",
    resources=flyte.Resources(cpu=1, memory="250Mi"),
)


@env.task(max_inline_io_bytes=100 * 1024)  # Limit inline I/O to 100 KiB
async def printer_task(x: str) -> str:
    print(f"Printer task received: {x}")
    return x


@env.task
async def large_inline_io() -> str:
    small = await printer_task("Hello, world!")
    print(f"Small string result: {small}")

    # A large string that exceeds the 100 KiB inline limit
    large_string = "A" * 10**6  # ~1 MiB
    try:
        return await printer_task(large_string)
    except flyte.errors.InlineIOMaxBytesBreached as e:
        print(f"Inline I/O limit breached: {e}")
        raise
```

The small string passes through, but the ~1 MiB string breaches the 100 KiB limit and raises
`flyte.errors.InlineIOMaxBytesBreached`. When you expect large values, raise `max_inline_io_bytes` or pass the
data as a `flyte.io.File` or `flyte.io.Dir` so it is offloaded to blob storage instead of travelling inline. A
runnable version of this example is available as
[`large_inline_io.py`](https://github.com/flyteorg/flyte-sdk/blob/main/examples/advanced/large_inline_io.py).

## Natively-supported exceptions

Flyte raises typed exceptions for the failure modes it recognizes, so you can catch exactly the condition you
care about. The most commonly caught errors are:

| Exception | Raised when |
|---|---|
| `flyte.errors.OOMError` | A task exceeds its memory allocation. |
| `flyte.errors.TaskTimeoutError` | A task runs longer than its configured timeout. |
| `flyte.errors.InlineIOMaxBytesBreached` | An input or output exceeds the task's `max_inline_io_bytes` limit. |
| `flyte.errors.RetriesExhaustedError` | A task fails after all of its automatic retries are used up. |
| `flyte.errors.TaskInterruptedError` | A task running on interruptible (spot) compute is preempted. |
| `flyte.errors.ActionAbortedError` | An action is aborted externally via the CLI, UI, or API. |
| `flyte.errors.ImagePullBackOffError` | The task's container image cannot be pulled. |
| `flyte.errors.NonRecoverableError` | A failure that should not be retried, regardless of the retry budget. |

These all derive from `flyte.errors.RuntimeUserError`, so a single `except flyte.errors.RuntimeUserError`
catches any of them when you want uniform handling. This is only a selection—for the complete catalog of
catchable exception classes, see the [`flyte.errors` API reference](../../api-reference/flyte-sdk/packages/flyte.errors/_index).

## Related pages

- [Retries and timeouts](../task-configuration/retries-and-timeouts) — configure automatic retries and execution time limits.
- [Abort and cancel actions](./abort-tasks) — stop actions programmatically or externally, and handle `flyte.errors.ActionAbortedError`.
