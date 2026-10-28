---
title: CallCounter
description: "Numbers identical sub-action calls made from one action scope: `foo(); foo(); foo()` → 1, 2, 3."
icon: braces
version: 2.12.1
variants: +flyte +union
layout: py_api
---

# CallCounter

**Package:** `flyte.models`

Numbers identical sub-action calls made from one action scope: `foo(); foo(); foo()` → 1, 2, 3.

The sequence disambiguates identical calls in a deterministic sub-action name. A TaskContext owns
one, and the TaskContext is built fresh for every action attempt, so numbering always starts from
zero — even in a reusable container where one controller outlives many actions and retries.
Controllers are the only callers.


## Parameters

```python
def CallCounter()
```
## Methods

| Method | Description |
|-|-|
| [`next()`](#next) | Return the next sequence number for *call_key*, starting at 1. |


### next()

```python
def next(
    call_key: str,
) -> int
```
Return the next sequence number for *call_key*, starting at 1.

`call_key` should combine the task identity, the inputs hash, and the group (every component that
is folded into the action name) so that concurrent calls producing different names never share a
count — sequence assignment (and therefore action names) then stays independent of event-loop
scheduling order. Calls that do share a count are byte-identical, same-group, and interchangeable.


| Parameter | Type | Description |
|-|-|-|
| `call_key` | `str` | |

