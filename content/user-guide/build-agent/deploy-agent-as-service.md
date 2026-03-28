---
title: Deploy an agent as a service
weight: 2
variants: +flyte +serverless +union
mermaid: true
---

# Deploy an agent as a service

{{< key product_name >}} makes it straightforward to deploy internal apps (chatbots, dashboards, API endpoints) behind a URL, with no separate infrastructure. This is how you turn an agent into a hosted service that your team (or other agents) can call.

## Chat agent with Gradio

This example takes the ReAct agent from [Building agentic workflows](./building-agents) and wraps it in a Gradio chat interface, deployed as a {{< key product_name >}} app. Users interact in the browser, and each reasoning step streams back in real time.

```python
# app.py
import json

import gradio as gr

import flyte
from flyte.app import AppEnvironment
from openai import AsyncOpenAI

# --- ReAct agent (same pattern as the ReAct agent in Building agentic workflows on {{< key product_name >}}) ---

TOOLS = {"add": lambda a, b: a + b, "multiply": lambda a, b: a * b}

async def reason(goal: str, history: str) -> dict:
    """LLM picks a tool or returns a final answer."""
    r = await AsyncOpenAI().chat.completions.create(
        model="gpt-4.1-nano",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content":
                f"Tools: {list(TOOLS)}. Respond JSON: "
                '{"thought":..,"tool":..,"args":{}} or '
                '{"thought":..,"done":true,"answer":..}'},
            {"role": "user", "content": f"Goal: {goal}\n\n{history}\nWhat next?"},
        ],
    )
    return json.loads(r.choices[0].message.content)

async def act(tool: str, args: dict) -> str:
    """Execute the chosen tool."""
    return str(TOOLS[tool](**args))

async def react_agent(message: str, history: list):
    """ReAct loop that streams intermediate steps, then the final answer."""
    output, trace = "", ""
    for step in range(1, 11):
        decision = await reason(message, trace)
        if decision.get("done"):
            yield output + f"\n\n**Answer:** {decision['answer']}"
            return
        result = await act(decision["tool"], decision["args"])
        trace += (
            f"Step {step}: {decision['thought']} "
            f"-> {decision['tool']}({decision['args']}) = {result}\n"
        )
        output += (
            f"**Step {step}:** {decision['thought']}\n"
            f"`{decision['tool']}({decision['args']})` -> `{result}`\n\n"
        )
        yield output
    yield output + "\n\nMax steps reached."

# --- Deploy as a {{< key product_name >}} app ---

serving_env = AppEnvironment(
    name="react-agent-chat",
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "gradio", "openai",
    ),
    secrets=[flyte.Secret(key="OPENAI_API_KEY")],
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
    port=7860,
)

@serving_env.server
def server():
    gr.ChatInterface(
        react_agent,
        title="ReAct Agent",
        examples=["What is (12 + 8) * 3?", "Add 99 and 1, then multiply by 5"],
    ).launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    flyte.init_from_config()
    flyte.serve(serving_env)
```

Run locally, then deploy to {{< key product_name >}} with one command:

```bash
# Local development
python app.py

# Deploy to {{< key product_name >}}
flyte deploy app.py serving_env
```

{{< key product_name >}} assigns a URL, handles TLS, and auto-scales the app.

**What's happening under the hood:**

- `AppEnvironment` defines the container image, secrets, resources, and port for the app
- `@serving_env.server` marks the function that {{< key product_name >}} calls on remote deployment
- `gr.ChatInterface` with an async generator gives streaming output: users see each reasoning step appear as the agent works
- `requires_auth=False` makes the app publicly accessible; set to `True` to require {{< key product_name >}} authentication

## Other deployment patterns

**FastAPI endpoint:** For API-first agents, use `FastAPIAppEnvironment` to expose your agent behind a REST endpoint that other services or agents can call programmatically.

**Webhook-triggered workflows:** [Deploy a FastAPI app](../build-apps/fastapi-app) that receives webhooks and calls `flyte.run()` on a [remote task](../task-programming/remote-tasks) to kick off longer agentic workflows as background tasks.

**Model serving:** [Serve open-weight LLMs](../build-apps/vllm-app) on GPUs behind an OpenAI-compatible API with `VLLMAppEnvironment` or `SGLangAppEnvironment`.

> [!TIP]
> See [Build Apps](../build-apps/_index), [App usage patterns](../build-apps/app-usage-patterns), and [Configure Apps](../configure-apps/_index) for more details.
> For a hands-on example with a research agent Gradio UI, see [workshops/starter-examples/flyte-local-dev](https://github.com/unionai/workshops/tree/main/tutorials/starter-examples/flyte-local-dev).
