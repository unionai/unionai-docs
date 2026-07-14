---
title: Parallelized autoresearch agent
weight: 2
variants: +flyte +union
---

# Parallelized autoresearch agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/parallelized_autoresearch).

This tutorial extends the [Autoresearch agent](../autoresearch/_index) pattern with a code-mode MLE agent that plans **batches** of training experiments, saves distinct `train.py` edits, and runs them **in parallel** via `flyte.map`. It follows the [karpathy/autoresearch](https://github.com/karpathy/autoresearch) loop (minimize validation bits-per-byte on a TinyGPT variant) but orchestrates fan-out batches with durable Flyte tasks and [unionai-sandbox](../../../user-guide/sandboxing/_index) execution.

Compared to the single-threaded Claude Code autoresearch tutorial, this agent:

- Edits full `train.py` source (upstream karpathy style) instead of calling a remote coding CLI
- Uses **`code_mode=True`** so the LLM writes Python plans that call batch tools such as `run_experiment_batch`
- Persists a **leaderboard**, code-edit history, and batch plans in `MemoryStore`
- **Right-sizes each experiment** with an LLM via a `@tool` **`call_handler`**, then retries on Flyte or sandbox OOM by bumping memory

Each experiment has different compute needs (wider models, larger batch sizes, longer training loops). A single static `flyte.Resources` on the task would either waste cluster memory or OOM on the heavy configs. Instead, this example uses the same [`call_handler` pattern](../../../user-guide/build-agent/flyte-agents) as the Flyte SDK self-correcting agent: before every run, a sizing LLM reads the tool name, docstring, and call arguments and returns a JSON resource spec; the handler applies it with `tool_fn.target.override(resources=...).aio(**kwargs)` and retries with more memory when needed.

## Define the task environments

The example uses three environments (bundle preparation, sandbox experiments, and the agent driver) sharing a Debian-based image with PyTorch and sandbox tooling.

{{< code file="/unionai-examples/v2/tutorials/parallelized_autoresearch/bundle.py" fragment=env lang=python >}}

Supporting modules (`train.py`, `prepare.py`, `tools.py`, and `ui.py`) live alongside the entry point in the example directory.

## Right-size experiments with `call_handler`

The right-sizing logic lives in `tools.py`. `execute_with_right_sizing` asks the LLM for a resource estimate, runs the underlying `@env.task` with `override(resources=...)`, and loops on `flyte.errors.OOMError` or a sandbox-reported OOM flag until the run succeeds or retries are exhausted:

{{< code file="/unionai-examples/v2/tutorials/parallelized_autoresearch/tools.py" fragment=right_size lang=python >}}

`right_size` is the pre-built handler passed to `@tool(call_handler=...)`. The agent does not need a back-reference to the `Agent` instance: the harness passes `call_llm` and `tool_fn.model` into the handler on each invocation.

The experiment task stacks `@tool(call_handler=tools.right_size)` on `@experiment_env.task`. The task body only loads edited code and runs sandbox training; sizing and OOM recovery happen in the handler:

{{< code file="/unionai-examples/v2/tutorials/parallelized_autoresearch/parallelized_autoresearch.py" fragment=run_experiment lang=python >}}

Batch fan-out calls `flyte.map.aio(run_experiment, ...)` from `run_experiment_batch`. That path invokes `run_experiment.aio()` directly (**not** through the agent registry) so the example binds `call_llm` and `model` on the tool after construction (see the `dataclasses.replace` block above). With Flyte SDK ≥ 2.5.5, `AgentTool.aio` routes through `call_handler`, so every mapped experiment gets LLM right-sizing even when the agent only exposes `run_experiment_batch` in code mode.

## The fan-out agent task

The driver task `parallelized_autoresearch` restores prior memory (default key `parallelized-autoresearch`), streams Activity / Leaderboard / Code edits / Memory report tabs, and runs the code-mode agent loop. The agent tool registry is trimmed to the batch workflow: `run_experiment` is internal to `run_experiment_batch`, not a sandbox function the LLM calls directly.

{{< code file="/unionai-examples/v2/tutorials/parallelized_autoresearch/parallelized_autoresearch.py" fragment=agent lang=python >}}

## Run the agent

### Create secrets

Register an Anthropic API key for agent LLM calls and for per-experiment resource sizing inside `call_handler`:

```
flyte create secret internal-anthropic-api-key <YOUR_ANTHROPIC_API_KEY>
```

### Run remotely

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/parallelized_autoresearch):

```
cd v2/tutorials/parallelized_autoresearch
uv run --script parallelized_autoresearch.py --n-experiments 6 --batch-size 3 --num-shards 1
```

Use `--memory-key` to resume a prior research session (default: `parallelized-autoresearch`). Pass a unique key (for example `parallelized-autoresearch-20260622-215057`) to start with empty memory. Code mode needs more turns than JSON tool mode. Increase `--max-turns` for larger sweeps.

Or invoke the agent task directly with `flyte run` (snake_case task inputs):

```
flyte run parallelized_autoresearch.py parallelized_autoresearch \
  --n_experiments 6 --batch_size 3 --num_shards 1 --max_turns 12 \
  --memory_key parallelized-autoresearch
```

> [!NOTE]
> The first run downloads climbmix data shards and trains a BPE tokenizer. Subsequent runs reuse cached bundle tasks. Requires **Flyte SDK ≥ 2.5.5** for `call_handler` support in code mode and on `AgentTool.aio` (used by `flyte.map` fan-out).

See also the single-task [Autoresearch agent](../autoresearch/_index) tutorial for the Claude Code + pull-request workflow.
