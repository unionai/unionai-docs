---
title: Evaluation
description: Evaluate an RL policy by sampling it many times on held-out problems, report avg@k and pass@k, watch training health, catch reward hacking, and see how this differs from evaluating a supervised model.
icon: clipboard-data
weight: 5
variants: +flyte +union
---

# Evaluation

Evaluating an RL policy takes more than evaluating a supervised model. The training reward is a proxy that the policy is optimized to exploit, and the data the policy trains on is data it generated itself. A rising reward can mean the policy got better, or that it found a flaw in the reward. Evaluation has to tell the two apart.

## How it differs from supervised evaluation

| | Supervised model | RL policy |
|---|---|---|
| **What you score** | One prediction per example, often with greedy decoding | Many samples per problem, at the temperature the policy will run at |
| **The metric** | Accuracy or loss on a held-out split | avg@k and pass@k on held-out problems, scored by a verifier the policy didn't train against |
| **Training signal** | The loss on labeled data, which tracks quality | The reward, which can rise while quality falls |
| **What can go wrong** | Overfitting to the training split | Reward hacking, entropy collapse, and loss of general capabilities |
| **Which checkpoint** | Usually the last, or the lowest validation loss | Often an earlier one, chosen by held-out evaluation |
| **Variance** | One run is usually representative | Results vary between seeds, so compare several runs |

For supervised evaluation, see [Evaluation](../model-training/evaluation) in Model training.

## Sample each problem many times

A policy samples, so one completion per problem gives a noisy score. Generate `k` completions per problem and report statistics over them:

- **avg@k** is the mean accuracy over all `k` samples. It estimates pass@1, the chance that one sample is right, with much less noise than a single sample.
- **pass@k** is the chance that at least one of `k` samples is right. It measures coverage: which problems the policy can solve at all.
- **maj@k** scores the most common answer among `k` samples. Report it when the policy will be used with majority voting.

Report both avg@k and pass@k. RL with verifiable rewards often raises avg@k much more than pass@k at large `k`: it makes the policy sample the answers it could already reach more reliably, and a base model sampled many times can solve as many problems. Comparing the policy with its base model on both metrics shows which one improved.

Evaluate at the sampling settings the policy will be used with, and state them with the results. Long chain-of-thought models are commonly evaluated at a temperature of about 0.6 with `top_p=0.95`, because greedy decoding makes them repeat themselves.

## Run evaluation as a task

The evaluation task loads the base model and the policy's adapter into vLLM, samples `n` completions for every problem, and scores them with the verifier:

```python
import math

import flyte

eval_env = flyte.TaskEnvironment(
    name="rl-eval",
    image=image,
    resources=flyte.Resources(cpu=4, memory="24Gi", gpu="L4:1"),
)


def pass_at_k(n: int, c: int, k: int) -> float:
    """The unbiased estimate of pass@k from n samples, c of them correct."""
    if n - c < k:
        return 1.0
    return 1.0 - math.comb(n - c, k) / math.comb(n, k)


@eval_env.task(cache="auto", retries=2)
async def evaluate_policy(
    base: flyte.io.Dir, adapter: flyte.io.Dir | None, benchmark: str, n: int = 16, k: int = 8
) -> dict[str, float]:
    from vllm import LLM, SamplingParams
    from vllm.lora.request import LoRARequest

    problems = load_problems(benchmark)  # held-out prompts with known answers
    engine = LLM(model=await base.download(), enable_lora=adapter is not None)
    lora = LoRARequest("eval", 1, await adapter.download()) if adapter else None
    sampling = SamplingParams(n=n, temperature=0.6, top_p=0.95, max_tokens=4096, seed=0)
    outputs = engine.generate([p.prompt for p in problems], sampling, lora_request=lora)

    correct = [sum(verify(o.text, p.answer) for o in out.outputs) for p, out in zip(problems, outputs)]
    lengths = [len(o.token_ids) for out in outputs for o in out.outputs]
    return {
        f"avg@{n}": sum(correct) / (n * len(problems)),
        f"pass@{k}": sum(pass_at_k(n, c, k) for c in correct) / len(problems),
        "mean_length": sum(lengths) / len(lengths),
    }
```

`load_problems` and `verify` are your own functions. Use the same answer extraction for every model you compare, and score an answer that can't be parsed as wrong.

