---
title: Agent chat UI
weight: 5
variants: +flyte +serverless +union
mermaid: true
---

# Agent chat UI

A useful way to interact with an agent is through a chat interface. Because {{< key product_name >}} can [host apps](../build-apps/_index) behind a URL, you can serve a chat UI for your agent with no separate infrastructure. There are two approaches:

1. **`AgentChatAppEnvironment`** — the fastest path. Any agent that implements the `AgentProtocol` (including the built-in `Agent`, in tool-use or `code_mode`) gets a hosted chat shell, tool sidebar, and streaming for free.
2. **A custom FastAPI app** — full control over the UI. Wrap the agent in a `FastAPIAppEnvironment` and serve your own HTML/CSS/JS.

Both reuse the same agent object, so you can start with the built-in shell and graduate to a custom UI later.

## Option 1: the built-in chat UI

`flyte.ai.chat.AgentChatAppEnvironment` wraps an agent in a hosted chat app. Since `Agent` implements the `AgentProtocol`, it plugs straight in:

{{< code file="/unionai-examples/v2/user-guide/build-agent/agent-chat-ui/agent_chat_ui.py" fragment="all" lang="python" >}}

The `task_entrypoint` is a parent task that owns the agent loop, so the nested durable tool tasks run correctly under it. The chat shell streams progress by subscribing to the agent's `agent_progress_cb` events.

## Option 2: a custom FastAPI chat app

When you want to control the look and feel, wrap any `AgentProtocol`-compatible agent in a `FastAPIAppEnvironment` and serve your own UI. A natural fit is an `Agent` in **code mode** (`code_mode=True`): each turn the LLM writes Python that runs in a [sandbox](../sandboxing/_index) with the tools exposed as functions, returning code + a summary (and any charts you choose to surface), all behind a conversational web interface.

The architecture is small:

```
Browser (Chat UI)
  ├── GET  /            -> embedded HTML/CSS/JS chat interface
  ├── GET  /api/tools   -> JSON list of available tool descriptions
  └── POST /api/chat    -> { message, memory } -> { code, charts, summary, error }
           └── Agent.run(message, memory)
```

The app itself is just a FastAPI server. The endpoints call the agent's `run.aio` and `tool_descriptions` methods:

```python
import pathlib

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import flyte
from flyte.ai.agents import Agent
from flyte.app.extras import FastAPIAppEnvironment

app = FastAPI(title="Chat Data Analytics Agent")

env = FastAPIAppEnvironment(
    name="chat-analytics-agent",
    app=app,
    image=flyte.Image.from_debian_base().with_pip_packages(
        "fastapi", "uvicorn", "httpx", "pydantic-monty", "litellm",
    ),
    secrets=flyte.Secret(key="internal-anthropic-api-key", as_env_var="ANTHROPIC_API_KEY"),
    scaling=flyte.app.Scaling(replicas=1),
)

agent = Agent(
    name="analytics",
    instructions="You are a data analyst. Use the tools to fetch, aggregate, and chart data.",
    tools=ALL_TOOLS,
    code_mode=True,
    max_turns=15,
)


class ChatRequest(BaseModel):
    message: str
    memory: list[dict] = []


class ChatResponse(BaseModel):
    code: str = ""
    charts: list[str] = []
    summary: str = ""
    error: str = ""


@app.get("/api/tools")
async def get_tools() -> list[dict]:
    """Return JSON descriptions of available tool functions (for the sidebar)."""
    return agent.tool_descriptions()


@app.post("/api/chat")
async def chat(req: ChatRequest) -> ChatResponse:
    """Generate code, run it in the sandbox, and return results."""
    result = await agent.run.aio(req.message, memory=req.memory)
    return ChatResponse(code=result.code, charts=result.charts,
                        summary=result.summary, error=result.error)


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    """Serve the embedded chat UI."""
    return HTMLResponse(content=CHAT_HTML)


if __name__ == "__main__":
    flyte.init_from_config(root_dir=pathlib.Path(__file__).parent)
    app_handle = flyte.serve(env)
    print(f"Deployed Chat Analytics Agent: {app_handle.url}")
```

`CHAT_HTML` is the embedded front-end (a single HTML string with the chat markup, styles, and a small fetch-based client that POSTs to `/api/chat` and renders the returned charts and summary). `ALL_TOOLS` is the agent's tool registry. Keeping both in their own modules means adding a tool is the only change required — the agent auto-generates its system prompt from each tool's signature and docstring.

Run it locally during development, then deploy with one command:

```bash
# Local development
python chat_app.py

# Deploy to {{< key product_name >}}
flyte deploy chat_app.py env
```

{{< key product_name >}} assigns a URL, handles TLS, and auto-scales the app.

> [!TIP]
> Drop `code_mode=True` to serve a standard tool-use [`Agent`](./flyte-agents) (or plug in any object implementing the `AgentProtocol`) behind the same UI. The endpoints only depend on `run.aio` and `tool_descriptions`.

## Next steps

- [The Flyte Agent harness](./flyte-agents): the agent powering the chat UI.
- [Sandboxing](../sandboxing/_index): how an `Agent` in code mode safely executes generated code.
- [Deploy an agent as a service](./deploy-agent-as-service): other ways to run an agent (task, schedule, webhook).
