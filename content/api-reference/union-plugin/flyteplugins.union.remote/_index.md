---
title: flyteplugins.union.remote
description: "Union remote control plane objects."
icon: box-seam
version: 0.14.0
variants: -flyte +union
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

    # Pod metrics of a run's task (root action, latest attempt) or of an app
    from flyteplugins.union.remote import Metrics

    for result in Metrics.get_for_action(run_name="my-run"):
        for series in result.series:
            print(result.name, series.labels, series.latest)

    Metrics.get_for_app(name="my-app", metrics=["app_requests"])
## Directory

### Classes

| Class | Description |
|-|-|
| [`ApiKey`](../flyteplugins.union.remote/apikey) | Represents a Union API Key (OAuth Application). |
| [`Assignment`](../flyteplugins.union.remote/assignment) | Represents role/policy assignments for an identity. |
| [`Cluster`](../flyteplugins.union.remote/cluster) | Represents a Union cluster. |
| [`ClusterConfig`](../flyteplugins.union.remote/clusterconfig) | The tracked ConfigMaps of a single cluster. |
| [`ClusterPool`](../flyteplugins.union.remote/clusterpool) | Represents a Union cluster pool — the configuration shared by its member clusters. |
| [`Environment`](../flyteplugins.union.remote/environment) | One environment version with its full spec, scaling and per-cluster status snapshots. |
| [`EnvironmentVersion`](../flyteplugins.union.remote/environmentversion) | One environment version as returned by the list call: its summary and per-cluster summaries. |
| [`Member`](../flyteplugins.union.remote/member) | Represents a Union organization member (user or application). |
| [`MetricResult`](../flyteplugins.union.remote/metricresult) | The result of querying one metric. |
| [`MetricSeries`](../flyteplugins.union.remote/metricseries) | One time series of a metric result, e.g. one container or one GPU device. |
| [`Metrics`](../flyteplugins.union.remote/metrics) | Pod metrics of a task's action attempt or of an app, as shown in the Union UI. |
| [`Policy`](../flyteplugins.union.remote/policy) | Represents a Union RBAC Policy. |
| [`Queue`](../flyteplugins.union.remote/queue) | Represents a Union scheduling queue. |
| [`Role`](../flyteplugins.union.remote/role) | Represents a Union RBAC Role. |
| [`SSHDebug`](../flyteplugins.union.remote/sshdebug) | Resolved SSH-into-task connect info for a running debug action. |
| [`SystemLogs`](../flyteplugins.union.remote/systemlogs) | Logs of the Union system components running on a cluster's dataplane. |
| [`User`](../flyteplugins.union.remote/user) | Represents a Union user. |
| [`VolumeExplore`](../flyteplugins.union.remote/volumeexplore) | A resolved `Volume` plus the IO to inspect and walk its lineage. |

### Errors

| Exception | Description |
|-|-|
| [`VolumeResolveError`](../flyteplugins.union.remote/volumeresolveerror) | No (or ambiguous) Volume-typed value could be resolved on an action. |

