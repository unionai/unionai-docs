---
title: Typed decisions for agentic pipelines
icon: sliders
description: Interleave a System One model with a generative one — typed guards, tool fan-out, a durable loop, and an A/B that prices both arms.
weight: 9
variants: +flyte +union
---

# Typed decisions for agentic pipelines

> [!NOTE]
> Code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/typesafe_ai).

Most agent pipelines spend a generative model on work that isn't generative. Classifying an intent, deciding whether an input is hostile, choosing which of four tools to run, deciding whether the loop has enough information to stop — each of those is a judgment a knowledgeable person makes in a couple of seconds, and each one currently costs a full autoregressive generation plus a parser to get the answer back out.

A **System One model** answers that kind of question directly. You hand it state and a set of typed questions; it answers them in parallel, in isolation from each other, with a calibrated probability on every answer. It never writes prose. The property the whole design rests on is that *adding questions barely changes the response time* — so the eleventh question is nearly free, and the right move is to ask everything at once and compose the result in code.

This tutorial builds a pull-request reviewer around that split:

```
System 1  ── typed answers (Choice / Score / Noul) ──▶  guards, routing, tool plans
System 2  ── open-ended reasoning and prose ────────▶  the review the author reads
Flyte     ── durable, observable, fans tools out ───▶  the runtime underneath
```

It ships three pipelines in increasing order of how much the model decides, and a benchmark that runs the **same battery, the same cases and the same routing code** with and without the System One half, so the comparison is about where the answers come from rather than about how much each arm was asked to produce.

