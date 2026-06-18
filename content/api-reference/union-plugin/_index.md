---
title: Union plugin
version: 0.4.2
variants: +flyte +union
layout: py_api
weight: 5
---

# Union plugin



## Directory

### Classes

| Class | Description |
|-|-|
| [`flyteplugins.union.errors.VolumeCommandError`](classes) | A backend CLI invocation (e. |
| [`flyteplugins.union.errors.VolumeCommitError`](classes) | A keep-alive checkpoint could not be made durable: the writeback staging. |
| [`flyteplugins.union.errors.VolumeError`](classes) | Base for Volume *system* failures — infra/runtime problems the caller. |
| [`flyteplugins.union.errors.VolumeMigrateNoop`](classes) | Metadata-store migration was requested to the store type already in use. |
| [`flyteplugins.union.errors.VolumeMountError`](classes) | The volume could not be mounted — the client exited prematurely, the. |
| [`flyteplugins.union.errors.VolumeMountTimeout`](classes) | The mount did not become a FUSE mountpoint within the timeout. |
| [`flyteplugins.union.errors.VolumeNoIndex`](classes) | An operation needs a published index, but the Volume has none. |
| [`flyteplugins.union.errors.VolumeNotForkable`](classes) | Fork was requested on a Volume that is neither mounted nor has an index. |
| [`flyteplugins.union.errors.VolumeNotMounted`](classes) | An operation that needs a live mount was called on an unmounted Volume. |
| [`flyteplugins.union.errors.VolumeStoreTypeNotSet`](classes) | The Volume's ``metadata_store_type`` is unset and couldn't be resolved. |
| [`flyteplugins.union.errors.VolumeUnmountError`](classes) | The volume could not be unmounted (``fusermount`` kept returning EBUSY). |
| [`flyteplugins.union.errors.VolumeUsageError`](classes) | Base for Volume *user* errors — caller misuse the caller can fix. |
| [`flyteplugins.union.io.ActionRef`](classes) | Provenance: the action (one task execution within a run) that. |
| [`flyteplugins.union.io.ROVolume`](classes) | Immutable, versioned volume — PRD §Core Concepts. |
| [`flyteplugins.union.io.RWVolume`](classes) | Mutable working copy — PRD §Core Concepts. |
| [`flyteplugins.union.io.Volume`](classes) | A persistent volume identified by its metadata index. |
| [`flyteplugins.union.remote.ApiKey`](classes) | Represents a Union API Key (OAuth Application). |
| [`flyteplugins.union.remote.Assignment`](classes) | Represents role/policy assignments for an identity. |
| [`flyteplugins.union.remote.Cluster`](classes) | Represents a Union cluster. |
| [`flyteplugins.union.remote.ClusterPool`](classes) | Represents a Union cluster pool — the configuration shared by its member clusters. |
| [`flyteplugins.union.remote.Member`](classes) | Represents a Union organization member (user or application). |
| [`flyteplugins.union.remote.Policy`](classes) | Represents a Union RBAC Policy. |
| [`flyteplugins.union.remote.Queue`](classes) | Represents a Union scheduling queue. |
| [`flyteplugins.union.remote.Role`](classes) | Represents a Union RBAC Role. |
| [`flyteplugins.union.remote.User`](classes) | Represents a Union user. |
| [`flyteplugins.union.remote.VolumeExplore`](classes) | A resolved :class:`Volume` plus the IO to inspect and walk its lineage. |
| [`flyteplugins.union.remote.VolumeResolveError`](classes) | No (or ambiguous) Volume-typed value could be resolved on an action. |
| [`flyteplugins.union.utils.auth.AppClientCredentials`](classes) | Application client credentials for API key. |

### Packages

| Package | Description |
|-|-|
| [`flyteplugins.union.cli`](packages/flyteplugins.union.cli) |  |
| [`flyteplugins.union.cli.cluster_pool`](packages/flyteplugins.union.cli.cluster_pool) |  |
| [`flyteplugins.union.cli.queue`](packages/flyteplugins.union.cli.queue) |  |
| [`flyteplugins.union.errors`](packages/flyteplugins.union.errors) | Volume-specific runtime errors. |
| [`flyteplugins.union.internal.validate.validate.validate_pb2`](packages/flyteplugins.union.internal.validate.validate.validate_pb2) | Generated protocol buffer code. |
| [`flyteplugins.union.io`](packages/flyteplugins.union.io) | Persistent, mountable :class:`Volume` type for the Flyte SDK v2. |
| [`flyteplugins.union.remote`](packages/flyteplugins.union.remote) | Union remote control plane objects. |
| [`flyteplugins.union.utils`](packages/flyteplugins.union.utils) | Public utilities for ``flyteplugins. |
| [`flyteplugins.union.utils.auth`](packages/flyteplugins.union.utils.auth) |  |
| [`flyteplugins.union.utils.image`](packages/flyteplugins.union.utils.image) | Shared helpers for building :class:`flyte. |

