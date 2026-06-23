---
title: Parallelized autoresearch agent
weight: 2
variants: +flyte +union
---

# Parallelized autoresearch agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/parallelized_autoresearch).

This tutorial extends the [Autoresearch agent](../autoresearch/_index) pattern with a code-mode MLE agent that plans **batches** of training experiments, saves distinct `train.py` edits, and runs them **in parallel** via `flyte.map`. It follows the [karpathy/autoresearch](https://github.com/karpathy/autoresearch) loop — minimize validation bits-per-byte on a TinyGPT variant — but orchestrates fan-out batches with durable Flyte tasks and [unionai-sandbox](https://www.union.ai/docs/v2/union/user-guide/sandboxing/interactive-sandboxes/) execution.

Compared to the single-threaded Claude Code autoresearch tutorial, this agent:

- Edits full `train.py` source (upstream karpathy style) instead of calling a remote coding CLI
- Uses **`code_mode=True`** so the LLM writes Python plans that call `run_experiment_batch` or `flyte_map`
- Persists a **leaderboard**, code-edit history, and batch plans in `MemoryStore`
- Self-heals **OOM** during sandbox training runs by bumping memory and retrying

## Define the task environments

The example uses three environments — bundle preparation, sandbox experiments, and the agent driver — sharing a Debian-based image with PyTorch and sandbox tooling.

{{< code file="/unionai-examples/v2/tutorials/parallelized_autoresearch/bundle.py" fragment=env lang=python >}}

Supporting modules (`train.py`, `prepare.py`, `tools.py`, and `ui.py`) live alongside the entry point in the example directory.

## The fan-out agent task

The driver task `parallelized_autoresearch` restores prior memory (default key `parallelized-autoresearch`), streams Activity / Leaderboard / Code edits / Memory report tabs, and runs the code-mode agent loop.

{{< code file="/unionai-examples/v2/tutorials/parallelized_autoresearch/parallelized_autoresearch.py" fragment=agent lang=python >}}

## Run the agent

### Create secrets

Register an Anthropic API key for the agent LLM calls:

```
flyte create secret internal-anthropic-api-key <YOUR_ANTHROPIC_API_KEY>
```

### Run remotely

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/parallelized_autoresearch):

```
cd v2/tutorials/parallelized_autoresearch
uv run --script parallelized_autoresearch.py -- --n-experiments 6 --batch-size 3 --num-shards 1
```

Use `--memory-key` to resume a prior research session (default: `parallelized-autoresearch`). Pass a unique key — for example `parallelized-autoresearch-20260622-215057` — to start with empty memory. Code mode needs more turns than JSON tool mode — increase `--max-turns` for larger sweeps.

Or invoke the agent task directly with `flyte run` (snake_case task inputs):

```
flyte run parallelized_autoresearch.py parallelized_autoresearch \
  --n_experiments 6 --batch_size 3 --num_shards 1 --max_turns 12 \
  --memory_key parallelized-autoresearch
```

> [!NOTE]
> The first run downloads climbmix data shards and trains a BPE tokenizer. Subsequent runs reuse cached bundle tasks.

See also the single-task [Autoresearch agent](../autoresearch/_index) tutorial for the Claude Code + pull-request workflow.
