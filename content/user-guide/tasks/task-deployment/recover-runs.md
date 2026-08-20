---
title: Recover a failed run
weight: 15
variants: +flyte +union
mermaid: true
---

# Recover a failed run

When a run fails partway through, most of its work is usually still good. **Recovery** launches a
new run that reuses the successful actions from a previous one and re-executes only what failed.
A reused action is not executed again at all: its recorded output is handed straight to whatever
consumes it.

This is the difference between recovery and a plain [re-run](./rerun-runs): a re-run starts the
whole run over from the beginning, while a recovery picks up where the failure left off.

Recovery is one of two behaviours of the same verb, `flyte rerun`. It is remote-only: rerun and
recover are not supported in local mode.

## What a recovery reuses

Given a run whose `summarize` task failed, leaving its downstream `report` task unreached:

```mermaid
flowchart LR
    subgraph src["Source run"]
        s1["prepare ×6<br/>succeeded"] --> s2["process ×6<br/>succeeded"] --> s3["summarize<br/>failed"] --> s4["report<br/>never ran"]
    end
    subgraph rec["Recovery run"]
        r1["prepare ×6<br/>reused"] --> r2["process ×6<br/>reused"] --> r3["summarize<br/>re-executed"] --> r4["report<br/>ran"]
    end
    s1 -. "matched by action name" .-> r1
    s2 -.-> r2
    s3 -.-> r3
    s4 -.-> r4
```

The parent task that issues these calls always re-executes, since it is the code that re-drives
the graph. Its children are then matched one at a time as it calls them.

## How this differs from caching

Caching and recovery both skip work that has already been done, but they are keyed on different
things, and they are not alternatives to one another.

Caching is **content-addressed**. A task's cache key comes from its inputs, name, interface, and
cache version, so a hit can be served to any run at any time, subject to the lookup scope. You opt
in per task, in code, and `flyte.TaskEnvironment` defaults to caching disabled.

Recovery is **scoped to a single run**. It reuses what one named run produced, at the position in
the graph where that run produced it. You opt in per run, at launch, and no task has to be marked
as anything beforehand.

| | Caching | Recovery |
|---|---|---|
| Keyed on | inputs and task version | the source run, plus the action's position within it |
| Reuse comes from | any prior run in the lookup scope | the one run you name |
| Enabled | per task, in code (off by default) | per run, at launch |
| Two identical calls in one run | the second is a cache hit | both remain distinct actions |

Three practical consequences follow:

- **Recovery needs no preparation.** A task that was never marked cacheable is recovered anyway,
  which is usually the situation you are in when a long run fails.
- **Each one makes a different claim.** Marking a task cached asserts that it is a pure function of
  its inputs, for every future run. Recovery asserts only that one run's result at one point is
  still good, so it can reuse output from tasks that would not be safe to cache at all.
- **They are independent.** Caching applies on any run, including a recovery run; recovery covers
  the actions caching does not. A recovered action is reported in its own terminal phase, distinct
  from an action that succeeded by executing.

## One verb, two behaviours

`flyte rerun` fetches the prior run's task spec and inputs from the platform. No local code is
involved, and nothing you edit locally is picked up.

| Call | What happens |
|---|---|
| `flyte rerun <run>` | A whole new run with the same inputs. Every action executes again, subject to global caching. |
| `flyte rerun <run> --recover` | A whole new run with the same inputs, but actions that already succeeded are reused as-is. Only what failed or never ran executes. |

Recovery is durability against *intermittent* failures, not a way to patch a run. It replays the
source run's code and inputs as-is, and the run environment (`-e KEY=VALUE`) is the only lever you
get. Combining `--recover` with changed inputs raises: change inputs on a plain rerun instead.

{{< variant union >}}
{{< markdown >}}

