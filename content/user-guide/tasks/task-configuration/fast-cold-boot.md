---
title: Fast cold boot
description: Start containers in seconds by building images with the remote image builder.
icon: lightning-charge
weight: 2
variants: -flyte +union
---

# Fast cold boot

**Cold boot** is the time between a task being scheduled on a node and its container starting.
Most of it is spent pulling the image.
On a fresh node, a 10 GB GPU image takes 4 to 5 minutes to pull.

With fast cold boot, images built by the [remote `ImageBuilder`](./container-images#remote-imagebuilder) start in seconds instead, even when they are many gigabytes.
You don't change your tasks.
If you build from a Dockerfile, keep building it your way and pass the result through the remote builder, as shown in [Use an image from your existing build system](#use-an-image-from-your-existing-build-system).

Fast cold boot is a data-plane setting, off by default.
On BYOC, ask Union.ai support to enable it.
On a self-managed data plane, set `nodeBootstrap.enabled` and then `imageBuilder.enableImageOptimization` in the [dataplane chart](../../../deployment/selfmanaged/helm-chart-reference/dataplane).

## How it works

The remote builder stores each image in a format that can be read lazily:

1. When a task lands on a node, the node downloads a small index of the image instead of every layer.
2. The container starts as soon as the index is mounted.
3. Files are fetched from the registry the first time the task reads them. Data is cached on the node's local disk and shared with other images on the same node.

Files the task never reads are never downloaded.
If your image carries CUDA libraries, test data, or tools your task doesn't use, they cost nothing at startup.

## Build an image with the remote builder

Set the builder to `remote` in your `config.yaml`:

```yaml
image:
  builder: remote
```

Or set the `FLYTE_IMAGE_BUILDER=remote` environment variable.

Any image you define with `flyte.Image` is then built remotely and gets fast cold boot:

```python
import flyte

image = (
    flyte.Image.from_debian_base()
    .with_apt_packages("ca-certificates")
    .with_pip_packages("torch", "transformers")
)

env = flyte.TaskEnvironment(name="train", image=image)


@env.task
async def train(epochs: int) -> float:
    ...
```

`flyte deploy` and `flyte run` build the image the first time, then reuse it until its definition changes.
An image built before fast cold boot was enabled keeps its standard format.
To convert it, rebuild it with `flyte.build(image, force=True)`.

## Use an image from your existing build system

If you already build images in CI or with another tool, keep that build.
Pass its output through the remote builder as a base image, and the remote builder rebuilds it in the fast cold boot format.
This adds no layers and leaves the image contents unchanged.

Wrap the image with `flyte.Image.from_base()` and call `clone()` with a `name`:

```python
import os

import flyte

# Set by CI to the image your build system just pushed, for example
# 123456789012.dkr.ecr.us-east-1.amazonaws.com/training:3f2c1ab
base_image = os.getenv("TRAINING_IMAGE", "123456789012.dkr.ecr.us-east-1.amazonaws.com/training:latest")

image = flyte.Image.from_base(base_image).clone(name="training")

env = flyte.TaskEnvironment(name="training", image=image)


@env.task
async def train(epochs: int) -> float:
    ...
```

Then deploy from the same CI job, after your own build pushes the image:

```bash
export TRAINING_IMAGE="123456789012.dkr.ecr.us-east-1.amazonaws.com/training:${GIT_SHA}"
export FLYTE_IMAGE_BUILDER=remote
flyte deploy --recursive workflows/
```

`TRAINING_IMAGE` is only read at deploy time.
Inside the task container the variable is unset, so the default value is never used to pull anything.

Keep these points in mind:

* **The base image must already run Flyte tasks.** It needs the `flyte` package installed and your task code importable. Because `clone()` adds no layers, a missing `flyte` package builds successfully and fails when the task starts. To adapt an image that isn't Flyte-ready, see [Bring your own image](../../project-patterns/bring-your-own-image).
* **The rebuilt image runs only on your data plane.** It is stored in a lazy-pull format that only nodes set up for fast cold boot can run. To run the image locally or in CI, use your original image, not the `clone()` output.
* **`clone()` triggers the remote build.** A bare `flyte.Image.from_base("...")` is used as-is and is never rebuilt, so it starts with a standard image pull.
* **Use an immutable tag for the base image**, such as a Git SHA or a digest. The remote builder rebuilds when the base image reference changes. If you push a new image under the same tag, such as `:latest`, the reference doesn't change and the old build is reused.
* **Leave `registry` unset in `clone()`.** The image is then stored in your data plane's internal registry, close to your nodes. Because files are fetched while the task runs, a registry outside your cloud network makes those reads slower.
* **Private base images** need registry credentials for the remote builder to pull them. Pass `registry_secret` to `clone()`, and leave out the `registry` argument shown in [ImageBuilder with external registries](./container-images#imagebuilder-with-external-registries).
* **To add layers** on top of the base image, pass `extendable=True` to `clone()` and chain `with_*` methods as usual.

## Benchmarks

Image pull time on a fresh node with an empty cache:

| Image | Compressed size | Standard pull | Fast cold boot | Speedup |
|---|---|---|---|---|
| TensorFlow (no CUDA) | 534 MB | 18.8 s | 1.1 s | 17x |
| PyTorch | 3.4 GB | 1 min 31 s | 4.7 s | 19x |
| PyTorch 1.13 + CUDA | 9.1 GB | 4 min 40 s | 1.13 s | 248x |
| CUDA + PyTorch | 9.9 GB | 4 min 38 s | 1.16 s | 240x |

On a node that has already run the image, startup takes 160 to 730 ms.

End-to-end time of a task on a fresh node, from scheduling to completion:

| | Image pull | Execution | Total |
|---|---|---|---|
| Standard pull | 2 min 3 s | 7 s | 2 min 10 s |
| Fast cold boot | 0.5 s | 29 s | 29.5 s |

Execution takes longer with fast cold boot because the task fetches files the first time it reads them.
The total still drops by 77%.
The saving is largest when a task reads a small part of a large image, and smallest when it reads most of the image right away.

Neither figure includes node provisioning, which happens before the image pull.

For the full benchmark write-up, see [We cut container cold boot from minutes to seconds](https://www.union.ai/blog-post/we-cut-container-cold-boot-from-minutes-to-seconds-heres-how).

## Related pages

* [Container images](./container-images): defining images with `flyte.Image` and configuring the builder.
* [Reusable containers](./reusable-containers): keep a warm container across tasks to skip startup entirely.
