---
title: TypeSafe AI
description: "Run TypeSafe's System One model (Jev) inside durable Flyte tasks."
icon: book
version: 2.9.0
variants: +flyte +union
layout: py_api
---

# TypeSafe AI



Run TypeSafe's System One model (Jev) inside durable Flyte tasks.

Jev answers typed questions in parallel instead of generating text, and returns
calibrated confidence with every answer. This plugin gives those answers a shape
that crosses a Flyte task boundary — `Choice`, `Score` and `Noul` — and a way to
ask a whole battery of them in a single request.

```python
import enum
from dataclasses import dataclass, field

import flyte
from flyteplugins.typesafe_ai import Choice, Noul, Score, ask

env = flyte.TaskEnvironment(
    "triage",
    secrets=[flyte.Secret(key="TYPESAFE_API_KEY", as_env_var="TYPESAFE_API_KEY")],
)


class Intent(enum.Enum):
    '''Which intent best fits the ticket?'''

    REFUND = "refund"
    '''they want money back'''
    DELIVERY = "delivery"
    '''they are asking where their order is'''


class Severity(enum.IntEnum):
    '''How badly is this customer affected?'''

    NONE = 0
    '''no impact; a question or a comment'''
    MINOR = 1
    '''inconvenient, but they can carry on'''
    SERIOUS = 2
    '''they are blocked'''


@dataclass
class Triage:
    # The enums above document themselves, so these fields need no metadata at all.
    intent: Choice[Intent]
    severity: Score[Severity]
    # A Noul has no vocabulary to document itself with, so it needs both.
    hostile: Noul = field(
        metadata={"question": "Is the customer hostile?", "criteria": {"true": "insults or threats", "false": "civil"}}
    )


@env.task
async def triage(ticket: str) -> Triage:
    return await ask(Triage, {"ticket": ticket})
```
## Directory

### Classes

| Class | Description |
|-|-|
| [`CallInfo`](./callinfo) | What one `system_one` call cost, for the report and for cost accounting. |
| [`Choice`](./choice) | One pick from a fixed vocabulary, carrying the calibration it came with. |
| [`Noul`](./noul) | Truthfulness in 0..1. |
| [`Score`](./score) | A position on a rubric. |

### Errors

| Exception | Description |
|-|-|
| [`BatteryError`](./batteryerror) | The questions cannot be compiled. |
| [`MissingAPIKey`](./missingapikey) | Raised at the point of use, in the task that actually needs the key. |

### Methods

| Method | Description |
|-|-|
| [`ask()`](#ask) | Answer a battery, a single question, or a mapping of them -- in one call. |
| [`ask_with_info()`](#ask_with_info) | Answer everything in one call, and report what the call cost. |
| [`client()`](#client) | An `AsyncTypeSafeClient`, or a message that says exactly what to do. |
| [`compile_questions()`](#compile_questions) | Build the SDK's question objects from any accepted form. |


### Variables

| Property | Type | Description |
|-|-|-|
| `API_KEY_ENV` | `str` |  |
| `CRITERIA_KEY` | `str` |  |
| `QUESTION_KEY` | `str` |  |

## Methods

#### ask()

```python
def ask(
    askable: Askable,
    state: Any,
    model: Optional[str] = None,
    client: Any = None,
) -> Any
```
Answer a battery, a single question, or a mapping of them -- in one call.

```python
triage = await ask(Triage, {"ticket": text})                  # -> Triage
intent = await ask(Choice[Intent], {"ticket": text})          # -> Choice[Intent]
both = await ask({"intent": Choice[Intent], "hot": Noul}, s)  # -> dict
```


| Parameter | Type | Description |
|-|-|-|
| `askable` | `Askable` | |
| `state` | `Any` | |
| `model` | `Optional[str]` | |
| `client` | `Any` | |

#### ask_with_info()

```python
def ask_with_info(
    askable: Askable,
    state: Any,
    model: Optional[str] = None,
    client: Any = None,
) -> Tuple[Any, CallInfo]
```
Answer everything in one call, and report what the call cost.


| Parameter | Type | Description |
|-|-|-|
| `askable` | `Askable` | |
| `state` | `Any` | |
| `model` | `Optional[str]` | |
| `client` | `Any` | |

#### client()

```python
def client(
    api_key: Optional[str] = None,
    model: Optional[str] = None,
    **kwargs: Any,
)
```
An `AsyncTypeSafeClient`, or a message that says exactly what to do.

Without this, a missing key surfaces as a 401 from inside the vendor SDK, which
tells you nothing about Flyte secrets.


| Parameter | Type | Description |
|-|-|-|
| `api_key` | `Optional[str]` | |
| `model` | `Optional[str]` | |
| `**kwargs` | `Any` | |

#### compile_questions()

```python
def compile_questions(
    askable: Askable,
) -> Dict[str, Any]
```
Build the SDK's question objects from any accepted form.


| Parameter | Type | Description |
|-|-|-|
| `askable` | `Askable` | |

