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
- `idle_ttl=300` shuts the whole pool down after 300 seconds with no calls, and `scaledown_ttl=120` removes each idle worker after 120 seconds. Set `idle_ttl` longer than one training step, so the pool survives while the trainer runs. To keep every worker warm across the step, not just one, set `scaledown_ttl` longer than the step too.

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

Each task starts a fresh container, and loading a base model into vLLM takes longer than generating one group. Give each rollout task enough work to amortize the load: pass it a batch of prompts and generate all of their groups in one vLLM call. Fan out a few of these batch tasks per iteration rather than one task per prompt:

```python
import flyte

rollout_env = flyte.TaskEnvironment(
    name="rollout",
    image=image,
    resources=flyte.Resources(cpu=4, memory="24Gi", gpu="L4:1"),
)


@rollout_env.task(retries=2)
async def generate_batch(
    base: flyte.io.Dir, prompts: list[str], adapter: flyte.io.Dir, version: int, seed: int
) -> list[list[str]]:
    from vllm import LLM, SamplingParams
    from vllm.lora.request import LoRARequest

    engine = LLM(model=await base.download(), enable_lora=True)
    lora = LoRARequest(f"policy-v{version}", version + 1, await adapter.download())
    sampling = SamplingParams(n=GROUP_SIZE, temperature=1.0, seed=seed)
    outputs = engine.generate(prompts, sampling, lora_request=lora)
    return [[o.text for o in out.outputs] for out in outputs]
```

The base model loads once per batch, and every prompt in the batch shares it. [Prefetching models](../inference/prefetching-models) cuts the load time further by reading the base model from your object store instead of Hugging Face.

To keep an engine loaded across iterations, serve the policy as a [vLLM app](../inference/self-hosted-endpoints/vllm) and send rollout requests to it. The app keeps the base model in GPU memory, scales its replicas, and serves the OpenAI-compatible API that agent frameworks expect. To move a new adapter into the running app, start vLLM with `--enable-lora` and `VLLM_ALLOW_RUNTIME_LORA_UPDATING=True`, then load each adapter version by name through its `/v1/load_lora_adapter` endpoint.

{{< /markdown >}}
{{< /variant >}}

## Move weights from the trainer to the generators

### Pass the weights as a directory

The trainer returns the new policy as a `flyte.io.Dir`, and the next round of rollout tasks receives it as an input:

1. The train task saves the weights, or only the LoRA adapter, and returns `await flyte.io.Dir.from_local(path)`.
2. The driver passes that `Dir` to the next round of rollout calls.
3. Each rollout task downloads it, or reads it by its path, before generating.

The weights travel through your object store, so the trainer and the generators never have to run at the same time or share a network connection. A LoRA adapter is a few megabytes, so the transfer is fast even when the base model is large. With full-weight updates, write the checkpoint once from rank 0 and pass the same `Dir` to every worker. To load full weights onto the GPU without writing them to local disk first, pass the `Dir`'s path to the model streamer. See [Stream model weights](../inference/stream-model-weights).

{{< variant union >}}
{{< markdown >}}

### When a volume helps

A [volume](../tasks/task-programming/volumes/_index) is a versioned file system that tasks mount. For moving weights, it doesn't beat a `Dir`:

- **Speed.** A rollout task reads the whole adapter or checkpoint, which a `Dir` download or the model streamer already does at object-store speed. Reads through a volume pass through a file-system layer, and loading weights into memory that way is slower than streaming them. See [Performance and trade-offs](../tasks/task-programming/volumes/performance#performance-and-trade-offs).
- **Durability.** Both are stored in your object store, and both are immutable once a task returns them.

A volume does help in these cases:

- **Many rollout pods on one node.** With `allow_volumes(shared_node_cache=True)`, read-only mounts on a node share one cache, so each node fetches the weights once instead of once per pod. This matters when you pack several single-GPU rollout pods onto each multi-GPU node.
- **Reading part of a large tree.** A task that needs only some files, such as one shard of a sharded checkpoint, mounts the volume and reads those files, instead of downloading the whole `Dir`.
- **Data that grows across iterations.** A rollout buffer that every iteration adds to can live on a volume, with each version storing only what changed. See [Keep rollouts on a volume](./training-loop#keep-rollouts-on-a-volume).
- **A browsable history of policies.** A volume declared as an artifact publishes each committed version with a parent edge to the one before it. See [Versions, artifacts and lineage](../tasks/task-programming/volumes/versions).

A volume has one writer while it is mounted, so in a multi-node trainer only one rank can write to it.

{{< /markdown >}}
{{< /variant >}}

## Keep rollouts on-policy

Training on rollouts from an older policy biases the update. Record which policy version produced each rollout, so the trainer can detect stale samples or correct for them. Pass the version number into the rollout task and return it with each rollout. To compute importance ratios, also store the token IDs and sampling log-probabilities the engine returns: set `SamplingParams(logprobs=0)`, which returns only the sampled token's log-probability, and keep it with the completion. Sample at `temperature=1.0` with `top_p=1.0`: vLLM reports log-probabilities after its sampling adjustments, so they equal the policy's own only at those settings. See [Overlap generation with training](./training-loop#overlap-generation-with-training) for the loss that uses them.

## Related

{{< variant union >}}
{{< markdown >}}

- [RL for LLMs with GRPO and LoRA](../../tutorials/reinforcement-learning/grpo-lora/_index): the rollout pool on this page, with the full loop around it.

{{< /markdown >}}
{{< /variant >}}

- [Durable agentic RL with SkyRL and Harbor](../../tutorials/reinforcement-learning/agentic-rl-skyrl/_index): rollouts that are multi-turn agent trajectories.
- [Training environment](./training-environment): where the policy's actions run.
- [Training loop](./training-loop): how the driver fans out rollouts and overlaps them with training.
- [Batch inference](../inference/batch-inference): the same engine patterns for scoring a dataset.
