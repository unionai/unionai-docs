---
title: Reinforcement learning
icon: trophy
description: Reinforcement learning on Union, from RL for LLMs to humanoid locomotion, model-written rewards, and self-play.
weight: 10
variants: -flyte +union
sidebar_expanded: true
---

# Reinforcement learning

Reinforcement learning trains a policy from rewards instead of labels: the policy acts, a reward
scores what it did, and an update moves the policy toward what scored well. The loop is the same
everywhere, but where the time and the risk go is not. These tutorials cover four very
different shapes of it, each tested end to end on a Union cluster:

| Tutorial | Policy | What makes it hard | What Union contributes |
| --- | --- | --- | --- |
| [RL for LLMs with GRPO and LoRA](./grpo-lora/_index) | An LLM, fine-tuned with a LoRA adapter | Generation, scoring, and training need different hardware in a tight loop | A warm pool of vLLM generators, a GPU trainer, and CPU reward workers, with checkpoints |
| [Teach a humanoid to run](./humanoid-locomotion/_index) | A Unitree G1 humanoid in MuJoCo | Hundreds of millions of simulation steps | 8,192 simulated robots on one GPU, a live video report, and a published policy |
| [Reward design with Claude and sandboxes](./eureka-reward-design/_index) | PPO on MountainCar, with rewards written by Claude | Every candidate reward is untrusted code and a training run | A sandbox per training run, a warm CPU pool for the fan-out, and traced LLM calls |
| [Self-play league for Connect Four](./self-play-league/_index) | A Connect Four agent trained against its past selves | Measuring progress when the opponent keeps changing | A warm GPU learner, match fan-out on CPUs, Elo, and an app to play the champion |

{{< grid >}}

{{< link-card target="grpo-lora" icon="trophy" title="RL for LLMs with GRPO and LoRA" >}}
Train a reasoning-style RL loop for an LLM with GRPO and LoRA, orchestrated by plain Flyte async tasks on a warm vLLM pool.
{{< /link-card >}}

{{< link-card target="humanoid-locomotion" icon="person-walking" title="Teach a humanoid to run" >}}
Train a running gait for the Unitree G1 humanoid with Brax PPO over MuJoCo MJX, 8,192 simulated robots on one GPU, with a live video report and a published policy.
{{< /link-card >}}

{{< link-card target="eureka-reward-design" icon="magic" title="Reward design with Claude and sandboxes" >}}
An Eureka-style loop where Claude writes reward functions, every candidate trains a policy inside a sandbox, and the best one's training statistics guide the next generation.
{{< /link-card >}}

{{< link-card target="self-play-league" icon="grid-3x3" title="Self-play league for Connect Four" >}}
Train a Connect Four agent by self-play against a league of its past selves, rate every snapshot with Elo, and serve the champion as an app you can play against.
{{< /link-card >}}

{{< /grid >}}

## Related

- [Reinforcement learning](../../user-guide/reinforcement-learning/_index) in the user guide: environments, rewards, rollouts, the training loop, and evaluation.
- [Durable agentic RL with SkyRL and Harbor](../frontier-ai/agentic-rl-skyrl/_index): agentic RL with sandboxed trials, verifiers, and LLM judges, made durable.
