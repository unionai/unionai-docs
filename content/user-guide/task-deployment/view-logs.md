---
title: View logs
weight: 3
variants: +flyte +union
---

# View logs

Every action in a run captures the logs its task emits while executing.
Because Flyte is a durable execution engine, these logs are persisted per action and per attempt, so you can retrieve them while a run is in progress or after it has reached a terminal state.

There are two ways to view logs:

- **The CLI** — stream logs for a run or a specific action with `flyte get logs`.
- **The console** — open the run in the UI and inspect logs on any of its actions.

## Stream logs with the CLI

Use `flyte get logs` to stream the logs for a run or action:

```bash
flyte get logs <run_name> [<action_name>]
```

If you provide only the run name, Flyte streams the logs for the run's parent (main) action:

```bash
flyte get logs my_run
```

To see the logs for a specific action within the run, provide the action name as the second argument. Action names such as `a0` (the main action) and `a1`, `a2`, … (nested actions) identify each task execution in the run — see [Interact with runs and actions](./interacting-with-runs#understanding-runs-and-actions):

```bash
flyte get logs my_run a0
```

### Raw vs. pretty output

By default, logs are shown in raw format and scroll the terminal as they arrive.

To instead tail the logs in an auto-scrolling box that shows only the most recent lines, pass `--pretty`. Use `--lines`/`-l` to set how many lines the box keeps in view (default `30`); this limit only applies in pretty mode:

```bash
flyte get logs my_run a0 --pretty --lines 50
```

To prepend a timestamp to each log line, add `--show-ts`:

```bash
flyte get logs my_run a0 --show-ts
```

## View the logs for a specific attempt

An action can run more than once: Flyte records a separate attempt for each user-configured retry and for each automatic system retry (see [Key concepts](./interacting-with-runs#key-concepts)).

By default, `flyte get logs` shows the logs for the **latest** attempt. To inspect an earlier attempt, pass its number with `--attempt`/`-a`:

```bash
flyte get logs my_run a0 --attempt 1
```

## Filter out system logs

Alongside your task's own output, the logs include system messages emitted by the Flyte runtime. To hide those and show only the logs produced by your task, pass `--filter-system`:

```bash
flyte get logs my_run a0 --filter-system
```

## Scope to a project and domain

Like other `flyte get` commands, `flyte get logs` resolves the run within your configured [project and domain](../core-concepts/projects-and-domains). Override them for a single invocation with `--project`/`-p` and `--domain`/`-d`:

```bash
flyte get logs my_run a0 --project my-project --domain development
```

## Command options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--lines`, `-l` | integer | `30` | Number of lines to show; only applies with `--pretty`. |
| `--show-ts` | boolean | `False` | Show timestamps. |
| `--pretty` | boolean | `False` | Show logs in an auto-scrolling box, limited to `--lines` lines. |
| `--attempt`, `-a` | integer | latest | Attempt number to show logs for; defaults to the latest attempt. |
| `--filter-system` | boolean | `False` | Filter all system logs from the output. |
| `--project`, `-p` | text | configured | Project to which this command applies. |
| `--domain`, `-d` | text | configured | Domain to which this command applies. |

For the full command reference, see [`flyte get logs`](../../api-reference/flyte-cli#flyte-get-logs).

## View logs in the console

Logs are also available in the {{< key product_name >}} console. Open the run — the `url` attribute of a `flyte.remote.Run` gives its console link:

```python
import flyte

flyte.init_from_config()

run = flyte.remote.Run.get("my_run")
print(run.url)  # Console URL for the run
```

From the run view, select an action to see its logs, phases, inputs, and outputs. Each attempt of an action has its own logs, as with the CLI.

> [!NOTE]
> The exact log-viewing controls in the console depend on your deployment and console version. If the layout differs from what is described here, verify the current behavior in your live console.

## Related

- [Interact with runs and actions](./interacting-with-runs) — retrieve runs, actions, inputs, and outputs.
- [Flyte CLI reference](../../api-reference/flyte-cli#flyte-get-logs) — the complete `flyte get logs` reference.
{{< variant union >}}
{{< markdown >}}
- [Debug a run](./debug-runs) — use logs and run information to diagnose failures.
{{< /markdown >}}
{{< /variant >}}
