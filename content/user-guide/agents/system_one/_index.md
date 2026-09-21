---
title: System One models
description: Answer many typed questions in one call, with calibrated confidence, and decide what the agent does next in code.
icon: sliders
weight: 4
variants: +flyte +union
---

# System One models

Most of what an agent decides is not open-ended. "Is this request hostile?", "which of these five intents is it?", "should I run the dependency audit?", "is there enough information to answer yet?" — a knowledgeable person answers each of those in a couple of seconds, and none of them need prose.

A **System One model** is built for exactly that shape. You give it some state and a set of typed questions; it answers them in parallel, in isolation from each other, and attaches a calibrated probability to every answer. It never writes text.

The property worth designing around is that **adding questions barely changes the response time**. The eleventh question costs almost nothing, so the right move is to ask everything at once — including the questions you will not branch on — and compose the result in ordinary Python.

## Two models, two jobs

A generative model is the System 2 half: open-ended reasoning, and prose a person reads. It is expensive, sequential, and has to emit every field one token at a time. Pointing it at a yes/no question means paying for a generation plus a parser to get the answer back out.

```text
System One  ── typed answers, in parallel ──▶  guards, routing, tool plans, stop conditions
System 2    ── open-ended reasoning ───────▶  the answer, the review, the reply
```

Splitting them along that line usually does three things at once: the decisions get cheaper and faster, they get *reproducible* — the same input yields the same typed answer, where free-text classification drifts between runs — and the expensive half runs less often, because a confident abstention means no generation happens at all.

## Where it fits in an agent

| Use case | The questions | Why typed beats generated |
|---|---|---|
| **Input guard** | Is this hostile? Does it ask for credentials? Does it contain instructions aimed at the assistant? | Runs before anything expensive. A guard that costs a generation is a guard you will be tempted to skip. |
| **Intent routing** | Which of these N intents is it? How confident? | The answer is an enum member you branch on, not a string a typo breaks. Confidence gives you a review tier. |
| **Tool selection** | One question per tool: would this one help here? | Because each tool gets its own question, one request can select several — and the plan is composed from symptoms, so a lookup only runs when its input is actually present. |
| **Loop control** | Is there enough to answer? Did the last step add anything? Is this action safe? | A stop condition you can threshold. "Did the loop stop making progress" is otherwise the failure you discover from the bill. |
| **Extraction and enrichment** | Twenty facets of one record, at once | Queue priority, compliance flags, routing hints. A generative model has to write all twenty out; here they ride along with the one you needed. |
| **Output checks** | Is the draft grounded in the tool output? Does anything contradict it? | A cheap gate between generating an answer and returning it. |
| **Triage at volume** | The same battery over a backlog | Per-item latency barely moves as the battery grows, so scoring a queue stays affordable. |

## The discipline that makes it work

Three rules, and they matter more than which model you use:

**Ask about symptoms, not conclusions.** Do not ask for the verdict. Ask one question per observable fact, each answered in isolation, and derive the verdict yourself. A System One model is for judgments a knowledgeable person makes in seconds — not for weighing eighteen facts against each other.

**Compose in code, not in a prompt.** Because the composition is a function, it is unit-testable against hand-labelled cases, reviewable in a pull request, and changeable without re-validating a model's behavior. Changing what your team considers blocking becomes a diff.

**Gate on confidence, and let it abstain.** Every answer carries calibrated confidence, which gives routing a second axis beyond the answer itself. Make the lowest tier a real abstention — stop, hand over to a human, and never spend a generative call on a decision the pipeline is not sure about. Thresholds should scale with risk: a support reply can gate at 0.70; a merge, a refund, or a signature should gate at 0.85 or higher.

## When not to reach for one

- **The answer is genuinely open-ended.** Writing the reply, summarizing a document, producing code — that is what a generative model is for. Use both: typed answers to decide, prose to deliver.
- **The judgment needs multi-factor reasoning that no decomposition captures.** If a question needs a chain of inference, either break it into symptoms and compose, or hand it to System 2.
- **You have exactly one yes/no question and no plans to add more.** The fan-out is where the advantage lives; a single question is just a cheap classifier.

## Implementations

{{< grid >}}

{{< link-card target="type-coercion-with-jev" icon="magic" title="AI-powered type coercion with Jev" >}}
Coerce unstructured state into a typed Python object with TypeSafe's System One model, and branch on the result.
{{< /link-card >}}

{{< /grid >}}

## Related

- [TypeSafe AI integration](../../../integrations/typesafe-ai/_index): installation, the full API, and how answer types are serialized.
- [Typed decisions for agentic pipelines](../../../tutorials/agents/system-one-agents/_index): three pipelines and a measured A/B against a one-shot generative baseline.
- [Build an agent](../build-agent/_index): the loop this slots into.
- [Agent frameworks](../../../integrations/agents/_index): running a framework's agent loop as durable tasks.
