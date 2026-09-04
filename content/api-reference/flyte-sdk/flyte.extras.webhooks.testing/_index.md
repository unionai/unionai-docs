---
title: flyte.extras.webhooks.testing
description: "Conformance harness — enforce the common provider format."
icon: box-seam
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# flyte.extras.webhooks.testing

Conformance harness — enforce the common provider format.

Every `flyteplugins.webhooks.<product>` plugin ships a one-line test:

```python
from flyte.extras.webhooks.testing import assert_provider_conforms
import flyteplugins.github as plugin


def test_conformance():
    assert_provider_conforms(plugin)
```

CI then fails if a plugin drifts from the shared format. The checks are the ones
that actually bit the per-product plugins this family replaces: verification
that raises instead of returning False, event constants that render as enum
names, dedupe keys that collapse distinct events onto one key.
## Directory

### Protocols

| Protocol | Description |
|-|-|
| [`ProviderFactory`](../flyte.extras.webhooks.testing/providerfactory) | What a plugin's exported provider class must look like. |

### Methods

| Method | Description |
|-|-|
| [`assert_provider_conforms()`](#assert_provider_conforms) | Assert that a provider plugin implements the common webhook contract. |


## Methods

#### assert_provider_conforms()

```python
def assert_provider_conforms(
    plugin: typing.Any,
)
```
Assert that a provider plugin implements the common webhook contract.

The contract:

1. exports exactly one `Provider` subclass, constructible with no arguments
   and whose `name` matches the plugin's module name, so `/webhook/<name>`
   routes to it and `providers=[SomethingProvider()]` is all a user writes;
2. exports an `events` module whose `__all__` names `EventType` subclasses,
   every member of which is a `str` that renders as its wire value;
3. exports `SAMPLE_DELIVERY`, a `(headers, body)` pair of a real payload,
   which must verify under a known secret, reject the wrong secret, survive
   hostile headers without raising, parse into a `WebhookEvent` carrying
   this provider's name, and dedupe stably.

Providers with `signed=True` must additionally reject a tampered body, since
a signature covers it. A shared token does not, so `signed=False` opts out of
that one check — and makes the dashboard say the product does not sign.

`SAMPLE_DELIVERY` is what makes the rest checkable: without a real payload
there is no way to assert that `parse` and `verify` actually agree with the
product, and every check here would be vacuous.

Raises `AssertionError` with a specific message on any deviation.


| Parameter | Type | Description |
|-|-|-|
| `plugin` | `typing.Any` | |

