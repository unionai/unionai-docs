---
title: ConnectPhase
description: "What ``env.connect`` is doing now, for a caller that shows its progress (``on_phase=``)."
icon: braces
version: 0.26.2
variants: -flyte +union
layout: py_api
---

# ConnectPhase

**Package:** `flyteplugins.union.sandbox`

What ``env.connect`` is doing now, for a caller that shows its progress
(``on_phase=``). It is told each change, never printed here.

``step`` is one of:

- ``finding``: looking the sandbox up, creating it if there is none;
- ``waiting``: it is pending, as ``state``/``phase`` say (``placed``
  tells a run no node has started yet from one starting on a node);
- ``restoring``: its run had ended, and it is being started again, as
  run ``generation``, from what its last run kept;
- ``connecting``: it is ready, and is being resumed if suspended, and
  checked it answers;
- ``resumed``: it was suspended, and has been resumed;
- ``ending``: it is suspended past its keep, and is waited for to end, to
  start it again;
- ``retrying``: it did not answer (``message`` says how), and is tried again;
- ``deleted``: this connect created it, and deleted it, unused (``message``
  says why); ``delete_failed``: it tried to, and could not.


## Parameters

```python
class ConnectPhase(
    step: str,
    sandbox: str,
    state: str = '',
    phase: str = '',
    generation: int = 0,
    queue: Optional[str] = None,
    message: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `step` | `str` | |
| `sandbox` | `str` | |
| `state` | `str` | |
| `phase` | `str` | |
| `generation` | `int` | |
| `queue` | `Optional[str]` | |
| `message` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `placed` | `bool` | Whether a node has started its run (it may still be booting). |

