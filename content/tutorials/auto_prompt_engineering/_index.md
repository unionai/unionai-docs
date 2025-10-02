---
title: Automatic prompt engineering
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Automatic prompt engineering

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/auto_prompt_engineering).

When building with LLMs and agents, the first prompt almost never works. We usually need several iterations before results are useful. Doing this manually is slow, inconsistent, and hard to reproduce.

Flyte turns prompt engineering into a systematic process. With Flyte we can:

- Generate candidate prompts automatically.
- Run evaluations in parallel.
- Track results in real time with built-in observability.
- Recover from failures without losing progress.
- Trace the lineage of every experiment for reproducibility.

And we're not limited to prompts. Just like [hyperparameter optimization](../hpo/_index.md) in ML, we can tune model temperature, retrieval strategies, tool usage, and more. Over time, this grows into full agentic evaluations, tracking not only prompts but also how agents behave, make decisions, and interact with their environment.

In this tutorial, we'll build an automated prompt engineering pipeline with Flyte, step by step.

## Set up the environment

First, let's configure our task environment.

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=env lang=python >}}

We need an API key to call GPT-4.1 (our optimization model). Add it as a Flyte secret:

```
flyte create secret openai_api_key <YOUR_OPENAI_API_KEY>
```

We also define CSS styles for live HTML reports that track prompt optimization in real time:

![Results](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/gifs/tutorials/prompt_engineering/results.gif)

## Prepare the evaluation dataset

Next, we define our golden dataset, a set of prompts with known outputs. This dataset is used to evaluate the quality of generated prompts.

For this tutorial, we use a small geometric shapes dataset. To keep it portable, the data prep task takes a CSV file (as a Flyte `File` or a string for files available remotely) and splits it into train and test subsets.

If you already have prompts and outputs in Google Sheets, simply export them as CSV with two columns: `input` and `target`.

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=data_prep lang=python >}}

This approach works with any dataset. You can swap in your own with no extra dependencies.

## Define models

We use two models:

- **Target model** → the one we want to optimize.
- **Review model** → the one that evaluates candidate prompts.

First, we capture all model parameters in a dataclass:

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=model_config lang=python >}}

Then we define a Flyte `trace` to call the model. Unlike a task, a trace runs within the same runtime as the parent process. Since the model is hosted externally, this keeps the call lightweight but still observable.

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=call_model lang=python >}}

{{< variant byoc selfmanaged >}}

You can also host your own models on Union. For example, we deploy <code>gpt-oss-20b</code> using vLLM.

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/gpt_oss.py" lang=python >}}

<p>We use an <code>A10G</code> GPU instance, and with streaming, you can load model weights directly into GPU memory instead of downloading the weights to disk first, then loading to GPU memory.</p>

<p>To deploy the model, cache the model from HuggingFace with a Union artifact:</p>

<pre>
union cache model-from-hf \
    --hf-token-key hf-api-key \
    --artifact-name gpt-oss-20b \
    --cpu 2 \
    --mem 8Gi \
    --ephemeral-storage 100Gi openai/gpt-oss-20b
</pre>

Then deploy it:

<pre>
union deploy apps gpt_oss.py gpt-oss-20b-vllm
</pre>

When using a hosted model, just provide its <code>hosted_model_uri</code> in <code>ModelConfig</code>. All inference happens locally, so your data never leaves your environment.

{{< /variant >}}

Finally, we wrap the trace in a task to call both target and review models:

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=generate_and_review lang=python >}}

## Evaluate prompts

We now define the evaluation process.

Each prompt in the dataset is tested in parallel, but we use a semaphore to control concurrency. A helper function ties together the `generate_and_review` task with an HTML report template. Using `asyncio.gather`, we evaluate multiple prompts at once.

The function measures accuracy as the fraction of responses that match the ground truth. Flyte streams these results to the UI, so you can watch evaluations happen live.

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=evaluate_prompt lang=python >}}

## Optimize prompts

Optimization builds on evaluation. We give the optimizer model:

- the history of prompts tested so far, and
- their accuracies.

The model then proposes a new prompt.

We start with a _baseline_ evaluation using the user-provided prompt. Then for each iteration, the optimizer suggests a new prompt, which we evaluate and log. We continue until we hit the iteration limit.

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=prompt_optimizer lang=python >}}

At the end, we return the best prompt and its accuracy. The report shows how accuracy improves over time and which prompts were tested.

![Report](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/gifs/tutorials/prompt_engineering/prompt_accuracies.png)

## Build the full pipeline

The entrypoint task wires everything together:

- Accepts model configs, dataset, iteration count, and concurrency.
- Runs data preparation.
- Calls the optimizer.
- Evaluates both baseline and best prompts on the test set.

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=auto_prompt_engineering lang=python >}}

## Run it

We add a simple main block so we can run the workflow as a script:

{{< code file="/external/unionai-examples/v2/tutorials/auto_prompt_engineering/optimizer.py" fragment=main lang=python >}}

Run it with:

```
uv run --prerelease=allow optimizer.py
```

![Execution](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/gifs/tutorials/prompt_engineering/execution.gif)

## Why this matters

Most prompt engineering pipelines start as quick scripts or notebooks. They're fine for experimenting, but they're difficult to scale, reproduce, or debug when things go wrong.

With Flyte 2, we get a more reliable setup:

- Run many evaluations in parallel with [async Python](../../user-guide/flyte-2/async.md#true-parallelism-for-all-workloads) or [native DSL](../../user-guide/flyte-2/async.md#the-flytemap-function-familiar-patterns).
- Watch accuracy improve in real time and link results back to the exact dataset, prompt, and model config used.
- Resume cleanly after failures without rerunning everything from scratch.
- Reuse the same pattern to tune other parameters like temperature, retrieval depth, or agent strategies, not just prompts.

## Next steps

You now have a working automated prompt engineering pipeline. Here’s how you can take it further:

- **Optimize beyond prompts**: Tune temperature, retrieval strategies, or tool usage just like prompts.
- **Expand evaluation metrics**: Add latency, cost, robustness, or diversity alongside accuracy.
- **Move toward agentic evaluation**: Instead of single prompts, test how agents plan, use tools, and recover from failures in long-horizon tasks.

With this foundation, prompt engineering becomes repeatable, observable, and scalable, ready for production-grade LLM and agent systems.
