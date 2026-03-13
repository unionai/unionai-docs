---
title: Programmatic tool calling for agents
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
llm_readable_bundle: true
---

# Programmatic tool calling for agents

**Programmatic tool calling** (also known as **code mode**) is a pattern where LLMs write executable code instead of making individual tool calls.
Rather than the model emitting a sequence of JSON tool-call objects and the system routing each one, the model generates a single block of code that calls multiple tools, transforms data, and applies logic — all executed in a sandbox.

The key insight: LLMs are trained on billions of lines of code, but only a small amount of synthetic tool-call data.
Code generation is a more natural and reliable output modality for models than structured tool-call schemas.

## Programmatic tool calling vs sequential tool calling

In sequential tool calling, every intermediate result passes through the model's context window.
The model calls one tool, reads the result, decides what to do next, calls another tool, and so on.
Each round-trip costs tokens and latency.

With programmatic tool calling, the model generates a complete program upfront.
The sandbox executes it, and only the final result returns to the model.

| Aspect | Sequential tool calling | Programmatic tool calling |
|--------|-------------|-----------|
| **Output format** | JSON tool-call objects, one at a time | A single block of executable code |
| **Data flow** | Every intermediate result passes through the model | Intermediate results stay in the sandbox |
| **Context overhead** | Grows with each tool call (all results in context) | Fixed — only tool signatures in context |
| **Multi-step logic** | Model re-invoked at every step | Sandbox executes loops, conditionals, transforms |
| **Scaling with tools** | Context grows linearly with number of tool definitions | Tools discovered progressively or loaded on demand |

## Why programmatic tool calling is powerful

### Token efficiency

Sequential tool calling loads all tool definitions into the context window upfront and passes every intermediate result through the model.
Programmatic tool calling reduces this dramatically:

- **98%+ context reduction** reported by Anthropic when using code execution with MCP servers — from 150,000 tokens down to 2,000 tokens for the same task.
- **99.9% reduction** reported by Cloudflare for large APIs — approximately 1,000 tokens with programmatic tool calling versus 1.17 million tokens when exposing each API endpoint as a separate tool.

### Performance

By eliminating round-trips through the model for intermediate steps, programmatic tool calling achieves significant speed improvements.
The sandbox evaluates conditionals, loops, and data transformations locally — no "time to first token" delay for each step.

### Natural programming patterns

Code naturally expresses patterns that are awkward or impossible in tool-call sequences:

- **Loops**: Process a list of items without the model deciding "call this tool again" for each one
- **Conditionals**: Branch on intermediate results without another model invocation
- **Data transformation**: Filter, map, and aggregate data before passing it to the next tool
- **Variable reuse**: Store intermediate results and reference them later

### Progressive tool discovery

Instead of loading hundreds of tool definitions into the context window, programmatic tool calling supports progressive discovery.
The model can search for relevant tools, load only what it needs, and compose them in code.

### Data privacy

Intermediate results stay in the sandbox execution environment.
They never re-enter the model's context window, which means sensitive data (PII, credentials, financial records) can be processed without the model seeing it.

## Example: sequential vs programmatic tool calling

Consider a task: "Analyze sales data, filter for Q4, calculate statistics, and create a chart."

### Sequential tool calling approach

The model makes serial tool calls, with each result passing through the context window:

```
Step 1: Model → tool_call: fetch_data("sales_2024")
        Result: [150KB of sales data] → back into model context

Step 2: Model → tool_call: filter_data(data, "month", ">=", "Oct")
        Result: [40KB of filtered data] → back into model context

Step 3: Model → tool_call: calculate_statistics(filtered, "revenue")
        Result: {"mean": 112000, ...} → back into model context

Step 4: Model → tool_call: create_chart("bar", "Q4 Revenue", ...)
        Result: "<canvas>...</canvas>" → back into model context
```

Four round-trips through the model.
The 150KB dataset enters the context window and stays there.

### Programmatic tool calling approach

