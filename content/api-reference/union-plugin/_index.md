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
| [`flyteplugins.union.errors.VolumeCommandError`](packages/flyteplugins.union.errors/volumecommanderror) | A backend CLI invocation (e. |
| [`flyteplugins.union.errors.VolumeCommitError`](packages/flyteplugins.union.errors/volumecommiterror) | A keep-alive checkpoint could not be made durable: the writeback staging. |
| [`flyteplugins.union.errors.VolumeError`](packages/flyteplugins.union.errors/volumeerror) | Base for Volume *system* failures — infra/runtime problems the caller. |
| [`flyteplugins.union.errors.VolumeMigrateNoop`](packages/flyteplugins.union.errors/volumemigratenoop) | Metadata-store migration was requested to the store type already in use. |
| [`flyteplugins.union.errors.VolumeMountError`](packages/flyteplugins.union.errors/volumemounterror) | The volume could not be mounted — the client exited prematurely, the. |
| [`flyteplugins.union.errors.VolumeMountTimeout`](packages/flyteplugins.union.errors/volumemounttimeout) | The mount did not become a FUSE mountpoint within the timeout. |
| [`flyteplugins.union.errors.VolumeNoIndex`](packages/flyteplugins.union.errors/volumenoindex) | An operation needs a published index, but the Volume has none. |
| [`flyteplugins.union.errors.VolumeNotForkable`](packages/flyteplugins.union.errors/volumenotforkable) | Fork was requested on a Volume that is neither mounted nor has an index. |
| [`flyteplugins.union.errors.VolumeNotMounted`](packages/flyteplugins.union.errors/volumenotmounted) | An operation that needs a live mount was called on an unmounted Volume. |
| [`flyteplugins.union.errors.VolumeStoreTypeNotSet`](packages/flyteplugins.union.errors/volumestoretypenotset) | The Volume's ``metadata_store_type`` is unset and couldn't be resolved. |
| [`flyteplugins.union.errors.VolumeUnmountError`](packages/flyteplugins.union.errors/volumeunmounterror) | The volume could not be unmounted (``fusermount`` kept returning EBUSY). |
| [`flyteplugins.union.errors.VolumeUsageError`](packages/flyteplugins.union.errors/volumeusageerror) | Base for Volume *user* errors — caller misuse the caller can fix. |
| [`flyteplugins.union.io.ActionRef`](packages/flyteplugins.union.io/actionref) | Provenance: the action (one task execution within a run) that. |
| [`flyteplugins.union.io.ROVolume`](packages/flyteplugins.union.io/rovolume) | Immutable, versioned volume — PRD §Core Concepts. |
| [`flyteplugins.union.io.RWVolume`](packages/flyteplugins.union.io/rwvolume) | Mutable working copy — PRD §Core Concepts. |
| [`flyteplugins.union.io.Volume`](packages/flyteplugins.union.io/volume) | A persistent volume identified by its metadata index. |
| [`flyteplugins.union.remote.ApiKey`](packages/flyteplugins.union.remote/apikey) | Represents a Union API Key (OAuth Application). |
| [`flyteplugins.union.remote.Assignment`](packages/flyteplugins.union.remote/assignment) | Represents role/policy assignments for an identity. |
| [`flyteplugins.union.remote.Cluster`](packages/flyteplugins.union.remote/cluster) | Represents a Union cluster. |
| [`flyteplugins.union.remote.ClusterPool`](packages/flyteplugins.union.remote/clusterpool) | Represents a Union cluster pool — the configuration shared by its member clusters. |
| [`flyteplugins.union.remote.Member`](packages/flyteplugins.union.remote/member) | Represents a Union organization member (user or application). |
| [`flyteplugins.union.remote.Policy`](packages/flyteplugins.union.remote/policy) | Represents a Union RBAC Policy. |
| [`flyteplugins.union.remote.Queue`](packages/flyteplugins.union.remote/queue) | Represents a Union scheduling queue. |
| [`flyteplugins.union.remote.Role`](packages/flyteplugins.union.remote/role) | Represents a Union RBAC Role. |
| [`flyteplugins.union.remote.User`](packages/flyteplugins.union.remote/user) | Represents a Union user. |
| [`flyteplugins.union.remote.VolumeExplore`](packages/flyteplugins.union.remote/volumeexplore) | A resolved :class:`Volume` plus the IO to inspect and walk its lineage. |
| [`flyteplugins.union.remote.VolumeResolveError`](packages/flyteplugins.union.remote/volumeresolveerror) | No (or ambiguous) Volume-typed value could be resolved on an action. |
| [`flyteplugins.union.utils.auth.AppClientCredentials`](packages/flyteplugins.union.utils.auth/appclientcredentials) | Application client credentials for API key. |

### Packages

| Package | Description |
|-|-|
| [`flyteplugins.union.cli`](packages/flyteplugins.union.cli/_index) |  |
| [`flyteplugins.union.cli.cluster_pool`](packages/flyteplugins.union.cli.cluster_pool/_index) |  |
| [`flyteplugins.union.cli.queue`](packages/flyteplugins.union.cli.queue/_index) |  |
| [`flyteplugins.union.errors`](packages/flyteplugins.union.errors/_index) | Volume-specific runtime errors. |
| [`flyteplugins.union.internal.validate.validate.validate_pb2`](packages/flyteplugins.union.internal.validate.validate.validate_pb2/_index) | Generated protocol buffer code. |
| [`flyteplugins.union.io`](packages/flyteplugins.union.io/_index) | Persistent, mountable :class:`Volume` type for the Flyte SDK v2. |
| [`flyteplugins.union.remote`](packages/flyteplugins.union.remote/_index) | Union remote control plane objects. |
| [`flyteplugins.union.utils`](packages/flyteplugins.union.utils/_index) | Public utilities for ``flyteplugins. |
| [`flyteplugins.union.utils.auth`](packages/flyteplugins.union.utils.auth/_index) |  |
| [`flyteplugins.union.utils.image`](packages/flyteplugins.union.utils.image/_index) | Shared helpers for building :class:`flyte. |

