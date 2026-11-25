---
title: Org
description: "A Union organization, with the limits and entitlements it runs with."
icon: braces
version: 0.26.2
variants: -flyte +union
layout: py_api
---

# Org

**Package:** `flyteplugins.union.remote`

A Union organization, with the limits and entitlements it runs with.



## Parameters

```python
class Org(
    pb2: org_definition_pb2.Org,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `org_definition_pb2.Org` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `enterprise_triggers` | `list[str]` | What would move this org to Enterprise, e.g. ``["clusters", "private_networking"]``. |
| `entitlements` | `org_definition_pb2.Entitlements` | The effective entitlements: each per-org override, else the tier default. |
| `limits` | `org_definition_pb2.Limits` | The effective limits: each per-org override, else the tier default. 0 means unlimited. |
| `name` | `str` |  |
| `plan_tier` | `str` | The org's billing plan, e.g. ``"v2_team"`` or ``"v2_enterprise"``; ``"unknown"`` when unset.  Only Teams and Enterprise plans have tier defaults; for the others ``tier_defaults_version`` is empty. |
| `tier_default_entitlements` | `org_definition_pb2.Entitlements \| None` | The tier-default entitlements for the org's plan, or None when the plan has none. |
| `tier_default_limits` | `org_definition_pb2.Limits \| None` | The tier defaults for the org's plan, or None when the plan has none. |
| `tier_defaults_version` | `str` | The tier-defaults version the effective values were resolved against; empty without tier defaults. |

## Methods

| Method | Description |
|-|-|
| [`entitlement_rows()`](#entitlement_rows) | Every entitlement, in field-number order, skipping deprecated fields. |
| [`get()`](#get) | Get an org with its effective limits and entitlements. |
| [`limit_rows()`](#limit_rows) | Every limit, in field-number order, skipping deprecated fields. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### entitlement_rows()

```python
def entitlement_rows()
```
Every entitlement, in field-number order, skipping deprecated fields.


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Org.get.aio()`.
```python
def get(
    cls,
    name: str | None = None,
) -> Org
```
Get an org with its effective limits and entitlements.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str \| None` | The org to get. Defaults to the org in the flyte.init config. Reading another org needs a Union-managed identity. |

### limit_rows()

```python
def limit_rows()
```
Every limit, in field-number order, skipping deprecated fields.

Iterates the Limits descriptor, so a limit the server adds shows up once the
stubs are regenerated, with no change here.


### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

