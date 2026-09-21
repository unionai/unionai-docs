---
title: AI-powered type coercion with Jev
description: Coerce unstructured state into a typed Python object with TypeSafe's System One model, and branch on the result.
icon: magic
weight: 1
variants: +flyte +union
---

# AI-powered type coercion with Jev

[TypeSafe](https://docs.typesafe.ai/introduction)'s System One model ("Jev") is reached through the `flyteplugins-typesafe-ai` plugin. The shape it gives you is worth naming precisely: **type coercion**.

An ordinary coercion turns a string into an `int` by applying a rule. `ask()` turns a ticket, a diff, or any other blob of state into an instance of a dataclass you declared — by asking a model one question per field, all in the same request:

```python
triage: Triage = await ask(Triage, {"ticket": ticket})
```

`Triage` is your type. Its fields are the questions. What comes back is a real instance, with an enum member where you declared an enum and a probability where you declared a `Noul` — not a JSON blob you have to validate, and not prose you have to parse. From there you are writing normal Python against a normal object.

```bash
pip install flyteplugins-typesafe-ai
```

> [!NOTE]
> This page is the how-to. For the category — what a System One model is, where it fits, and the discipline that makes it pay off — see [System One AI](./_index). For installation detail and the full API, see the [TypeSafe AI integration](../../integrations/typesafe-ai/_index).

## The three field types

These are what you coerce *into*. Each is a plain dataclass carrying the answer plus its calibrated confidence.

| Type | Holds | Useful members |
|---|---|---|
| `Choice[SomeEnum]` | the picked enum member, `confidence`, the whole `probabilities` distribution | `.certain(threshold)`, `.runner_up()` |
| `Score[SomeIntEnum]` | the picked rung, the unrounded `position` on the scale, `confidence` | `.at_least(rung)` |
| `Noul` | truthfulness in 0..1 | `.at(threshold)` |

`Choice` comes back as the **enum member**, not a string, so you branch on `t.intent.value is Intent.REFUND` rather than on a string comparison that a typo silently breaks. `Score` keeps both representations on purpose: `value` is the rung you branch on, `position` is where on the scale the answer actually landed, which is what you sort and threshold by.

`Noul` deliberately has no `__bool__`. `if noul:` would treat 0.02 and 0.98 alike, and picking the threshold is precisely the part that belongs in reviewable code.

## Declare the target type

The dataclass is the schema, and the vocabulary documents itself — an enum's **class docstring** is the question and its **member docstrings** are the criteria, so a well-documented enum needs nothing at the call site. A `Noul` has no vocabulary to document itself with, so it always carries its own question.

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=vocabulary lang=python >}}

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=battery lang=python >}}

Thirteen fields, three of which decide what happens. The rest ride along because they are nearly free in the same call, and a real support desk wants them for queue priority and compliance flags. A generative model would have to emit all thirteen one token at a time.

## Coerce

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=guard-task lang=python >}}

`ask()` compiles the whole dataclass into a **single** request. Three separate `ask()` calls are three round trips; one battery is one. `ask_with_info()` returns the model name, question count, token usage and latency alongside the answers, which is what you want when you are measuring the fan-out.

The environment mounts the API key as an environment variable and nothing else:

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=env lang=python >}}

## Derive the verdict from the fields

Do not add a `verdict` field and let the model fill it in. Coerce the symptoms, then derive:

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=compose lang=python >}}

Because the composition is a function rather than a prompt, it is unit-testable against hand-labelled cases, reviewable in a pull request, and changeable without re-validating a model's behavior.

## Gate on confidence, and mean it

Every `Choice` and `Score` field carries calibrated confidence, which gives routing a second axis beyond the answer itself:

{{< code file="/unionai-examples/v2/user-guide/system-one/agent_guard.py" fragment=handle lang=python >}}

`escalate` is a real abstention, not a label. The pipeline stops, hands over to a human, and never spends a generative call on a decision it is not sure about. That is where most of the cost saving comes from in practice — not from the cheaper model, but from the calls that never happen.

## Coerce the agent's next move

The same coercion drives a loop. Instead of an all-purpose model picking the next move in free text and a regex fishing it back out, one `Step` object per turn carries the action, the confidence, and the stop conditions:

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=actions lang=python >}}

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=step lang=python >}}

Each turn asks all five questions in one request. Tools are ordinary tasks, so every step of the loop is a durable child action:

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=tools lang=python >}}

{{< code file="/unionai-examples/v2/user-guide/system-one/typed_loop.py" fragment=loop lang=python >}}

Two things to notice. The gate is the **confidence**, not the `Choice` — a confident wrong action is rarer than a low-confidence right one. And `made_progress` is what stops a loop that has started spinning, which is otherwise the failure mode you only discover from the bill.

## Coerced values cross task boundaries

`Choice`, `Score` and `Noul` are plain dataclasses, so Flyte carries them with nothing registered — including on their own, not just inside a battery:

```python
@env.task
async def classify(message: str) -> Choice[Action]:
    return await ask(Choice[Action], {"message": message})
```

The caller gets a real `Choice` back, with the picked member, its confidence, and the whole distribution. That means the coercion step can be its own cached, retryable task rather than a function call buried inside a larger one.

## Related

- [System One AI](./_index): the category, the use cases, and when not to reach for one.
- [TypeSafe AI integration](../../integrations/typesafe-ai/_index): installation, the full API, and how answer types are serialized.
- [Typed decisions for agentic pipelines](../../tutorials/agents/system-one-agents/_index): three pipelines and a measured A/B against a one-shot generative baseline.
- [Build an agent](../agents/build-agent/_index): the loop this slots into.
