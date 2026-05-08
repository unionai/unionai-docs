---
title: Settings
version: 2.2.2
variants: +flyte +union
layout: py_api
---

# Settings

**Package:** `flyte.remote`

Hierarchical configuration settings with inheritance support.

This class manages settings across ORG, DOMAIN, and PROJECT scopes,
supporting local overrides and inheritance from parent scopes.


## Parameters

```python
class Settings(
    effective_settings: list[EffectiveSetting],
    local_settings: list[LocalSetting],
    domain: str | None,
    project: str | None,
    _version: int,
    _parent_effective: dict[str, EffectiveSetting],
    _map_entry_origins: dict[str, dict[str, EffectiveSetting]],
    _list_item_origins: dict[str, list[EffectiveSetting]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `effective_settings` | `list[EffectiveSetting]` | |
| `local_settings` | `list[LocalSetting]` | |
| `domain` | `str \| None` | |
| `project` | `str \| None` | |
| `_version` | `int` | |
| `_parent_effective` | `dict[str, EffectiveSetting]` | |
| `_map_entry_origins` | `dict[str, dict[str, EffectiveSetting]]` | |
| `_list_item_origins` | `dict[str, list[EffectiveSetting]]` | |

## Methods

| Method | Description |
|-|-|
| [`available_keys()`](#available_keys) | Return every dot-notation key that can be set on a Settings scope. |
| [`effective_values()`](#effective_values) | Return resolved effective settings as a flat dict for programmatic use. |
| [`get_settings_for_edit()`](#get_settings_for_edit) | Retrieve settings at the requested scope along with parent scopes. |
| [`local_overrides()`](#local_overrides) | Return local overrides as a flat dict for programmatic use. |
| [`parse_yaml()`](#parse_yaml) | Parse YAML content into a dict of overrides. |
| [`scope_description()`](#scope_description) | Human-readable label for the scope this Settings object was fetched for. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`to_yaml()`](#to_yaml) | Generate YAML representation of this scope. |
| [`to_yaml_sections()`](#to_yaml_sections) | Return the YAML content split into labelled sections. |
| [`update_settings()`](#update_settings) | Replace the complete set of local overrides for this scope. |


### available_keys()

```python
def available_keys()
```
Return every dot-notation key that can be set on a Settings scope.


### effective_values()

```python
def effective_values()
```
Return resolved effective settings as a flat dict for programmatic use.


### get_settings_for_edit()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Settings.get_settings_for_edit.aio()`.
```python
def get_settings_for_edit(
    cls,
    project: str | None,
    domain: str | None,
) -> Settings
```
Retrieve settings at the requested scope along with parent scopes.

Returns a Settings object containing both the effective (resolved) settings
with inheritance, and the local overrides at the requested scope.

The scope is determined by ``domain`` and ``project``:

- no args → ORG scope.
- ``domain`` only → DOMAIN scope.
- ``domain`` + ``project`` → PROJECT scope, inherits from DOMAIN.

These are explicit parameters — they are **not** inferred from
``flyte.init()``.

:returns: Settings object with effective_settings, local_settings, and version.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `project` | `str \| None` | Project name. Requires ``domain`` to also be set. |
| `domain` | `str \| None` | Domain name. |

### local_overrides()

```python
def local_overrides()
```
Return local overrides as a flat dict for programmatic use.


### parse_yaml()

```python
def parse_yaml(
    yaml_content: str,
) -> dict[str, Any]
```
Parse YAML content into a dict of overrides.

Uses ``yaml.safe_load``, so all YAML syntax is supported — including
flow collections (``[a, b]``, ``{k: v}``) and block collections — for
the list and map leaves (``labels``, ``annotations``,
``environment_variables``). Commented lines are ignored (template
entries stay as comments until the user uncomments them).


| Parameter | Type | Description |
|-|-|-|
| `yaml_content` | `str` | |

### scope_description()

```python
def scope_description()
```
Human-readable label for the scope this Settings object was fetched for.


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

### to_yaml()

```python
def to_yaml()
```
Generate YAML representation of this scope.

Three comment prefixes form a visibility hierarchy for both human
readers and line-based stylers:

* ``###`` — section headers (scope header, section titles). Prominent.
* ``##`` — descriptions and metadata (per-field docs, inline origin
  annotations). Dim.
* ``#`` — a commented-out setting. Uncomment (strip a single leading
  ``#``) to activate.

A bulk ``# `` → `` pass safely activates every setting while leaving
descriptions (``##`` → ``#``) and section headers (``###`` → ``##``)
intact as comments.

Output has up to three sections:

* **Local overrides** — already applied at this scope.
* **Inherited settings** — resolved from a parent scope; uncomment to
  override here.
* **Available settings** — every key not yet set anywhere, with
  illustrative placeholders; uncomment and edit to set it here.


### to_yaml_sections()

```python
def to_yaml_sections()
```
Return the YAML content split into labelled sections.

Each tuple is ``(section_title, yaml_body)``; sections are omitted
when they have no entries. See :meth:`to_yaml` for the comment-prefix
convention.

Section titles: ``"Local overrides"``, ``"Inherited settings"``, ``"Available settings"``.


### update_settings()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Settings instance>.update_settings.aio()`.
```python
def update_settings(
    overrides: dict[str, Any],
)
```
Replace the complete set of local overrides for this scope.

Uses the scope (``domain`` / ``project``) this object was retrieved for.
Settings not included in ``overrides`` will inherit from the parent scope.

Uses optimistic locking via the version obtained from
``get_settings_for_edit``.



| Parameter | Type | Description |
|-|-|-|
| `overrides` | `dict[str, Any]` | Dict of flat dot-notation keys to values. Example: ``{"run.default_queue": "gpu", "security.service_account": "my-sa"}`` |

