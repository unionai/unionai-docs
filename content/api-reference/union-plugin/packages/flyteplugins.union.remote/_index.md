---
title: flyteplugins.union.remote
version: 0.4.3
variants: +flyte +union
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
| [`Assignment`](../flyteplugins.union.remote/assignment) | Represents role/policy assignments for an identity. |
| [`Cluster`](../flyteplugins.union.remote/cluster) | Represents a Union cluster. |
| [`ClusterPool`](../flyteplugins.union.remote/clusterpool) | Represents a Union cluster pool — the configuration shared by its member clusters. |
| [`Member`](../flyteplugins.union.remote/member) | Represents a Union organization member (user or application). |
| [`Policy`](../flyteplugins.union.remote/policy) | Represents a Union RBAC Policy. |
| [`Queue`](../flyteplugins.union.remote/queue) | Represents a Union scheduling queue. |
| [`Role`](../flyteplugins.union.remote/role) | Represents a Union RBAC Role. |
| [`SSHDebug`](../flyteplugins.union.remote/sshdebug) | Resolved SSH-into-task connect info for a running debug action. |
| [`User`](../flyteplugins.union.remote/user) | Represents a Union user. |
| [`VolumeExplore`](../flyteplugins.union.remote/volumeexplore) | A resolved :class:`Volume` plus the IO to inspect and walk its lineage. |

### Errors

| Exception | Description |
|-|-|
| [`VolumeResolveError`](../flyteplugins.union.remote/volumeresolveerror) | No (or ambiguous) Volume-typed value could be resolved on an action. |

