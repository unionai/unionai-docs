---
title: Recover a failed run
weight: 15
variants: -flyte +union
---

# Recover a failed run

When a long run fails, it is rarely the whole run that is broken. One task has a bug, or a single
action is lost to a preempted node or a network blip. Rerunning from scratch pays again for every
action that already succeeded: the GPU hours, the data loads, the deterministic preprocessing.

**Recovery** launches a new run that references a prior run. Every action that succeeded in the
source run is reused, with its recorded output copied across and no compute scheduled. Only the
actions that failed, were aborted, timed out, or changed are executed again. The source run is not
modified: recovery produces a distinct new run with its own name and history.

## Recovery compared with rerunning

[Rerunning](./rerun-runs) and recovering both launch a new run from an existing one. The difference
is what the new run executes.

| | Rerun | Recover |
|---|---|---|
| What executes | Everything, from the start | Only the failed, aborted, timed-out, or changed actions |
| Succeeded actions from the source run | Executed again | Reused, with their outputs copied across |
| Typical use | Reproduce a result, or retry a run that failed early | Resume a long run that failed late |
| Source run must have finished | No | Yes |

A rerun is the right tool when you want a clean, independent execution. Recovery is the right tool
when the expensive part of the run already succeeded and you only want to pay for the rest.

This matters most for workloads where a single run is long and front-loaded with cost:

- **Fine-tuning**: dataset preparation, tokenization, and sharding succeed, then the training action
  fails on a bad hyperparameter. Recovery re-enters at training with the prepared data already in
  place.
- **Reinforcement learning**: a rollout sweep completes and the aggregation or scoring step fails.
  Recovery reuses the rollouts instead of regenerating them.
- **Computer vision**: decoding, resizing, and embedding a large image corpus succeed, then the
  downstream indexing action fails. Recovery keeps the embeddings.

## Recover from the CLI

There are two commands, depending on whether you want the source run's code or your current local
code.

### `flyte rerun --recover`: recover using the source run's own code

`flyte rerun` fetches the prior run's task and inputs from the backend, so no local code is needed.
Adding `--recover` makes the new run reuse that run's succeeded actions:

```bash
flyte rerun <run-name> --recover
```

Use this when the failure was transient (a preemption, a timeout, a flaky dependency) and the code
is fine as it is.

### `flyte run --recover-from`: recover using new local code

`flyte run --recover-from <run-name>` launches **your local code** as a fresh run that recovers from
the named prior run:

```bash
flyte run --recover-from <run-name> main.py main --epochs 10
```

Use this when you have fixed the bug that caused the failure. The tasks you edited re-execute with
the new code; the tasks you did not touch are reused from the source run. Inputs come from the
command line as they do for any `flyte run`, so pass the per-task input flags as usual.

Both forms are remote-only. `--recover-from` cannot be combined with `--local`.

## What is reused and what runs again

Recovery matches actions between the two runs by **action name**, and an action's name is derived
from a stable identity rather than from the build:

```text
action name = hash(parent action name + inputs + task identity + call sequence [+ group])
task identity = task name + interface + per-task code version
```

The per-task code version is the task's cache version when caching is enabled on that task, and
otherwise an automatically computed hash of the task function's own body. The consequences are worth
reading closely, because they determine what you pay for:

- **Editing one task's body** changes only that task's identity. That task re-runs with the new code.
  Its siblings and everything upstream are reused. Downstream tasks re-run only if the edited task's
  output actually differs, because a changed output changes the downstream inputs hash.
- **Formatting or comment-only edits** do not change the identity, so everything is reused.
- **Changing a task's signature** changes its interface hash, so it re-runs. This is deliberate:
  a recorded output that no longer satisfies the new signature is never reused.
- **Rebuilding the image or the code bundle** does not by itself change any identity. The container
  image, code bundle version, resources, and environment variables are deliberately excluded so that
  a rebuild alone does not invalidate the whole run.
- **The root action `a0` always runs fresh.** It re-drives the graph, and the reuse decision is made
  for each action it enqueues.
- **Inputs are part of the identity.** Different inputs mean a different action name and a fresh
  execution. Inputs listed in `cache_ignore_input_vars` are excluded, so declared-nondeterministic
  values such as timestamps or seeds do not force a re-run.

Recovery uses the same identity computation as caching, but it looks up the **source run's** results
rather than the cache. The reuse decision is therefore unaffected by `overwrite_cache`,
`disable_run_cache`, and `cache_lookup_scope`. Those settings still apply as usual to the actions
that do execute.