The model generates a single code block:

```python
data = fetch_data("sales_2024")
q4_months = ["Oct", "Nov", "Dec"]
q4_data = [row for row in data if row["month"] in q4_months]
stats = calculate_statistics(q4_data, "revenue")

months = []
revenues = []
for row in q4_data:
    if row["month"] not in months:
        months.append(row["month"])
for month in months:
    total = 0
    for row in q4_data:
        if row["month"] == month:
            total = total + row["revenue"]
    revenues.append(total)

chart = create_chart("bar", "Q4 Revenue by Month", months, revenues)
{"charts": [chart], "summary": "Q4 stats: " + str(stats)}
```

One model invocation.
The data never re-enters the model's context window.
The sandbox handles the filtering, aggregation, and chart creation locally.

## Example: defining tools

Tools are plain Python functions with type annotations and docstrings.
The agent auto-generates its system prompt from these signatures, so adding a tool requires no other changes.

```python
async def fetch_data(dataset: str) -> list:
    """Fetch tabular data by dataset name.

    Available datasets:
    - "sales_2024": columns month, region, revenue, units
    - "employees": columns name, department, salary, years_exp, performance_rating
    - "website_traffic": columns date, page, visitors, bounce_rate, avg_duration
    - "inventory": columns product, category, stock, price, supplier
    """
    ...


async def create_chart(chart_type: str, title: str, labels: list, values: list) -> str:
    """Generate a self-contained Chart.js HTML snippet.

    Args:
        chart_type: One of "bar", "line", "pie", "doughnut".
        title: Chart title displayed above the canvas.
        labels: X-axis labels (or slice labels for pie/doughnut).
        values: Either a flat list of numbers, or a list of
                {"label": str, "data": list[number]} dicts for multi-series.
    """
    ...


async def calculate_statistics(data: list, column: str) -> dict:
    """Calculate descriptive statistics for a numeric column.

    Returns dict with keys: count, mean, median, min, max, std_dev.
    """
    ...


async def filter_data(data: list, column: str, operator: str, value: object) -> list:
    """Filter rows where column matches the condition.

    Operator: one of "==", "!=", ">", ">=", "<", "<=".
    """
    ...


ALL_TOOLS = {
    "fetch_data": fetch_data,
    "create_chart": create_chart,
    "calculate_statistics": calculate_statistics,
    "filter_data": filter_data,
}
```

The `ALL_TOOLS` dict is the single source of truth.
The agent introspects it to build the system prompt, and the sandbox uses it to resolve function calls.

## Example: programmatic tool-calling agent

The `CodeModeAgent` implements the generate-execute-retry loop:

```python
import flyte.sandbox
from _tools import ALL_TOOLS


class CodeModeAgent:
    def __init__(self, tools, *, model="claude-sonnet-4-6", max_retries=2):
        self._tools = tools
        self._model = model
        self._max_retries = max_retries
        # System prompt auto-generated from tool signatures + docstrings
        self.system_prompt = self._build_system_prompt()

    async def run(self, message: str, history: list[dict]) -> AgentResult:
        messages = [*history, {"role": "user", "content": message}]

        # Step 1: LLM generates Python code
        code = await generate_code(self._model, self.system_prompt, messages)

        # Step 2: Execute in Monty sandbox with registered tools
        for attempt in range(1 + self._max_retries):
            try:
                result = await flyte.sandbox.orchestrate_local(
                    code,
                    inputs={"_unused": 0},
                    tasks=list(self._tools.values()),
                )
                return AgentResult(code=code, charts=result.get("charts", []),
                                   summary=result.get("summary", ""))
            except Exception as exc:
                if attempt < self._max_retries:
                    # Step 3: Feed error back to LLM for retry
                    code = await generate_code(
                        self._model, self.system_prompt,
                        [*messages,
                         {"role": "assistant", "content": f"```python\n{code}\n```"},
                         {"role": "user", "content": f"Error: {exc}\nFix the code."}],
                    )
                    continue
                return AgentResult(code=code, error=str(exc))
```

