---
title: AutoTrain
weight: 3
variants: +flyte +union
---

# AutoTrain: A Multi-Agent AutoML Pipeline on Union

## Background

Most AutoML tools stop at trying a handful of models and picking the best one. Real machine learning work involves more: understanding a raw, often messy dataset, choosing a sane starting architecture for its size and modality, then iterating the way a researcher would, reading results, diagnosing failures, and deciding what to try next.

AutoTrain automates that whole loop behind a simple web interface: a user submits a dataset link and a few fields, and a FastAPI app kicks off a three-stage Flyte pipeline. A **data agent** profiles and cleans the dataset, a **design agent** turns that profile into a concrete experiment plan and a starting `train.py`, and a **research agent** runs an iterative improve-and-evaluate loop with the Claude Agent SDK, committing progress to GitHub and opening a PR with the results. Every step is a task or trace visible in the Union UI. Architecturally, this is a hybrid app-task graph: the frontend and the pipeline's tasks are deployed to the same Union project/domain, and the app submits runs programmatically (`flyte.run.aio()`) on the user's behalf, then polls the cluster to report progress back to them.

![](../../../_static/images/tutorials/auto_train/auto_train.png)

> [!NOTE]
> Full code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/auto_train).

## Layout

| Path | Purpose |
|---|---|
| `app.py` | FastAPI frontend + `FastAPIAppEnvironment` (web image only) |
| `pipeline.py` | Task environments (cpu/gpu images, secrets) and the `automl_pipeline` task |
| `agents/` | Data / design / research agents (imported lazily inside tasks) |
| `templates/` | Jinja2 pages for the submission form and the status page |

## The Frontend App

The frontend is a small FastAPI app (`app.py`) whose only job is to take a submission, kick off a Flyte run, and let the user watch it progress - it holds no state of its own. That statelessness is deliberate: every submission becomes a Flyte run named `automl-<job_id>`, labeled `app=automl-webapp` and `automl-job-id=<job_id>`, and the status endpoint always resolves progress by querying the cluster for that run. If the app restarts or gets redeployed mid-run, the status page keeps working, because nothing about job progress lived in the app's memory to begin with.

### Serving, submitting, and tracking runs

`app.py` builds its own lightweight image (fastapi, uvicorn, jinja2, flyte client) and only imports `pipeline.py` lazily inside the `/run` handler, so deploying the frontend doesn't drag in the heavyweight cpu/gpu task images - those build later, the first time a run actually needs them.

{{< code file="/unionai-examples/v2/tutorials/auto_train/app.py" fragment="web_image_and_environment" lang="python" >}}

The `/run` endpoint submits without blocking: it generates a job id, fires the submission as a background `asyncio.create_task` on the same event loop Flyte was initialized on (`flyte.run.aio()` can't be driven from a separate thread's event loop), and immediately 303-redirects to a status page. Submission failures - which happen before a run exists to query - land in a small in-process error map just so the status page has something to show.

{{< code file="/unionai-examples/v2/tutorials/auto_train/app.py" fragment="submit_run_endpoint" lang="python" >}}

Because the app keeps no job state, `/api/status/{job_id}` reconstructs everything from the cluster: the run's phase maps to a status (`starting`/`running`/`done`/`error`), and while a run is in flight, the app walks its child actions to build a step list (data → design → research) with per-step phases.

{{< code file="/unionai-examples/v2/tutorials/auto_train/app.py" fragment="job_status_resolution" lang="python" >}}

### The submission form and status page

The UI itself is two Jinja2 templates with no client-side framework: `templates/index.html` is a plain HTML form (GitHub repo, dataset link, target column, domain hint, and training-budget fields):

![](../../../_static/images/tutorials/auto_train/training_form.png)

`templates/status.html` polls `/api/status/{job_id}` on an interval and renders whichever state comes back - a running step list, a completed result with a link to the GitHub PR, or an error traceback. While running, it shows each agent's progress - data agent, design agent, and research agent - with the currently running step highlighted:

