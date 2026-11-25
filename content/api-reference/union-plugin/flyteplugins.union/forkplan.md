---
title: ForkPlan
description: "What a fork of *source_run* would reuse, as of *as_of*."
icon: braces
version: 0.26.2
variants: -flyte +union
layout: py_api
---

# ForkPlan

**Package:** `flyteplugins.union`

What a fork of *source_run* would reuse, as of *as_of*. Built client-side from the source
run's action list; see `fork_plan`.

Buckets (the root action `a0` is in none of them; it always runs):

- `reused`: succeeded (or recovered) in the source; the fork reuses their outputs. With a
  code change (`task_template`), any of them whose code changed re-runs instead, which only
  the fork itself can tell, so this is an upper bound.
- `in_flight`: still queued, running or paused in the source. Each runs again in the fork
  unless it finishes in the source before the fork reaches it — so it may run twice.
- `rerun`: failed, aborted or timed out in the source; they run again in the fork.
- `overridden`: `task_action_inputs` keys (and a non-root `target_action`): they re-run with
  the new inputs or code. `override_inputs` names the inputs each one changes.
- `implied_reruns`: other actions the fork re-runs on purpose: the ancestors of the overridden
  actions, which re-run to call them again, and `force_rerun_actions` (`forced_reruns`).
- `truncated`: the source has more actions than the plan listed (see `fork_plan`'s
  *max_actions*), so the buckets cover only the first ones.


## Parameters

```python
class ForkPlan(
    source_run: str,
    source_phase: ActionPhase,
    as_of: datetime,
    reused: List[PlannedAction] = <factory>,
    in_flight: List[PlannedAction] = <factory>,
    overridden: List[str] = <factory>,
    implied_reruns: List[str] = <factory>,
    rerun: List[PlannedAction] = <factory>,
    forced_reruns: List[str] = <factory>,
    override_inputs: Dict[str, List[str]] = <factory>,
    truncated: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `source_run` | `str` | |
| `source_phase` | `ActionPhase` | |
| `as_of` | `datetime` | |
| `reused` | `List[PlannedAction]` | |
| `in_flight` | `List[PlannedAction]` | |
| `overridden` | `List[str]` | |
| `implied_reruns` | `List[str]` | |
| `rerun` | `List[PlannedAction]` | |
| `forced_reruns` | `List[str]` | |
| `override_inputs` | `Dict[str, List[str]]` | |
| `truncated` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `source_is_running` | `bool` |  |

## Methods

| Method | Description |
|-|-|
| [`to_dict()`](#to_dict) |  |


### to_dict()

```python
def to_dict()
```
