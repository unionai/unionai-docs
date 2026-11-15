---
title: Fork a run
description: Replay a prior run with your current code and inputs, reusing what still holds.
icon: signpost-split
weight: 16
variants: -flyte +union
mermaid: true
---

# Fork a run

Forking replays a prior run with the code and inputs you have **now**: the actions that succeeded
are reused, and the ones you changed re-execute. It is time-travel debugging for a pipeline. Go
back to a run, change a task or an input, and re-run only what that change actually affects.

```bash
flyte fork <run-name> main.py main
```

A fresh code bundle is built from your working tree, so nothing about the source run's code is
replayed except where it is unchanged.

> [!NOTE] Availability
> `flyte fork` ships in `flyteplugins-union` 0.8.1 and later (`pip install flyteplugins-union`),
> alongside `flyte` 2.6.5. It is remote-only: forking a run has no local equivalent.
> `--task-action-inputs` and `--target-action` require `flyteplugins-union` 0.21.1 and `flyte`
> 2.13.4 or later, both where you fork and in the image of every task in the run, and a Union.ai
> backend that supports action overrides.

## How it relates to rerun and recover

[Recovery](./recover-runs) deliberately refuses to substitute your code, because it exists to
survive infrastructure failures rather than to patch a run. Fork is the verb that does substitute
it, and the three form a progression:

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

Fork can also change the root action's inputs, or the inputs of any task action inside the run.
The substitute code is optional too: `fork(run, threshold=0.9)` with no `task_template` replays the
source run's task spec against new inputs, which makes fork the way to recover a run with different
inputs. On the CLI the file and task can be left out only when you pass `--task-action-inputs`.

## Fork from the CLI

`flyte fork` takes the run first, then the file and task (optional with `--task-action-inputs`).
`flyte run`'s options (image, copy style, service account, env, labels, queue) come before the run
name:

```bash
flyte fork <run-name> main.py main
flyte fork --name fix-1 --env LOG_LEVEL=debug <run-name> main.py main
```

`--force-rerun-action` forces an action to re-execute even though it succeeded in the source run:

```bash
flyte fork --force-rerun-action a3 <run-name> main.py main
```

List action names with `flyte get action <run-name>`. A listed parent re-enqueues its children, so
list those too to force a whole subtree; unknown names are ignored.

### Changing inputs

The task's inputs become options, built from the signature in your local code. They are optional
and carry no defaults: an input you leave out keeps the source run's value, so changing one input
of a five-input task is one flag rather than five. Booleans take `--x/--no-x` so either value stays
expressible, and unknown input names are rejected up front.

```bash
flyte fork <run-name> main.py main --threshold 0.9
```

> [!WARNING] Recovered actions keep their original outputs
> An action reused from the source run keeps the output it produced under the **original** inputs.
> Fork does not recompute it against the new ones. Name the actions that must re-execute in
> `--force-rerun-action`.

When the inputs you pass cover the whole interface, the source run's inputs are never fetched, so a
run whose inputs have been cleaned up from storage can still be forked.

### Changing the inputs of actions inside the run

`--task-action-inputs` sets new inputs on specific task actions, as JSON keyed by action name, or
`@` followed by the path of a JSON file. Without a file and task, the fork replays the source run's
code:

```bash
flyte fork <run-name> --task-action-inputs '{"a3": {"learning_rate": 0.01}}'
flyte fork <run-name> --task-action-inputs @overrides.json main.py main
```

Each overridden action re-runs with its new inputs, and so does everything that consumes its
outputs. Its ancestors re-run to call it again, without the task cache. Everything else is
recovered from the source run. Inputs you leave out keep the value the forked run computes. The
key `a0` is the root action, the same as passing its inputs as options.

Every action name must be a task action of the source run, and every input must be on that
action's interface; otherwise the fork is refused before anything is submitted. Values convert the
way `flyte run` JSON inputs do (ints for floats, ISO dates, enums by member name, dataclasses as
objects). For `File` and `Dir` inputs, pass a remote URI, or a local path that is uploaded when the
fork is submitted; a local directory must be non-empty and contain no subdirectories. `DataFrame`
inputs take a remote URI.

The fork logs a warning when an override may not apply: when it is nested under another overridden
action, or when you also change the root inputs. Either can rename the overridden action, and
actions are matched by name.

### Changing one action's code

`--target-action` applies your local code to one task action instead of the whole run. That action
and the tasks it calls run your code; every other action keeps the source run's code. The task you
name must be the one that action runs, and its input options set that action's inputs:

```bash
flyte fork <run-name> --target-action a2 main.py train
flyte fork <run-name> --target-action a2 --task-action-inputs '{"a3": {"x": 1}}' main.py train
```

Only the action's code is replaced. Its interface, image, resources, cache settings and retries
still come from its parent's copy of the task, so a local change to the task's interface is
refused: fork the whole run instead. The target action re-runs without the task cache.

## Fork programmatically

```python
from flyteplugins.union import fork, with_forkcontext

fork("<run-name>", task_template=main)                          # new code
fork("<run-name>", task_template=main, threshold=0.9)           # new code and inputs
fork("<run-name>", threshold=0.9)                               # source code, new inputs
fork("<run-name>", task_template=main, force_rerun_actions=["a3"])
fork("<run-name>", task_action_inputs={"a3": {"learning_rate": 0.01}})  # one action's inputs
fork("<run-name>", task_template=train, target_action="a2")            # one action's code
```

`task_action_inputs` and `target_action` follow the same rules as `--task-action-inputs` and
`--target-action`, and have the same requirements. With `target_action`, keyword inputs are that
action's inputs.

`with_forkcontext()` accepts the same keyword arguments as `flyte.with_runcontext()` and returns a
runner that can also `fork()`:

```python
with_forkcontext(name="fix-1", env_vars={"LOG_LEVEL": "debug"}).fork("<run-name>", task_template=main)
```

## What re-executes

A fork reuses an action when its **action name** matches one that succeeded in the source run,
unless it is forced to re-run (`--force-rerun-action`, an action whose inputs or code you override,
and that action's ancestors). Action names are computed rather than assigned:

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

Two properties follow, and they explain nearly everything about what a fork re-runs:

- **Deployment details are excluded on purpose.** Changing a task's resources or image does not
  rename its action, so the rest of the run stays reusable. Raising the memory on a task that hit
  `flyte.errors.OOMError` and forking does exactly what you would hope: the successful upstream is
  reused, and the failed task re-executes with its new limit.
- **Matching follows the data.** Because a child's name folds in its inputs hash, an upstream task
  that re-executes but produces *identical* outputs leaves its downstream actions matchable, and
  they are still reused.

### What a code change re-runs

| You change | On fork |
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
causes it to re-execute instead of replaying its recorded result. A helper it calls still does not
count as a change.

Runs launched from a notebook or with a pickled code bundle behave differently: they version on the
bundle itself, so any code change renames every action and nothing is reused.

## Related

- [Recover a failed run](./recover-runs): replay a failed run with its original code, reusing what succeeded.
- [Re-run a run](./rerun-runs): launch a fresh run from a previous one, without reusing its actions.
- [Debug a run](./debug-runs): inspect a failure before deciding how to fork it.
- [Interact with runs and actions](./interacting-with-runs): retrieve, monitor, and inspect runs and actions.
