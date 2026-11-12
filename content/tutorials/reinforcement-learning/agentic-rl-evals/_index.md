---
title: Harness evals and trace audits for agentic RL
icon: clipboard-check
description: Treat the agent harness as a versioned input, cache every eval cell, and mine published RL traces for failure modes before you train.
weight: 6
variants: -flyte +union
---

# Harness evals and trace audits for agentic RL

Before an agentic RL run spends GPU time, two questions decide whether the reward means anything: does the harness work, and what do the failures look like? This tutorial builds both checks as pipelines:

- **A harness eval.** A Claude agent answers analyst questions from a company's shared drive (PDF, spreadsheet, slide deck, inbox) under two harness versions. Every (task, harness, model, pass) cell is a cached action, so a harness fix re-runs only the cells it touches, and adding a model runs only that model's cells.
- **A trace audit.** A fan-out over published agent trajectories that computes deterministic features for every trajectory and labels every failure with an LLM. It runs on the Terminal-Bench 2.1 traces that Mercor published with its 397B SkyRL training guide.

Both follow the same lesson from that guide: harness fixes alone raised Mercor's untrained 35B policy from 22.74% to 28.69% mean reward, which it describes as "roughly what one epoch of training would have bought."

> [!NOTE]
> Full code is available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/agentic_rl_evals).
> You need an Anthropic API key stored as a secret named `ANTHROPIC_API_KEY`.
> To use a secret with another name, set `ANTHROPIC_SECRET=<name>` when you launch.

## Run it

```bash
git clone https://github.com/unionai/unionai-examples
cd unionai-examples/v2/tutorials/agentic_rl_evals

flyte run harness_eval.py compare_harnesses   # harness v1 vs v2 on claude-haiku-5-5
flyte run harness_eval.py leaderboard         # several models on harness v2
flyte run trace_audit.py audit                # Mercor's Terminal-Bench 2.1 traces
flyte run trace_audit.py audit --classify false   # features only, no LLM calls
```

## The harness is an input

A harness is everything between the model and the world: tool implementations, timeouts, retries, the packages in the code sandbox, and the budget nudge. In this example it's a Pydantic model, so it's part of every trial's cache key.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_world.py" fragment="harness" lang="python" >}}

`HARNESS_V1` reproduces the bug classes that Mercor's guide reports finding in its traces. `HARNESS_V2` fixes each one.

| Bug in v1 | What the agent sees | Fix in v2 |
| --- | --- | --- |
| PDF reader follows the content stream (`pypdf`) | A headcount table whose values come out in reverse order, so labels pair with the wrong numbers | Layout-aware tables (`pdfplumber`) |
| Slides tool returns `None` on every call | `None`, even though the tool did its work | Return the slide text |
| `pdfplumber` and `python-pptx` missing from the code sandbox | `ModuleNotFoundError` from `run_python` | Install them |
| Email search has no timeout in front of a flaky server | A call that never returns, so the trial hits its deadline | 10-second tool timeout and one retry |
| No budget nudge | Nothing | "N turns left. Submit your best answer soon." at 75% of the turn budget |

Bump `Harness.version` whenever tool code changes. Cache keys come from a task's inputs and its own function body, not from helper modules it imports, so a change to `harness_world.py` alone doesn't invalidate cached trials.

## Worlds and tasks

Each world is a deterministic company: a board-report PDF, an operating-model workbook with formulas, a strategy deck, and an inbox. Each world has four tasks with exact answers.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_world.py" fragment="tasks" lang="python" >}}

`build_world` writes the files once per world and returns them as a `flyte.io.Dir`. The task is cached, so every later run reuses the same world.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_eval.py" fragment="build_world" lang="python" >}}

## One trial is one cached action

The agent loop sends tool failures back to the model as errors. Only the harness's limits end a trial. Each tool call is recorded before it's awaited, so a call that hangs still appears in the trajectory.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_world.py" fragment="agent_loop" lang="python" >}}

`run_trial` wraps the loop in a task. It downloads a private copy of the world, so writes from one trial never reach another.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_eval.py" fragment="run_trial" lang="python" >}}

Failures land in three places:

- **The harness deadline** (`agent_timeout_s`) ends a stuck trial and records it as `agent_timeout`. The trajectory is a result, and it's cached like any other.
- **Transient API errors** (rate limits, 5xx, dropped connections) raise, and the task retries the whole trial with exponential backoff.
- **Bad credentials** raise `flyte.errors.NonRecoverableError`, so the task fails at once instead of retrying.

The task's own `timeout` is a backstop for anything that ignores `asyncio`, such as a blocking native call.

The trial environment is a warm pool (`flyte.ReusePolicy`) because trials spend most of their time waiting on the model API. For worlds that run MCP servers inside the sandbox, run one pod per trial with `run_trial.override(reusable="off")`.

## Grade separately from generating

The verifier is deterministic and decides the reward. The LLM judge scores the justification against a rubric, and it's wrapped in `@flyte.trace`, so a retried grading task replays the score instead of paying for it again.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_eval.py" fragment="grade" lang="python" >}}

Because `grade` is its own action and `Rubric` is an input, a new rubric re-grades the stored trajectories without re-running the agent.

## Evaluate and compare harnesses

