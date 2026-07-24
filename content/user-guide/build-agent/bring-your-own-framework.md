---
title: Bring your own framework
weight: 3
variants: +flyte +serverless +union
---

# Bring your own framework

The [supported plugins](../../integrations/agents/_index) are worked examples of one underlying idea: **{{< key product_name >}} is the runtime, your framework is the loop.** If your agent library is written in Python, it runs on {{< key product_name >}} with no special plugin.

This page is a framework-agnostic template for the frameworks that don't have one. Drop in any library ([AutoGen](https://microsoft.github.io/autogen/), [smolagents](https://github.com/huggingface/smolagents), [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents), a raw provider SDK, or your own homegrown loop) wherever the comments say so.

> [!NOTE] Check for a plugin first
> If your framework is one of the ten with a first-party adapter, use that instead. The plugins give you per-tool containerization, model-turn replay and cross-run memory that this template does not. See [Agent frameworks](../../integrations/agents/_index).

## How much control does the framework give you?

Frameworks differ in how much of the agent loop they own, which shapes how you integrate them:

| Level of control | What it means | Integration pattern |
|------------------|---------------|---------------------|
| **You own the loop** | The framework gives you primitives (graph nodes, tools) and you wire the control flow | Decorate nodes with `@flyte.trace` and run the compiled graph inside a task |
| **The framework owns the loop, you own the tools** | The framework runs the tool-calling loop; you provide tools as plain functions | Have tools delegate to durable `@env.task`s |
| **The framework owns everything** | The framework builds and runs the agent from configuration | Wrap the whole run in a task and trace the seam below the loop |

Whichever model your framework uses, the integration is the same in spirit: the framework decides *what* the agent does next, and {{< key product_name >}} decides *where and how durably* each step runs.

## The core pattern

Put your framework's agent invocation inside an `@env.task`. The task gives you a container, durable inputs/outputs, retries, and a span in the dashboard. Everything inside the task is ordinary Python, so the framework behaves exactly as it does locally.

```python
import flyte

# 1. Declare the runtime: image (with YOUR framework's deps), resources, secrets.
env = flyte.TaskEnvironment(
    name="my-agent",
    image=flyte.Image.from_debian_base(python_version=(3, 13)).with_pip_packages(
        # --> your agent framework + its provider packages go here, e.g.:
        # "crewai", "smolagents", "autogen-agentchat", ...
    ),
    resources=flyte.Resources(cpu=1, memory="1Gi"),
    secrets=[flyte.Secret(key="ANTHROPIC_API_KEY")],  # --> your model provider key(s)
)


@env.task(report=True)
async def run_agent(prompt: str) -> str:
    # 2. Build/configure your framework's agent exactly as you would locally.
    #    --> your framework setup goes here
    # agent = MyFramework.Agent(model=..., tools=[...], instructions=...)

    # 3. Run it. Use the framework's own (sync or async) entry point.
    #    --> invoke your framework here
    # result = await agent.run(prompt)

    # 4. Return a serializable value (str, pydantic model, dataclass, ...).
    # return result.output
    ...


if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(run_agent, prompt="...")  # --> your prompt / inputs
    print(run.url)
```

That is the whole integration. The remaining sections are optional enhancements that make the framework more durable and observable.

## Make tools durable

Most frameworks let a tool be any Python callable. To make a tool durable, retryable, and independently observable, have the framework's tool delegate to an `@env.task`. The framework still "owns" the tool; the heavy lifting runs on-cluster.

```python
# A durable task that does the real work (IO, compute, external calls).
@env.task
async def fetch_data(source: str) -> dict:
    # --> your real tool implementation (API call, DB query, scrape, ...)
    ...


# Register it with your framework using whatever tool API it exposes.
# The body just awaits the durable task.
#
#   @my_framework.tool                  # --> your framework's tool decorator/registration
#   async def get_data(source: str) -> dict:
#       """Tool description the LLM sees."""
#       return await fetch_data(source)   # runs as a Flyte task, durable + traced
```

> [!TIP]
> Reach for an `@env.task` when a tool does real work you want retried, cached, or run on its own hardware (GPU, more memory). For lightweight in-process helpers, a plain `@flyte.trace` function (below) is enough.

## Trace the framework's internals

If your framework exposes hooks, callbacks, or lets you wrap its node/step functions, decorate those with `@flyte.trace` to turn each LLM call, tool call, and routing decision into a span, with inputs and outputs captured and checkpointed.

```python
@flyte.trace
async def call_model(messages: list[dict]) -> str:
    # --> wrap the framework's model call (or pass this as the framework's LLM hook)
    ...


@flyte.trace
async def route(state) -> str:
    # --> wrap a routing / decision function so the branch is visible in the dashboard
    ...
```

For frameworks that don't expose hooks, wrap the whole run in `flyte.group(...)` to keep its trace tidy:

```python
@env.task(report=True)
async def run_agent(prompt: str) -> str:
    with flyte.group("my-framework-run"):  # groups everything below under one span
        # --> your framework invocation
        ...
```

## Fan out across containers

Run many independent agents in parallel, each in its own container, with `asyncio.gather()`. This works for any framework because each call is just an awaited task.

```python
import asyncio


@env.task
async def run_one(task_input: str) -> str:
    # --> one self-contained agent run for a single input
    ...


@env.task
async def run_many(inputs: list[str]) -> list[str]:
    # Each run_one call lands in its own container.
    results = await asyncio.gather(*[run_one(i) for i in inputs])
    return list(results)
```

## Checklist

To bring any Python agent framework onto {{< key product_name >}}:

1. **Wrap the run**: call the framework's entry point inside an `@env.task`.
2. **Declare deps**: add the framework + provider packages to the task's `image`.
3. **Supply secrets**: mount model-provider API keys via `flyte.Secret`.
4. **(Optional) Durable tools**: have tools delegate to `@env.task`s.
5. **(Optional) Observe**: decorate hooks/steps with `@flyte.trace`, or wrap in `flyte.group(...)`.
6. **(Optional) Scale**: fan out with `asyncio.gather()` for parallel, per-container runs.

## Next steps

- [Agent frameworks](../../integrations/agents/_index): the ten frameworks with a first-party plugin, if yours is one of them.
- [The Flyte Agent harness](./flyte-agents): a built-in, batteries-included loop if you'd rather not bring a framework.
- [Build an agent with pure Python](./python-agents): hand-roll the loop with no framework at all.
- [Deploy an agent as a service](./deploy-agent-as-service): run your agent on a schedule or behind a webhook.
