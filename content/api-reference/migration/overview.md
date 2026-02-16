---
title: Philosophy and imports
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Philosophy and imports

## Key paradigm shifts

| Concept | Flyte 1 (flytekit) | Flyte 2 (flyte) |
|---------|--------------|------------|
| Workflow definition | `@workflow` decorator (DSL-constrained) | Tasks calling tasks (pure Python) |
| Task configuration | Per-task decorator parameters | `TaskEnvironment` (shared config) |
| Parallelism | `map_task()` function | `flyte.map()` or `asyncio.gather()` |
| Conditionals | `flytekit.conditional()` | Native Python `if/else` |
| Error handling | Decorator-based retries | Python `try/except` + retries |
| Execution model | Static DAG compilation | Dynamic pure Python execution |

## What Flyte 2 eliminates

- **`@workflow` decorator**: No longer exists. Workflows are just tasks that call other tasks.
- **`@dynamic` decorator**: No longer needed. All tasks can have dynamic behavior.
- **DSL constraints**: No more restrictions on what Python constructs you can use.
- **Separate workflow/task execution contexts**: Everything runs as a task.

## What Flyte 2 introduces

- **`TaskEnvironment`**: Centralized configuration for groups of tasks.
- **Native async support**: First-class `async/await` with distributed execution.
- **`flyte.map()`**: Simplified parallel execution with generator support.
- **`Trigger`**: Task-based scheduling (replaces LaunchPlan schedules).
- **Pure Python workflows**: Full Python flexibility in orchestration logic.

For more on the pure Python model, see [Pure Python](../../user-guide/flyte-2/pure-python).
For more on the async model, see [Asynchronous model](../../user-guide/flyte-2/async).

## Package imports

### Basic import changes

{{< tabs "migration-imports" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
import flytekit
from flytekit import task, workflow, dynamic, map_task
from flytekit import ImageSpec, Resources, Secret
from flytekit import current_context, LaunchPlan, CronSchedule
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
import flyte
from flyte import TaskEnvironment, Resources, Secret
from flyte import Image, Trigger, Cron
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Import mapping table

| Flyte 1 import | Flyte 2 import | Notes |
|-----------|-----------|-------|
| `flytekit.task` | `env.task` | Decorator from TaskEnvironment |
| `flytekit.workflow` | `env.task` | Workflows are now tasks |
| `flytekit.dynamic` | `env.task` | All tasks can be dynamic |
| `flytekit.map_task` | `flyte.map` / `asyncio.gather` | Different API |
| `flytekit.ImageSpec` | `flyte.Image` | Different API |
| `flytekit.Resources` | `flyte.Resources` | Similar API |
| `flytekit.Secret` | `flyte.Secret` | Different access pattern |
| `flytekit.current_context()` | `flyte.ctx()` | Different API |
| `flytekit.LaunchPlan` | `flyte.Trigger` | Different concept |
| `flytekit.CronSchedule` | `flyte.Cron` | Used with Trigger |
| `flytekit.conditional` | Native `if/else` | No longer needed |
