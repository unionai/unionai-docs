---
title: Training environment
description: Set up what the policy acts in, from datasets of verifiable problems to simulators and sandboxed agent environments, with each episode isolated and reproducible.
icon: globe2
weight: 1
variants: +flyte +union
---

# Training environment

The environment is what the policy acts in and what produces the observations a reward scores. Its shape depends on the task:

| Environment | Example | Each episode is |
|---|---|---|
| A dataset of verifiable problems | Math word problems with known answers | One prompt, and the completions the policy samples for it |
| A simulator | A MuJoCo or Brax physics model | A trajectory of observations, actions, and rewards |
| A sandboxed world | A filesystem and tools an agent explores | A multi-turn trajectory of tool calls and their results |

Whatever the shape, the environment has to be cheap to reset, isolated between episodes, and reproducible, so that a retried episode produces the same result.

## Use a dataset as the environment

For RL on reasoning tasks, the environment is a set of prompts with checkable answers. The driver samples a batch each iteration, and the reward compares each completion with the answer. Load the dataset in a task with `cache="auto"`, or bundle a small one with the code. The loop on these pages rotates through a fixed list of prompts:

```python
def _sample_prompts(iteration: int) -> list[tuple[str, str]]:
    start = (iteration * PROMPTS_PER_ITER) % len(DATASET)
    return [DATASET[(start + i) % len(DATASET)] for i in range(PROMPTS_PER_ITER)]
```

Sampling deterministically from the iteration number means a resumed loop picks up the same prompts it would have used.

## Build a world once and share it

An agentic environment is a world the policy explores, such as a directory of documents, a repository, or a database. Building it can take longer than an episode, so build each world once in a cached task and pass it to every episode:

{{< variant flyte >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable_oss.py" fragment="build-world" lang=python >}}
{{< markdown >}}

The world is a `flyte.io.Dir` in your object store. Each episode downloads its own copy, so changes one episode makes to its files never reach another.

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="build-world" lang=python >}}
{{< markdown >}}

The world is a read-only [volume](../tasks/task-programming/volumes/_index). Each episode forks it into an instant private copy and mounts the fork:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/skyrl/agentic_rl_durable.py" fragment="generate" lang=python >}}
{{< /variant >}}

`cache="auto"` on the build task means every run, including one that re-scores old episodes with a new reward, gets the same world. That keeps the cache keys of the downstream tasks stable.

## Run each episode in its own task

Running an episode as its own task gives it the properties an environment needs:

- **Isolation.** Each episode gets a fresh container, so a policy that deletes files or fills the disk only affects its own episode.
- **Limits.** `timeout=flyte.Timeout(max_runtime=300)` stops an episode that loops forever, and `retries=1` reruns one that hits a transient failure.
- **Reproducibility.** Seed the episode's randomness from its ID, so a retry produces the same trajectory instead of a different one.
- **Separate sizing.** The environment tier gets CPU and memory for the simulator or tools, with no GPU.

Episodes are independent, so the driver launches all of them at once with `asyncio.create_task` and collects them with `asyncio.as_completed`. It awaits each episode in a `try` block, so an episode that still fails after its retries is skipped instead of failing the iteration. See [Training loop](./training-loop).

## Run model-written code safely

When the policy writes code that runs during an episode or during scoring, such as a generated function and the test suite that checks it, run that code in a sandbox rather than in the task's own process. See [Code sandboxing](../agents/sandboxing/code-sandboxing), and the [MLE bot](../../tutorials/agents/mle-bot/_index) tutorial for an agent whose generated code runs in a sandbox.

## Serve the environment as an app

Some environments are long-running servers that clients step through over HTTP, such as an environment that keeps game state between calls. Deploy the server as an [app](../apps/_index) and connect to it from the rollout tasks by its URL. The app scales and restarts independently of the training loop, and any number of rollout tasks can share it.

## Related

- [Reward setup](./reward-setup): score what happened in each episode.
- [Inference rollouts](./inference-rollouts): generate the policy's actions.
- [Durable agentic RL with SkyRL and Harbor](../../tutorials/frontier-ai/agentic-rl-skyrl/_index): the world-building and episode code on this page, in a complete loop.
