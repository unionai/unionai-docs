---
title: Code mode analytics agent
weight: 8
variants: +flyte +union
---

# Code mode analytics agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/code_mode_agent).

This tutorial builds a "chat with your data" app. You ask a question in the browser, and the app launches a Flyte run to answer it. Inside that run, Claude writes one small Python program, the program executes in Flyte's [Monty sandbox](../../../user-guide/sandboxing/code-sandboxing), and the only things it can touch are the tools you registered. The heavy tool, a DuckDB `query`, is a durable Flyte task, so every query the model writes shows up as a tracked, retryable child task you can open in the UI. The cheap tools that render metrics, charts, and tables run in-process. The app itself is a thin front end that gates access behind Union auth and hands each question off to a real workflow.

![Code mode analytics agent](../../../_static/images/tutorials/code_mode_agent/code-mode-agent.gif)

## Why code mode

Most tool-using agents call tools one at a time. The model asks for a tool, the result comes back, it reasons, it asks for the next one. For anything multi-step that turns into a lot of round-trips, and the orchestration logic lives in a loop you have to babysit.

In [code mode](../../../user-guide/sandboxing/code-mode), the model writes a single program that orchestrates the tools instead, with real control flow and composition, and you run that program once. A question like "revenue by region, then the top region broken down by month" becomes one script with a couple of queries and a comprehension, not five tool calls glued together with model turns.

The code runs inside Monty, a restricted interpreter with no imports, no filesystem access, no network access, and near-instant startup. It can only use the tools you explicitly make available to the sandbox. That means the model isn't running arbitrary Python with unrestricted access. It can only work within the boundaries you've defined.

## What runs where

The example splits work by how expensive and how worth-tracking each piece is.

| Piece                                                                   | Where it runs             | Why                                                                                                             |
| ----------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| the app (`/api/chat`)                                                   | a CPU app pod             | Serves the UI and launches one analysis run per question.                                                       |
| the data preview (`/api/dataset`)                                       | in-process in the app pod | A cheap sample of the rows for demos. No run, no LLM, just shows the data before you query it.                  |
| `analyze`                                                               | a Flyte task (the run)    | Owns the code-mode loop: prompt the model, run its code in the sandbox, return the report blocks and a summary. |
| `query(sql)`                                                            | a durable child task      | DuckDB over the data. Real work worth tracking, retrying, and caching. Dispatched from inside the sandbox.      |
| `create_metric`, `create_chart`, `create_table`, `calculate_statistics` | in-process in `analyze`   | Microseconds of pure Python. Making them tasks would add a round-trip for nothing.                              |
| the model's code                                                        | the Monty sandbox         | Untrusted LLM code, confined to calling the tools above.                                                        |

The interesting line is the split between `query` and the render helpers. Both are tools the model calls the same way, but one is a durable Flyte task and the rest are plain functions. The next few sections show how one registry supports both.

## The heavy tool: a durable query

The dataset is a small `orders` table (ecommerce orders for 2024) that the example generates deterministically, so there is nothing to fetch. `query` runs read-only DuckDB SQL against it and returns row dicts, coercing dates to ISO strings on the way out:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/tools.py" fragment=query_tool lang=python >}}

To point this at your own data, for example, change the DataFrame the query registers to read a Parquet file or a warehouse table.

## One registry, two bindings

The agent keeps two mappings that share the same tool names. `tools` is used to describe the tools to the model, and `execution_tools` is what actually runs when the model calls them. The model writes against one contract, and each call is routed to either a durable task or an in-process function depending on which binding you gave it:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/analysis.py" fragment=registry lang=python >}}

Here `query` points at the durable `@env.task` for execution, and the four render helpers point at plain functions. That single difference is what makes every query the model writes a tracked child task while the chart rendering stays free.

## The durable environment

`query` becomes durable by living in a `flyte.TaskEnvironment`. The environment carries the image (DuckDB, pandas, the Anthropic SDK, and the Monty sandbox package) and the Anthropic API key as a `flyte.Secret`:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/analysis.py" fragment=env lang=python >}}

The `query` task itself is a thin wrapper over the tool function, so the durable version and the in-process version run identical code. Only the binding differs, and the task carries `cache="auto"`:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/analysis.py" fragment=query_task lang=python >}}

Caching is scoped to `query`, not the whole environment. The same SQL over a fixed dataset is deterministic, so identical queries return instantly from cache and dedupe across every conversation and user. `analyze` is deliberately left uncached: it is a non-deterministic model turn keyed on the whole conversation, so it rarely repeats, and caching it could freeze a transient failure.

## Turning the registry into a prompt

The system prompt is generated from the tool registry rather than hand-written. The agent introspects each function's signature and docstring, so adding a tool is a matter of writing a function, and the prompt updates itself:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/agent.py" fragment=describe_tools lang=python >}}

The rest of the prompt drops these tool descriptions into a template alongside the sandbox's own syntax rules (`flyte.sandbox.ORCHESTRATOR_SYNTAX_PROMPT`), the dataset schema, and the contract for what to return: a dict with an ordered list of HTML `blocks` and a one-line `summary`. That contract is what lets the model assemble a small report of metrics, a chart, and a table rather than a single lonely graph.

