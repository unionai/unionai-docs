---
title: Mount volumes
description: Mount block volumes in a Sandbox VM next to its disk, read-only or read-write, and commit what a session writes to them as new versions.
weight: 9
variants: -flyte +union
---

# Mount volumes

A sandbox's disk holds its operating system and the files it works on. Some data doesn't belong there: a dataset that many sandboxes read, or checkpoints that a training script writes and a later task needs. Mount each as a [block volume](../tasks/task-programming/volumes/block-volumes) at a path of its own.

This task trains in a sandbox. The dataset is mounted read-only, and the checkpoints read-write. The task returns the checkpoints as a new version of the volume:

```python
import flyte
from flyteplugins.union import sandbox
from flyteplugins.union.io import ROBlockVolume

trainer = sandbox.SandboxEnvironment(name="trainer", resources=flyte.Resources(cpu=2, memory="4Gi"))
env = flyte.TaskEnvironment(
    name="train",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-union>=0.26.0"),
)


@env.task
async def train(dataset: ROBlockVolume, checkpoints: ROBlockVolume) -> ROBlockVolume:
    async with trainer.session(
        "train",
        volumes={
            "/data": dataset,  # read-only
            "/ckpt": sandbox.Mount(checkpoints, mode="rw"),  # read-write
        },
    ) as sb:
        await sb.fs.upload("train.py", "train.py")
        await sb.run("python train.py --data /data --out /ckpt")
        return await sb.volumes["/ckpt"].commit()
```

Use a mounted volume instead of the sandbox's disk when the data has a life of its own: it comes from a task, or goes to one, or several sandboxes read it. Use the disk for the environment itself. See [Save and fork disks](./persist-and-fork).

## Name the volumes when the session starts

`volumes=` takes a mapping from a path in the sandbox to a volume. It is a different argument from `volume=`, without the "s", which sets the sandbox's own disk.

| You pass | The sandbox gets |
| --- | --- |
| `volumes={"/data": v}` | A read-only mount of `v` at `/data`. |
| `volumes={"/ckpt": sandbox.Mount(v, mode="rw")}` | A read-write mount of a private copy of `v` at `/ckpt`. |

