---
title: Network
description: "Outbound network for a sandbox."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# Network

**Package:** `flyteplugins.union.sandbox`

Outbound network for a sandbox. Default: none (loopback only).

Enforced outside the sandbox, on every TCP and UDP flow: the microVM has no
network device, and its traffic leaves only through the node's agent.
Private ranges (the cluster's pods, services and nodes) are refused unless
``allow_cidrs`` names them; link-local addresses (the cloud metadata
server) and loopback are always refused. TLS is end to end.


## Parameters

```python
class Network(
    open: bool = False,
    allow_domains: Tuple[str, ...] = (),
    allow_cidrs: Tuple[str, ...] = (),
)
```
| Parameter | Type | Description |
|-|-|-|
| `open` | `bool` | |
| `allow_domains` | `Tuple[str, ...]` | |
| `allow_cidrs` | `Tuple[str, ...]` | |

## Methods

| Method | Description |
|-|-|
| [`allow()`](#allow) | Outbound only to ``domains`` and ``cidrs``. |
| [`blocked()`](#blocked) | No outbound network: the default. |
| [`internet()`](#internet) | All outbound traffic, except the ranges above. |
| [`pypi()`](#pypi) | Only PyPI, for ``pip install``. |


### allow()

```python
def allow(
    *domains: str,
    cidrs: Tuple[str, ...] = (),
) -> Network
```
Outbound only to ``domains`` and ``cidrs``.


| Parameter | Type | Description |
|-|-|-|
| `*domains` | `str` | |
| `cidrs` | `Tuple[str, ...]` | |

### blocked()

```python
def blocked()
```
No outbound network: the default.


### internet()

```python
def internet()
```
All outbound traffic, except the ranges above.


### pypi()

```python
def pypi()
```
Only PyPI, for ``pip install``.


