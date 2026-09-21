---
title: TypeSafe AI
description: Run TypeSafe's System One model inside durable Flyte tasks, and carry its typed answers across task boundaries.
icon: sliders
weight: 1
variants: +flyte +union
---

# TypeSafe AI

The `flyteplugins-typesafe-ai` plugin runs [TypeSafe](https://docs.typesafe.ai/introduction)'s System One model ("Jev") inside Flyte tasks.

Jev does not write text. It answers typed questions — in parallel, in isolation, and with calibrated confidence attached to every answer. The documented property worth building around is that *adding questions barely changes the response time*, so the right move is to ask many small questions in one call and compose the result in code you can read and change.

The plugin supplies the two things that Flyte needs: a shape for the answers that survives a task boundary, and a way to ask a whole battery at once.

```bash
pip install flyteplugins-typesafe-ai
```

## When to use this plugin

- You want a fast, model-based I/O guard in front of a generative model — filtering hostile input, or parsing one raw request into clean typed fields for several downstream steps.
- Your agent's control flow is a set of small decisions (which intent, which tool, is there enough to answer) that you would rather branch on directly than fish back out of prose.
- You want the routing thresholds in reviewable Python, and the answers to carry calibrated confidence so abstention is a real option.

For the pattern in full — composing verdicts from atomic questions, confidence-gated routing, and typed agent loops — see [System One datatypes](../../user-guide/system-one-datatypes/_index) in the user guide.

For a complete pipeline built on this plugin — three patterns and a measured A/B against a one-shot generative baseline — see [Typed decisions for agentic pipelines](../../tutorials/agents/system-one-agents/_index).

## The three answer types

| Type | Holds | Useful members |
|---|---|---|
| `Choice[SomeEnum]` | the picked enum member, `confidence`, `probabilities` | `.certain(threshold)`, `.runner_up()` |
| `Score[SomeIntEnum]` | the picked rung, the unrounded `position`, `confidence` | `.at_least(rung)` |
| `Noul` | truthfulness in 0..1 | `.at(threshold)` |

`Choice` comes back as the **enum member**, not a string, and `Score` keeps both representations on purpose: `value` is the rung you branch on, `position` is where on the scale the answer actually landed, which is what you sort and threshold by.

`Noul` deliberately has no `__bool__`. `if noul:` would treat 0.02 and 0.98 alike, and picking the threshold is the part that belongs in reviewable code.

These are plain dataclasses, so **pydantic is not required** and there is no bespoke type transformer — they reuse Flyte's built-in dataclass handling. The plugin registers them with the type engine through the standard `flyte.plugins.types` entry point, so `flyte.init()` picks them up, and importing the package registers them too.

## Setup

The TypeSafe SDK reads the key from `TYPESAFE_API_KEY`, so mount your secret as that environment variable. There is no helper for this — it is a plain `flyte.Secret`:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/_env.py" fragment=env lang=python >}}

`flyte.Secret` derives `as_env_var` from the key by upper-casing it and swapping `-` for `_`, so a secret named `TYPESAFE_API_KEY` mounts correctly from `flyte.Secret(key="TYPESAFE_API_KEY")` alone. Spelling `as_env_var` out is worth the extra words: it is the string you will grep for when a task cannot find the key.

Create the secret once:

```bash
flyte create secret TYPESAFE_API_KEY --value <your key>
```

If the key is missing, the failure happens **at the point of use** — in the task that actually calls System One — with a message naming the declaration and the CLI command. That is deliberate: a module's tasks are imported together on the dataplane, so an import-time raise would take down tasks that never touch System One, and a task that merely passes answers along needs no key at all.

## Declaring questions

The vocabulary documents itself. An enum's **class docstring** is the question and its **member docstrings** are the criteria, so a documented enum needs nothing at the call site:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/triage.py" fragment=vocabulary lang=python >}}

Group the questions into a dataclass. A `Noul` has no vocabulary to document itself with, so it always carries its own question — and, where a bare question would be ambiguous, its own criteria:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/triage.py" fragment=battery lang=python >}}

Override either the question or the criteria in ordinary `dataclasses.field` metadata, under two keys named after the SDK's own arguments:

| key | meaning |
|---|---|
| `question` | the instructions for this question |
| `criteria` | the same shape `typesafe_sdk` takes for that question type |

`criteria` follows the SDK exactly: a mapping keyed by enum **member name** for a `Choice`, a **positional** sequence of rungs for a `Score` (so the `IntEnum` must number its rungs `0..n-1` — a gap is rejected with an error that says so), and `{"true": ..., "false": ...}` for a `Noul`.

Member docstrings are not stored on the object at runtime, so they are read by parsing the source, the same way pydantic implements attribute docstrings. That makes them best-effort: where the source is not available (a REPL, `exec`, some frozen deployments) the criterion falls back to the member name rather than failing.

## Three ways to ask

`ask()` takes any of these and compiles them into a **single** `system_one` call:

```python
triage = await ask(Triage, state)                      # a battery dataclass -> Triage
intent = await ask(Choice[Intent], state)              # one question        -> Choice[Intent]
answers = await ask({"intent": Choice[Intent],         # an ad-hoc battery   -> dict
                     "hostile": Noul}, state)
```

Outside a dataclass there is no field to hang metadata on, so `Annotated` carries it instead — a mapping, or a bare string when all you have is the question:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/answer_types.py" fragment=standalone lang=python >}}

Both forms work on a dataclass field too. If a field has metadata *and* an `Annotated` annotation, the field metadata wins — it is the more specific place to say it.

**Prefer one call to several.** Three separate `ask()` calls are three round trips, while a battery or a mapping asks everything at once, which is the property the whole design rests on:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/answer_types.py" fragment=one-call lang=python >}}

Use `ask_with_info()` when you want the model name, question count, token usage and latency back alongside the answers:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/triage.py" fragment=triage-task lang=python >}}

The name collision with `typesafe_sdk`'s own `Choice` / `Score` / `Noul` is deliberate and one-directional: those describe the **question**, these hold the **answer**. You write the ones in this package; the plugin builds the SDK's from your battery.

## Branching on the answers

Thresholds live in your code, not in a prompt:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/triage.py" fragment=routing lang=python >}}

## Answers as task inputs and outputs

`Choice`, `Score` and `Noul` are plain dataclasses, so Flyte carries them with nothing registered — including on their own, not just inside a battery:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/answer_types.py" fragment=answer-as-output lang=python >}}

They also get the dict coercion every dataclass input gets, so a caller may pass `{"value": "refund", "confidence": 0.91}` where a `Choice[Intent]` is expected, and omitted fields fall back to their defaults. Note that an enum nested in a dataclass is spelled by its **value** (`"refund"`), not its name — that is mashumaro's convention for dataclass fields, and it differs from the name-based spelling Flyte uses for a bare enum at the top level.

Inference is never implicit. A dict arriving for a `Choice[Intent]` is the *serialized answer*, never a state to go ask about — the two are indistinguishable by shape, and replay depends on the serialized reading winning. If you want the interface to say "System One produces this", make it a task: you get durability, caching and retries, and the call stays visible in the run graph.

## Two kinds of parallelism

Flyte runs one durable task per item across the cluster; inside each task, System One answers the whole battery in a single request. The second one is why per-item latency barely moves when you add questions.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/typesafe-ai/fanout.py" fragment=fanout lang=python >}}

## A note on `IntEnum`

`Score` takes an `IntEnum` because a rubric is ordered. Flyte's enum transformer accepts `IntEnum` as well as string-valued enums, serialized by member name like every other enum, so a bare `severity: Severity` also works as a task input or output. `Flag` and `IntFlag` remain unsupported, with a message explaining why: a composite member like `READ|WRITE` has a name but cannot be looked up by it, so it cannot come back.

A parameterized dataclass such as `Choice[Intent]` is a generic *alias*, which `dataclasses.is_dataclass()` rejects. The type engine resolves the alias to its origin for structural checks while keeping the alias itself for decoding, which is what binds the type variable — so `Choice[Intent]` works as a task type directly.

## Next steps

- [System One datatypes](../../user-guide/system-one-datatypes/_index): the guard, composition and confidence-gating patterns, end to end.
- [Typed decisions for agentic pipelines](../../tutorials/agents/system-one-agents/_index): three pipelines built on this plugin, plus a measured A/B against a one-shot generative baseline.
- [Agent frameworks](../agents/_index): running a framework's own agent loop as durable Flyte tasks.
