---
title: Serve and retrain draft models
icon: arrow-repeat
description: Serve Qwen3-8B with an EAGLE-3, DFlash, or DSpark drafter as a vLLM app, record an agent's traces with flyte.trace, and retrain each drafter nightly, promoting it only when it drafts better.
weight: 5
variants: +flyte +union
---

# Serve and retrain draft models

A drafter trained on last month's traffic drafts worse for this month's. New tools, new
prompt templates, and new response formats lower its acceptance length, and with it the
speedup, while outputs stay correct. Nothing fails loudly; responses get slower.

The fix is a loop. The application's own model calls are the training data, because every
response the target served is, by definition, what the target says. This page serves a
drafter of any family, runs an agent against it, and retrains each family's drafter every
night on the agent's traces.

## Serve the target with a drafter

`drafter_app` builds a `VLLMAppEnvironment` for any family. It passes the drafter as
`draft_model_path`, and the family's speculative method and draft length from its recipe:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/serve.py" fragment="app" lang="python" >}}

- **One app per family.** `qwen3-8b-eagle3`, `qwen3-8b-dflash`, and `qwen3-8b-dspark` serve the
  same target with different drafters, so you can route traffic to the family that wins your
  [benchmark](./benchmark).
- **`flyte.app.RunOutput`** resolves to the `Dir` returned by the latest successful run of the
  family's training pipeline, so each app serves whatever that pipeline last trained.
  `--run <name>` pins a specific run.
- **Both models load from disk.** With a draft model set, the plugin turns off weight
  streaming and downloads both models to the container, so give the app enough `disk`.
- **The endpoint is public with an API key.** `requires_auth=False` opens the URL, and vLLM's
  `--api-key` checks every request against the `specdec-api-key` secret. Create it first:

  ```bash
  flyte create secret specdec-api-key --project <project> --domain <domain>
  ```

  Enter any random string when prompted.

Deploy an app:

```bash
python serve.py                    # EAGLE-3
python serve.py --method dflash    # or dspark
```

The first start takes several minutes: vLLM loads both models and captures CUDA graphs for
the draft and verify passes.

## Record the agent's traces

The application is a tool-calling agent that runs as a task and calls one of the apps.
`depends_on` deploys every app with the task environment. Each scales to zero, so an app
holds no GPU until traffic reaches it:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/serve.py" fragment="agent-env" lang="python" >}}

Every model call is a `flyte.trace`. The trace records each call's inputs and output in the
run, so you can inspect what the agent asked and what the model answered in the UI. The job
also returns its episodes as a file:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/serve.py" fragment="agent-job" lang="python" >}}

The job's report shows what the agent did: episodes, failures, tool calls, latency per
episode, the most called tools, and a rendered example. Send traffic through an app:

```bash
python serve.py --agent 500                    # through the EAGLE-3 app
python serve.py --method dflash --agent 500    # through the DFlash app
```

These are the traces the retraining loop consumes. Every response in them is the target's,
whichever drafter served it, so one stream of traffic trains every family. In your own
application, any task or app that logs its prompts, tool schemas, and the model's responses in
OpenAI chat format can feed the same loop. Training data needs no hidden states: the trainer
recomputes them from the text.

> [!WARNING]
> Traces contain whatever your users send. Filter or redact personal data before traces
> reach training, and keep trace files under the same access controls as your logs.

## Retrain nightly, promote only on improvement

`retrain` runs every night once per family, from 03:00 UTC, an hour apart so their GPU jobs
do not start at once. It finds the agent runs from the past day with `flyte.remote`, and the
family's production drafter from its newest successful `retrain` or training pipeline run:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/flywheel.py" fragment="collect" lang="python" >}}

It then warm-starts from that drafter, trains one epoch on the new traces plus replayed chat
data, and benchmarks the candidate against the current drafter on the newest 10% of traces,
which training did not see:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/flywheel.py" fragment="retrain" lang="python" >}}

Each cycle's report records the decision: the family and trace window, how many traces
trained the candidate and how many prompts tested it, both acceptance lengths, and whether the
candidate was promoted.

Design choices that keep the loop safe:

- **The gate measures acceptance length, not training loss.** Loss and acceptance length can
  disagree. The gate serves both drafters in vLLM and measures what production would see.
- **Evaluation uses the newest traffic.** Holding out the most recent traces checks the
  candidate against where traffic is heading, not where it was.
- **Replay prevents forgetting.** Each cycle mixes in regenerated general chat. The replay
  shard has the same inputs as the pipeline's, so it is a cache hit and costs no GPU time.
- **A warm start keeps the drafter's architecture.** Starting from an existing drafter,
  `train_drafter` drops the flags that shape a new model, such as DSpark's layer count, and
  trains the drafter as it is.
- **Too little traffic is a no-op.** Below `min_traces`, the task returns the current drafter
  unchanged.
- **A losing candidate is discarded.** The task returns the current drafter, so the newest
  `retrain` output for a family is always the drafter that should be in production.

Register the triggers, or run one cycle now:

```bash
python flywheel.py                        # deploys the environment and its nightly triggers
python flywheel.py --now --method dspark  # one cycle immediately, for one family
```

To roll an app forward, redeploy it pinned to the `retrain` run:
`python serve.py --method dspark --run <retrain-run>`.

> [!NOTE] Retrain whenever the target changes
> A drafter is trained on one target's hidden states. If you fine-tune, quantize, or upgrade
> the target model, retrain every drafter before serving them together.

{{< variant union >}}
{{< markdown >}}

## Version drafters and traces as artifacts

On Union, publish each promoted drafter as a version of its family's artifact, such as
`qwen3-8b-dflash-drafter`, with a model card. The card shows the family, its recipe, the run
that produced it, and its benchmark results: acceptance length, speedup, and agreement with
no speculation, per workload.

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/promote.py" fragment="model-card" lang="python" >}}
{{< markdown >}}

Publish the traces a drafter trained on as a data artifact. Its data card summarizes the
episodes and tools and renders an example episode:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/promote.py" fragment="data-card" lang="python" >}}
{{< markdown >}}

Serve the artifact instead of a run output. `ArtifactValue` without a version resolves to
the latest version, and pinning a version rolls back:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/promote.py" fragment="artifact-app" lang="python" >}}
{{< markdown >}}

```bash
python promote.py --method dflash --run <training-run> --benchmarks <compare-run>
python promote.py --traces <agent-job-run> ...       # publish traces, with a data card
python promote.py --method dflash --serve            # serve the latest drafter
python promote.py --method dflash --rollback <version>
```

{{< /markdown >}}
{{< /variant >}}

## When a learned drafter is not the answer

On highly repetitive agent traffic, where outputs copy long spans from the prompt or earlier
turns, **suffix decoding** often accepts more tokens than any learned drafter, with no
training. The SuffixDecoding paper reports about 6.2 accepted tokens per step on an agentic
text-to-SQL workload, against about 3.2 to 3.6 for EAGLE-3. The [benchmark](./benchmark)
includes a `suffix` configuration so you can check this on your own traffic before investing
in a training loop.
