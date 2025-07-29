---
title: Migration
weight: 13
variants: +flyte +serverless +byoc +selfmanaged
---

# Migration from Flyte 1 to Flyte 2

> [!NOTE]
> Automated migration from Flyte 1 to Flyte 2 is coming soon.

Flyte 2 will soon offer automated migration from Flyte 1 to 2.

In the meantime you can migrate manually by following the steps below.:

### 1. Move task configuration to a `TaskEnvironment` object

- Instead of configuring the image, hardware resources and so forth direcly in the task decorator.
You configure it in `TaskEnvironment` object. For example:

```python

env = flyte.TaskEnvironment(
    name="my_task_env",
    image="docker.io/myorg/myimage:latest"
)
```

### 2. Replace workflow decorators

Then, you replace the `@workflow` and `@task` decorators with `@env.task` decorators,

```python
# Flyte 1
@workflow
def my_workflow(data: List[str]) -> List[str]:
    return [process_item(item=item) for item in data]

# Flyte 2
@env.task
async def my_workflow(data: List[str]) -> List[str]:
    tasks = [process_item.aio(item) for item in data]
    return await asyncio.gather(*tasks)
```

Note that the reason our task decorator uses `env` is simply because that is the variable to which we assigned
the `TaskEnvironment` above.

### 3. Adopt async patterns

- Use `asyncio.gather()` or `flyte.map()` for parallel execution
- Add `async`/`await` keywords where you want parallelism
- Keep existing sync task functions unchanged

### 4. Leverage enhanced capabilities

- Add conditional logic and loops within workflows
- Implement proper error handling with try/except
- Create dynamic workflows that adapt to runtime conditions