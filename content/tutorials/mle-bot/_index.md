---
title: MLE Bot
weight: 1
variants: +flyte +union
---

# MLE Bot: an autonomous ML engineer

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/mle_bot).

You have a dataset and a business question. Today, going from a raw CSV to a trained, evaluated model with a written report takes an ML engineer hours of experimentation: profiling the data, picking algorithms, engineering features, tuning hyperparameters, analyzing results, and iterating. What if you could describe the problem in plain English and let an agent handle the rest?

This tutorial walks you through building exactly that. You'll construct an autonomous ML engineer that takes a problem description and a dataset, designs experiments, runs them on cloud infrastructure, analyzes results, iterates, and produces a report summarizing the best model it found.

## TL;DR

- You'll build an agent that takes a natural language problem description and a CSV file, then produces a trained model and a detailed report comparing the results.
- The LLM reasons over dataset statistics, never raw data. Trusted tools compute statistics in the cloud, and only those statistics reach the LLM.
- LLM-generated orchestration code runs inside Flyte's sandbox: no imports, no network access, no filesystem. It can only call pre-approved tool functions.
- Each tool function runs as a durable Flyte task in the cloud, with retries, observability, and full traceability.

## The problem with LLMs and ML pipelines

If you ask an LLM to "train a model on this dataset," you run into a few issues fast. The LLM might hallucinate sklearn APIs that don't exist. It has no access to real compute, so it can't actually train anything. It runs everything in a single context with no way to handle large datasets. And if something goes wrong, there's no structured way to iterate.

The core tension is that LLMs are genuinely good at reasoning about *what* to try. Given a dataset profile showing class imbalance and temporal structure, a capable model will suggest rolling window features and appropriate resampling strategies. But LLMs are unreliable at *executing* those plans. They generate buggy code, lose track of variable names, and have no way to dispatch real compute.

The solution is to separate the two concerns. Let the LLM handle the planning: which algorithms to try, what feature engineering to apply, which hyperparameters to tune. Then hand the execution to trusted tool functions that run on real infrastructure. The LLM controls *what* happens. The tools control *how*.

Think of it like giving a junior engineer access to a curated set of approved tools and reviewing their work. They can compose those tools in creative ways, but they can't go off-script and install random packages or hit arbitrary endpoints.

## How it works

The agent runs in five phases:

1. **Profile** the dataset using a trusted tool. The tool returns statistics (shape, class balance, feature correlations, missing values). The LLM never touches the raw data.
2. **Design** a batch of experiments. The LLM reads the profile and proposes 2 to 3 experiments, each with an algorithm, hyperparameters, and a feature engineering strategy.
3. **Execute** each experiment in parallel. For each one, the LLM generates Python orchestration code that chains together pre-approved tool functions. That code runs inside a restricted sandbox, and each tool call dispatches as a durable Flyte task on cloud compute.
4. **Analyze** the results. The LLM reviews metrics across experiments, optionally requests targeted data explorations (e.g., "are failures concentrated on specific machines?"), and decides whether to iterate with new experiments.
5. **Produce a report** summarizing the winning model, the experiment journey, and deployment recommendations.

Two things make this work. First, the LLM never sees raw data. The profiling tool runs in the cloud on managed compute and returns only aggregated statistics. This keeps prompt sizes manageable and avoids leaking sensitive data into LLM API calls. Second, the LLM-generated code runs inside Flyte's sandbox where the only thing it can do is call your pre-approved tool functions. More on that shortly.

### What to expect

Here's what an actual run looks like on a synthetic predictive maintenance dataset (175k rows of sensor data from 20 industrial pumps, ~3% failure rate).

In the first iteration, the agent designed three experiments: a logistic regression baseline, an XGBoost model with rolling window features, and a random forest with lag features. After reviewing the results, it decided to continue. It requested two targeted explorations ("do failure cases show meaningfully higher vibration?" and "how do feature-target correlations vary by pump?"), then used those findings to design a second round of experiments with tuned feature engineering and class weighting.

After two iterations and five total experiments, the final rankings looked like this:

| Rank | Experiment | ROC-AUC | F1 | Recall | Precision |
|------|-----------|---------|------|--------|-----------|
| 1 | **Random Forest with Balanced Class Weights** | 0.7983 | 0.4284 | 0.4561 | 0.4038 |
| 2 | XGBoost with Feature Engineering | 0.7847 | 0.4568 | 0.4722 | 0.4425 |
| 3 | Enhanced XGBoost with Focused Feature Engineering | 0.7821 | 0.3565 | 0.4973 | 0.2778 |
| 4 | Random Forest with Lag Features | 0.7651 | 0.5206 | 0.4104 | 0.7116 |
| 5 | Baseline Logistic Regression | 0.7528 | 0.118 | 0.6496 | 0.0649 |

