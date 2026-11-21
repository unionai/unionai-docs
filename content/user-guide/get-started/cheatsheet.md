---
title: Cheatsheet
description: One-page reference for the most-used Flyte 2 SDK constructs and CLI commands, each linked to its full page.
icon: card-checklist
weight: 4
variants: +flyte +union
---

# Cheatsheet

This page lists the SDK constructs and CLI commands you use most often.
Each row links to the page that documents it in full.

## SDK constructs

| Construct | What it does | Full page |
|-----------|--------------|-----------|
| `flyte.TaskEnvironment(name="my-env", image=..., resources=...)` | Groups tasks that share a container image, resources, secrets, and cache settings. | [TaskEnvironment](./core-concepts/task-environment) |
| `@env.task` | Turns a sync or async Python function into a task that runs in `env`. | [Tasks](./core-concepts/tasks) |
| `flyte.map(my_task, items)` | Runs one task on every item of an iterable, in parallel, and yields the results in input order. In an async task, use `flyte.map.aio`. | [Mapping over inputs](../tasks/task-programming/map) |
| `await asyncio.gather(*[my_task(x) for x in items])` | Runs task calls in parallel from an async task. Use it to fan out across different tasks. | [Fanout](../tasks/task-programming/fanout) |
| `flyte.Image.from_debian_base().with_pip_packages("pandas")` | Defines the container image a task environment runs in. | [Container images](../tasks/task-configuration/container-images) |
| `flyte.Resources(cpu=1, memory="1Gi", gpu="A100:1")` | Requests CPU, memory, GPUs, and disk for a task environment or task. | [Resources](../tasks/task-configuration/resources) |
| `cache="auto"` | Reuses a task's earlier output when its inputs match. Set it on `TaskEnvironment` or `@env.task`. For more control, pass `flyte.Cache`. | [Caching](../tasks/task-configuration/caching) |
| `retries=3` | Retries a failed task attempt. Set it on `@env.task`. For backoff between attempts, pass `flyte.RetryStrategy`. | [Retries and timeouts](../tasks/task-configuration/retries-and-timeouts) |

## CLI commands

| Command | What it does | Full page |
|---------|--------------|-----------|
| `flyte run hello.py my_task --arg1 value1` | Runs a task from a Python file. Task arguments go after the task name. | [Run command options](../tasks/task-deployment/run-command-options) |
| `flyte run --local hello.py my_task` | Runs the task in your local Python process instead of on the backend. | [Run locally in Python](./run-modes/running-locally) |
| `flyte deploy hello.py my_env` | Deploys a task environment and its tasks. | [Deploy command options](../tasks/task-deployment/deploy-command-options) |
| `flyte deploy --all hello.py` | Deploys every task environment in a file. Add `--recursive` and pass a directory to deploy every environment under it. | [Deploy command options](../tasks/task-deployment/deploy-command-options) |
| `flyte get run [NAME]` | Lists runs, or shows one run's details. | [`flyte get run`](../../api-reference/flyte-cli#flyte-get-run) |
| `flyte get logs RUN_NAME [ACTION_NAME]` | Shows the logs of a run or one of its actions. | [`flyte get logs`](../../api-reference/flyte-cli#flyte-get-logs) |
| `flyte get io RUN_NAME [ACTION_NAME]` | Shows the inputs and outputs of a run or action. | [`flyte get io`](../../api-reference/flyte-cli#flyte-get-io) |
| `flyte create config --local-persistence` | Creates `.flyte/config.yaml` for the CLI. Pass at least one of `--endpoint`, `--org`, or `--local-persistence`. | [Quickstart](./quickstart#configure) |
| `flyte create secret MY_SECRET --value my_value` | Creates a secret. Without `--value`, the CLI prompts for the value. | [Secrets](../tasks/task-configuration/secrets) |

For every command and option, see the [Flyte CLI reference](../../api-reference/flyte-cli).