To replay a run with *new* code, see [Fork a run with new code](#fork-a-run-with-new-code) below.

{{< /markdown >}}
{{< /variant >}}

## Recover from the CLI

```bash
flyte rerun <run-name> --recover --follow
```

| Option | Description |
|---|---|
| `--recover` | Reuse the prior run's succeeded actions, re-running only what failed or never ran. |
| `--action-name <action>` | Re-run only this action, rooted at its task with the inputs it received. Cannot be combined with `--recover`. |
| `--force-rerun-action <action>` | With `--recover`, re-execute an action even though it succeeded in the source run. Repeatable. |
| `--allow-missing-outputs` | Proceed when the source run's outputs have been cleaned up from storage. |
| `-e`, `--env KEY=VALUE` | Set an environment variable on the new run. Repeatable. |

Action names are deterministic hashes rather than positions, so list them with
`flyte get action <run-name>` and copy the one you want. A listed parent re-enqueues its children,
so list those too to force a whole subtree; unknown names are ignored.

Reused actions land in the `RECOVERED` phase, which is terminal and success-equivalent, so
`flyte get action <run-name>` tells you exactly what recovery skipped.

Because recovery matches succeeded actions by name, and a run rooted at a single action has a
different action tree, `--action-name` cannot be combined with `--recover`.

## Recover programmatically

`flyte.rerun()` takes the same arguments the CLI exposes:

```python
import flyte

flyte.init_from_config()

# Re-run everything with the prior run's inputs:
flyte.rerun("<run-name>")

# Reuse the succeeded actions, re-running only what failed or never ran:
flyte.rerun("<run-name>", recover=True)

# Force specific actions to re-execute even though they succeeded:
flyte.rerun("<run-name>", recover=True, force_rerun_actions=["a3", "a7"])

# Re-run a single action, rooted at its task with the inputs it received:
flyte.rerun("<run-name>", action_name="a3")
```

`allow_missing_source_outputs=True` is the programmatic equivalent of `--allow-missing-outputs`.
Launch settings still come from `flyte.with_runcontext()`:

```python
flyte.with_runcontext(name="retry-1", env_vars={"LOG_LEVEL": "20"}).rerun("<run-name>", recover=True)
```

Task inputs share the keyword namespace with those arguments, so a task input named `run_name`,
`action_name`, `recover` or `force_rerun_actions` cannot be passed this way.

{{< variant union >}}
{{< markdown >}}

## Fork a run with new code

Recovery deliberately refuses to substitute your code. `fork` is the verb that does, and it is
the Union half of the pair: go back to a run, change code, and replay only what that change
affects.

```bash
flyte fork <run-name> main.py main
```

A fresh code bundle is built from your working tree, so actions whose code changed re-execute
while everything that succeeded and is unchanged is reused.

| Command | Code | Actions |
|---|---|---|
| `flyte rerun <run>` | the source run's | everything re-executes |
| `flyte rerun <run> --recover` | the source run's | succeeded actions reused |
| `flyte fork <run> <file> <task>` | **yours** | succeeded actions reused |

```mermaid
flowchart LR
    R["Source run<br/>(failed)"] -- "same code<br/>everything re-runs" --> A["flyte rerun"]
    R -- "same code<br/>reuse succeeded" --> B["flyte rerun --recover"]
    R -- "reuse succeeded" --> C["flyte fork"]
    L["Your working tree"] -- "new code" --> C
```

Inputs always come from the source run, so `flyte fork` takes no task inputs. Replaying a run
with changed inputs is a separate feature and is not implemented. Forking is remote-only: there
is no local equivalent.

`--force-rerun-action` works here too, forcing an action to re-execute even though it succeeded:

```bash
flyte fork --force-rerun-action a3 <run-name> main.py main
```

`flyte run`'s options (image, copy-style, service account, env, labels, queue) come before the
run name. In Python the verb is imported from the plugin:

```python
from flyteplugins.union import fork, with_forkcontext

fork("<run-name>", task_template=main)
with_forkcontext(name="fix-1").fork("<run-name>", task_template=main)
```

`with_forkcontext()` accepts the same keyword arguments as `flyte.with_runcontext()` and returns
a runner that can also `fork()`.

## How actions are matched

Recovery matches actions from the source run **by action name**, and action names are computed
rather than assigned:

```mermaid
flowchart LR
    tn["task name"] --> TI["task identity"]
    ih["interface hash"] --> TI
    fb["hash of the task<br/>function's own body"] --> TI

    TI --> AN["action name"]
    pan["parent action name"] --> AN
    inh["inputs hash"] --> AN
    seq["call sequence"] --> AN
    grp["group"] --> AN

    ex["image · resources<br/>env vars · code bundle"] -. "not included" .-x AN
```

Two properties follow from this, and they explain nearly everything about recovery behavior:

- **Deployment details are excluded on purpose.** Changing a task's resources or image does not
  rename its action, so the rest of the run stays reusable. Raising the memory on a task that hit
  `flyte.errors.OOMError` and recovering does exactly what you would hope: the successful upstream
  is reused, and the failed task re-executes with its new limit.
- **Matching follows the data.** Because a child's name folds in its inputs hash, an upstream task
  that re-executes but produces *identical* outputs leaves its downstream actions matchable, and
  they are still reused.

### What re-runs after a code change

| You change | On recovery |
|---|---|
| A task's function body | that task re-runs |
| A task's signature | that task re-runs |
| A task's docstring | that task re-runs |
| The task function's name | that task re-runs |
| The `flyte.TaskEnvironment` name | every task in it re-runs |
| Comments inside a task | reused |
| Formatting or whitespace | reused |
| `flyte.Resources` (cpu, memory) | reused |
| The image, or added packages | reused |
| A module-level constant a task reads | reused (see below) |
| A helper function a task calls | reused (see below) |

> [!WARNING] Identity is the function body, and only the function body
> A task's identity hashes only the decorated function's own source. If you edit a module-level
> constant it reads, or a helper function it calls, the action name does not change, so a task
> that already succeeded is reused and your change has no effect on it. Nothing warns you.
>
> Use `--force-rerun-action` to re-execute those actions explicitly, or move the changed logic
> into the task body.

The same rule governs `flyte.trace` functions: a traced function hashes its own body, so editing it
causes it to re-execute instead of replaying its recorded result. A helper it calls still does
not count as a change.

Runs launched from a notebook or with a pickled code bundle behave differently: they version on the
bundle itself, so any code change renames every action and nothing is reused.

{{< /markdown >}}
{{< /variant >}}

## Related

- [Re-run a run](./rerun-runs): launch a fresh run from a previous one, without reusing its actions.
- [Interact with runs and actions](./interacting-with-runs): retrieve, monitor, and inspect runs and actions.
- [Run command options](./run-command-options): the full set of `flyte run` options.
{{< variant union >}}
{{< markdown >}}
- [Debug a run](./debug-runs): inspect a failure before deciding how to recover from it.
{{< /markdown >}}
{{< /variant >}}
