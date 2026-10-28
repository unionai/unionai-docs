---
title: Work with a volume on your machine
icon: laptop
weight: 3
variants: -flyte +union
description: Mount a Volume on a laptop, a dev box or a CI runner with the flyte CLI - a durable working copy you can resume, and warm for working offline.
---

# Work with a volume on your machine

[Using a volume in a task](./volumes-in-tasks) runs everything inside the
cluster. You can also mount a volume **on your own machine** - a laptop, a dev
box, a CI runner - and read and write it like any other directory. No FUSE
tooling to install: on macOS the volume is served over a loopback NFS mount
instead, so `mount volume` works there without macFUSE.

This is the workflow for building a dataset by hand, inspecting one in place
with ordinary tools, or carrying one onto a plane.

## Create a volume

```bash
flyte create volume my-dataset --project my-project --domain development
```

You do not have to say where it lives. The CLI asks the control plane for the
storage this project and domain already use - the same raw-data path a task
would be given - so a volume you create from a laptop lands exactly where a
volume created inside a task lands. It prints the bucket it chose and the
locator of the new (empty) version.

Pass `--bucket s3://my-bucket/volumes` to choose explicitly; with an explicit
bucket the command contacts no control plane at all. `--size 64G` makes a
[block volume](./block-volumes) instead, which is much faster for workloads
with many small files - but only on Linux: macOS has neither an ext4 driver nor
a loop device to attach the image to, so `--size` is refused there.

> [!NOTE]
> The discovered bucket is the one your **tasks** use, and your laptop is a
> different access domain. If `create` fails with *"Access denied reading the
> bucket"*, your local credentials cannot reach that bucket even though they
> are valid - use a profile or role that can (`AWS_PROFILE=...`), or pass
> `--bucket` to use one you already have access to.

## Mount it

Name the volume with exactly one of `--artifact`, `--run` (with `--action`), or
`--locator`. The mount point is the only positional argument:

```bash
# By artifact, which is the name you would normally use
flyte mount volume ~/data --artifact my-dataset

# A specific version, by the locator create or commit printed. Needs no
# control plane at all - only object-store credentials.
flyte mount volume ~/data --locator s3://my-bucket/volumes/versions/volumes/<id>.metadata.json
```

The volume is **forked first** and the fork is what gets mounted, so writing
through the mount cannot touch the version you named. A fork copies no data.

The command then holds the terminal. Press **Ctrl-C** to drain, unmount, and
publish your writes as a new version, whose locator it prints - as do `kill`
and closing the terminal, so a mount does not get orphaned by a closed window.
`--no-commit` throws the writes away instead, and `--read-only` mounts without
forking at all - use it when you only have read access, or only want to look.

## A local mount is a durable working copy

A local mount is not a scratch directory. The fork is recorded on disk, so a
second `mount volume` of the same volume comes back to it rather than making
another one - and **if the first mount ended without publishing, the work is
still there and the mount picks it up.** Losing your connection, your
credentials expiring, or the machine restarting all leave the work recoverable.

**Resuming needs no network.** The fork's own record is kept with the working
copy, so rebuilding it does not re-read anything from the bucket. That is the
difference between resuming on a plane and resuming after you land.

Three commands manage that local state:

```bash
flyte status volume              # what is held locally, and how much of it is unpublished
flyte status volume my-dataset   # just this one
flyte unmount volume my-dataset  # stop a mount running in another terminal, publishing as it goes
flyte forget volume my-dataset   # remove the local copy
```

`forget` refuses to take unpublished work with it unless you pass `--discard`.

If the published version has moved on while your local work sat there, the next
mount says so and asks which you want. Keeping your work is the default,
including when there is no terminal to ask - a prompt nobody can answer is not
consent to delete. `--discard-local` chooses the other way explicitly.

> [!NOTE]
> The mount is served by a client process that outlives the CLI. If you kill
> the CLI with `SIGKILL` (rather than Ctrl-C), that client keeps running and
> keeps the local index open, and the next mount will tell you so and name the
> process. Your work is safe - it is in the local index, not in that process.
> Stop it and mount again, and the resume picks the work up.

## Take it offline

Reads are served on demand, so a mount needs the network for anything it has
not already cached - and an uncached read with no network is an **I/O error**,
not a slow read. Warm the cache before you disconnect:

```bash
# A subtree you know you need
flyte mount volume ~/data --artifact my-dataset --warmup models/

# Everything
flyte mount volume ~/data --artifact my-dataset --warmup .
```

`--warmup` names a path **inside** the volume, relative to the mount point, and
can be repeated. You can also warm a mount that is already up, from another
terminal:

```bash
flyte warmup volume ~/data            # the whole volume
flyte warmup volume ~/data models/    # just this subtree
flyte warmup volume ~/data --check    # report what is already cached
```

On macOS the client's own parallel prefetch is unavailable (it drives the mount
through a control file the NFS server does not serve), so warming reads the
files instead. It is slower and the end state is the same.

> [!NOTE]
> `flyte create volume --mount` is **not** resumable, and says so when you use
> it. A volume you have just declared has no published version yet, so there is
> nothing to fork and come back to. Create it, then `flyte mount volume` the
> locator it printed - that path resumes.

## Inspecting a volume

To browse a volume without mounting it, use the CLI. `flyte explore volume`
opens an interactive view of a volume's file tree and its version history,
reading only the small metadata index (no FUSE mount and no file downloads):

```bash
# Explore the volume produced by a run (auto-discovers the volume output)
flyte explore volume <run-name>

# Pin a specific action and the exact output to inspect
flyte explore volume <run-name> <action-name> --op-name my_volume
```

It follows the version lineage, so you can step back through earlier commits and
jump to the action that produced any version. To open an index you already have
on disk, pass `--from-file <path> --store-type sqlite`.

## Next

- [Use a volume in a task](./volumes-in-tasks) - the same volume, from inside
  the cluster.
- [Performance, caching and tuning](./volumes-performance) - what the local
  cache is doing, and the knobs that apply to any mount.
