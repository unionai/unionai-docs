---
title: Training loop
description: Tie rollouts, rewards, and policy updates together in a durable driver task, scale the trainer across nodes, and overlap generation with training.
icon: arrow-repeat
weight: 4
variants: +flyte +union
---

# Training loop

The training loop runs every iteration of RL: sample prompts, generate rollouts, score them, update the policy, and repeat with the new weights. In Flyte, the loop is a Python `for` loop in a driver task. The driver holds no GPU and does no heavy work; it calls tasks in the rollout, reward, and train environments, and keeps track of where the run is.

## Define the environments

Each part of the loop gets its own environment. The trainer needs a GPU only while it updates the policy, and the driver is a small CPU task:

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="train_env" lang=python >}}
{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="driver_env" lang=python >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="envs" lang=python >}}
{{< /variant >}}

`depends_on` lists every environment the driver calls, so deploying the driver deploys the whole loop. For the rollout and reward environments, see [Inference rollouts](./inference-rollouts) and [Reward setup](./reward-setup).

## Write the loop

The driver runs one iteration per loop pass:

{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="train_rl" lang=python >}}
{{< markdown >}}

Each part of the loop uses one construct:

- **Fan-out.** `asyncio.create_task` launches every rollout group at once.
- **Overlapping reward with generation.** `asyncio.as_completed` hands each group to `score_group` the moment it finishes, so scoring runs while slower groups are still generating.
- **The update.** `train_step` takes the rollouts and rewards and returns the next adapter as a `flyte.io.Dir`, which the next iteration's rollouts receive.
- **One node per iteration in the UI.** `flyte.group(f"iter-{it}")` collects an iteration's rollout, reward, and train actions, so you can open iteration 12 and see exactly which completions it trained on.
- **A live report.** `report=True` and `flyte.report.replace.aio` publish reward, accuracy, and loss after every iteration.
- **Resuming.** The driver saves the iteration number, the adapter's path, and the report history to `flyte.ctx().checkpoint` after every iteration. If a later attempt of the driver starts, it loads that state and continues from the next iteration instead of from the start. Set `retries` on the driver task so that a failed or preempted driver gets another attempt. The checkpoint belongs to the task's attempts within one run, so a new run starts from iteration 0.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="driver" lang=python >}}
{{< markdown >}}

Each part of the loop uses one construct:

- **Fan-out.** `asyncio.create_task` launches every episode at once, and each one carries the current weights as an input.
- **Overlapping reward with generation.** `asyncio.as_completed` hands each trajectory to `verify_and_judge` the moment it finishes. An episode that still fails after its retries is skipped, not fatal to the step.
- **Stable inputs.** The rewards are sorted by trial ID before training, because `as_completed` returns them in a different order on each attempt. Sorted inputs hash the same way, so a replayed step can be reused.
- **The update.** `train_step` is a pure task: it takes the weights and rewards and returns the next weights, which are the step's checkpoint.
- **One node per step in the UI.** `flyte.group(f"step-{step}")` collects a step's episodes, judging, and update.
- **A live report.** `report=True` and `tab.log` publish the reward and weights version after every step.
- **Resuming.** If the driver fails and is retried, the actions it already completed are reused, so it reaches the step where it stopped without rerunning episodes. `flyte.durable.now()` records the start time once and returns the same value on a retry.

{{< /markdown >}}
{{< /variant >}}

## Compute the update

The trainer turns rewards into a learning signal. GRPO normalizes each completion's reward against the other completions of the same prompt:

{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="advantages" lang=python >}}

A completion that scored above its group's mean gets a positive advantage, and the update makes it more likely. A group where every completion scored the same gives no signal and is skipped. The policy update itself is ordinary PyTorch inside `train_step`. Libraries such as TRL work there too.

## Scale the trainer across nodes

When the policy is too large to update on one node, make the trainer a `flyte.clustered.ClusteredTaskEnvironment`:

{{< code file="/unionai-examples/v2/tutorials/multinode_rl_grpo_lora/rl_grpo_lora_clustered.py" fragment="clustered_env" lang=python >}}