## Running the code, then fixing it

Execution is a single call. `orchestrate_local` takes the generated code and the execution tools, classifies each tool, and runs the program in the sandbox. A tool that is a Flyte task gets dispatched as a durable child task, and a plain callable runs in-process, so the durable `query` and the in-process render helpers coexist in one sandbox call:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/agent.py" fragment=execute lang=python >}}

Generated code fails sometimes. The model reaches for a builtin the sandbox does not allow, or writes SQL that does not parse. Rather than give up, the agent hands the error and the failed code back to Claude and asks for a fix, then tries again up to a small retry budget:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/agent.py" fragment=run lang=python >}}

On success it also records which tools the code called and how many times, which the UI shows as a strip under each answer.

> [!NOTE]
> This does not have to be Claude. The only model-specific code is the LLM call in `_call_llm` (in `agent.py`). Everything around it, building the prompt from the registry, running the code in the sandbox, and the self-repair retry, is model-agnostic. Point that call at any chat-completion endpoint and the rest of the loop is unchanged. That endpoint can be an open model you host yourself, for example [an LLM served with vLLM](../../../user-guide/native-app-integrations/vllm-app) as its own app right alongside this one, which keeps the data and the model on your own infrastructure and drops the per-call API cost in exchange for running the inference yourself.

## The analysis task

`analyze` is the task that ties the loop together. It takes the question and the prior conversation as `history`, so a follow-up like "now break that down by month" is answered with the earlier turns as context. Because it runs inside a task context, the `query` calls made by its sandboxed code are dispatched as durable child tasks rather than running locally. It returns a `ChatResponse` carrying the blocks, the summary, the generated code, and the tools that ran:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/analysis.py" fragment=analyze lang=python >}}

You can run this half on its own with `python analysis.py`, which submits one analysis as a durable `flyte.run` and prints the run URL, no app required.

## Serving it as an app that launches runs

The app is where a subtle rule of Flyte apps shows up. An app's request handler has no task context, so calling a task directly from it would run the task locally in the app pod, not on the cluster, and you would lose durability and the child-task graph. The fix is to launch the work as a run.

The app initializes the client once in its lifespan with `flyte.init_in_cluster`, which resolves project, domain, endpoint, and identity from the app pod. It also warms the data sample so the first preview click is instant:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/app.py" fragment=lifespan lang=python >}}

The one thing app pods are not handed is the org, and launching a run needs it. The deploy step reads the org from your config and passes it in through the `ANALYSIS_ORG` environment variable, which the lifespan feeds to `init_in_cluster`.

The app environment declares its image, pins one replica, depends on the analysis environment so both deploy together, and requires auth.

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/app.py" fragment=app_env lang=python >}}

The chat handler launches a run per question and streams two messages back. A run has a URL the moment it is submitted, so the handler sends that link first, before the run finishes: the UI shows a live link into the Union UI right away. It then streams the result once the run completes. Inside that run there is a task context, so the sandbox's `query` calls become durable child tasks, which you can watch appear on that live run page:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/app.py" fragment=chat lang=python >}}

This is the "call a task from an app" shape: initialize in-cluster once in the lifespan, then use `flyte.run.aio(...)` per request. For more on apps and tasks calling each other, see [hybrid app-task graphs](../../../user-guide/build-apps/hybrid-graphs), and for how apps are served, see [how app serving works](../../../user-guide/serve-and-deploy-apps/how-app-serving-works).

## Previewing the data

It helps to show the data before you start querying it, right? The preview reads a handful of row dicts straight from the cached generator, with no run and no query engine, so it returns instantly:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/tools.py" fragment=dataset_sample lang=python >}}

The endpoint wraps that sample in the same table renderer the model uses and returns it, so the preview looks like the reports the agent produces:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/app.py" fragment=dataset lang=python >}}

In the UI, the **Preview the dataset** button drops the schema and a sample of rows into the conversation.

## Deploy and run

Deploying is one command. The entry point uses the remote image builder so no local Docker is needed, injects the org, and serves the app and its analysis environment together:

{{< code file="/unionai-examples/v2/tutorials/code_mode_agent/app.py" fragment=deploy lang=python >}}

Register your Anthropic key as a secret and deploy:

```shell
$ flyte create secret anthropic_api_key <your-anthropic-key>
$ python app.py
```

That prints the app URL. Open it, click **Preview the dataset** to show the schema and a sample of rows, then ask something like "give me a 2024 revenue overview" or "return rate by channel". Each answer comes back as a short report of headline numbers, a chart, and sometimes a table, along with the tools the code called, the generated code under a disclosure, and a link to the run so you can see the query tasks it dispatched.

## Going further

- **Point at a real dataset.** Swap the generated table for a Parquet file in object storage or a warehouse connection. Because `query` is a durable task, large or slow queries get retries and caching for free.
- **Add a model-based tool.** A tool that calls another model, such as an LLM judge or an embedder, registers like any other. Cheap tools stay in-process, and expensive ones become tasks.
- **Add more tools.** Write a function with a docstring and add it to the registry. The prompt regenerates from the signatures, so there is nothing else to wire up.