The pattern:

1. **Generate**: The LLM receives tool signatures and the user's request, and outputs Python code.
2. **Execute**: The code runs in the Monty sandbox. Tool calls pause the sandbox, dispatch to real implementations, and resume with results.
3. **Retry**: If execution fails, the error message is fed back to the LLM, which generates a corrected version. This repeats up to `max_retries` times.

## Example: chat app

Wrap the agent in a FastAPI endpoint to create a conversational analytics assistant:

```python
from _agent import CodeModeAgent
from _tools import ALL_TOOLS
from fastapi import FastAPI

import flyte
from flyte.app.extras import FastAPIAppEnvironment

app = FastAPI(title="Chat Data Analytics Agent")

env = FastAPIAppEnvironment(
    name="chat-analytics-agent",
    app=app,
    image=flyte.Image.from_debian_base().with_pip_packages(
        "fastapi", "uvicorn", "httpx", "pydantic-monty",
    ),
    secrets=flyte.Secret(key="anthropic-api-key", as_env_var="ANTHROPIC_API_KEY"),
)

agent = CodeModeAgent(tools=ALL_TOOLS, max_retries=2)


@app.post("/api/chat")
async def chat(req: ChatRequest) -> ChatResponse:
    result = await agent.run(req.message, req.history)
    return ChatResponse(
        code=result.code,
        charts=result.charts,
        summary=result.summary,
        error=result.error,
    )
```

Users send natural language requests (`"Show me monthly revenue trends for 2024"`), the agent generates analysis code, the sandbox executes it with the registered tools, and the response includes charts and a text summary.

## Example: durable agent

For production workloads, wrap the tools as `@env.task` so the sandbox dispatches them as durable Flyte tasks through the controller.
This gives you execution history, retries, caching, and full observability.

```python
from _agent import CodeModeAgent
from _tools import ALL_TOOLS

import flyte
import flyte.report

env = flyte.TaskEnvironment(
    name="llm-code-mode",
    secrets=[flyte.Secret(key="anthropic-api-key", as_env_var="ANTHROPIC_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages(
        "httpx", "pydantic-monty", "unionai-reuse",
    ),
)


# Wrap each tool as a durable task
@env.task
async def fetch_data(dataset: str) -> list:
    return await _tools.fetch_data(dataset)


@env.task
async def create_chart(chart_type: str, title: str, labels: list, values: list) -> str:
    return await _tools.create_chart(chart_type, title, labels, values)

# ... wrap remaining tools similarly ...


# Agent uses plain functions for prompt generation,
# @env.task versions for durable sandbox execution
durable_tools = {t.func.__name__: t for t in [fetch_data, create_chart, ...]}
agent = CodeModeAgent(tools=ALL_TOOLS, execution_tools=durable_tools)


@env.task(report=True)
async def analyze(request: str) -> str:
    """Run the code-mode agent and render an HTML report."""
    result = await agent.run(request, [])
    report_html = build_report(request, result)
    await flyte.report.replace.aio(report_html)
    await flyte.report.flush.aio()
    return result.summary
```

The key difference from the chat app: each tool call goes through the Flyte controller as a durable task.
If `fetch_data` fails, Flyte retries it automatically.
Every tool invocation is recorded and visible in the execution timeline.

Run it with:

```bash
flyte run durable_agent.py analyze \
    --request "Show me monthly revenue trends for 2024, broken down by region"
```

## References

- [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic engineering blog on the code execution pattern
- [Code Mode](https://blog.cloudflare.com/code-mode/) — Cloudflare's introduction to code mode for LLM tool calling
- [Code Mode MCP](https://blog.cloudflare.com/code-mode-mcp/) — Cloudflare's server-side code mode implementation
- [Code Mode Protocol](https://github.com/universal-tool-calling-protocol/code-mode) — Open specification for the code mode pattern
