---
title: System One models
description: Answer many typed questions in one call, with calibrated confidence, and decide what the agent does next in code.
icon: sliders
weight: 4
variants: +flyte +union
---

# System One models

Most of an agent's decisions are not open-ended. "Is this request hostile?", "which of these five intents is it?", "is there enough information to answer yet?" — a knowledgeable person answers each of those in a couple of seconds, and none of them need prose.

A **System One model** is built for exactly that shape. You give it some state and a set of typed questions; it answers them in parallel, in isolation from each other, and attaches a calibrated probability to every answer. It never writes text. The property worth designing around is that adding questions barely changes the response time, so the right move is to ask many small questions in one call and compose the result in ordinary Python.

That fits the front and the middle of an agent loop: guard the input, route it, pick the tools, check whether the loop has enough to stop. The generative model — the System 2 half — is then spent only on the part that genuinely needs prose.

> [!NOTE]
> The examples on this page use [TypeSafe](https://docs.typesafe.ai/introduction)'s System One model through the `flyteplugins-typesafe-ai` plugin. See the [TypeSafe AI integration](../../integrations/typesafe-ai/_index) for installation, the full API, and how the answer types cross a task boundary.

```bash
pip install flyteplugins-typesafe-ai
```

## Three answer types

| Type | Holds | Useful members |
|---|---|---|
| `Choice[SomeEnum]` | the picked enum member, `confidence`, the whole `probabilities` distribution | `.certain(threshold)`, `.runner_up()` |
| `Score[SomeIntEnum]` | the picked rung, the unrounded `position` on the scale, `confidence` | `.at_least(rung)` |
| `Noul` | truthfulness in 0..1 | `.at(threshold)` |

`Choice` comes back as the **enum member**, not a string, so you branch on `t.intent.value is Intent.REFUND` rather than on a string comparison that a typo silently breaks. `Score` keeps both representations on purpose: `value` is the rung you branch on, `position` is where on the scale the answer actually landed, which is what you sort and threshold by.

`Noul` deliberately has no `__bool__`. `if noul:` would treat 0.02 and 0.98 alike, and picking the threshold is precisely the part that belongs in reviewable code.

## Declare the battery

Group the questions into a dataclass. The vocabulary documents itself — an enum's **class docstring** is the question and its **member docstrings** are the criteria — so a well-documented enum needs nothing at the call site. A `Noul` has no vocabulary to document itself with, so it always carries its own question.

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=vocabulary lang=python >}}

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=battery lang=python >}}

Thirteen questions, three of which decide what happens. The rest ride along because they are nearly free in the same call, and a real support desk wants them for queue priority and compliance flags. A generative model would have to emit all thirteen fields one token at a time.

## Ask once

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=guard-task lang=python >}}

`ask()` compiles the whole dataclass into a **single** request. Three separate `ask()` calls are three round trips; a battery is one. `ask_with_info()` returns the model name, question count, token usage and latency alongside the answers, which is what you want when you are measuring the fan-out.

The environment mounts the API key as an environment variable and nothing else:

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=env lang=python >}}

## Compose the verdict in code

Do not ask a System One model for the verdict. Ask it one question per symptom, in isolation, and derive the verdict yourself:

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=compose lang=python >}}

This is the part worth internalizing. Because the composition is a function rather than a prompt, it is unit-testable against hand-labelled cases, reviewable in a pull request, and changeable without re-validating a model's behavior. Changing what your team considers blocking becomes a diff.

## Gate on confidence, and mean it

Every `Choice` and `Score` answer carries calibrated confidence, which gives routing a second axis beyond the answer itself:

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=handle lang=python >}}

`escalate` is a real abstention, not a label. The pipeline stops, hands over to a human, and never spends a generative call on a decision it is not sure about. That is where most of the cost saving comes from in practice — not from the cheaper model, but from the calls that never happen.

Thresholds should scale with risk. A support reply can gate at 0.70; a merge, a refund, or a signature should gate at 0.85 or higher.

## Type the agent's control flow

The same types drive a loop. Instead of an all-purpose model picking the next move in free text and a regex fishing it back out, a `Choice` picks the action, a `Score` gates on confidence, and a `Noul` decides whether there is enough to answer:

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=actions lang=python >}}

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=step lang=python >}}

Each turn asks all five questions in one request. Tools are ordinary tasks, so every step of the loop is a durable child action:

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=tools lang=python >}}

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=loop lang=python >}}

Two things to notice. The gate is the **confidence**, not the `Choice` — a confident wrong action is rarer than a low-confidence right one. And `made_progress` is what stops a loop that has started spinning, which is otherwise the failure mode you only discover from the bill.

## Answers cross task boundaries

`Choice`, `Score` and `Noul` are plain dataclasses, so Flyte carries them with nothing registered — including on their own, not just inside a battery:

```python
@env.task
async def classify(message: str) -> Choice[Action]:
    return await ask(Choice[Action], {"message": message})
```

The caller gets a real `Choice` back, with the picked member, its confidence, and the whole distribution. That means the classification step can be its own cached, retryable task rather than a function call buried inside a larger one.

## When not to reach for one

- **The answer is genuinely open-ended.** Writing the customer's reply, summarizing a document, producing code — that is what a generative model is for. Use both: typed answers to decide, prose to deliver.
- **The judgment needs multi-factor reasoning that no decomposition captures.** A System One model answers questions a knowledgeable person could answer in seconds. If a question needs a chain of inference, either break it into symptoms and compose, or hand it to System 2.
- **You have exactly one yes/no question and no plans to add more.** The fan-out is where the advantage lives; a single question is just a cheap classifier.

## Related

- [TypeSafe AI integration](../../integrations/typesafe-ai/_index): installation, the full API, and how answer types are serialized.
- [Typed decisions for agentic pipelines](../../tutorials/agents/system-one-agents/_index): three pipelines and a measured A/B against a one-shot generative baseline.
- [Build an agent](./build-agent/_index): the loop this slots into.
- [Agent frameworks](../../integrations/agents/_index): running a framework's agent loop as durable tasks.
