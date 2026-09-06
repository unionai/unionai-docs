---
title: Durable agentic RL with SkyRL and Harbor
icon: arrow-repeat
description: Make SkyRL/Harbor-style agentic RL rollouts durable — trials that survive driver crashes, judges that are never re-billed, and training steps that apply exactly once.
weight: 2
variants: +flyte +union
---

# Durable agentic RL with SkyRL and Harbor

Reinforcement learning for LLM agents has a different shape than classic RLHF. In frameworks like [SkyRL](https://github.com/NovaSky-AI/SkyRL) and agentic environment suites like [Harbor](https://github.com/laude-institute/harbor), each training sample is a *trial*: the policy is dropped into a sandboxed environment with a filesystem and tools, takes many turns to attempt a task, and is then scored by a deterministic verifier plus an LLM judge. A training step fans out dozens or hundreds of these trials, collects the rewards, and updates the policy.

This inverts where the wall-clock time and the money go. SkyRL's own benchmarks show that rollout scheduling, not gradient computation, is the lever on agentic workloads: trials are long (minutes of tool calls), heterogeneous (some finish in 3 turns, some in 30), and flaky (sandboxes die, judge APIs rate-limit and time out). And the failure economics are brutal:

- A **driver crash** at step 40 of 50 loses every completed rollout in flight — hours of GPU inference regenerated from scratch.
- A **flaky sandbox** that kills one trial shouldn't kill the step, but in a monolithic training loop it often does.
- A **judge retry** that re-calls the LLM re-bills you for tokens you already paid for.
- Wanting to **re-score old rollouts with a new rubric** — the cheapest experiment in agentic RL — usually means regenerating everything, because trajectories and scores are entangled in the trainer's process.

SkyRL itself has no fault-tolerance or Kubernetes story; that's the layer this tutorial builds. We take a Harbor-shaped agentic RL loop — per-trial sandboxes, verifier + LLM judge, a bandit trainer standing in for the GPU trainer — and structure it so that **every trial, judgment, and training step is a durable, independently retryable unit**. The training here is a toy multi-armed bandit so the whole thing runs on CPU, but every structural decision is the real one.

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> Full code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/skyrl/agentic_rl_durable_oss.py).
> The same folder contains a [Union-backend variant](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/skyrl/agentic_rl_durable.py)
> that additionally uses reusable containers, copy-on-write volumes, and run forking.

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}

> [!NOTE]
> Full code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/skyrl/agentic_rl_durable.py),
> alongside the design document and measured experiments behind it.

{{< /markdown >}}
{{< /variant >}}

## Overview

The loop is the standard agentic RL loop:

1. **Generate**: for each trial, the policy explores a private copy of a "world" (a filesystem of documents, one of which contains a secret) using its current weights.
2. **Verify and judge**: a deterministic verifier checks correctness; a (simulated) LLM judge scores the trajectory against a *rubric* — correctness, efficiency, tidiness.
3. **Train**: rewards update the policy, and the next step's trials use the new weights.

What makes it durable is how the loop maps onto Flyte's execution model:

{{< variant union >}}
{{< markdown >}}

| Failure mode | What handles it |
|---|---|
| Driver crash mid-run | Every completed action is durably recorded; the retried driver **replays** completed steps in ~0.07 s each and resumes where it left off — on the *same warm Ray cluster*, because the cluster's lifetime is scoped to the run, not the driver attempt |
| Flaky sandbox kills a trial | Each trial is its own task with `retries=1` and a timeout; a trial that fails after retries is **skipped, never fatal** to the step |
| Judge task fails after the LLM call | The judge call is wrapped in `@flyte.trace`, so the retry **replays** the recorded result instead of re-billing the API |
| Training step re-executes | The trainer actor tracks applied steps, so an update is applied **exactly once** |
| New rubric, old rollouts | `flyte.rerun(recover=True, rubric=new)` **forks** the finished run: every rollout whose inputs are unchanged is recovered; only judging and training re-run |

