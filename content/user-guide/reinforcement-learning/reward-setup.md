---
title: Reward setup
description: Score rollouts with verifiers, reward functions, and LLM judges in their own CPU tier, without paying for a judge twice or regenerating rollouts to try a new reward.
icon: bullseye
weight: 2
variants: +flyte +union
---

# Reward setup

The reward turns what the policy did into the number the trainer optimizes. Most rewards combine some of these:

- **A verifier** checks a result against ground truth: an exact answer, a passing test suite, or a state the environment can confirm. It is deterministic and cheap.
- **A rule-based score** rewards properties of the output, such as the requested format or a length limit.
- **A judge** is a model that grades what a verifier can't check, such as helpfulness or efficiency. It is slower, costs money per call, and can fail.

In Flyte, scoring runs in its own CPU environment. It never holds a GPU, and its retries and timeouts are separate from generation and training.

## Write a verifiable reward

A verifiable reward is a plain Python function. This one gives 1.0 for the correct answer and 0.2 for using the required answer format:

{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="reward" lang=python >}}

Keep the reward function outside of any task, so you can unit-test it against hand-labeled completions without running the loop.

## Score a group per task

A rule-based reward takes microseconds, so a task per completion would spend nearly all of its time starting containers. Score a whole group of completions in one task:

{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="reward_env" lang=python >}}

{{< code file="/unionai-examples/v2/tutorials/rl_grpo_lora/rl_grpo_lora.py" fragment="score_group" lang=python >}}

The group is the unit the rollout task already returns, and the unit GRPO normalizes rewards over. Scoring at that granularity keeps reward observable as its own step in the UI, at a fraction of the task count. The driver scores each group as soon as its rollouts arrive. See [Training loop](./training-loop).

## Call a judge without paying for it twice

A judge call is an API request that costs money and can fail after it returns, for example while uploading the result. Wrap the call in `@flyte.trace`, so a retried task replays the recorded result instead of calling the judge again:

{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="judge" lang=python >}}

`verify_and_judge` combines both kinds of signal: the deterministic verifier decides whether the answer is correct, and the judge grades how the policy got there. The task returns a typed `Reward`, so each component is visible in the UI and the trainer can weight them. See [Traces](../tasks/task-programming/traces).

## Change the reward without regenerating rollouts

Reward design is iterative. When you change the rubric, the rollouts from earlier steps are still valid inputs, and regenerating them costs GPU time. Pass the rubric to the loop as an input, and choose how to reuse the rollouts:

**Recover the finished run with a new rubric.** Every action whose inputs didn't change is reused, and judging and training run again:

{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="fork" lang=python >}}

See [Recover a failed run](../tasks/task-deployment/recover-runs#changing-inputs).

**Start a new run and let the cache find the reuse.** Set `cache="auto"` on the world-building and rollout tasks. A new run with a new rubric gets every rollout whose inputs are unchanged from the cache:

{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="rescore" lang=python >}}

Either way, the first step's rollouts are reused, because the worlds and starting weights are the same. After the new reward changes the weights, later rollouts have different inputs and run again. Flyte finds that boundary from the inputs, without any extra code.

## Related

{{< variant union >}}
{{< markdown >}}

- [RL for LLMs with GRPO and LoRA](../../tutorials/reinforcement-learning/grpo-lora/_index): the verifiable reward and group scoring on this page.

{{< /markdown >}}
{{< /variant >}}

- [Durable agentic RL with SkyRL and Harbor](../../tutorials/reinforcement-learning/agentic-rl-skyrl/_index): the judge on this page, and re-scoring old rollouts with a new rubric.
- [Training environment](./training-environment): what produces the trajectories you score.
- [Training loop](./training-loop): how rewards become advantages for the policy update.
- [Run model-written code safely](./training-environment#run-model-written-code-safely): sandbox the code a reward executes.
- [Evaluation gates](../project-patterns/software-development-lifecycle/evaluation-gates): score a model before it is promoted.
