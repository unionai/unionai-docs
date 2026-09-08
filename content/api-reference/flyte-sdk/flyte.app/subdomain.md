---
title: Subdomain
description: "A subdomain that is resolved at deploy time, when the deployment project and domain are known."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# Subdomain

**Package:** `flyte.app`

A subdomain that is resolved at deploy time, when the deployment project and domain are known.

Use `Subdomain.from_app_name` for the built-in naming schemes:

- `project_domain_suffix="hash"`: the subdomain is `{app_name}-{hash}`, where the hash is computed
  from `{project}-{domain}`. This keeps subdomains short and stable per project/domain.
- `project_domain_suffix="default"`: the subdomain is `{app_name}-{project}-{domain}`.

Use `Subdomain.from_function` for full control: the function receives the `AppEnvironment` and the
deployment `SerializationContext` (project, domain, org, version, ...) and returns the subdomain.

The final subdomain string is produced by `resolve()` during serialization.


## Parameters

```python
class Subdomain(
    app_name: typing.Optional[str] = None,
    project_domain_suffix: typing.Literal['hash', 'default'] = 'hash',
    function: typing.Optional[typing.Callable[[ForwardRef('AppEnvironment'), ForwardRef('SerializationContext')], str]] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `app_name` | `typing.Optional[str]` | |
| `project_domain_suffix` | `typing.Literal['hash', 'default']` | |
| `function` | `typing.Optional[typing.Callable[[ForwardRef('AppEnvironment'), ForwardRef('SerializationContext')], str]]` | |

## Methods

| Method | Description |
|-|-|
| [`from_app_name()`](#from_app_name) | Create a subdomain for an app whose final value depends on the deployment project and domain. |
| [`from_function()`](#from_function) | Create a subdomain computed by a user-provided function at deploy time. |
| [`resolve()`](#resolve) | Resolve to the final subdomain string for the given app environment and deployment context. |


### from_app_name()

```python
def from_app_name(
    app_name: str,
    project_domain_suffix: typing.Literal['hash', 'default'] = 'hash',
) -> Subdomain
```
Create a subdomain for an app whose final value depends on the deployment project and domain.



| Parameter | Type | Description |
|-|-|-|
| `app_name` | `str` | Name of the app. |
| `project_domain_suffix` | `typing.Literal['hash', 'default']` | `"hash"` for `{app_name}-{hash-of-project-domain}`, or `"default"` for `{app_name}-{project}-{domain}`. |

### from_function()

```python
def from_function(
    function: typing.Callable[[ForwardRef('AppEnvironment'), ForwardRef('SerializationContext')], str],
) -> Subdomain
```
Create a subdomain computed by a user-provided function at deploy time.



| Parameter | Type | Description |
|-|-|-|
| `function` | `typing.Callable[[ForwardRef('AppEnvironment'), ForwardRef('SerializationContext')], str]` | Called with the `AppEnvironment` being deployed and the deployment `SerializationContext`; returns the subdomain string. |

### resolve()

```python
def resolve(
    app_env: AppEnvironment,
    serialization_context: SerializationContext,
) -> str
```
Resolve to the final subdomain string for the given app environment and deployment context.


| Parameter | Type | Description |
|-|-|-|
| `app_env` | `AppEnvironment` | |
| `serialization_context` | `SerializationContext` | |