Uses [TypeSafe](https://docs.typesafe.ai/introduction)'s System One model through the [TypeSafe AI plugin](../../../integrations/typesafe-ai/_index). For the pattern on its own, without the benchmark, see [System One models](../../../user-guide/agents/system_one) in the user guide.

## The four patterns it is built around

| Pattern | What it means here |
|---|---|
| **Speculative fan-out** | Every question goes in one call, including the ones the verdict never reads. Ten of the eighteen questions below exist because a real reviewer wants them and they cost almost nothing. |
| **Atomic decomposition, verdict in code** | The model is never asked "what is the verdict?". It is asked one question per symptom, and a precedence rule in Python composes the verdict. |
| **Composite scoring** | Severity and the tool plan are both derived from the symptoms — a dependency audit only runs if a dependency actually changed. |
| **Confidence-gated routing** | `auto` / `review` / `escalate`, with thresholds that scale with risk. Escalation is a real abstention: the pipeline stops and never spends a generation. |

## Setting up the environment

One environment carries both keys, so a single task can interleave the two models. The driver is separate and larger: it holds every result in memory at once and renders the report, so its footprint grows with the size of the matrix rather than with the work of any single unit.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/_runtime.py" fragment=env lang=python >}}

## The vocabulary

An enum's class docstring is the question and its member docstrings are the criteria, so a documented enum needs no metadata at the call site.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/battery.py" fragment=vocabulary lang=python >}}

## The battery

Eighteen questions in one request. Note what is *not* here: there is no `verdict` question. Every entry is a single symptom, evaluated in isolation — which also avoids the context rot you get from asking one model to weigh eighteen facts at once.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/battery.py" fragment=battery lang=python >}}

The first five are hard guards: any one of them firing means the change must not be merged. The next three are what the verdict falls back to. The last ten are speculative — a human reviewer wants to know whether tests were added and whether a hot path got slower, and asking costs almost nothing once the call is already in flight.

## Composing the verdict

This is the part worth internalizing. Because the composition is a function rather than a prompt, it is unit-testable against hand-labelled cases, reviewable in a pull request, and changeable without re-validating a model's behavior.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/battery.py" fragment=compose lang=python >}}

Changing what your team considers blocking is a diff. So is changing where the confidence gate sits — and the gate is the thing that decides whether a generative model is called at all.

## The tools, and the cases

The backend tools are deterministic and read only the diff they are handed — never a case's ground-truth label — so the with-System-1 arm gets no hint the baseline arm could not also get.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/battery.py" fragment=tools lang=python >}}

Eight hand-labelled pull requests, four of them benign and four carrying planted code: an auth backdoor, environment-variable exfiltration, a typosquatted dependency, and a comment addressed at the reviewer telling it to approve without reading the rest of the diff.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/battery.py" fragment=cases lang=python >}}

That last one is worth calling out. Refusing to *follow* an instruction planted in a diff is not a reason to stop *analysing* that diff — the tools here only read the input, so a hostile diff still gets scanned, and the scan is the evidence the escalation rests on.

## Pattern 1: System One as a typed guard

The lowest-agenticness shape. One request answers the whole battery; code composes the verdict, picks the tools and gates on confidence; only then does anything generative run.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/agents.py" fragment=guard lang=python >}}

The report shows the routing tier, the composed verdict against ground truth, and which atomic signals fired — and counts the generations that never happened.

```bash
flyte run agents.py guard_review
```

## Pattern 2: plan, fan out, aggregate

The middle shape, and the one where the runtime earns its keep:

> System 1 structures the request → code composes a tool plan → **Flyte fans every selected tool out in parallel** → System 1 aggregates the pooled output → System 2 writes the answer.

Each tool is its own cached, retryable child action:

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/agents.py" fragment=tool-task lang=python >}}

The aggregation is a second System One call, this time over a mapping assembled at runtime rather than a dataclass — the questions are not known until the tools have run, and they still cost a single request:

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/agents.py" fragment=aggregate lang=python >}}

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/agents.py" fragment=fanout lang=python >}}

Because the plan is composed from the symptoms rather than asked for, one case can select several tools, which is what makes the fan-out wide.

```bash
flyte run agents.py plan_and_execute
```

## Pattern 3: a loop whose control flow is typed

The highest-agenticness shape. Instead of a generative model choosing the next move in free text and a regex fishing it back out, a `Choice` picks the action, a `Score` gates on confidence, and a `Noul` decides whether there is enough evidence to stop.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/agents.py" fragment=loop-types lang=python >}}

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/agents.py" fragment=loop lang=python >}}

Three things make this loop different from a prompt-driven one:

- **The gate is the confidence, not the `Choice`.** A confident wrong action is rarer than a low-confidence right one, so the abstention keys on `Score[Confidence]`, and below `MEDIUM` the loop hands over without spending a generation.
- **`made_progress` stops a spinning loop.** That is otherwise the failure mode you discover from the bill.
- **Every tool call is a child action.** A worker that dies on turn three resumes from the record instead of re-running the first two.

```bash
flyte run agents.py durable_review --case_id c4
```

## The benchmark

The interesting comparison is not "typed answers versus a verdict string". It is **the same deliverable, produced two ways**. Both arms owe the whole battery — eighteen typed answers — and both are composed and routed by the identical code in `battery.py`. The only thing that changes is where the answers come from.

The baseline arm's JSON schema is derived from the same dataclass, so the two arms cannot drift:

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/system2.py" fragment=schema lang=python >}}

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/system2.py" fragment=answer-battery lang=python >}}

Each `(case, arm, repeat)` is an independent Flyte action, so the whole matrix fans out across the cluster:

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/benchmark.py" fragment=unit lang=python >}}

`repeat` is part of the task signature on purpose. Every repetition gets its own identity, so it is separately retried and separately visible in the run graph — and repeats are what let the report say anything about *stability*, which is the second half of the claim. A System One model is not only cheaper; it is reproducible, where free-text classification drifts between runs on identical input.

{{< code file="/unionai-examples/v2/tutorials/typesafe_ai/benchmark.py" fragment=benchmark lang=python >}}

```bash
flyte run benchmark.py run_benchmark
flyte run benchmark.py run_benchmark --repeats 3 --num_cases 8
```

### What to look at in the report

| Column | Why it is there |
|---|---|
| **latency** | Mean and standard deviation. "Faster" without an error bar is not a claim. |
| **$ / case** | Every token priced at its vendor's published list rate, split System 1 versus System 2. |
| **verdict** | Label accuracy against ground truth — the check that cheaper did not mean worse. |
| **guard** | Hostile diffs escalated. With fewer than eight cases this column is meaningless, because the hostile cases sit at positions 4 through 7. |
| **agreement** | Share of repeats that agree on the modal verdict. This is the reproducibility number. |
| **escalated** | Units that abstained. A high number here is why the cost column is low — the savings come from the generations that never happened. |

Two honest caveats to keep in mind when you read your own numbers:

- **Cost is list-price equivalent.** No prompt caching and no batch discount are applied, so every token bills at the base rate. A negotiated contract bills something different. TypeSafe publishes no separate output price, so System 1 output is charged at the input rate; output is a small fraction of System 1's tokens, so that assumption moves the figure by a few percent at most.
- **Eight cases and a handful of repeats do not clear the noise threshold** on accuracy. Latency and cost gaps are usually large enough to survive it; label differences are not. Scale `--repeats` before drawing a conclusion about quality.

### Why the baseline has to owe the whole battery

It is tempting to benchmark against a one-shot call that returns four fields. Don't — it measures the wrong thing. Producing eighteen typed answers autoregressively is exactly what a generative model is bad at: every field costs tokens and latency, and a model loaded with eighteen fields to emit tends to drop precision on the ones it used to get right. Asking the baseline for less structure hides the effect that motivates using a System One model in the first place.

## Secrets

| Secret | Used for |
|---|---|
| `TYPESAFE_API_KEY` | System 1 — the TypeSafe API |
| `ANTHROPIC_API_KEY` | System 2 — the generative model |

```bash
flyte create secret TYPESAFE_API_KEY --value <your key>
flyte create secret ANTHROPIC_API_KEY --value <your key>
```

## Adapting it to your own task

Everything task-specific is in `battery.py`: the vocabulary, the battery, the composition rule, the thresholds, the tools and the cases. The three pipelines and the benchmark import from it and are otherwise task-agnostic — swap that one file and the same harness triages support tickets or reviews draft contracts instead.

When you do, keep the discipline that makes it work: one question per symptom, the verdict composed in code, the thresholds where a reviewer can see them, and an escalation tier that genuinely stops.

## Related

- [System One models](../../../user-guide/agents/system_one): the pattern on its own.
- [TypeSafe AI integration](../../../integrations/typesafe-ai/_index): installation, the full API, and how the answer types cross task boundaries.
- [Agent frameworks](../../../integrations/agents/_index): making a framework's own generative loop durable.
