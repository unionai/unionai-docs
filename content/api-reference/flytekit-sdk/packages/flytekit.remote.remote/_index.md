---
title: flytekit.remote.remote
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.remote


This module provides the ``FlyteRemote`` object, which is the end-user's main starting point for interacting
with a Flyte backend in an interactive and programmatic way. This of this experience as kind of like the web UI
but in Python object form.

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteRemote`](../flytekit.remote.remote/flyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`ResolvedIdentifiers`](../flytekit.remote.remote/resolvedidentifiers) |  |

### Errors

| Exception | Description |
|-|-|
| [`RegistrationSkipped`](../flytekit.remote.remote/registrationskipped) | RegistrationSkipped error is raised when trying to register an entity that is not registrable. |

### Variables

| Property | Type | Description |
|-|-|-|
| `LATEST_VERSION_STR` | `str` |  |
| `PICKLE_FILE_PATH` | `str` |  |

