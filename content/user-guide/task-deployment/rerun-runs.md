---
title: Re-run a run
weight: 14
variants: +flyte +union
---

# Re-run a run

Every run in {{< key product_name >}} is durable: its task, code, inputs, and configuration are all
recorded on the backend. That means you can launch a brand-new run from any previous one without
having the original code checked out locally. This is useful for retrying a transient failure,
reproducing a result, or tweaking a few inputs and running again.

You can re-run at two levels of granularity:

- **The whole run**: re-execute the entry point task (the `a0` action) and everything it calls.
- **A single action**: re-execute one nested action on its own.

And you can trigger a re-run from three places: the **UI**, the **CLI**, or **programmatically**
with the Python SDK.

## Re-run from the UI

### Re-run an entire run

Open the run in the UI. In the top-right corner of the run view, click **Rerun**.

This opens the launch form pre-filled with the original run's inputs, environment variables, and
code. You can either:

- Trigger the run as-is to reproduce the original execution exactly, or
- Edit the inputs, environment variables, and other launch settings in the form before triggering
  to run a variation.

### Re-run a single action

You can also re-run an individual action without re-running the whole workflow. Navigate to the
action in the run's action list, open its details view, and use the **Rerun action** option (in the
action menu in the top-right of the action details panel).

This launches a new run starting from that action, using the action's recorded inputs. As with a
full re-run, you can adjust the inputs in the launch form first.

## Re-run from the CLI

The CLI offers two complementary commands depending on whether you want the **original code** or
**new local code**.

### `flyte rerun`: re-run with the original code and inputs

`flyte rerun` fetches the prior run's task **and** inputs from the backend and launches a new run.
You don't need the original code checked out locally. Everything is pulled from the platform:

```bash
# Re-run with the prior run's exact code and inputs
flyte rerun <run-name>

# Give the new run a name and stream its parent-action logs
flyte rerun <run-name> --name retry-1 --follow
```

Common options:

| Option | Description |
|---|---|
| `-p`, `--project` | Project for the new run (defaults to your config). |
| `-d`, `--domain` | Domain for the new run (defaults to your config). |
| `--name` | Name for the new run (a random name is generated if unset). |
| `-e`, `--env KEY=VALUE` | Override an environment variable for the new run. Repeatable. |
| `--label KEY=VALUE` | Set a label on the new run. Repeatable. |
| `-f`, `--follow` | Stream the parent action's logs after launch. |

> [!NOTE]
> `flyte rerun` reuses the prior run's inputs as-is. To change input values from the command line,
> use the programmatic `flyte.rerun(<run-name>, key=value)` form shown below.

### `flyte run --rerun-from`: re-run with new local code

When you've changed your code locally but want to reuse a prior run's inputs, use `flyte run` with
the `--rerun-from` flag. This deploys **your local code** and feeds it the inputs from the prior
run, so you don't need to re-specify any per-task input flags:

```bash
flyte run --rerun-from <run-name> main.py main
```

`--rerun-from` is remote-only; it cannot be combined with `--local`.

### Choosing between the two

| Command | Code | Inputs |
|---|---|---|
| `flyte run <file> <task>` | local | from CLI |
| `flyte run --rerun-from <run> <file> <task>` | local | prior run's |
| `flyte rerun <run>` | fetched from backend | prior run's |

## Re-run programmatically

Use `flyte.rerun()` to re-run from Python. Like the CLI, it fetches the prior run's task and inputs
from the backend, so no local code is required:

```python
import flyte

flyte.init_from_config()

# Re-run a prior run with its exact inputs (task + inputs fetched from the platform):
flyte.rerun("ul56wcvgqrb9vzhzz5l2")

# Change input parameters — they are converted against the prior run's interface:
flyte.rerun("ul56wcvgqrb9vzhzz5l2", x_list=[1, 2, 3])

# Substitute new code while reusing the original run's inputs:
flyte.rerun("ul56wcvgqrb9vzhzz5l2", task_template=fixed_task)
```

`flyte.rerun()` returns a `flyte.remote.Run`, just like `flyte.run()`, so you can monitor it, wait
on it, and retrieve its outputs in the same way. See
[Interact with runs and actions](./interacting-with-runs) for details.

To control launch settings (name, project, domain, environment variables, labels) use
`flyte.with_runcontext(...).rerun(...)`:

```python
flyte.with_runcontext(
    name="retry-1",
    env_vars={"LOG_LEVEL": "20"},
).rerun("ul56wcvgqrb9vzhzz5l2")
```

## Related

- [Interact with runs and actions](./interacting-with-runs): retrieve, monitor, and inspect runs and actions.
- [Run command options](./run-command-options): the full set of `flyte run` options.
