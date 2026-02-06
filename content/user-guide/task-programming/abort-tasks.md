---
title: Abort and cancel actions
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Abort and cancel actions

When running complex workflows, you may need to stop actions that are no longer needed.
This can happen when one branch of your workflow makes others redundant, when a task fails and its siblings should not continue, or when you need to manually intervene in a running workflow.

Flyte provides three mechanisms for stopping actions:

- **Automatic cleanup**: When a root action completes, all its in-progress descendant actions are automatically aborted.
- **Programmatic cancellation**: Cancel specific `asyncio` tasks from within your workflow code.
- **External abort**: Stop individual actions via the CLI, the UI, or the API.

For background on runs and actions, see [Runs and actions](../../core-concepts/runs-and-actions).

## Action lifetime

The lifetime of all actions in a [run](../../core-concepts/runs-and-actions) is tied to the lifetime of the root action (the first task that was invoked).
When the root action exits—whether it succeeds, fails, or returns early—all in-progress descendant actions are automatically aborted and no new actions can be enqueued.

This means you don't need to manually clean up child actions. Flyte handles it for you.

Consider this example where `main` exits after 10 seconds, but it has spawned a `sleep_for` action that is set to run for 30 seconds:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/abort-tasks/action_lifetime.py" lang="python" >}}

When `main` returns after 10 seconds, the `sleep_for` action (which still has 20 seconds remaining) is automatically aborted.
The `sleep_for` task receives an `asyncio.CancelledError`, giving it a chance to handle the cancellation gracefully.

## Canceling actions programmatically

As a workflow author, you can cancel specific in-progress actions by canceling their corresponding `asyncio` tasks.
This is useful in scenarios like hyperparameter optimization (HPO), where one action converges to the desired result and the remaining actions can be stopped to save compute.

To cancel actions programmatically:

1. Launch actions using `asyncio.create_task()` and retain references to the returned task objects.
2. When the desired condition is met, call `.cancel()` on the tasks you want to stop.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/abort-tasks/cancel_tasks.py" lang="python" >}}

In this code:

* The `main` task launches 30 `sleepers` actions in parallel using `asyncio.create_task()`.
* It then calls `failing_task`, which raises a `ValueError`.
* The error is caught as a `flyte.errors.RuntimeUserError` (since user-raised exceptions are wrapped by Flyte).
* On catching the error, `main` cancels all sleeping tasks by calling `.cancel()` on each one, freeing their compute resources.

This pattern lets you react to runtime conditions and stop unnecessary work. For more on handling errors within workflows, see [Error handling](./error-handling).

## External abort

Sometimes you need to stop an action manually, outside the workflow code itself. You can abort individual actions using the CLI, the UI, or the API.

When an action is externally aborted, the parent action that awaits it receives a [`flyte.errors.ActionAbortedError`](../../api-reference/flyte-sdk/packages/flyte.errors/actionabortederror). You can catch this error to handle the abort gracefully.

### Aborting via the CLI

To abort a specific action:

```shell
flyte abort <run-name> <action-name>
```

### Handling external aborts

When using `asyncio.gather()` with `return_exceptions=True`, externally aborted actions return an `ActionAbortedError` instead of raising it. This lets you inspect results and handle aborts on a per-action basis:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/abort-tasks/external_abort.py" lang="python" >}}

In this code:

* The `main` task launches 10 `long_sleeper` actions in parallel.
* If any action is externally aborted (via the CLI, the UI, or the API) while running, `asyncio.gather` captures the `ActionAbortedError` as a result instead of propagating it.
* The `main` task iterates over the results and logs which actions were aborted.
* Because the abort is handled, `main` can continue executing and return its result normally.

Without `return_exceptions=True`, an external abort would raise `ActionAbortedError` directly, which you can handle with a standard `try...except` block.