![](../../../_static/images/tutorials/auto_train/training_progress.png)

On completion, if the agent's own convergence check flagged the result as unsatisfactory, a plain-language explanation of what went wrong and what to try next.



## Three Agents, One Pipeline

The pipeline itself (`pipeline.py`) is three tasks chained together, each running in its own `TaskEnvironment` with the resources the job actually needs, plus a lightweight orchestrator task that calls them in sequence. Each stage is deliberately a separate task, not a function call inside one big task: the data and design stages are cheap CPU work, while the research stage needs a GPU for hours at a time - collapsing them into one task would mean paying for GPU time during data profiling.

{{< code file="/unionai-examples/v2/tutorials/auto_train/pipeline.py" fragment="task_environments" lang="python" >}}

### Agent 1: Data Agent - ingest, profile, clean

`DataAgent` (`agents/data_agent.py`) takes whatever the user points it at - a CSV/Parquet URL, a HuggingFace dataset ID, a Kaggle dataset, a zipped image folder, FASTA sequences - and turns it into a `DataProfile`: modality (tabular / image / sequence / timeseries), inferred task type, class distribution, missingness, and a quality score with concrete recommendations (e.g. "severe class imbalance, use focal loss or oversampling"). Modality detection combines file-extension sniffing with domain-hint keywords (`"satellite"` → image, `"dna"`/`"protein"` → sequence), because a bare CSV of DNA k-mers looks tabular until you actually read the values.

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/data_agent.py" fragment="data_profile_dataclass" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/data_agent.py" fragment="modality_detection" lang="python" >}}

The Flyte task wrapping this agent (`run_data_agent`) is careful about what it uploads: raw downloads live in a scratch dir that's never persisted, and only `profile.json` plus the cleaned data get packaged into the `flyte.io.Dir` that's handed to the next stage.

{{< code file="/unionai-examples/v2/tutorials/auto_train/pipeline.py" fragment="data_agent_task" lang="python" >}}

### Agent 2: Design Agent - from profile to experiment plan

`DesignAgent` (`agents/design_agent.py`) runs once and produces everything the research loop needs to get started: it picks a GPU tier based on data size and modality, asks Claude to choose the right evaluation metric (`roc_auc`, `macro_f1`, `rmse`, ...) for the task, and - the more interesting decision - asks Claude to pick a *starting tier* off a modality-specific strategy ladder (e.g. for images: frozen-backbone-plus-sklearn for under 1k samples, up through a full EfficientNet-B4 fine-tune for 50k+). This means the research agent doesn't waste its first few experiments discovering that a linear model is too weak for a 200k-row image dataset; the design agent already reasoned about that from the data profile.

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/design_agent.py" fragment="compute_tier_selection" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/design_agent.py" fragment="starting_strategy_selection" lang="python" >}}

