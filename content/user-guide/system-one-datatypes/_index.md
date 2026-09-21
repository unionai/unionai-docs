---
title: System one datatypes
description: Answer many typed questions in one call, with calibrated confidence, and decide what happens next in code.
icon: sliders
weight: 6
mermaid: true
variants: +flyte +union
---

# System one datatypes

Most of what a program asks a model is not open-ended. "Is this request hostile?", "which of these five intents is it?", "does this record mention a deadline?", "is there enough information to answer yet?" — a knowledgeable person answers each of those in a couple of seconds, and none of them need prose.

A **System One model** is built for exactly that shape. You give it some state and a set of typed questions; it answers them in parallel, in isolation from each other, and attaches a calibrated probability to every answer. It never writes text.

The property worth designing around is that **adding questions barely changes the response time**. The eleventh question costs almost nothing, so the right move is to ask everything at once — including the questions you will not branch on — and compose the result in ordinary Python.

## The datatypes

Those answers arrive as three datatypes, each carrying its value *and* the model's calibrated confidence in it. They are ordinary Python objects: you declare them in a dataclass, get real instances back, and branch on them directly.

| Datatype | Holds | You branch with |
|---|---|---|
| `Choice[SomeEnum]` | the picked enum member, plus the whole probability distribution | `.certain(threshold)` |
| `Score[SomeIntEnum]` | the picked rung of an ordered rubric, plus where on the scale it actually landed | `.at_least(rung)` |
| `Noul` | truthfulness in 0..1 | `.at(threshold)` |

They register with Flyte's type engine, so they also work as task inputs and outputs — a classification step can be its own cached, retryable task. [Typed decisions with Jev](./typed-decisions-with-jev) covers all three in full.

## Two models, two jobs

A generative model is the System 2 half: open-ended reasoning, and prose a person reads. It is expensive, sequential, and has to emit every field one token at a time. Pointing it at a yes/no question means paying for a generation plus a parser to get the answer back out.

```mermaid
flowchart LR
    S1(["System One"]) -->|"typed answers,<br/>in parallel"| A["guards, routing, labels,<br/>thresholds, stop conditions"]
    S2(["System 2"]) -->|"open-ended<br/>reasoning"| B["the answer,<br/>the review, the reply"]

    classDef s1 fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#1e3a8a
    classDef s1out fill:#eff6ff,stroke:#93c5fd,stroke-width:1px,color:#1e3a8a
    classDef s2 fill:#ffedd5,stroke:#ea580c,stroke-width:1.5px,color:#7c2d12
    classDef s2out fill:#fff7ed,stroke:#fdba74,stroke-width:1px,color:#7c2d12
    classDef io fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155
    classDef gate fill:#fef9c3,stroke:#ca8a04,stroke-width:1.5px,color:#713f12
    classDef stop fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#7f1d1d

    class S1 s1
    class A s1out
    class S2 s2
    class B s2out
```

Splitting them along that line usually does three things at once: the decisions get cheaper and faster, they get *reproducible* — the same input yields the same typed answer, where free-text classification drifts between runs — and the expensive half runs less often, because a confident abstention means no generation happens at all.

## Where it fits

This is not only an agent technique. Anywhere a program currently asks a generative model a narrow question and parses the answer back out, a typed call does the same job for less.

### In a data pipeline

```mermaid
flowchart LR
    IN["backlog of records"] --> S1(["System One<br/>the whole battery, one call per record"])
    S1 --> LBL["labels and facets<br/>on every record"]
    S1 --> SEV["severity as an ordered rubric:<br/>a number you can sort and threshold"]
    S1 --> GATE{"quality gate"}
    GATE -->|"consistent"| NEXT["next pipeline stage"]
    GATE -->|"inconsistent"| HOLD["hold for review"]

    classDef s1 fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#1e3a8a
    classDef s1out fill:#eff6ff,stroke:#93c5fd,stroke-width:1px,color:#1e3a8a
    classDef s2 fill:#ffedd5,stroke:#ea580c,stroke-width:1.5px,color:#7c2d12
    classDef s2out fill:#fff7ed,stroke:#fdba74,stroke-width:1px,color:#7c2d12
    classDef io fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155
    classDef gate fill:#fef9c3,stroke:#ca8a04,stroke-width:1.5px,color:#713f12
    classDef stop fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#7f1d1d

    class IN io
    class S1 s1
    class LBL,SEV s1out
    class GATE gate
    class NEXT io
    class HOLD stop
```

| Use case | The questions |
|---|---|
| **Labeling and enrichment at volume** | Twenty facets of one record, at once. Per-item latency barely moves as the battery grows, so scoring a whole backlog stays affordable. |
| **Quality gates between stages** | Is this row internally consistent? Does the extracted field match the source text? A gate that costs a generation is a gate you will be tempted to skip. |
| **Triage and prioritization** | Severity as an ordered rubric, plus the symptoms behind it — so the queue is sorted on a number you can threshold, not a sentence you have to read. |