The agent autonomously explored different algorithms, feature strategies, and class imbalance techniques, then ranked everything by ROC-AUC. The full report includes the LLM's reasoning and generated code for every experiment, so you can trace exactly why it chose each approach and what code it wrote to implement it. Since the LLM makes different decisions each run, your results will vary, but the overall pattern (profile, design, execute, analyze, iterate) stays the same.

## Declaring task environments

Before writing any tasks, you need to declare *where* and *how* they run. In Flyte v2, a `TaskEnvironment` bundles together the container image, resource requirements, secrets, and dependencies for a group of tasks.

The MLE Bot uses two environments. One for the ML tools (pandas, sklearn, xgboost) and one for the agent itself (the OpenAI client and the sandbox runtime):

{{< code file="/unionai-examples/v2/tutorials/mle_bot/mle_bot/environments.py" fragment=environments lang=python >}}

A few things to note. `flyte.Resources` sets the CPU and memory for every task in that environment. `flyte.Image.from_debian_base()` builds a container image on the fly with the packages you declare, so you never need to manage Dockerfiles. `flyte.Secret` injects a secret from your cluster's secret store as an environment variable. And `depends_on=[tool_env]` tells Flyte that the agent environment needs to be able to dispatch tasks in the tool environment. This is what enables the sandbox to call tool functions that run on separate, appropriately-resourced compute.

## Building durable tool functions

Each tool is a regular Python async function decorated with `@env.task`. That decorator turns it into a durable Flyte task: it runs in its own container with the resources declared on the environment, it's automatically retried on transient failures, and every invocation is tracked in the Flyte UI.

Data flows between tasks as `flyte.io.File` objects. A `File` is a reference to data in cloud storage. When a task needs the actual bytes, it calls `await data.download()` to pull them into the container's local filesystem. When it produces output, it creates a `File` from a local path and returns it. Flyte handles the upload to cloud storage when the task completes. The data itself never passes through the agent or the LLM.

Here's what the training tool looks like:

{{< code file="/unionai-examples/v2/tutorials/mle_bot/mle_bot/tools/training.py" fragment=train_model lang=python >}}

And here's the profiling tool, which is the first thing the agent calls. It computes dataset statistics that the LLM will use to design experiments:

{{< code file="/unionai-examples/v2/tutorials/mle_bot/mle_bot/tools/data.py" fragment=profile_dataset lang=python >}}

The full tool inventory includes ten functions: `profile_dataset`, `split_dataset`, `explore_dataset`, `engineer_features`, `select_features`, `resample_dataset`, `train_model`, `get_predictions`, `evaluate_model`, and `rank_experiments`. Each one does exactly one thing. The LLM composes them into pipelines, but each tool enforces its own correctness guarantees internally. For example, `resample_dataset` only applies resampling to training data, never test data, regardless of what the LLM asks for.

## Guiding the LLM with domain knowledge

The quality of the agent's experiments depends heavily on what you tell it. The MLE Bot bakes ML best practices directly into its system prompts, so the LLM starts from a solid foundation rather than relying on whatever it picked up during pretraining.

The orchestration prompt, for example, includes guidance on feature engineering strategies, class imbalance handling, and algorithm selection. It's dynamically built from the dataset profile, so the LLM sees concrete context alongside the general advice:

```python
def _build_orchestration_system_prompt(profile: dict) -> str:
    return f"""\
You are an expert ML engineer. Your job is to design and write the best
possible pipeline for a machine learning experiment.

## Dataset context
Shape: {shape[0]:,} rows × {shape[1]} columns
Numeric features: {numeric_cols}
Class balance: {class_balance}, imbalanced: {is_imbalanced}
Feature-target correlations (raw): {corr_str}

## General ML best practices
**Feature engineering**:
- Sequential/time-series data: rolling window features capture trends
  that point-in-time readings miss. Choose window sizes relative to
  the prediction horizon and temporal resolution of the data.
- Consider skipping feature engineering entirely for a baseline.

**Class imbalance** (when is_imbalanced=true):
- Tree ensembles: use class_weight="balanced" or scale_pos_weight.
- The default 0.5 decision threshold may not be optimal.

**Algorithm selection**:
- XGBoost: strong default for tabular data. Start here.
- RandomForest: more robust to outliers, good for noisy data.
- LogisticRegression: fast linear baseline.
...
"""
```

This means the LLM doesn't just get a blank canvas. It gets a structured briefing that combines the actual dataset characteristics with best practices for handling them. When the profile shows class imbalance, the prompt tells it which hyperparameters to adjust and which resampling strategies to consider. When there's a timestamp column, the prompt suggests rolling window features with guidance on window sizing.