The agent then has Claude generate a **data-loading skeleton only** - explicitly no model, optimizer, or training loop - and writes it as `train.py` alongside a `program.md` (the research agent's instructions: metric, strategy ladder, hard constraints) and an empty `progress.csv`. All three files get pushed to a new branch in the target GitHub repo. This branch is the handoff between design and research - it's why a **writable** GitHub token is required even for public repos.

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/design_agent.py" fragment="generate_train_skeleton" lang="python" >}}

### Agent 3: Research Agent - the improve-and-evaluate loop

`ResearchAgent` (`agents/research_agent.py`) is where most of the engineering complexity lives. It clones the branch the design agent pushed, then runs a bounded loop (up to `max_experiments` iterations, each capped at `time_budget_per_experiment_seconds`):

1. **Experiment 0** hands `train.py` (still just the data-loading skeleton) to a `claude-agent-sdk` session, which reads `program.md`'s recommended starting tier and implements a complete baseline - model, training loop, metric printing.
2. **Every subsequent experiment** hands the current `train.py` plus `progress.csv`'s history to a fresh, short SDK session (`max_turns=10`) that reads what's been tried, diagnoses the current bottleneck, and applies exactly one focused change - or replies `STOP` if it thinks nothing further will help.
3. Python - not Claude - actually **runs** `train.py` as a subprocess with a hard timeout, parses the printed metric, and decides whether the change was an improvement. If it crashed, one extra LLM call attempts a targeted fix and one retry. Improvements get committed and pushed; non-improvements get the previous best `train.py` restored.

The reason this is split between "Claude decides what to change" and "Python runs the training" is that training is slow and needs a strict timeout, while proposing a change is fast and bounded - mixing them into one long agent session would make timeouts and reproducibility much harder to reason about.

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/research_agent.py" fragment="implement_baseline" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/research_agent.py" fragment="propose_change" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/research_agent.py" fragment="research_loop" lang="python" >}}

Every step of the loop - CLI setup, git clone, the baseline implementation, each change proposal, each training run, crash fixes, commits, PR creation, the final convergence check - is wrapped in `@flyte.trace`, so it shows up as a distinct traced action in the Union UI with its own inputs, outputs, and timing, all nested inside the single `run_research` task. Because a trace's identity is `(function name, input hash)`, every per-experiment call takes `exp_id` (and `run_training` an attempt counter) as an explicit input - otherwise a repeated call with the same arguments would replay a cached result instead of re-running.

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/research_agent.py" fragment="run_training_subprocess" lang="python" >}}

The loop also streams a `flyte.report` as it goes: the main tab is a live, styled trace of what each experiment tried and how it turned out, and a "Performance" tab holds a Plotly chart - the running best as a step line, rejected experiments as gray dots, improvements as green dots - rebuilt from `progress.csv` after every experiment.

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/research_agent.py" fragment="progress_plot" lang="python" >}}

At the end of the loop, the agent opens (or finds) a results PR on GitHub and asks Claude one more time to judge convergence - is the best metric actually good given the dataset, or did every experiment plateau/crash - and streams that verdict into the report and back to the app via a callback.

{{< code file="/unionai-examples/v2/tutorials/auto_train/agents/research_agent.py" fragment="pr_and_convergence" lang="python" >}}

### Orchestration

`automl_pipeline` is the thin task that wires the three agents together: data → design → research, `await`-ing each handoff. `pipeline_env`'s `depends_on=[data_env, design_env, research_env]` ensures its image is only built once the environments it calls into are resolved.

{{< code file="/unionai-examples/v2/tutorials/auto_train/pipeline.py" fragment="pipeline_orchestration" lang="python" >}}

## Running the Pipeline

### Prerequisites

1. A Flyte config (`~/.flyte/config.yaml`) pointing at your target cluster.
2. Two secrets created in the project/domain you deploy to:

   ```sh
   flyte create secret --project flytesnacks --domain development internal-anthropic-api-key <key>
   flyte create secret --project flytesnacks --domain development autotrain-github-token <PAT>
   ```

   The GitHub token must be able to **push and open PRs** on the experiments repo - for a fine-grained PAT that means Repository access limited to the target repo(s), **Contents: Read and write**, **Pull requests: Read and write**. (The "Public repositories" preset is read-only and will not work.) For an org-owned repo, the token's resource owner must be the org, and org policy may require approving it first.

3. [`uv`](https://docs.astral.sh/uv/) installed locally - the deploy command below runs the app via `uvx`.

### Deploy

```sh
uvx --with fastapi --with uvicorn --with jinja2 --with python-multipart \
    --with "connectrpc==0.10.1" --from "flyte==2.5.9" \
    flyte serve --project flytesnacks --domain development app.py automl_webapp
```

This only builds the **web** image - the cpu/gpu task images are built remotely the first time a run actually needs them (the gpu image takes roughly 5-7 minutes the first time; it's cached after that). The app itself scales to zero when idle, so the first request after a quiet period can take 30-60 seconds.

For local UI development against your real cluster config: `python app.py --local`.

### Using it

Open the deployed app's URL (`flyte get app --project flytesnacks --domain development` will print it) and submit the form, or POST directly:

```sh
curl -i -X POST https://<app-endpoint>/run \
  -d "dataset_link=https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" \
  -d "target_column=Survived" \
  -d "github_repo=your-org/your-experiments-repo" \
  -d "domain=auto" -d "max_experiments=1" -d "time_budget=60" -d "max_samples_raw=100"
```

The response is a 303 redirect to `/status/{job_id}` (a browser-friendly progress page); `/api/status/{job_id}` returns the same status as JSON, for scripting.

### Debugging

Because the app tracks no state of its own, the run itself is always the source of truth:

```sh
flyte get run    --project flytesnacks --domain development                 # recent runs
flyte get action --project flytesnacks --domain development <run>           # actions + errorInfo
flyte get logs   --project flytesnacks --domain development <run> <action>  # task logs
```

The most common failure isn't a bug - it's the status page sitting on "Building container images…" during the very first run, while the gpu image builds. If a run never appears at all, the submission itself failed before creating one; the status page will show the traceback in that case, and the app logs will have it too.

## What You Get

After a run completes:

- **Union UI**: a live report on the research task. The main tab is a running trace of every experiment the research agent tried and how it turned out:

  ![](../../../_static/images/tutorials/auto_train/main_tab.png)

  The Performance tab charts the metric across experiments: a yellow step line for the running best, gray dots for experiments with no improvement, and green dots for experiments that pushed the running best higher.

  ![](../../../_static/images/tutorials/auto_train/preformance_tab.png)

  And full logs are available for every stage:

  <!-- placeholder image: full logs -->

- **GitHub**: an experiment branch with the full history of `train.py` revisions (one commit per improvement) and a PR summarizing the best result, ready to review or merge.
- **The status page**: the best metric value, a link to the PR, and - if the agent's own convergence check flagged the result as unsatisfactory - a plain-language explanation of what went wrong and what to try next.

## Why Union?

You could wire something similar together with a cron job or a long-running script on a VM. A few things would be harder to get back once you did.

**Compute isolation.** Data profiling and experiment design are cheap CPU work; the research loop needs a GPU for hours at a stretch. Because each stage is its own `TaskEnvironment`, you only pay for GPU time during the part of the pipeline that actually needs one - the data and design agents run on 2-core CPU containers regardless of how large the eventual model turns out to be.

**Observability into an unattended, multi-hour process.** The research loop can run for a long time with no one watching. Every internal step - installing the CLI, cloning the branch, implementing the baseline, each change proposal, each training run, crash fixes, commits, PR creation, the final convergence check - is wrapped in `@flyte.trace`, so it shows up as its own action in the Union UI with inputs, outputs, and timing, nested inside the single task container. If experiment 14 crashes, you're not left with a bare stack trace - you can see exactly what the previous 13 experiments tried and why.

**Live results instead of a black box.** `flyte.report` streams the trace and a Plotly performance chart as the loop runs, so you can watch the metric improve (or stall) in real time instead of waiting for the whole run to finish before finding out it went nowhere.

**Secrets scoped to what needs them.** The Anthropic API key and the GitHub token are injected as `flyte.Secret`s on the task environments that need them, not baked into an image or handled in application code. A task pod that references a secret which doesn't exist in the target project/domain fails fast at admission, rather than midway through a training run.

**A frontend that doesn't carry the pipeline's weight.** The FastAPI app builds and deploys a small web image; the cpu/gpu task images are only built the first time a run actually needs them. Deploying or redeploying the frontend is fast, and because the app keeps no state of its own - status is always resolved from the run itself - a redeploy mid-run doesn't lose anyone's progress.

AutoTrain is a specific example of a more general pattern: an LLM decides what to try next, and Union handles how that work actually runs - on the right compute, with the right secrets, with every step traceable, whether the loop takes five minutes or five hours.