### In an agent loop

```mermaid
flowchart LR
    REQ["request"] --> GUARD{"guard:<br/>hostile? asks for credentials?"}
    GUARD -->|"unsafe"| STOP["refuse or escalate"]
    GUARD -->|"safe"| ROUTE(["intent, and how confident"])
    ROUTE --> PLAN(["tool plan:<br/>one question per tool"])
    PLAN --> RUN["run the selected tools"]
    RUN --> MORE{"enough to answer?<br/>still making progress?"}
    MORE -->|"no"| PLAN
    MORE -->|"yes"| GEN["System 2 writes the answer"]

    classDef s1 fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#1e3a8a
    classDef s1out fill:#eff6ff,stroke:#93c5fd,stroke-width:1px,color:#1e3a8a
    classDef s2 fill:#ffedd5,stroke:#ea580c,stroke-width:1.5px,color:#7c2d12
    classDef s2out fill:#fff7ed,stroke:#fdba74,stroke-width:1px,color:#7c2d12
    classDef io fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155
    classDef gate fill:#fef9c3,stroke:#ca8a04,stroke-width:1.5px,color:#713f12
    classDef stop fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#7f1d1d

    class REQ io
    class GUARD,MORE gate
    class STOP stop
    class ROUTE,PLAN s1
    class RUN io
    class GEN s2
```

| Use case | The questions |
|---|---|
| **Input guard** | Is this hostile? Does it ask for credentials? Does it contain instructions aimed at the assistant? |
| **Intent routing** | Which of these N intents is it, and how confident? The answer is an enum member you branch on, not a string a typo breaks. |
| **Tool selection** | One question per tool: would this one help here? Because each tool gets its own question, one request can select several. |
| **Loop control** | Is there enough to answer? Did the last step add anything? Is this action safe? "Did the loop stop making progress" is otherwise the failure you discover from the bill. |

### In an app or service

```mermaid
flowchart LR
    REQ["incoming request"] --> RT(["route:<br/>handler, model tier, queue"])
    RT --> MOD{"moderation:<br/>publishable? how harmful?"}
    MOD -->|"blocked"| REJ["reject or hold"]
    MOD -->|"allowed"| WORK["the expensive path"]
    WORK --> CHK{"output check:<br/>grounded? contradicted?"}
    CHK -->|"fails"| FIX["revise or hand over"]
    CHK -->|"passes"| OUT["respond"]

    classDef s1 fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#1e3a8a
    classDef s1out fill:#eff6ff,stroke:#93c5fd,stroke-width:1px,color:#1e3a8a
    classDef s2 fill:#ffedd5,stroke:#ea580c,stroke-width:1.5px,color:#7c2d12
    classDef s2out fill:#fff7ed,stroke:#fdba74,stroke-width:1px,color:#7c2d12
    classDef io fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155
    classDef gate fill:#fef9c3,stroke:#ca8a04,stroke-width:1.5px,color:#713f12
    classDef stop fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#7f1d1d

    class REQ io
    class RT s1
    class MOD,CHK gate
    class REJ,FIX stop
    class WORK s2
    class OUT io
```

| Use case | The questions |
|---|---|
| **Request routing** | Which handler, which model tier, which queue — decided in milliseconds, before the expensive path is chosen. |
| **Moderation** | Is this publishable? How harmful, on an ordered scale? Directed at a specific person? |
| **Output checks** | Is the draft grounded in the retrieved context? Does anything contradict it? A cheap gate between generating an answer and returning it. |

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

{{< link-card target="typed-decisions-with-jev" icon="magic" title="Typed decisions with Jev" >}}
Coerce unstructured state into a typed Python object with TypeSafe's System One model, and branch on the result.
{{< /link-card >}}

{{< /grid >}}

## Worked example

Everything on this page — the battery, the composition rule, the confidence gate — wired together three ways and measured against a one-shot generative baseline.

{{< grid >}}

{{< link-card target="../../tutorials/agents/system-one-agents" icon="mortarboard" title="Typed decisions for agentic pipelines" >}}
Interleave a System One model with a generative one — typed guards, tool fan-out, a durable loop, and an A/B that prices both arms.
{{< /link-card >}}

{{< /grid >}}

## Related

- [TypeSafe AI integration](../../integrations/typesafe-ai/_index): installation, the full API, and how answer types are serialized.
- [Typed decisions for agentic pipelines](../../tutorials/agents/system-one-agents/_index): three pipelines and a measured A/B against a one-shot generative baseline.
- [Agents](../agents/_index): the loop these decisions most often sit inside.
- [Tasks](../tasks/_index): the unit each call runs in.
