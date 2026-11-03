---
title: Inference rollouts
description: Generate completions and trajectories from the current policy on a pool of GPU workers, and move each new set of weights from the trainer to the generators.
icon: speedometer2
weight: 3
variants: +flyte +union
---

# Inference rollouts

A rollout is the policy acting: sampling completions for a prompt, or taking an agent's turns in an environment. In LLM RL, generating rollouts usually takes more time than the policy update, so the rollout tier decides how fast the loop runs.

Rollouts need three things from the platform:

- **An inference engine on a GPU**, such as vLLM, that batches many sequences per call.
- **The current policy weights**, which change every iteration.
- **Parallelism**, so many prompts generate at once.

## Generate a group per call

GRPO compares several completions of the same prompt, so ask the engine for the whole group in one call. vLLM's `SamplingParams(n=GROUP_SIZE)` samples them as one batch, and the task returns them together for scoring.

{{< variant union >}}
{{< markdown >}}

## Keep the engine loaded between calls

Loading a base model into vLLM takes much longer than generating a group, so don't do it on every call. A [reusable container](../tasks/task-configuration/reusable-containers) keeps a pool of rollout workers running between calls:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="rollout_env" lang=python >}}
{{< markdown >}}

- `replicas=(1, 4)` scales the pool from one to four GPU workers with the number of groups in flight.
- `concurrency=1` sends one call at a time to each worker. A single vLLM engine batches internally and isn't safe to drive from several calls at once.
- `idle_ttl` keeps idle workers alive. Set it longer than one training step, so the pool is still warm when the next iteration starts.

Load the engine once per worker and cache it at module level:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="engine_cache" lang=python >}}
{{< markdown >}}

The first call on a worker builds the engine; every later call reuses it. The image needs the `unionai-reuse` package for reusable environments.

## Generate with the current adapter

Each call attaches the current LoRA adapter to the resident base model, by version:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="generate" lang=python >}}
{{< markdown >}}

Each adapter version is downloaded once per worker. The base weights in GPU memory never reload, so moving to a new policy costs one small download.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

## Amortize the engine load

Each task starts a fresh container, and loading a base model into vLLM takes longer than generating one group. Give each rollout task enough work to amortize the load: pass it a batch of prompts and generate all of their groups in one vLLM call. Fan out a few of these batch tasks per iteration rather than one task per prompt. [Prefetching models](../inference/prefetching-models) cuts the load time further by reading the base model from your object store instead of Hugging Face.

To keep an engine loaded across iterations, serve the policy as a [vLLM app](../inference/self-hosted-endpoints/vllm) and send rollout requests to it. The app keeps the base model in GPU memory, scales its replicas, and serves the OpenAI-compatible API that agent frameworks expect.

{{< /markdown >}}
{{< /variant >}}

## Move weights from the trainer to the generators

The trainer returns the new policy as a `flyte.io.Dir`, and the next round of rollout tasks receives it as an input:

1. The train task saves the weights, or only the LoRA adapter, and returns `await flyte.io.Dir.from_local(path)`.
2. The driver passes that `Dir` to the next round of rollout calls.
3. Each rollout task downloads it, or reads it by its path, before generating.

The weights travel through your object store, so the trainer and the generators never have to run at the same time or share a network connection. A LoRA adapter is a few megabytes, so the transfer is fast even when the base model is large. With full-weight updates, write the checkpoint once from rank 0 and pass the same `Dir` to every worker.

## Keep rollouts on-policy

Training on rollouts from an older policy biases the update. Record which policy version produced each rollout, so the trainer can detect stale samples or correct for them. Pass the version number into the rollout task and return it with each rollout. To compute importance ratios, also store the sampling log-probabilities the engine returns.

## Related

- [Training environment](./training-environment): where the policy's actions run.
- [Training loop](./training-loop): how the driver fans out rollouts and overlaps them with training.
- [Batch inference](../inference/batch-inference): the same engine patterns for scoring a dataset.
