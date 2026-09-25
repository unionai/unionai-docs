---
title: Union plugin
description: "Union SDK - Proprietary extensions for Flyte."
icon: book
version: 0.13.0
variants: -flyte +union
layout: py_api
weight: 5
---

# Union plugin



## Directory

### Classes

| Class | Description |
|-|-|
| [`flyteplugins.union.factory.Factory`](flyteplugins.union.factory/factory) | A set of builds. |
| [`flyteplugins.union.factory.TimeRange`](flyteplugins.union.factory/timerange) | A trailing window, relative to the consumer's own time value, ending at that value. |
| [`flyteplugins.union.io.ActionRef`](flyteplugins.union.io/actionref) | Provenance: the action (one task execution within a run) that produced a particular `Volume` version, plus the output slot it was returned as. |
| [`flyteplugins.union.io.ROVolume`](flyteplugins.union.io/rovolume) | Immutable, versioned volume — PRD §Core Concepts. |
| [`flyteplugins.union.io.RWVolume`](flyteplugins.union.io/rwvolume) | Mutable working copy — PRD §Core Concepts. |
| [`flyteplugins.union.io.Volume`](flyteplugins.union.io/volume) | A persistent volume identified by its metadata index. |
| [`flyteplugins.union.remote.ApiKey`](flyteplugins.union.remote/apikey) | Represents a Union API Key (OAuth Application). |
| [`flyteplugins.union.remote.Assignment`](flyteplugins.union.remote/assignment) | Represents role/policy assignments for an identity. |
| [`flyteplugins.union.remote.Cluster`](flyteplugins.union.remote/cluster) | Represents a Union cluster. |
| [`flyteplugins.union.remote.ClusterConfig`](flyteplugins.union.remote/clusterconfig) | The tracked ConfigMaps of a single cluster. |
| [`flyteplugins.union.remote.ClusterPool`](flyteplugins.union.remote/clusterpool) | Represents a Union cluster pool — the configuration shared by its member clusters. |
| [`flyteplugins.union.remote.Environment`](flyteplugins.union.remote/environment) | One environment version with its full spec, scaling and per-cluster status snapshots. |
| [`flyteplugins.union.remote.EnvironmentVersion`](flyteplugins.union.remote/environmentversion) | One environment version as returned by the list call: its summary and per-cluster summaries. |
| [`flyteplugins.union.remote.Member`](flyteplugins.union.remote/member) | Represents a Union organization member (user or application). |
| [`flyteplugins.union.remote.MetricResult`](flyteplugins.union.remote/metricresult) | The result of querying one metric. |
| [`flyteplugins.union.remote.MetricSeries`](flyteplugins.union.remote/metricseries) | One time series of a metric result, e.g. one container or one GPU device. |
| [`flyteplugins.union.remote.Metrics`](flyteplugins.union.remote/metrics) | Pod metrics of a task's action attempt or of an app, as shown in the Union UI. |
| [`flyteplugins.union.remote.Policy`](flyteplugins.union.remote/policy) | Represents a Union RBAC Policy. |
| [`flyteplugins.union.remote.Queue`](flyteplugins.union.remote/queue) | Represents a Union scheduling queue. |
| [`flyteplugins.union.remote.Role`](flyteplugins.union.remote/role) | Represents a Union RBAC Role. |
| [`flyteplugins.union.remote.SSHDebug`](flyteplugins.union.remote/sshdebug) | Resolved SSH-into-task connect info for a running debug action. |
| [`flyteplugins.union.remote.SystemLogs`](flyteplugins.union.remote/systemlogs) | Logs of the Union system components running on a cluster's dataplane. |
| [`flyteplugins.union.remote.User`](flyteplugins.union.remote/user) | Represents a Union user. |
| [`flyteplugins.union.remote.VolumeExplore`](flyteplugins.union.remote/volumeexplore) | A resolved `Volume` plus the IO to inspect and walk its lineage. |
| [`flyteplugins.union.remote.VolumeResolveError`](flyteplugins.union.remote/volumeresolveerror) | No (or ambiguous) Volume-typed value could be resolved on an action. |

### Functions

| Function | Description |
|-|-|
| [`flyteplugins.union.debug()`](flyteplugins.union/_index#debug) | Launch a task, or relaunch an existing run, with ssh-into-task debug enabled. |
| [`flyteplugins.union.fork()`](flyteplugins.union/_index#fork) | Fork run *run_name*, replaying it with new code and/or inputs. |
| [`flyteplugins.union.with_debugcontext()`](flyteplugins.union/_index#with_debugcontext) | Like `flyte.with_runcontext`, but preconfigured for ssh-into-task debug. |
| [`flyteplugins.union.with_forkcontext()`](flyteplugins.union/_index#with_forkcontext) | Like `flyte.with_runcontext`, but the returned runner can also `fork(run_name, ...)`. |
| [`flyteplugins.union.factory.build()`](flyteplugins.union.factory/_index#build) | Name the artifact (or artifacts) one task call makes. |
| [`flyteplugins.union.factory.materialize()`](flyteplugins.union.factory/_index#materialize) | Start a run of ``<factory>.materialize`` and return the ``flyte.remote.Run``. |
| [`flyteplugins.union.factory.partition()`](flyteplugins.union.factory/_index#partition) | Pass the instance's value of ``dim`` to a task parameter. |
| [`flyteplugins.union.factory.source()`](flyteplugins.union.factory/_index#source) | An artifact made outside this factory. |
| [`flyteplugins.union.io.allow_volumes()`](flyteplugins.union.io/_index#allow_volumes) | Enable `Volume` mounts in a task pod with **zero privileges**. |
| [`flyteplugins.union.io.with_high_throughput_volume_deps()`](flyteplugins.union.io/_index#with_high_throughput_volume_deps) | Prepare ``base`` for high-throughput (Redis-backed) Volumes. |
| [`flyteplugins.union.io.with_local_flyteplugins()`](flyteplugins.union.io/_index#with_local_flyteplugins) | Package the **locally checked-out** flyteplugins-union (built to a wheel) and an optional local ``juicefs`` binary into ``base`` — for iterating on an *unreleased* plugin build against a real cluster. |
| [`flyteplugins.union.utils.with_local_flyteplugins_union()`](flyteplugins.union.utils/_index#with_local_flyteplugins_union) | Layer the locally-built ``flyteplugins-union`` wheel onto ``img``. |

### Packages

| Package | Description |
|-|-|
| [`flyteplugins.union`](flyteplugins.union/_index) | Union SDK - Proprietary extensions for Flyte. |
| [`flyteplugins.union.factory`](flyteplugins.union.factory/_index) | Factories: a declared graph of partitioned artifacts the platform can materialize on demand. |
| [`flyteplugins.union.io`](flyteplugins.union.io/_index) | Persistent, mountable :class:`Volume` type for the Flyte SDK v2. |
| [`flyteplugins.union.remote`](flyteplugins.union.remote/_index) | Union remote control plane objects. |
| [`flyteplugins.union.utils`](flyteplugins.union.utils/_index) | Public utilities for ``flyteplugins.union``. |