`evaluate` fans out every (task, pass) cell for one policy and one harness, then summarizes them. The summary includes the share of trials a Mercor-style masking rule would drop from the gradient: any error masks a task's group, two or more timeouts mask the group, and fewer timeouts mask only themselves.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_eval.py" fragment="evaluate" lang="python" >}}

`compare_harnesses` runs both harness versions on the same model, then asks `claude-sonnet-5-5` to read the failed v1 trajectories and list suspected tool or environment bugs.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_eval.py" fragment="compare" lang="python" >}}

On `claude-haiku-5-5` with 6 worlds and 3 passes (72 trials per harness):

| | Harness v1 | Harness v2 |
| --- | --- | --- |
| Pass@1 | 76.4% (±2.0 across passes) | 100% |
| PDF table / email lookup tasks | 50% / 56% | 100% / 100% |
| Slides / spreadsheet tasks | 100% / 100% | 100% / 100% |
| Agent timeouts | 8 | 0 |
| Trials masked by the Mercor-style rule | 12.5% | 0% |
| Tool calls / mean turns | 231 / 3.83 | 180 / 3.24 |
| Tool error rate | 0.0% | 0.6% |

The tool error rate is 0% on the broken harness. The bugs that cost the most points return wrong output without raising, so an error-rate metric can't see them.

The slides tasks pass on v1 because the agent works around the bug. After `read_slides` returns `None` and `import pptx` fails, it opens the `.pptx` as a zip file and reads the slide XML. During RL, a workaround like this is behavior the policy learns.

The audit named the PDF layout bug and the email hang without being told what to look for. Clip long tool output in the audit digest with an explicit marker. Otherwise the auditor reports your own truncation as a tool bug.

## Add a model, pay for its cells

`leaderboard` evaluates several models on one harness. Cells that already exist come back from the cache, so a new model costs only its own trials.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/harness_eval.py" fragment="leaderboard" lang="python" >}}

Running `leaderboard` for `claude-haiku-5-5` and `claude-sonnet-5-5` after `compare_harnesses` reused 60 of Haiku's 72 v2 cells and ran 72 new Sonnet cells. Each trajectory records `produced_by_run`, so the summary can count cells executed in the current run and cells reused from earlier ones.

## Audit published traces

`trace_audit.py` reads a trace set from Hugging Face, computes features for every trajectory, and labels each failure with one category from a fixed taxonomy.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/trace_audit.py" fragment="types" lang="python" >}}

Downloading and feature extraction are cached per trace set. The classifier (model, prompt version, and taxonomy) is an input to the labeling task, so changing it re-labels the failures and leaves the downloads and features alone.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/trace_audit.py" fragment="classify" lang="python" >}}

Each labeling task handles a chunk of about 20 trajectories. That keeps pod startup small relative to the work, and a retried chunk replays the LLM calls it already finished.

{{< code file="/unionai-examples/v2/tutorials/agentic_rl_evals/trace_audit.py" fragment="driver" lang="python" >}}

Results on `mercor/ApexAgentsRecipe-TBench2_1-EvalTraces` (89 tasks, 3 rollouts each, 267 trajectories per set). Pass@1 matches the dataset card.

| Set | Pass@1 | Minutes, p50 / p90 / max | Time in slowest 10% | Failed but ≥75% of tests passed | Most common failure label |
| --- | --- | --- | --- | --- | --- |
| Qwen3.6-35B untrained | 44.6% | 27 / 184 / 243 | 27% | 24 of 148 | false completion (89) |
| Qwen3.6-35B trained | 50.9% | 31 / 184 / 249 | 30% | 14 of 131 | false completion (55) |
| Qwen3.5-397B untrained | 50.6% | 10 / 182 / 201 | 49% | 31 of 132 | false completion (74) |
| Qwen3.5-397B trained | 55.4% | 11 / 183 / 212 | 42% | 21 of 119 | false completion (60) |

A false completion is a trajectory where the agent declares the task done and the tests disagree. In the trained 35B set, failures labeled as tool or harness problems rise from 11 to 38. Those failures include model-endpoint errors after hours of work and terminals that stop responding. Labels come from an LLM, so read them as a starting point for looking at traces, not as ground truth.

## Gotchas

- **Concurrent calls to the same cached task can both run.** If two evaluations call `build_world("w5")` at the same moment, both can miss the cache. Each then keys its trials on a different output. Give shared inputs `cache=flyte.Cache(behavior="auto", serialize=True)`, as `build_world` does here: one call runs and the others wait for its cached result.
- **Child task specs are built in the parent's container.** Module-level configuration, such as a secret name read from an environment variable, is evaluated again in every container. Pass it to the parent's environment with `env_vars` so child tasks get the same value.
- **Warm replicas keep the secrets they started with.** If you rotate the API key, give the reusable environment a new name or let the pool idle out.
- **Bump `Harness.version` when tool code changes.** Cache keys don't include imported helper modules.

## Related

- [Durable agentic RL with SkyRL and Harbor](../agentic-rl-skyrl/_index) builds the training side: durable trials, a memoized judge, and exactly-once training steps.
- [Can a LoRA screen pick the right ablation?](../lora-ablation-screen/_index) compares LoRA and full-weight rankings of RL loss aggregations.
