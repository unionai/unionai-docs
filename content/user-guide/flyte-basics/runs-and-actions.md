---
title: Runs and actions
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Runs and actions

When you execute a task on Flyte, the system creates a **run** to track it. Each individual task execution within that run is an **action**. Understanding this hierarchy helps you navigate the UI and debug your workflows.

## What is a run?

A **run** is the execution of a task that you directly initiate, plus all its descendant task executions, considered as a single unit.

When you execute:

```shell
flyte run my_script.py pipeline --x 5
```

Flyte creates a run for `pipeline`. If `pipeline` calls other tasks, those executions are part of the same run.

## What is an action?

An **action** is the execution of a single task, considered independently. A run consists of one or more actions.

Consider this workflow:

```python
@env.task
def step_one(x: int) -> int:
    return x * 2

@env.task
def step_two(x: int) -> int:
    return x + 10

@env.task
def pipeline(x: int) -> int:
    a = step_one(x)
    b = step_two(a)
    return b
```

When you run `pipeline(5)`:

- **1 run** is created for the entire execution
- **3 actions** are created: one for `pipeline`, one for `step_one`, one for `step_two`

## Runs vs actions in practice

| Concept | What it represents | In the UI |
|---------|-------------------|-----------|
| **Run** | Complete execution initiated by user | Runs list, top-level view |
| **Action** | Single task execution | Individual task details, logs |

For details on how to run tasks locally and remotely, see [Tasks](./tasks#running-tasks-locally).

## Viewing runs in the UI

After running a task remotely, click the URL in the output to see your run in the UI:

```shell
$ flyte run my_script.py pipeline --x 5
abc123xyz
https://my-instance.example.com/v2/runs/project/my-project/domain/development/abc123xyz
Run 'a0' completed successfully.
```

In the UI, you can:

- See the overall run status and duration
- Navigate to individual actions
- View inputs and outputs for each task
- Access logs for debugging
- See the execution graph

## Understanding the execution graph

The UI shows how tasks relate to each other:

```
pipeline (action)
├── step_one (action)
└── step_two (action)
```

Each box is an action. Arrows show data flow between tasks. This visualization helps you understand complex workflows and identify bottlenecks.

## Checking run status

From the command line:

```shell
# Get details of a specific run
flyte get run <run-id>
```

From Python:

```python
import flyte

flyte.init_from_config()
run = flyte.run(pipeline, x=5)

# The run object has status information
print(run.status)
```

## Next steps

You now understand tasks and how Flyte tracks their execution. Next, let's learn about [apps](./introducing-apps) - Flyte's approach to long-running services.