Three of these lean on Union-backend capabilities — [reusable containers](../../../user-guide/tasks/task-configuration/reusable-containers) for the warm Ray cluster, [volumes](../../../user-guide/tasks/task-programming/volumes) for instant per-trial world copies, and [run forking](../../../user-guide/tasks/task-deployment/fork-runs) for rubric re-scoring. The rest is core Flyte 2.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

| Failure mode | What handles it |
|---|---|
| Driver crash mid-run | Every completed action is durably recorded; the retried driver **replays** completed trials and steps from the record instead of re-executing them, and resumes from the last completed step's checkpointed weights |
| Flaky sandbox kills a trial | Each trial is its own task with `retries=1` and a timeout; a trial that fails after retries is **skipped, never fatal** to the step |
| Judge task fails after the LLM call | The judge call is wrapped in `@flyte.trace`, so the retry **replays** the recorded result instead of re-billing the API |
| Training step re-executes | The training step is a **pure, deterministic function** of its inputs, so re-execution recomputes the identical update |
| New rubric, old rollouts | Rollout generation is cached with `cache="auto"`; a new run with a new rubric **reuses** every rollout whose inputs are unchanged and re-runs only judging and training |

{{< /markdown >}}
{{< /variant >}}

The result: in a run with a driver crash injected after step 1, 25% of sandboxes failing, and 30% of judge tasks failing *after* the judge call, all 18 trials completed, the judge was called exactly once per trial, and the bandit still learned (mean turns to find the secret dropped from 3.83 to 1.5, mean reward rose from 1.62 to 2.36).

## Implementation

### Environments: one failure domain per tier

Each tier of the loop — sandboxed rollouts, judging, training, and the driver — gets its own `flyte.TaskEnvironment`, so its resources, retries, and timeouts are independent.

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="envs" lang="python" >}}
{{< markdown >}}

Two things to notice:

- **The trainer runs on one long-lived Ray cluster.** `reusable=flyte.ReusePolicy(replicas=1, idle_ttl=600, scope="run")` keeps the same Ray head alive for the whole run. Every training step is a separate Flyte task *submitted to that same cluster* — so the step is a durable boundary, but the expensive state (in real training: FSDP shards and optimizer state; here: the bandit's priors) never leaves GPU/memory between steps. Critically, the cluster's lifetime is scoped to the **run**, not the driver attempt: a driver crash does not tear it down.
- **The sandbox environment allows FUSE** (`flyte.PodTemplate().allow_fuse()`) so each trial pod can mount a forked volume — more on that below.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="envs" lang="python" >}}
{{< markdown >}}

The separation is the point: a trial pod that OOMs takes down one trial, not the step; the judge tier's retry policy is independent of the sandbox tier's; and the driver is a cheap CPU pod whose only job is orchestration — all the expensive work happens in child actions that outlive it.

{{< /markdown >}}
{{< /variant >}}

### Weights travel as inputs (pull-based sync)

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="types" lang="python" >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="types" lang="python" >}}
{{< /variant >}}

The `Weights` model *is* the policy, and it flows from the trainer to every rollout as an ordinary task **input**. This is the pull-based weight-sync shape that fits LoRA adapters and small models: the rollout tier needs no NCCL group, no engine control plane, and no connection back to the trainer — which is exactly what lets a rollout be retried on a fresh pod minutes later with no coordination.

Just as important: `Rubric` is an input to judging, not a constant baked into the code. Every input is part of an action's content-hashed identity, and that identity is what makes selective re-execution possible later.

### Worlds: built once, private copy per trial

Each world is a small filesystem of documents; one document contains a (hashed) secret the agent must find. Agent trials mutate their environment, so every trial needs its **own** copy — stale state from a previous attempt is how you get silently corrupted training data.

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="build-world" lang="python" >}}
{{< markdown >}}