The user's problem description also has a significant impact on the agent's behavior. A query like "Predict pump failures 24 hours before they happen based on sensor readings" tells the LLM that this is a time-series classification problem with a specific prediction horizon. That shapes everything: the LLM will favor temporal feature engineering (rolling windows sized relative to that 24-hour horizon), pick algorithms that handle imbalanced binary classification well, and focus on recall as a key metric because missing a failure is worse than a false alarm. Change the query to something like "Classify machine health status from the latest sensor snapshot" and the same dataset would produce a completely different set of experiments, with less emphasis on temporal features and more on cross-sectional patterns.

## The agent loop: profile, design, execute, iterate

The agent's main function orchestrates five phases. Let's walk through each one.

**Phase 1: Profile.** The agent calls `profile_dataset` directly as a trusted tool. This isn't sandboxed because there's nothing to protect against here: the function is your code, running on your compute. The `flyte.group` call organizes this step in the Flyte UI so you can inspect it later.

```python
with flyte.group("profile"):
    profile = await profile_dataset(data, target_column)
```

**Phase 2: Design.** The profile dict goes to the LLM along with the problem description. The LLM returns a structured response matching the `InitialDesign` schema:

{{< code file="/unionai-examples/v2/tutorials/mle_bot/mle_bot/schemas.py" fragment=schemas lang=python >}}

The LLM typically proposes 2 to 3 experiments: a baseline with minimal feature engineering, an experiment with rolling window features for temporal data, and perhaps one testing a different algorithm or resampling strategy.

**Phase 3: Execute in parallel.** All experiments in a batch run simultaneously using `asyncio.gather()`. Each experiment dispatches its own set of durable Flyte tasks:

{{< code file="/unionai-examples/v2/tutorials/mle_bot/mle_bot/agent.py" fragment=parallel_execute lang=python >}}

**Phase 4: Analyze and iterate.** After each batch completes, the LLM reviews the results and decides whether to continue. It can optionally request targeted data explorations before designing the next round. If the LLM requests explorations (e.g., "do failure cases show higher vibration readings?"), the agent runs `explore_dataset` with those configurations, feeds the results back to the LLM, and lets it refine the next batch of experiments based on what it learned. The loop continues until the LLM decides to stop, the target metric threshold is reached, or the maximum number of iterations is exhausted.

## Running LLM-generated code in Flyte's sandbox

This is where it gets interesting. The LLM doesn't just pick parameters from a dropdown. For each experiment, it writes actual Python code that decides how to compose the tool functions into a pipeline. Maybe it splits the data, engineers rolling window features, applies SMOTE resampling on the training split, trains an XGBoost model, and evaluates it. Or maybe it skips feature engineering entirely for a baseline. The LLM decides the structure.

That code runs inside Flyte's sandbox, a restricted execution environment that enforces strict constraints:

- No `import` statements. The only callable functions are the ones you explicitly provide.
- No network access and no filesystem access.
- No `try`/`except`, no `class` definitions, no augmented assignment (`+=`).
- No `with` statements, no generators, no `global`/`nonlocal`.

The sandbox sees your pre-approved tool functions as plain function calls. When the code calls `train_model(...)`, the sandbox pauses execution, dispatches the call to Flyte (which runs it as a durable task on cloud compute with the resources declared on `tool_env`), waits for the result, and resumes. The LLM-generated code looks like synchronous Python, but under the hood each tool call is a full Flyte task execution.

Here's how the sandbox is invoked:

```python
result = await flyte.sandbox.orchestrate_local(
    code,
    inputs={
        "data": data,
        "target_column": target_column,
        "time_column": time_column,
        "experiment_name": exp_name,
    },
    tasks=TOOLS,
)
```

The `code` parameter is a string of Python generated by the LLM. `inputs` provides the variables that the code can reference. `tasks` is the allowlist: a list of Flyte task functions that the code is permitted to call. Nothing else is available.

Here's an example of what the LLM might generate for a single experiment:

```python
train_file = split_dataset(data, target_column, 0.2, time_column, "train")
test_file  = split_dataset(data, target_column, 0.2, time_column, "test")

eng_train = engineer_features(train_file, {
    "rolling_columns": ["vibration_mms", "temperature_c"],
    "windows": [6, 12, 24],
    "group_column": "machine_id",
    "time_column": "timestamp"
})
eng_test = engineer_features(test_file, {
    "rolling_columns": ["vibration_mms", "temperature_c"],
    "windows": [6, 12, 24],
    "group_column": "machine_id",
    "time_column": "timestamp"
})

model_file = train_model(eng_train, target_column, "xgboost", {
    "n_estimators": 200, "max_depth": 8, "scale_pos_weight": 33
})
eval_result = evaluate_model(model_file, eng_test, target_column)

{"experiment_name": experiment_name, "algorithm": "xgboost",
 "metrics": eval_result["metrics"],
 "confusion_matrix": eval_result["confusion_matrix"],
 "threshold_analysis": eval_result["threshold_analysis"],
 "n_samples": eval_result["n_samples"]}
```

