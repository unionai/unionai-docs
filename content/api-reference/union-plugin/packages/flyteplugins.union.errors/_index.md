---
title: flyteplugins.union.errors
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# flyteplugins.union.errors

Volume-specific runtime errors.

These subclass the :mod:`flyte.errors` taxonomy, so they keep flyte's
system/user recoverability classification (and their ``str()`` is the
message), while giving callers a stable ``flyteplugins.union.errors`` surface
to catch — e.g. ``except VolumeMountError`` or, more broadly, ``except
VolumeError`` (system) / ``except VolumeUsageError`` (caller misuse).

Each concrete type carries a fixed error ``code`` (surfaced on the flyte error
envelope) via the ``_code`` class attribute; subclasses just override it.
## Directory

### Errors

| Exception | Description |
|-|-|
| [`VolumeCommandError`](../flyteplugins.union.errors/volumecommanderror) | A backend CLI invocation (e. |
| [`VolumeCommitError`](../flyteplugins.union.errors/volumecommiterror) | A keep-alive checkpoint could not be made durable: the writeback staging. |
| [`VolumeError`](../flyteplugins.union.errors/volumeerror) | Base for Volume *system* failures — infra/runtime problems the caller. |
| [`VolumeMigrateNoop`](../flyteplugins.union.errors/volumemigratenoop) | Metadata-store migration was requested to the store type already in use. |
| [`VolumeMountError`](../flyteplugins.union.errors/volumemounterror) | The volume could not be mounted — the client exited prematurely, the. |
| [`VolumeMountTimeout`](../flyteplugins.union.errors/volumemounttimeout) | The mount did not become a FUSE mountpoint within the timeout. |
| [`VolumeNoIndex`](../flyteplugins.union.errors/volumenoindex) | An operation needs a published index, but the Volume has none. |
| [`VolumeNotForkable`](../flyteplugins.union.errors/volumenotforkable) | Fork was requested on a Volume that is neither mounted nor has an index. |
| [`VolumeNotMounted`](../flyteplugins.union.errors/volumenotmounted) | An operation that needs a live mount was called on an unmounted Volume. |
| [`VolumeStoreTypeNotSet`](../flyteplugins.union.errors/volumestoretypenotset) | The Volume's ``metadata_store_type`` is unset and couldn't be resolved. |
| [`VolumeUnmountError`](../flyteplugins.union.errors/volumeunmounterror) | The volume could not be unmounted (``fusermount`` kept returning EBUSY). |
| [`VolumeUnmountUnsupportedError`](../flyteplugins.union.errors/volumeunmountunsupportederror) | The runtime cannot unmount the FUSE client at all because ``fusermount``. |
| [`VolumeUsageError`](../flyteplugins.union.errors/volumeusageerror) | Base for Volume *user* errors — caller misuse the caller can fix. |

