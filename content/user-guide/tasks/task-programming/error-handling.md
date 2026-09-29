---
title: Error handling
description: Catch and recover from task failures, including out-of-memory errors, timeouts, missing GPU capacity, and GPU hardware faults.
icon: exclamation-triangle
weight: 13
variants: +flyte +union
---

# Error handling

One of the key features of Flyte 2 is the ability to recover from user-level errors in a workflow execution.
This includes out-of-memory errors, timeouts, GPUs that can't be scheduled or that fault mid-run, oversized
inline I/O, and other exceptions.

In a distributed system with heterogeneous compute, certain types of errors are expected and even, in a sense, acceptable.
Flyte 2 recognizes this and allows you to handle them gracefully as part of your workflow logic.

This ability is a direct result of the fact that workflows are now written in regular Python,
giving you all the power and flexibility of Python error handling.
When a task fails, Flyte surfaces the failure to the calling task as a typed exception that you can catch with a
standard `try...except` block and respond to however you like: retry with more resources, fall back to a different
code path, or clean up and re-raise.

## How Flyte represents failures

When a downstream task fails, the failure propagates to the awaiting parent task as an exception from the
`flyte.errors` module. Every native exception derives from a small hierarchy of base classes:

- `flyte.errors.BaseRuntimeError`: the root of all Flyte runtime errors.
- `flyte.errors.RuntimeUserError`: the failure was caused by your code (a bug, an exception you raised, an
  out-of-memory condition, and so on). An exception you raise inside a task, say a `ValueError`, is wrapped and
  surfaces to the parent as a `flyte.errors.RuntimeUserError`.