### Reuse rests on the cache's trust model

The automatic code version hashes the decorated task function's own source, so it does not see
changes in a helper function the task calls, a module-level constant, a library version, or the
image. Those edits leave the action name unchanged and the previous result is reused. This is the
same blind spot the cache has, and recovery adopts it deliberately: recovery is explicit opt-in, and
`--force-rerun-action` below is the escape hatch when you need to override it.

## Force specific actions to re-run

`--force-rerun-action` names an action that must execute again even though it succeeded in the source
run. Repeat the flag for more than one action:

```bash
flyte rerun <run-name> --recover --force-rerun-action a3 --force-rerun-action a7
```

The same flag works with `flyte run --recover-from`:

```bash
flyte run --recover-from <run-name> --force-rerun-action a3 main.py main
```

Listing a parent action re-enqueues its children, but each child is still evaluated on its own
identity, so list the children too if you want to force a whole subtree. Names that do not match any
action are ignored. `--force-rerun-action` is only valid together with `--recover` or
`--recover-from`.

## Recover programmatically

Set `recover` on `flyte.with_runcontext()`. It takes a run name, and the new run recovers from that
run:

```python
import flyte

flyte.init_from_config()

# Launch this local code as a new run that recovers from a prior run.
flyte.with_runcontext(recover="ul56wcvgqrb9vzhzz5l2").run(main, epochs=10)
```

To recover using the source run's own code and inputs, combine it with `.rerun()`. Passing
`recover=True` there means "recover from the run being rerun":

```python
# Fetch the prior run's task and inputs from the backend, and recover from it.
flyte.with_runcontext(recover=True).rerun("ul56wcvgqrb9vzhzz5l2")
```

`recover=True` is only valid with `.rerun()`, since a plain `.run()` has no run to recover from.
Pass a run name instead on `.run()`.

The escape hatch is `recover_force_rerun_actions`:

```python
flyte.with_runcontext(
    recover="ul56wcvgqrb9vzhzz5l2",
    recover_force_rerun_actions=["a3", "a7"],
).run(main, epochs=10)
```

Both return a `flyte.remote.Run`, exactly as `flyte.run()` does, so you monitor, wait on, and read
outputs from a recovery run in the usual way. See
[Interact with runs and actions](./interacting-with-runs).

> [!NOTE]
> `flyte.rerun()` on its own never recovers. Recovery is a run-context setting, so go through
> `flyte.with_runcontext(recover=...)`.

## Identify a recovered action

An action that was reused rather than executed reports the **Recovered** phase. It is terminal and
counts as a success, and it carries a `recovered_from` pointer to the source run, so you can tell at
a glance which parts of a run cost compute and which were carried over.

The new run also records the source run as its parent, the same lineage that a rerun records. See
[Run lineage](./rerun-runs#run-lineage).

## Requirements and limitations

- **The source run must have finished.** Recovery reads a point-in-time snapshot, so recovering from
  a run that is still going is rejected. Recovering from a run that itself was recovered is allowed.
- **The source run must be in the same project and domain** as the new run.
- **The source run's data must still exist.** If retention has cleaned up the source run's stored
  data, `flyte rerun` fails with a message naming what is missing. When you know the inputs are
  intact, `--allow-missing-outputs` proceeds anyway; if they turn out to be gone, the new run fails
  at runtime. Actions recovered against deleted outputs fail when something consumes them, so use
  `--force-rerun-action` to re-execute those.
- **Recovery is remote-only.** Setting `recover` in local or hybrid mode raises an error rather than
  being silently ignored.
- **The source run must have been launched with `flyte` 2.6.0 or later.** The action-naming scheme
  that makes reuse code-aware changed, so a run launched by an older SDK matches nothing and every
  action executes again.
- **Inserting or removing calls shifts the call sequence.** Adding or deleting a call to the same
  task under the same parent renumbers the calls after it, so those re-run.
- **Interactive and notebook sessions re-run everything.** Bundles built in interactive mode take
  their version from the bundle, so any edit changes every task's identity.
- **Reuse never blocks progress.** If a lookup fails for any reason, that action simply runs fresh,
  which is the same behavior as not recovering at all.

## Related

- [Rerun a run](./rerun-runs): launch a new run from an existing one, executing everything again.
- [Run context](./run-context): the full set of `flyte.with_runcontext()` parameters.
- [Caching](../task-configuration/caching): how task-level caching and cache versions work.
- [Interact with runs and actions](./interacting-with-runs): retrieve, monitor, and inspect runs.
