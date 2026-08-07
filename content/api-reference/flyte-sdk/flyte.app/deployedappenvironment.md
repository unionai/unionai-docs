---
title: DeployedAppEnvironment
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# DeployedAppEnvironment

**Package:** `flyte.app`

## Parameters

```python
class DeployedAppEnvironment(
    env: AppEnvironment,
    deployed_app: 'App',
)
```
| Parameter | Type | Description |
|-|-|-|
| `env` | `AppEnvironment` | |
| `deployed_app` | `'App'` | |

## Methods

| Method | Description |
|-|-|
| [`env_repr()`](#env_repr) |  |
| [`get_name()`](#get_name) | Returns the name of the deployed environment. |
| [`summary_repr()`](#summary_repr) |  |
| [`table_repr()`](#table_repr) |  |


### env_repr()

```python
def env_repr()
```
### get_name()

```python
def get_name()
```
Returns the name of the deployed environment.


### summary_repr()

```python
def summary_repr()
```
### table_repr()

```python
def table_repr()
```