- `flyte.errors.RuntimeSystemError`: the failure was caused by the platform rather than your code.
- `flyte.errors.RuntimeUnknownError`: the failure could not be classified as a user or system error.
Every concrete error carries a `code` attribute (a short, stable string identifier, often the exception's class name, e.g. `"TaskTimeoutError"`) that you can
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
> Catching an exception and re-running a task is *programmatic* recovery: you decide what to do differently on
> the next attempt. This is distinct from Flyte's *automatic* retries (`retries=N` on a task), which simply
> re-run the same attempt unchanged. The two compose: automatic retries handle transient failures, while a
> `try...except` handles failures you want to respond to deliberately. See
> [Retries and timeouts](../task-configuration/retries-and-timeouts).

### Out-of-memory on the GPU

`flyte.errors.OOMError` covers the container running out of host memory, which the platform detects when it
kills the pod. Running out of *GPU* memory is different: the process keeps running and your framework raises
its own exception, such as `torch.cuda.OutOfMemoryError`. Like any exception raised in a task, it reaches the
parent as a `flyte.errors.RuntimeUserError`, with the exception's class name as its `code`:

```python
@env.task
async def main() -> str:
    try:
        return await train(batch_size=64)
    except flyte.errors.RuntimeUserError as e:
        if e.code != "OutOfMemoryError":
            raise
        # The GPU ran out of memory: retry with a smaller batch.
        return await train(batch_size=32)
```

## Falling back when GPU capacity isn't available

A task that asks for a scarce accelerator can sit in the **Queued** or **Waiting for resources** phase for a
long time if the cluster has none free. Set
[`max_queued_time`](../task-configuration/retries-and-timeouts#max_queued_time-fail-fast-when-capacity-isnt-available)
to bound that wait. When it fires, the parent catches `flyte.errors.MaxQueuedTimeExceededError` and can try a
different accelerator instead of waiting forever:

```python
from datetime import timedelta

import flyte
import flyte.errors

gpu_env = flyte.TaskEnvironment(
    name="trainer",
    resources=flyte.Resources(cpu=8, memory="64Gi", gpu="H100:1"),
)
driver = flyte.TaskEnvironment(name="driver", depends_on=[gpu_env])


@gpu_env.task(timeout=flyte.Timeout(max_queued_time=timedelta(minutes=10)))
async def train(epochs: int) -> str:
    ...


# Tried in order. The first one that is scheduled within max_queued_time wins.
GPU_OPTIONS = ["H100:1", "A100 80G:1", "L40s:1"]


@driver.task
async def main(epochs: int = 3) -> str:
    for gpu in GPU_OPTIONS:
        try:
            resources = flyte.Resources(cpu=8, memory="64Gi", gpu=gpu)
            return await train.override(resources=resources)(epochs=epochs)
        except flyte.errors.MaxQueuedTimeExceededError as e:
            print(f"No {gpu} capacity within 10 minutes, trying the next option: {e}")
    raise RuntimeError(f"No capacity for any of {GPU_OPTIONS}")
```

The per-attempt queue budget is what keeps each step of the fallback short. Without it, the first option would
wait until capacity appeared or a `deadline` fired, and the loop would never advance.

{{< variant union >}}
{{< markdown >}}

### Routing each option to a different queue

Different GPU pools often live behind different [queues](../task-configuration/queues), each bound to its own
cluster or node pool. Override `queue` along with `resources` so each option is scheduled where that GPU
actually exists:

```python
# (queue, GPU) pairs, tried in order.
PLACEMENTS = [
    ("gpu-h100", "H100:1"),
    ("gpu-a100", "A100 80G:1"),
    ("gpu-l40s-secondary", "L40s:1"),
]


@driver.task
async def main(epochs: int = 3) -> str:
    for queue, gpu in PLACEMENTS:
        try:
            resources = flyte.Resources(cpu=8, memory="64Gi", gpu=gpu)
            return await train.override(queue=queue, resources=resources)(epochs=epochs)
        except flyte.errors.MaxQueuedTimeExceededError:
            print(f"Queue {queue} had no {gpu} capacity, moving on")
    raise RuntimeError("No queue had capacity")
```

Queues are created by your platform admin; see [Managing queues](../../cluster-workload-management/queues).

{{< /markdown >}}
{{< /variant >}}

### Telling the timeout bounds apart

Each bound in `flyte.Timeout` raises its own subclass of `flyte.errors.TaskTimeoutError`, so the parent can tell
"never started" from "started but ran too long":

| Exception | Bound that fired | Typical response |
|---|---|---|
| `flyte.errors.MaxQueuedTimeExceededError` | `max_queued_time`: the attempt never started running. | Try a different accelerator, queue, or cluster. |
| `flyte.errors.MaxRuntimeExceededError` | `max_runtime`: the attempt ran too long. | Give it more time, more compute, or less work. |
| `flyte.errors.DeadlineExceededError` | `deadline`: the total budget across all attempts ran out. | Usually give up, since the time budget is gone. |

Existing `except flyte.errors.TaskTimeoutError` handlers catch all three. A backend that doesn't report which
bound fired raises the base `flyte.errors.TaskTimeoutError`, so keep a handler for it if you need to support
older deployments.

## Handling GPU hardware faults (Xid errors)

GPUs fail in ways CPUs don't: a GPU can fall off the PCIe bus, hit an uncorrectable ECC error, or report an NVIDIA
**Xid** (or an NVSwitch **SXid**) that kills the process. When the platform attributes a task failure to one of
these faults, the parent receives a `flyte.errors.GPUFaultError`. It has two concrete subclasses, and they mean
very different things:

- `flyte.errors.GPUFaultUserError`: the workload caused the fault. User-severity Xids (13, 31, 43, 45) include
  out-of-bounds memory accesses and illegal instructions. The GPU is healthy once the process exits, but the same
  code will fault again. These faults count against the task's own retry budget, so by the time you see this
  error the task's retries are already used up. Fix the code, or change what you run (a different kernel,
  precision, or batch size); don't simply re-run it.
- `flyte.errors.GPUFaultSystemError`: the hardware failed, for example an uncorrectable ECC error, a GPU that
  fell off the bus, or an NVLink error. The platform retries these without charging your retry budget and
  reschedules onto other hardware where it can. You only see this error after the platform has given up, so
  retrying in place is unlikely to help. Move to a different GPU type, queue, or cluster instead.

Catch `flyte.errors.GPUFaultError` to handle both, then branch on the attributes:

| Attribute | Meaning |
|---|---|
| `code` | `GpuXidError` (catch-all), `GpuFallenOffBus`, `GpuEccUncorrectable`, `GpuRowRemapPending`, `GpuNvlinkError`, or `GpuGspError`. |
| `xid` / `sxid` | The NVIDIA Xid or NVSwitch SXid number. Only one is set, depending on `fault_kind`. |
| `fault_name` | A readable name for the fault. |
| `severity` | `"user"`, `"warn"`, or `"critical"`. |
| `node`, `gpu_uuid`, `gpu_index`, `pci_bus_id` | Where the fault happened. Useful when reporting bad hardware. |
| `process` | The process the driver attributed the fault to. |

Any of these attributes can be `None` if the platform didn't supply them, so read them defensively.

The following example puts the pieces together. It walks a list of GPU options and moves on when an option
can't be scheduled, when its hardware fails, or when the model doesn't fit in its memory. A fault caused by the
workload itself is re-raised, because a different GPU won't fix a bug:

```python
@driver.task
async def main(epochs: int = 3) -> str:
    for gpu in GPU_OPTIONS:
        resources = flyte.Resources(cpu=8, memory="64Gi", gpu=gpu)
        try:
            return await train.override(resources=resources)(epochs=epochs)
        except flyte.errors.MaxQueuedTimeExceededError:
            print(f"No {gpu} capacity, trying the next option")
        except flyte.errors.GPUFaultSystemError as e:
            print(f"{gpu} hardware fault {e.code} (xid={e.xid}) on node {e.node}, trying the next option")
        except flyte.errors.GPUFaultUserError as e:
            print(f"Workload fault {e.fault_name} (xid={e.xid}); a different GPU won't help")
            raise
        except flyte.errors.RuntimeUserError as e:
            if e.code != "OutOfMemoryError":
                raise
            print(f"Model doesn't fit on {gpu}, trying the next option")
    raise RuntimeError(f"No GPU option succeeded: {GPU_OPTIONS}")
```

Order matters: `GPUFaultUserError` and `MaxQueuedTimeExceededError` are both subclasses of `RuntimeUserError`, so
their clauses must come before the generic `RuntimeUserError` clause.

> [!NOTE] GPU fault errors depend on the platform
> These exceptions are raised only when the platform detected and classified the fault. On a platform or
> version that doesn't, the same failure arrives as an ordinary runtime error with no fault attributes. Don't
> depend on `GPUFaultError` firing: keep a handler for ordinary task failures as well.

## Handling the failure of a run you launched

A task (or a script) can also launch a whole *run* with `flyte.run` rather than calling a task as a sub-action,
for example to compose several independent runs into a larger pipeline. A sub-action failure raises in the
parent automatically. A run you launched doesn't, because `flyte.run` returns a `flyte.remote.Run` handle
immediately. Wait on the handle, then call `flyte.remote.Run.raise_for_status()`:

```python
run = await flyte.run.aio(train, epochs=3)
await run.wait.aio(quiet=True)
await run.raise_for_status.aio()   # Does nothing if the run succeeded.
result = (await run.outputs.aio())[0]
```

Like `requests.Response.raise_for_status`, it does nothing when the run succeeded. Otherwise it raises the same
exception that awaiting the task as a sub-action would have raised, so everything on this page applies to runs
too:

- A run that timed out raises the matching `flyte.errors.TaskTimeoutError` subclass, such as
  `flyte.errors.MaxQueuedTimeExceededError`.
- An aborted run raises `flyte.errors.ActionAbortedError`, including the abort reason.
- A failed run raises the error converted from its error code: `flyte.errors.OOMError`, a
  `flyte.errors.GPUFaultError` subclass, or a `flyte.errors.RuntimeUserError` carrying your exception's class name
  as its `code`.
- A run that hasn't finished raises `flyte.errors.RuntimeUserError` with code `RunNotDoneError`. Call `wait()`
  first.

Outside an async context, use the synchronous forms: `run.wait()` then `run.raise_for_status()`.

The capacity fallback from earlier works the same way at the run level. The following driver launches a
training run on an H100 and falls back to an A100 run if no H100 is scheduled in time:

```python
async def run_to_completion(task, run_name: str, **inputs) -> str:
    run = await flyte.with_runcontext(name=run_name).run.aio(task, **inputs)
    await run.wait.aio(quiet=True)
    await run.raise_for_status.aio()
    return (await run.outputs.aio())[0]


@flyte.trace
async def train_h100(run_name: str, epochs: int) -> str:
    return await run_to_completion(train, run_name, epochs=epochs)


@flyte.trace
async def train_a100(run_name: str, epochs: int) -> str:
    a100 = train.override(resources=flyte.Resources(cpu=8, memory="64Gi", gpu="A100 80G:1"))
    return await run_to_completion(a100, run_name, epochs=epochs)


@driver.task
async def main(epochs: int = 3) -> str:
    # Child run names derive from this run's name, so they stay the same across retries.
    prefix = flyte.ctx().action.run_name
    try:
        return await train_h100(f"{prefix}-h100", epochs)
    except flyte.errors.MaxQueuedTimeExceededError:
        return await train_a100(f"{prefix}-a100", epochs)
```

Wrapping each launch in `@flyte.trace` with a stable run name makes the driver safe to retry. A finished step
replays its recorded result or error. A step that was still waiting when the driver died launches again under
the same name, and creating a run with an existing name returns that run, so the driver waits on it rather than
starting a duplicate. For the full example, see
[`run_of_runs.py`](https://github.com/flyteorg/flyte-sdk/blob/main/examples/advanced/run_of_runs.py).

{{< variant union >}}
{{< markdown >}}

To send a child run to a different queue, pass `queue` when you launch it:
`flyte.with_runcontext(name=run_name, queue="gpu-a100").run.aio(task, **inputs)`.

{{< /markdown >}}
{{< /variant >}}

## Limiting inline I/O

Small task inputs and outputs are passed *inline* (embedded directly in the task's metadata) rather than offloaded
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
| `flyte.errors.TaskTimeoutError` | A task exceeds one of its `flyte.Timeout` bounds. The subclasses below say which one. |
| `flyte.errors.MaxQueuedTimeExceededError` | A task waits longer than `max_queued_time` to start, for example because no GPU is free. |
| `flyte.errors.MaxRuntimeExceededError` | A task attempt runs longer than `max_runtime`. |
| `flyte.errors.DeadlineExceededError` | A task doesn't finish within its `deadline`, across all attempts. |
| `flyte.errors.GPUFaultUserError` | The workload caused a GPU fault, such as Xid 31 (GPU memory page fault). |
| `flyte.errors.GPUFaultSystemError` | GPU hardware failed, such as an uncorrectable ECC error or a GPU that fell off the bus. |
| `flyte.errors.InlineIOMaxBytesBreached` | An input or output exceeds the task's `max_inline_io_bytes` limit. |
| `flyte.errors.RetriesExhaustedError` | A task fails after all of its automatic retries are used up. |
| `flyte.errors.TaskInterruptedError` | A task running on interruptible (spot) compute is preempted. |
| `flyte.errors.ActionAbortedError` | An action is aborted externally via the CLI, UI, or API. |
| `flyte.errors.ImagePullBackOffError` | The task's container image cannot be pulled. |
| `flyte.errors.NonRecoverableError` | A failure that should not be retried, regardless of the retry budget. |

All of these except `flyte.errors.GPUFaultSystemError` derive from `flyte.errors.RuntimeUserError`, so a single
`except flyte.errors.RuntimeUserError` catches them when you want uniform handling. `GPUFaultSystemError` is a
`flyte.errors.RuntimeSystemError`, because the hardware failed rather than your code; catch it separately, or
catch `flyte.errors.BaseRuntimeError` to handle everything. This is only a selection. For the complete catalog of
catchable exception classes, see the [`flyte.errors` API reference](../../../api-reference/flyte-sdk/flyte.errors/_index).

## Related pages

- [Retries and timeouts](../task-configuration/retries-and-timeouts): configure automatic retries and execution time limits.
- [Abort and cancel actions](./abort-tasks): stop actions programmatically or externally, and handle `flyte.errors.ActionAbortedError`.