Each function call in that snippet dispatches a separate Flyte task. The `split_dataset` calls run on the tool environment's compute (2 CPU, 4Gi memory). The `train_model` call trains an actual XGBoost model. The last expression (a dict literal) is returned as the sandbox result.

Sometimes the LLM generates code with bugs, like a wrong variable name or a missing argument. The agent handles this with a retry loop. If the sandbox raises an exception, the error message and the failing code are fed back to the LLM, which gets a chance to fix the issue:

{{< code file="/unionai-examples/v2/tutorials/mle_bot/mle_bot/agent.py" fragment=retry_loop lang=python >}}

On the first attempt, `previous_error` and `previous_code` are empty. On subsequent attempts, the LLM sees exactly what went wrong and can fix it. In practice, most experiments succeed on the first try, with occasional recoveries on the second.

## Streaming results to a live report

While the agent runs, it streams results to the Flyte UI in real time using `flyte.report.log.aio()`. You don't have to wait for the full run to finish to see how experiments are performing.

The entrypoint task enables this with `report=True`:

{{< code file="/unionai-examples/v2/tutorials/mle_bot/mle_bot/agent.py" fragment=entrypoint lang=python >}}

As each experiment completes, the agent streams its metrics to the report:

```python
await flyte.report.log.aio(
    f"<h3>Iteration {iteration + 1}: {exp_result.name}</h3>"
    f"<p><b>Algorithm:</b> {exp_result.algorithm} &nbsp;|&nbsp; "
    f"<b>ROC-AUC:</b> {m.get('roc_auc')} &nbsp;|&nbsp; "
    f"<b>F1:</b> {m.get('f1')}</p>",
    do_flush=True,
)
```

The final report includes a dataset summary, per-experiment metrics with expandable reasoning and generated code, the analysis decisions at each iteration, a final rankings table, and an experiment journey summary showing how the agent's strategy evolved.

## Running it

First, generate the synthetic demo dataset (a predictive maintenance scenario with 175k+ rows of simulated sensor data from 20 industrial pumps):

```bash
uv run main.py generate-data
```

Then submit the agent to your Flyte cluster:

```bash
uv run main.py run \
    --data data/predictive_maintenance.csv \
    --problem "Predict pump failures 24 hours before they happen" \
    --target failure_24h \
    --time-column timestamp \
    --max-iterations 3 \
    --output results/report.md
```

The agent connects to your cluster via `~/.flyte/config.yaml`, uploads the CSV, and submits the agent task. You'll see a URL to track the execution in the Flyte UI, and logs will stream to your terminal.

> [!NOTE]
> You'll need to register your OpenAI API key as a cluster secret before running:
> `flyte create secret openai-api-key <YOUR_KEY>`

If you want to see the self-healing retry loop in action, add the `--inject-failure` flag. This deliberately corrupts the first experiment so the agent has to detect the error and recover, which makes for a nice demo of the durability guarantees.

## Why Flyte?

You could build something similar with plain Python and `exec()`. But there are a few things you'd lose.

**Safety.** Flyte's sandbox restricts LLM-generated code to calling your pre-approved functions and nothing else. No imports, no network, no filesystem. If you wouldn't give an intern root access to your production cluster, you probably shouldn't give an LLM unrestricted code execution either.

**Durability.** Every tool call is a Flyte task. If the agent process crashes halfway through iteration 3, the experiments that already completed are cached. You restart and pick up where you left off instead of retraining models from scratch. For long-running ML experiments, this matters.

**Observability.** You can see every LLM prompt, every generated code snippet, every tool invocation, and every result in the Flyte UI. When the agent makes a questionable decision (like skipping feature engineering on temporal data), you can trace exactly why: the prompt it received, the profile it read, the reasoning it generated.

**Compute isolation.** The ML tools run on cloud instances with the CPU and memory they need. The agent itself runs on a small 1-CPU instance since all it does is call the LLM and dispatch tool tasks. You're not bottlenecked by your laptop, and you're not paying for GPU-class compute to run an orchestration loop.

**Parallelism.** Multiple experiments run simultaneously via `asyncio.gather()`, each dispatching its own durable tasks. Flyte handles the scheduling. If you have three experiments in a batch and each involves training + evaluation, that's six tasks running concurrently on cloud compute.

The MLE Bot is a specific example of a more general pattern: giving an LLM the ability to reason about *what* work should be done, while Flyte handles *how* that work gets executed safely, durably, and at scale. The sandbox is the boundary between the two. Everything above the boundary is LLM-generated and untrusted. Everything below it is your code, running on your infrastructure, with all the guarantees you'd expect from a production orchestrator.