`resources` applies to each pod, and the train task runs on every rank, as in [Pre-training](../model-training/pretraining#run-torchrun-across-nodes). Rank 0 saves the new adapter and broadcasts its path, so every rank returns the same values of the declared types. Rank 0's return value becomes the task's output, so the driver's loop doesn't change. A multi-node trainer has a cold start of its own, because every pod has to be scheduled before the step begins. The next section hides it.

## Overlap generation with training

In a sequential loop, the GPUs for generation wait while the trainer runs, and the trainer waits while generation runs. Start generating the next batch before training on the current one. The body of the pipelined loop, simplified from the multi-node example:

```python
for it in range(start_iter, num_iterations):
    rollouts, rewards = await pending

    # Generate batch N+1 with the current adapter while batch N trains.
    if it + 1 < num_iterations:
        with flyte.group(f"iter-{it + 1}-generate"):
            pending = asyncio.create_task(generate_and_score(it + 1, adapter, version))

    version += 1
    with flyte.group(f"iter-{it}-train"):
        adapter, opt_state, metrics = await train_step_clustered(
            base, rollouts, rewards, adapter, version, opt_state
        )
```

Before the loop, the driver starts `pending` for the first batch. Each trained adapter gets a new `version`, which the rollout tasks use to tell adapters apart.

The trainer's time, including its cold start, now runs under generation, and each iteration takes about as long as generation alone. The cost is that batch N+1 is generated by a policy one step behind the one it trains. Correct for this in the loss with a clipped importance ratio, using the sampling log-probabilities recorded during generation:

{{< code file="/unionai-examples/v2/tutorials/multinode_rl_grpo_lora/rl_grpo_lora_clustered.py" fragment="grpo_loss" lang=python >}}

`old_logp` comes from the rollout, `new_logp` from the policy being trained, and `ref_logp` from the base model with the adapter turned off. The ratio of new to old is clipped, so a stale sample can't move the policy far, and the KL term keeps the policy close to the base model. See [Keep rollouts on-policy](./inference-rollouts#keep-rollouts-on-policy).

Run held-out evaluation off the critical path too. Launch the evaluation of step N with `asyncio.create_task` and await it after step N+1 trains, so it never sits between iterations. See [Evaluation](./evaluation).

{{< variant union >}}
{{< markdown >}}

For a GRPO loop on Qwen3-8B with a two-node, eight-GPU trainer, overlapping cut each iteration from 434 seconds to 298 in steady state. See [We ran multi-node GRPO on 8 GPUs and the trainer cost us nothing](https://www.union.ai/blog-post/we-ran-multi-node-grpo-on-8-gpus-and-the-trainer-cost-us-nothing).

{{< /markdown >}}
{{< /variant >}}

## Make each step durable

Checkpointing the driver protects the loop's position. To also protect the work inside an iteration, make each step a pure function of its inputs:

- Set `retries` on rollout, reward, and train tasks, so a transient failure reruns one task, not the iteration.
- Seed each rollout from its prompt and iteration, for example with vLLM's `SamplingParams(seed=...)`, so a retried rollout produces the same result. Without a seed, sampling at a nonzero temperature gives a different result on every attempt, and caching the rollout isn't sound.
- Pass weights and optimizer state in and out of the train task as `flyte.io.Dir`, instead of keeping them in a long-lived process. A replayed step then recomputes the same outputs.
- Set `cache="auto"` on steps that are pure, so a rerun of the loop returns finished steps from the cache.

{{< variant union >}}
{{< markdown >}}

## Keep rollouts on a volume

Weights and optimizer state move best as a `flyte.io.Dir`, because every task that receives them reads all of them. See [Move weights from the trainer to the generators](./inference-rollouts#move-weights-from-the-trainer-to-the-generators). Rollouts are different: they accumulate across iterations, and later work often reads only part of them. An off-policy trainer samples from a replay buffer, an analysis reads the completions from a few iterations, and an evaluation rescores them with a new verifier.

Store them on a [volume](../tasks/task-programming/volumes/_index) that each iteration forks and adds to:

```python
import json

import flyte
from flyteplugins.union.io import ROVolume, allow_volumes

buffer_env = flyte.TaskEnvironment(
    name="rollout-buffer",
    image=image.with_pip_packages("flyteplugins-union"),
    pod_template=allow_volumes(cache_size="20Gi"),
    resources=flyte.Resources(cpu=2, memory="4Gi"),
)


@buffer_env.task
async def add_rollouts(
    buffer: ROVolume, it: int, completions: list[str], rewards: list[float]
) -> ROVolume:
    rw = await buffer.fork(name=f"rollouts-iter-{it}")
    data = await rw.mount()
    rows = (json.dumps({"iteration": it, "completion": c, "reward": r}) for c, r in zip(completions, rewards))
    (data / f"iter-{it:05d}.jsonl").write_text("\n".join(rows))
    return await rw.finalize(message=f"iteration {it}")
```

- **Each version is cheap.** A fork is copy-on-write, so each iteration's version stores only its own new file and shares the rest with the version before it.
- **Readers mount only what they need.** A trainer task that receives the `ROVolume` mounts it and reads the iterations it samples from, without downloading the whole buffer.
- **Every version stays addressable.** The driver keeps the `ROVolume` for each iteration, and any later task or run can mount the buffer as it was after any iteration.

Create the first, empty version with `Volume.new()` in a task before the loop, and pass the version each call returns to the next one, so the buffer is a chain of versions. Each fork has one writer, so writes never collide.

{{< /markdown >}}
{{< /variant >}}

## Related

{{< variant union >}}
{{< markdown >}}

- [RL for LLMs with GRPO and LoRA](../../tutorials/reinforcement-learning/grpo-lora/_index): the loop on this page, including the multi-node, pipelined version.

{{< /markdown >}}
{{< /variant >}}

- [Durable agentic RL with SkyRL and Harbor](../../tutorials/frontier-ai/agentic-rl-skyrl/_index): an agentic loop with sandboxed episodes and a judge.
- [Intra-task checkpoints](../tasks/task-programming/intra-task-checkpoints): the checkpoint store the driver uses.
- [Grouping actions](../tasks/task-programming/grouping-actions): how `flyte.group` organizes the run's UI.
