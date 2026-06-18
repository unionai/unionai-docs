---
title: ActionRef
version: 0.4.2
variants: +flyte +union
layout: py_api
---

# ActionRef

**Package:** `flyteplugins.union.io`

Provenance: the action (one task execution within a run) that
produced a particular :class:`Volume` version, plus the output slot it
was returned as.

Stamped at reseal time (commit / fork / finalize) onto ``produced_by``,
and carried onto the next version's ``parent_produced_by`` so lineage
is navigable. Mirrors the fields of :class:`flyte.models.ActionID` so the
explore TUI / lineage tooling can attribute each version to the run and
action that created it, and jump to that action's logs.

``locator`` is the object-store path of *this* version's published
metadata object (see :func:`_publish_metadata`). It's what makes lineage
walkable offline and at full fidelity: every published version — including
intra-action intermediates that were never task outputs — is addressable,
so ``parent_produced_by.locator`` loads the parent's complete Volume value,
whose own ``parent_produced_by.locator`` continues the chain.

``output_name`` (e.g. ``"o0"``) is the task output the value was returned
as. Only the value actually returned from a task has one (filled in by the
type transformer); intermediates leave it ``None``. It deep-links to a
specific output in the action UI — complementary to ``locator``.


## Parameters

```python
class ActionRef(
    name: str,
    run_name: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    org: typing.Optional[str],
    output_name: typing.Optional[str],
    locator: typing.Optional[str],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `run_name` | `typing.Optional[str]` | |
| `project` | `typing.Optional[str]` | |
| `domain` | `typing.Optional[str]` | |
| `org` | `typing.Optional[str]` | |
| `output_name` | `typing.Optional[str]` | |
| `locator` | `typing.Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`from_action_id()`](#from_action_id) | Build an :class:`ActionRef` from a :class:`flyte. |


### from_action_id()

```python
def from_action_id(
    action: Any,
    output_name: Optional[str],
    locator: Optional[str],
) -> 'ActionRef'
```
Build an :class:`ActionRef` from a :class:`flyte.models.ActionID`.


| Parameter | Type | Description |
|-|-|-|
| `action` | `Any` | |
| `output_name` | `Optional[str]` | |
| `locator` | `Optional[str]` | |