The world is built once per run (the task is cached) and sealed as a read-only volume. Each trial then forks it:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="generate" lang="python" >}}
{{< markdown >}}

`world.fork(...)` is a copy-on-write fork of the volume — about 0.1 s to fork plus 0.55 s to mount for a 1 GB world, versus 6+ s to download the same world from blob storage, and the gap widens with world size. The trial writes freely into its private copy; reset is free because the parent volume never changes. The pod is the sandbox, the forked volume is the world.

The task itself carries the trial-level durability contract: `retries=1`, a 300 s timeout, and idempotency by construction (the trajectory is seeded by `trial_id`, so a retry is a clean regeneration, not a replay of half-mutated sandbox state). The `flaky_rate` parameter injects sandbox failures on attempt 0 so you can watch the retries work.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="build-world" lang="python" >}}
{{< markdown >}}

The world is built once (the task is cached) and uploaded as a `flyte.io.Dir`. Each trial downloads its own private copy:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="generate" lang="python" >}}
{{< markdown >}}

The pod's own filesystem is the sandbox: the downloaded copy is private, writes never leak between trials, and everything vanishes with the pod. (On a Union backend, `Volume.fork()` replaces the download with a sub-second copy-on-write fork — worth knowing about when worlds get large.)

The task carries the trial-level durability contract: `retries=1`, a 300 s timeout, and idempotency by construction (the trajectory is seeded by `trial_id`, so a retry is a clean regeneration, not a replay of half-mutated sandbox state). It's also cached with `cache="auto"` — that's what powers rubric re-scoring later. The `flaky_rate` parameter injects sandbox failures on attempt 0 so you can watch the retries work.

{{< /markdown >}}
{{< /variant >}}

### The judge is memoized: retried, never re-billed

Scoring is two things fused into one task: a deterministic verifier (in Harbor terms, the environment's `test.sh`) and an LLM judge that scores the trajectory against the rubric.

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="judge" lang="python" >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="judge" lang="python" >}}
{{< /variant >}}

The `@flyte.trace` decorator is the important line. The judge call's result is durably recorded the moment it returns. If the surrounding task then fails — the injected `judge_flake_rate` failure simulates a post-judge upload error — the retry **replays** the recorded result instead of calling the judge again. In the failure-injected runs, retried judge tasks show `JUDGE CALLED` exactly once in their attempt-0 logs and zero times on the retry.

At scale this is real money: a judge pass over hundreds of long trajectories is a substantial LLM bill, and infrastructure flakiness shouldn't multiply it. Keep your vendor judge; just never re-bill it.

### Training steps that can't double-apply

{{< variant union >}}
{{< markdown >}}

The trainer's state lives in a **detached, namespaced Ray actor** on the reusable cluster — the stand-in for GPU-resident FSDP shards and optimizer state. Each training step is a Flyte task that re-attaches to the actor by name:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="trainer" lang="python" >}}
{{< markdown >}}

Two details make this crash-safe:

- **The actor is `detached` and `namespaced`.** Each Flyte task on the reusable cluster is a new Ray job in a new process; module globals don't survive between steps. A detached, namespaced actor does — across steps, across step retries, and across driver crashes. In the failure-injected run, all three training steps report the same actor PID even though the driver died between steps 1 and 2.
- **Updates are exactly-once by construction.** The actor records which step indices it has applied (`self.applied`). A re-executed step task — a retry after the actor already applied the update, or a driver replay — gets the recorded result back instead of applying the gradient twice.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

The trainer is a **pure function**: current weights and rewards in, new weights out.

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="train-step" lang="python" >}}
{{< markdown >}}

The returned weights are the checkpoint. Every step's output is durably recorded as the action's result, so a driver crash resumes from the last completed step with no checkpoint-restore code at all. And because the function is deterministic, re-execution is harmless: a replayed step recomputes the identical update, so there's no double-apply to guard against.

