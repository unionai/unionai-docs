---
title: flyteplugins.union.remote
version: 0.1.1
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.union.remote

Union remote control plane objects.

This module provides remote object classes for Union-specific control plane
entities, following the same pattern as flyte.remote objects.

Example:
    from flyteplugins.union.remote import ApiKey

    # List all API keys
    keys = ApiKey.listall()
    for key in keys:
        print(key.client_id)

    # Create a new API key
    api_key = ApiKey.create(name="my-ci-key")
    print(api_key.client_secret)

    # Get a specific API key
    key = ApiKey.get(client_id="my-client-id")

    # Delete an API key
    ApiKey.delete(client_id="my-client-id")

## Directory

### Classes

| Class | Description |
|-|-|
| [`ApiKey`](../flyteplugins.union.remote/apikey) | Represents a Union API Key (OAuth Application). |

