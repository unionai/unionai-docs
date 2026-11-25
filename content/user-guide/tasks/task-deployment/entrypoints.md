---
title: Entrypoint tasks
description: Mark the tasks meant to be launched directly, so the task list stays readable as a project grows.
icon: door-open
weight: 11
variants: +flyte +union
---

# Entrypoint tasks

As a project grows, the number of deployed tasks in a project/domain grows with it. Every `@env.task` you deploy shows up as a flat entry in the **Tasks list** alongside every other task, including internal helpers, leaf tasks, and intermediate steps that users aren't meant to invoke directly. Finding the handful of tasks that are actually meant to be *run* becomes a navigation problem.

{{< variant union >}}
{{< markdown >}}

**Entrypoint tasks** solve this by letting you mark which tasks in an environment are the ones intended to be invoked by humans or other services. It's a purely declarative hint: it doesn't change how the task executes.

{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

**Entrypoint tasks** let you mark which tasks in an environment are the ones intended to be invoked by humans or other services. It's a purely declarative hint: it doesn't change how the task executes.

{{< /markdown >}}
{{< /variant >}}

## When to use entrypoints

Mark a task as an entrypoint when:

{{< variant union >}}
{{< markdown >}}

- **It is meant to be run directly**, by a user, a teammate, or a service, rather than only being called from another task.
- **You want it to be discoverable** in the ways listed under [Discover entrypoint tasks](#discover-entrypoint-tasks).
- **You are sharing tasks with team members** and want the "start here" tasks to stand out from internal helpers.

{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

- **It is meant to be run directly**, by a user, a teammate, or a service, rather than only being called from another task.
- **You are sharing tasks with team members** and want to record in the code which tasks are the "start here" tasks.

{{< /markdown >}}
{{< /variant >}}

Conversely, don't mark a task as an entrypoint if it only exists as a subtask called by another task, or if it's a utility helper not intended to be invoked on its own.

> [!NOTE]
> Entrypoints and [triggers](../../triggers/_index) solve related but distinct problems. A **trigger** automates *when* a task runs (on a schedule, on an event). An **entrypoint** declares *which* tasks are meant to be run at all. A task can be both: a scheduled entrypoint is simply a named starting point that also runs on a cron.

## Mark a task as an entrypoint

Pass `entrypoint=True` to the `@env.task` decorator:

```python
import flyte

env = flyte.TaskEnvironment(
    name="hello_world",
    resources=flyte.Resources(cpu=1, memory="1Gi"),
)

@env.task
async def square(i: int) -> int:
    return i * i

@env.task(entrypoint=True)
async def say_hello_nested(data: str = "default string", n: int = 3) -> str:
    vals = [await square(i=i) for i in range(n)]
    return f"Hello {data} {vals}"
```

Here `say_hello_nested` is the intended starting point; `square` is an internal helper that `say_hello_nested` calls. Both get deployed, but only `say_hello_nested` is marked as an entrypoint.

The flag is also available on `task.override()`, so you can promote or demote a task as an entrypoint at invocation time without editing the source:

```python
promoted = square.override(entrypoint=True)
```

The default is `entrypoint=False`. If you don't mark anything, nothing is treated as an entrypoint.

## Discover entrypoint tasks

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> The open-source Flyte backend ignores the entrypoint filter. `flyte get task --entrypoint` and `flyte.remote.Task.listall(entrypoint=True)` list every task there, not only entrypoints.

{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

Once deployed, entrypoint tasks can be surfaced in three ways.

### CLI

Filter `flyte get task` to only entrypoint tasks:

```bash
flyte get task --entrypoint
```

This lists the tasks in the configured project/domain that were deployed with `entrypoint=True`, up to `--limit` tasks (100 by default).

### Programmatic

Pass `entrypoint=True` to `flyte.remote.Task.listall()`:

```python
import flyte

flyte.init_from_config()

for task in flyte.remote.Task.listall(entrypoint=True):
    print(task.name, task.version)
```

This is useful for building your own catalogs, dashboards, or tooling on top of the Flyte API.

### UI

The **Tasks list** in the UI has an **entrypoints** toggle that filters the view to only tasks marked as entrypoints. Use this when you're browsing a project and want to see only the tasks meant to be run.

{{< /markdown >}}
{{< /variant >}}