This is the trade against keeping trainer state resident in a long-lived process (as the Union-backend variant does with a detached Ray actor on a reusable cluster): weights must be small enough to serialize every step — the LoRA/small-model shape — in exchange for a trainer with no state to lose.

{{< /markdown >}}
{{< /variant >}}

### The driver: a durable log of the training run

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="driver" lang="python" >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="driver" lang="python" >}}
{{< /variant >}}

The driver reads as a plain Python training loop, but every call in it is a durable action. That has three consequences worth spelling out:

- **Pipelined, not batched.** Trials are launched concurrently and judged the moment each one lands (`asyncio.as_completed`), so a 30-turn straggler doesn't hold up scoring for the trials that finished in 3. A trial that fails after its retries is logged and skipped — `skip_failed_rollouts`, as SkyRL calls it — never fatal to the step.
- **A driver crash is a replay, not a restart.** When the driver task is retried (the example injects a `RuntimeSystemError` after a chosen step to demonstrate), completed child actions are not re-executed: the retry replays them from the durable record and picks up at the first incomplete action. Notice there is no checkpointing code, no state file, no resume flag anywhere in the loop.
- **Canonicalize step inputs.** The one subtle line is `rewards = sorted(..., key=lambda r: r.trial_id)`. The first version of this example didn't sort, and a driver replay collected the same rewards in a different `as_completed` order — so the training step's inputs hashed differently, the step re-ran instead of replaying, and (in the stateful-trainer version) the update applied twice. If a replayed step's inputs must hash identically, make them order-independent. This bug cost a debugging session; the fix is one `sorted()`.

`flyte.durable.now()` records the wall-clock start once and replays it on retry — so even the report's timestamps are stable across driver attempts. Progress streams to a live report tab in the UI as the run executes.

### Re-scoring old rollouts with a new rubric

Rubric iteration is the cheapest experiment in agentic RL — *if* you can re-judge existing trajectories without regenerating them. Because the rubric is an input to judging (not to generation), changing it should invalidate only judging and everything downstream.

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="fork" lang="python" >}}
{{< markdown >}}

`flyte.rerun(run_name, recover=True, rubric=new)` forks the finished run with one changed input. Recovery walks the action graph by content-hashed identity: worlds, trainer setup, and every step-0 `generate` action are **recovered** (reused as-is); `verify_and_judge` re-runs everywhere because its rubric input changed; and — correctly — steps 1 and 2 regenerate too, because the new rewards changed the policy after step 0, so later rollouts depend on different weights. Nothing in the driver knows about forks; content-hashed identity finds that invalidation frontier by itself.

In the measured fork, step-0 rollouts were re-scored from 1.62 to 2.41 mean reward on *identical* trajectories — the new rubric valued efficiency more, and the judging cost was the only cost paid for them.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="rescore" lang="python" >}}
{{< markdown >}}

Here the reuse comes from **caching** rather than run recovery: `build_world` and `generate` are cached with `cache="auto"`, worlds and initial weights are deterministic, so a new run with a new rubric hits the cache for every step-0 rollout — identical spec, weights, and world — and reuses it. Judging re-runs (its rubric input changed), the new rewards change the weights after step 0, so later steps' `generate` inputs differ, miss the cache, and regenerate. Same invalidation frontier, found by cache-key identity instead of fork recovery.

(A Union backend adds [run forking]({{< docs_home union v2 >}}/user-guide/tasks/task-deployment/fork-runs) — `flyte.rerun(recover=True, rubric=new)` — which reuses *non-cached* actions too and links the fork to its parent run in the UI.)

{{< /markdown >}}
{{< /variant >}}

## Run it

{{< variant union >}}
{{< markdown >}}

The example needs a Union backend with the FUSE device plugin (for volumes) and KubeRay (for the Ray environment):

