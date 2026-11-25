---
title: Rubric rewards and checkpoints on Harvey's LAB
icon: briefcase
description: Run Harvey's Legal Agent Benchmark through Flyte on US open-weight models, audit what a rubric reward pays for and how noisy its judge is, test whether padding buys rubric points, and pick a checkpoint with a cached eval matrix and a pairwise tournament.
weight: 8
variants: -flyte +union
---

# Rubric rewards and checkpoints on Harvey's LAB

Harvey's [Tenet recipe on US open-weight models](https://www.harvey.ai/blog/applying-the-harvey-tenet-training-recipe-to-us-open-weight-models) trains legal agents with reinforcement learning against an LLM judge that grades expert rubrics. The reward is `0.35 c + 0.35 h + 0.30 a`: the fraction of criteria passed, the fraction of issue groups passed in full, and an all-pass bonus, with zero for an episode cut off by its turn or context limit. The training tasks come from Harvey's [Legal Agent Benchmark](https://github.com/harveyai/harvey-labs) (LAB): 2,010 legal tasks with about 114,000 pass/fail criteria, an agent harness, and a grader, all MIT-licensed.

This tutorial runs LAB itself, through Flyte, with US open-weight models served by vLLM on the same GPU node, and asks four questions about that kind of reward:

1. Which term of the reward actually moves a GRPO advantage, and how much of it is judge noise?
2. Does the rubric pay for padding, and does a pairwise judge agree?
3. What changes across checkpoints when you train against it?
4. How many pairwise judgments does it take to call a preference result a null?

It is not a replication of Harvey's results. LAB publishes no hold-out split, so the tasks are a seeded sample; the judges are open-weight models; the policies are 20B–120B; and episodes are capped at a few dozen turns.

> [!NOTE]
> Full code is available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/legal_agent_rl).
> The examples were run on one 8× AMD Instinct MI355X node from a GPU market, reached through a queue, and on a single NVIDIA L40S.
> The calibration step uses LAB's standard hosted judges and needs secrets named `ANTHROPIC_API_KEY` and `OPENAI_API_KEY`.

## Run it

```bash
git clone https://github.com/unionai/unionai-examples
cd unionai-examples/v2/tutorials/legal_agent_rl
export CLUSTER=amd GPU_QUEUE=<your GPU queue>   # or CLUSTER=demo for one NVIDIA GPU
python smoke.py                                  # one rollout per model, both judges, one LoRA step
python sweep.py --tasks 48 --samples 8           # base rollouts and grades
python audit.py --sweep-run <run>                # the reward and judge audit, on CPU
python padding.py --sweep-run <run>              # the padding probe
python train.py                                  # checkpoints
python checkpoints.py --train-run <run>          # checkpoint matrix and tournament
```

## LAB in a pod

LAB runs each agent in its own `--network=none` Podman container. A Kubernetes pod can't start containers, so the GPU image is built from LAB's own sandbox image, and `PodSandbox` implements LAB's sandbox interface over a private directory per rollout. The agent still sees LAB's canonical paths (`/workspace`, `/workspace/documents`, `/workspace/output`) and LAB's tools, system prompt, skills and agent loop, unchanged.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/lab_harness.py" fragment="pod_sandbox" lang="python" >}}

Two differences from LAB's own runs follow from this, and both are worth stating: the pod has a network, and several rollouts share one container.

The images start from that sandbox image and add vLLM. vLLM publishes ROCm wheels, so the AMD image comes from Flyte's builder like the CUDA one, without a `vllm serve` entrypoint to work around:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/images.py" fragment="images" lang="python" >}}

## One rollout

A rollout is one agent episode on one LAB task. The adapter is LAB's OpenAI-compatible one, extended to ask vLLM for the token IDs and log-probabilities it sampled, so the same rollout can be used for training without re-tokenizing.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/lab_harness.py" fragment="rollout" lang="python" >}}

Grading is LAB's `score_rubric`, unchanged. The only new piece is a judge that sends LAB's `rubric_criterion` prompt to an OpenAI-compatible server, so a rubric can be graded by an open-weight model on the same node. The reward terms follow Harvey's post:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/lab_harness.py" fragment="reward" lang="python" >}}

LAB's public rubrics have no issue-group field, so the sweep asks the judge model to group each task's criteria by legal issue, once per task. That grouping is a stand-in for Harvey's, not theirs.

## A sweep on a node that can be taken back

