---
title: flytekit.tools.ignore
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.ignore

## Directory

### Classes

| Class | Description |
|-|-|
| [`DockerIgnore`](../flytekit.tools.ignore/dockerignore) | Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`FlyteIgnore`](../flytekit.tools.ignore/flyteignore) | Uses a. |
| [`GitIgnore`](../flytekit.tools.ignore/gitignore) | Uses git cli (if available) to list all ignored files and compare with those. |
| [`Ignore`](../flytekit.tools.ignore/ignore) | Base for Ignores, implements core logic. |
| [`IgnoreGroup`](../flytekit.tools.ignore/ignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`StandardIgnore`](../flytekit.tools.ignore/standardignore) | Retains the standard ignore functionality that previously existed. |

### Variables

| Property | Type | Description |
|-|-|-|
| `STANDARD_IGNORE_PATTERNS` | `list` |  |