```bash
# clean run
flyte --config <your-config> run agentic_rl_durable.py train

# same run with every failure path exercised: driver crash after step 1,
# 25% flaky sandboxes, 30% judge tasks that fail after the judge call
flyte --config <your-config> run agentic_rl_durable.py train \
    --crash_driver_at_step 1 --flaky_trial_rate 0.25 --judge_flake_rate 0.3

# fork a finished run with a new rubric
FLYTE_CONFIG=<your-config> python agentic_rl_durable.py fork <run-name>
```

In the fully failure-injected run (3 steps × 3 worlds × 2 samples):

| | count | note |
|---|---|---|
| `generate` succeeded / retried | 18 / 6 | 6 injected sandbox failures, each retried once, none fatal |
| `verify_and_judge` succeeded / retried | 18 / 6 | retried actions log `JUDGE CALLED` once on attempt 0 and never on the retry |
| `train_step` | 3 | all on the same actor PID across the driver crash |
| driver | 2 attempts | crashed after step 1; attempt 2 replayed steps 0–1 (~0.07 s each) and ran step 2 |
| learning | ✓ | mean turns 3.83 → 1.33 → 1.50; mean reward 1.62 → 2.35 → 2.36 |

Despite a driver crash, a third of sandboxes flaking, and a third of judge tasks failing, the run completed with zero lost rollouts and zero re-billed judge calls.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

```bash
# clean run
flyte --config <your-config> run agentic_rl_durable_oss.py train

# same run with every failure path exercised: driver crash after step 1,
# 25% flaky sandboxes, 30% judge tasks that fail after the judge call
flyte --config <your-config> run agentic_rl_durable_oss.py train \
    --crash_driver_at_step 1 --flaky_trial_rate 0.25 --judge_flake_rate 0.3

# re-score with a new rubric (caching reuses worlds + step-0 rollouts)
flyte --config <your-config> run agentic_rl_durable_oss.py rescore
```

In the failure-injected run, watch three things in the UI:

- **Retried `generate` actions** — each injected sandbox failure retries once and succeeds; the step completes with all trials.
- **Retried `verify_and_judge` actions** — their attempt-0 logs show `JUDGE CALLED`; their retry logs don't. The trace replayed.
- **The driver's second attempt** — completed trials and steps replay from the durable record; only work after the crash point actually executes.

{{< /markdown >}}
{{< /variant >}}

## What this means for real training

The bandit stands in for a GPU trainer, but the structure transfers directly to a SkyRL/Harbor-scale stack:

- **The trial is the unit of durability.** Generation and judging are separate actions per trial, so the blast radius of any single failure — sandbox, network, judge API — is one trial, and the recovery cost is one retry.
- **Weights-as-inputs is the LoRA/small-model sync path.** For full-parameter training with NCCL-based weight broadcast, the inner loop stays inside the training framework; the durable boundary moves up to the step level.
{{< variant union >}}
{{< markdown >}}
- **Steps-as-tasks on a reusable cluster** gives you a durable training log without paying cluster spin-up per step (~18 s of Ray job submission overhead per step is the price; a fresh cluster per step would be minutes). The expensive in-memory state lives in the cluster; the *record* of training lives in Flyte.
- **Fork is the experiment multiplier.** Any finished (or crashed) run can be forked with changed inputs — a new rubric, a new judge model, a fixed bug — and recovery reuses everything the change doesn't invalidate.
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
- **Checkpoint-as-output scales down gracefully.** Threading weights through step tasks costs a serialization per step but makes the trainer stateless — the strongest possible recovery story. When trainer state gets too big to serialize per step, keep it in the training framework's own checkpoint format and pass a reference (`flyte.io.File`/`Dir`) between steps instead.
- **Caching is the experiment multiplier.** Cache generation on its true inputs and any re-run — new rubric, new judge, fixed bug downstream — reuses every rollout the change doesn't invalidate.
{{< /markdown >}}
{{< /variant >}}

The pattern generalizes beyond RL: any loop of *expensive, flaky, independently-scoreable work items* — evaluation harnesses, synthetic data generation, agent benchmarking — gets the same durability for the same restructuring.