The GPU market grants whole nodes and can take one back at any time. The sweep is one task per node, and every rollout and every grade inside it is a `@flyte.trace`:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/sweep.py" fragment="traced" lang="python" >}}

When the task retries on a new node, finished rollouts and grades replay from the record and only the rest run. The task is cached on its config, so asking for the same sweep twice costs nothing.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/sweep.py" fragment="sweep" lang="python" >}}

<!-- RESULTS: sweep -->

## What the reward pays for

The trainer never sees the reward's terms on their own. It sees each rollout's advantage: its reward minus its group's mean. So `reward_audit.py` asks, within each group of G rollouts of one task, how much of the reward's variance comes from each term. Each term's share is `Cov(part, R) / Var(R)`, and the shares sum to 1.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/reward_audit.py" fragment="term_shares" lang="python" >}}

Judge noise is measured the same way: re-grade the same rollouts and compare how much a rollout's reward moves between gradings with how much rewards differ within its group.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/reward_audit.py" fragment="judge_noise" lang="python" >}}

The audit is CPU work over verdicts that are already paid for, so changing the weights is a new run of `audit.py`, not a new sweep.

<!-- RESULTS: audit -->

## Does the rubric pay for padding?

`padding.py` takes real deliverables and appends four plausible but non-responsive issues, either generic cautions or matter-specific speculation, then grades each variant with the rubric and compares it with the unpadded draft in both orders:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/preference.py" fragment="both_orders" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/padding.py" fragment="summarize" lang="python" >}}

<!-- RESULTS: padding -->

## Training to make checkpoints

`train.py` uses the loss Harvey describes: rank-64 LoRA, CISPO's clipped, gradient-free importance weight, Dr. GRPO's advantage and constant normalizer (`T0 = 55,000`), G = 8, and only model-generated tokens in the loss.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/train.py" fragment="cispo" lang="python" >}}

Each turn's prompt is the conversation as the server rendered it, so a rollout becomes one training sequence per run of turns whose prompts extend each other:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/train.py" fragment="merge" lang="python" >}}

Things that differ from the published recipe, and why:

- **Synchronous, not asynchronous.** Sample, grade, one optimizer step, repeat. The importance weight corrects train/inference numerics, not staleness.
- **A bf16 copy of gpt-oss-20b.** vLLM's LoRA path for gpt-oss's MXFP4 weights builds an emulation kernel at startup that a pip-installed ROCm stack can't compile, so the policy is dequantized once and served and trained in bf16.
- **LoRA on the attention projections.** Harvey's adapter covers the whole network, routed experts included. Expert LoRA only fits 16k-token sequences on this stack, and attention projections are the layers vLLM hot-loads for gpt-oss.
- **Four data-parallel trainer ranks** on the node's last four GPUs, with the adapter's gradients all-reduced.

<!-- RESULTS: training -->

## A checkpoint matrix of cached cells

Picking a checkpoint is a matrix: checkpoints down one side, eval suites across the top. Every cell is its own cached task in a reusable environment, so the cells share one warm node, the policy server holds every checkpoint as a LoRA adapter, and a new checkpoint or a new suite runs only its new cells.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/checkpoints.py" fragment="reusable" lang="python" >}}

The tournament is cells too: one per pair of checkpoints, sample-matched, both orders, including an A/A pair of a checkpoint against itself.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/checkpoints.py" fragment="pair_cell" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/preference.py" fragment="bradley_terry" lang="python" >}}

<!-- RESULTS: matrix -->

## Things this example hit

- **aiter compiles at first use.** On a pip-installed ROCm stack, vLLM's aiter kernels fail their runtime build and the engine dies on the first request. `servers.py` sets `VLLM_ROCM_USE_AITER=0`.
- **Every model needs its tool-call parser.** `--enable-auto-tool-choice` without `--tool-call-parser` exits at startup; `servers.PARSERS` holds the ones used here.
- **A custom base image needs Flyte in its own interpreter.** Building from LAB's sandbox image put Flyte in a separate virtual environment the entrypoint couldn't find; installing into the image's Python fixes it and keeps `lab_core` next to the agent's document tools.
- **Not every model is an agent in this harness.** Olmo 3 7B Instruct answered in prose instead of calling tools, and vLLM 0.34 doesn't support Inkling 2 Mini's architecture yet.
- **Whole-node GPU pools.** GPUs go in a pod template, every task in the run goes to the pool's queue, and images are built off-queue and pinned.