- **Each mount is a private copy.** The volume you pass is never changed, whatever the mode. Any number of sandboxes can mount the same volume at once.
- **Only committed block volumes.** Pass an `ROBlockVolume`: what `BlockVolume.commit()` returns, or a task input. A regular volume is refused. See [Mount a regular volume](#mount-a-regular-volume).
- **At most six volumes** per sandbox.
- **Named at the start.** A running sandbox can't mount another volume.
- **Not on a scratch disk.** A session on a `ScratchVolume` can't mount volumes.
- **Both runtimes.** Mounts work in microVM and gVisor sandboxes.

A mount path is absolute and normalized. It can't be `/`, and it can't be at or under `/proc`, `/sys`, `/dev`, `/tmp`, `/work`, `/.union`, or `/sbx`. One mount can't be inside another. A `volumes=` that breaks these rules raises `SandboxUsageError` before anything starts.

`sb.volumes` lists what a sandbox mounts, by path. Each entry has a `path`, a `mode` (`"ro"` or `"rw"`), and the `volume` it was copied from.

## Mount a regular volume

A sandbox mounts block volumes only: a `BlockVolume` or `ROBlockVolume`, which is one ext4 image. A regular volume, the kind `Volume.new()` creates, stores each file separately and can't be mounted in a sandbox of either runtime. Nothing converts it for you. Passing one raises `SandboxUsageError` before the session starts:

```text
volume my-data at '/data' is not a block volume: a session mounts BlockVolumes (one ext4 image) only. Convert it with BlockVolume.from_volume()
```

`flyte connect sandbox --with-volume` fails with the same message, before it creates anything. In the console, the volume picker of **New Sandbox** lists block volumes only. If a volume you expect is missing there, it is a regular volume.

There are two ways to get a volume a sandbox can mount.

**Create it as a block volume.** Do this when the volume is meant for sandboxes. Forks of a block volume are block volumes too:

```python
from flyteplugins.union.io import BlockVolume

vol = BlockVolume.new(name="my-data", size="1G", artifact="my-data")
```

See [Block volumes](../tasks/task-programming/volumes/block-volumes#create-and-use-a-block-volume) for how to fill and commit it.

**Convert a regular volume in a task.** `BlockVolume.from_volume()` copies the files into a new ext4 image. The source isn't changed. A small volume takes a few seconds:

```python
import flyte
from flyteplugins.union.io import BlockVolume, ROBlockVolume, Volume, allow_volumes

convert_env = flyte.TaskEnvironment(
    name="volume-convert",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-union>=0.26.0"),
    pod_template=allow_volumes(),
    resources=flyte.Resources(cpu="1", memory="4Gi"),
)


@convert_env.task
async def to_block(locator: str) -> ROBlockVolume:
    src = await Volume.from_locator(locator)
    bv = await BlockVolume.from_volume(src, name=f"{src.name}-blk")
    return await bv.finalize(message=f"block copy of {src.name}")
```

The image is sized from the source's recorded usage, with headroom. Pass `size=` to choose it yourself. A task can also take the regular volume as an `ROVolume` input instead of a locator.

The task returns an `ROBlockVolume`, which goes straight into `volumes=`. This task converts a regular volume and reads it in a sandbox:

```python
from flyteplugins.union import sandbox

reader = sandbox.SandboxEnvironment(name="reader")


@convert_env.task
async def count_files(locator: str) -> str:
    data = await to_block(locator)  # regular volume in, block volume out
    async with reader.session("count", volumes={"/data": data}) as sb:
        return (await sb.run("find /data -type f | wc -l")).stdout.strip()
```

To mount it from the CLI instead, use the block volume's `.locator`.

## Commit what a session writes

A commit is the only thing that keeps what a session writes to a volume:

```python
new_checkpoints = await sb.volumes["/ckpt"].commit()  # an ROBlockVolume
```

`commit()` saves the session's copy as it is at that moment and returns it as a new `ROBlockVolume`. The session keeps running. Its writes to the volume wait while the copy is frozen for the commit. The result is a regular task input and output, and other sandboxes can mount it.

- **Nothing is committed for you.** When a session closes, is cancelled, or fails, what it wrote since the last commit is dropped. Commit before the block exits.
- **`sb.commit()` does not include volumes.** It saves the sandbox's own disk only.
- **A read-only mount can't be committed.** `commit()` on one raises `SandboxUsageError`.

## What carries the volumes

| You continue with | Volumes in the new sandbox |
| --- | --- |
| `env.session(name, volume=disk)`, from `sb.commit()` | Only the `volumes=` you name. The disk doesn't remember any. |
| `env.session(name, snapshot=snap)`, from `sb.snapshot()` or `sb.suspend()` | The ones the sandbox had, as they were at the instant of the snapshot. |
| `sb.fork(name)` | A copy of each of the parent's, in the same mode, taken at the same instant as the disk. |
| `sb.fork(name, volumes={...})` | The ones you name instead. `volumes={}` mounts none. |
| `sb.fork(name, memory=True)` | The parent's. It takes no `volumes=`. |
| `env.connect(name)` to a sandbox that exists | The ones it was created with. A read-write one is as the sandbox's last run left it. |

A snapshot, a suspend, and a fork save the disk and every volume together, so the sandbox continues with a consistent set. These saved copies belong to the snapshot or the fork. They are not versions of your volumes: to get an `ROBlockVolume` you can pass on, call `commit()` on the mount.

When you continue from a snapshot, `volumes=` may only repeat paths the sandbox already mounts, each in the same mode. Anything else raises `SandboxUsageError`.

With `env.connect`, `volumes=` applies only when the call creates the sandbox, and `create=False` takes none. See [Keep a sandbox and come back to it](./reconnect).

## Mount a volume from the CLI

`flyte connect sandbox` mounts volumes in a sandbox it creates. The option is `--with-volume PATH=LOCATOR`: the path in the sandbox, then `=`, then the volume's locator. Repeat it for more volumes:

```bash
flyte connect sandbox my-agent --with-volume /data=s3://my-bucket/volumes/<id>.metadata.json
```

- **The value after `=` is a locator, not a name.** `flyte get volumes` lists the volumes registered as artifacts, with their locators.
- **Mounts from the CLI are read-only.**
- **Only for a sandbox the command creates.** A sandbox that already exists keeps the volumes it has, and the option is ignored.
- **Block volumes only.** See [Mount a regular volume](#mount-a-regular-volume).

The command reads the volume's metadata from object storage on your machine, not through Union.ai, so your shell needs credentials for the bucket. On AWS, setting `AWS_PROFILE` is not enough. Export the profile's credentials first:

```bash
eval "$(aws configure export-credentials --profile <your-profile> --format env)"
```

Replace `<your-profile>` with the AWS profile that can read the bucket. Without credentials, the command fails after about 25 seconds of trying to reach the EC2 metadata endpoint.

### List a volume in `flyte get volumes`

A volume shows up in `flyte get volumes` and in the console only if it is published as an artifact. That takes two things:

- An artifact identity on the volume: `BlockVolume.new(..., artifact="my-data")` or `Volume.new(..., artifact="my-data")`.
- `@env.task(produces_artifacts=True)` on every task that returns the volume. Without it, nothing is registered and no error is raised.

See [Tracking versions as artifacts](../tasks/task-programming/volumes/versions#tracking-versions-as-artifacts). A disk that a sandbox publishes with `publish_on_exit` needs neither.

## Volumes written by untrusted code

> [!WARNING] A committed volume can attack whoever mounts it
> A volume committed from a read-write mount holds an ext4 filesystem that the sandbox's code wrote. The kernel of whatever mounts it next reads that filesystem, and it can be crafted to attack that kernel. A task pod and a gVisor sandbox mount it with the node's kernel.

For code you don't trust:

- Mount volumes read-only, or mount none.
- If the code must write a volume, mount the result only in microVM sandboxes, where the guest kernel reads it. Don't mount it in a task pod or a gVisor sandbox.
- Copy results out with `sb.fs` instead of a volume when a few files are enough. See [Work with files](./files).

See [Network and security](./network-and-security#mounted-volumes).

## Requirements

- `flyteplugins-union` 0.26.0 or later.
- Block volumes. A regular volume has to be converted first. See [Mount a regular volume](#mount-a-regular-volume).
- Sandbox nodes that support mounts. An older node refuses a session that names `volumes=`, instead of starting it without them. Ask your Union.ai solutions team to update the node pool.