- **`adapter=None` evaluates the base model** with the same code, which gives you the baseline to compare against.
- **`cache="auto"`** keys the result on the checkpoint, the benchmark, and the settings. Re-evaluating a checkpoint you already scored costs nothing.
- **`seed=0`** makes a retried evaluation produce the same samples.

Run one task per checkpoint and benchmark, all at once:

```python
import asyncio


@driver_env.task(report=True)
async def evaluate_checkpoints(
    base: flyte.io.Dir, adapters: list[flyte.io.Dir], benchmarks: list[str]
) -> list[dict[str, float]]:
    candidates = [None, *adapters]  # the base model first
    return await asyncio.gather(
        *(evaluate_policy(base, a, b) for a in candidates for b in benchmarks)
    )
```

Train on one set of problems and evaluate on problems the policy never saw, such as a held-out split of the same dataset or a public benchmark: AIME and MATH-500 for math, LiveCodeBench for code, or SWE-bench Verified and Terminal-Bench for agents. Check that no evaluation problem appears in the training prompts.

## Evaluate during training

Evaluate the policy every few iterations, so you see held-out accuracy next to the training reward. In the driver loop, launch the evaluation of iteration N with `asyncio.create_task` and collect it later, so it never sits between iterations. See [Overlap generation with training](./training-loop#overlap-generation-with-training).

Evaluate the base model before the first iteration too, so every later score has a baseline. Afterwards, evaluate every saved checkpoint on the full benchmarks. The best checkpoint is often not the last one.

## Watch training health

Some failures show up in the loop's own numbers before they show up in an evaluation. Log these from the train task every iteration, and plot them in the driver's report:

| Metric | What to watch for |
|---|---|
| Mean reward, and each reward component | A reward that rises while held-out accuracy stays flat |
| Reward standard deviation within groups | Falling toward zero, which means the policy gives every completion the same score |
| Fraction of groups with zero advantage | A high fraction means most prompts give no learning signal, because they are too easy or too hard |
| Policy entropy | A fast collapse toward zero, which means the policy has stopped exploring |
| KL divergence to the reference model | Steady growth, which means the policy is drifting far from the base model |
| Clip fraction | A high fraction means the policy changes too much per step |
| Mean response length, and the fraction cut off at the length limit | Growth without a gain in accuracy, or completions that hit the limit |

## Catch reward hacking

The policy optimizes the reward you wrote, including its mistakes. Look for these signs:

- **The training reward and held-out accuracy diverge.** The reward keeps rising, and accuracy on the held-out verifier doesn't.
- **A judge and a verifier disagree.** If the reward uses an LLM judge, score a sample of completions with a deterministic verifier or a second judge, and track how often they disagree.
- **The output gets longer without getting better.** A judge that prefers longer answers rewards length itself.
- **The verifier accepts wrong answers.** Before training, test the reward against outputs that should fail, such as answers in the wrong format or empty code.

Keep the evaluation verifier separate from the reward function, so a flaw in the reward doesn't also hide in the evaluation. Because every completion a rollout task returns is stored, you can read the completions the reward scored highest at any iteration and check them yourself.

## Check what the policy may have lost

RL on a narrow task can lower performance on others. Rerun a broad suite, such as instruction-following and general-knowledge benchmarks, on the final policy and on the base model. [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) and [lighteval](https://github.com/huggingface/lighteval) run standard benchmarks with a vLLM backend. [Inspect](https://inspect.aisi.org.uk/) runs agentic and multi-turn evaluations. Run each suite in its own task, so suites run in parallel and are cached separately.

## Compare runs across seeds

Two RL runs with different seeds can end far apart. Before you conclude that one setting beats another, train each with several seeds and compare the distributions, not single runs. For classic RL, report the episode return over 10 or more seeds with confidence intervals, and use the interquartile mean, which is less sensitive to outlier runs. [rliable](https://github.com/google-research/rliable) computes both. Each seed is its own run of the training loop, so launch them in parallel from one driver.

## Related

- [Reward setup](./reward-setup): the reward the policy trains on.
- [Training loop](./training-loop): where evaluation runs during training.
- [Evaluation gates](../project-patterns/software-development-lifecycle/evaluation-gates): promote a policy only when it beats what is live.
- [Evaluation](../model-training/evaluation): evaluating supervised models.
