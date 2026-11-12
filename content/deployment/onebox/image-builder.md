---
title: Image builder
description: Build task images inside your cluster with BuildKit, push them to a registry your nodes pull from, and reuse them across runs.
icon: hammer
weight: 9
variants: -flyte +union
---

# Image builder

With the image builder, the SDK builds a task's container image inside your cluster instead of on the machine that runs `flyte run`. It runs a `build-image` task that sends the build to BuildKit and pushes the result to a registry. Before building, the SDK asks onebox whether the image already exists, so an image is built once and reused. Onebox registers the `build-image` task itself. You bring BuildKit and the registry, or, on a single-user or evaluation cluster, have the chart run both. Onebox doesn't depend on any of them to start.

## Requirements

- **BuildKit**, reachable from task pods. BuildKit runs privileged, or rootless on kernels 5.11 and later.
- **A registry** that:
  - BuildKit can push to without credentials;
  - your nodes can pull from, at the same address BuildKit pushed to;
  - onebox can read anonymously, possibly at a different address.

  Registries that require credentials aren't supported.
- **Access to the build task's images.** The `build-image` task runs the `build-image` image and has BuildKit use the `frontend-v2` image, both published by Union at `ghcr.io/unionai/imagebuilder` with each release, for amd64 and arm64. The chart uses them at its `appVersion` unless you set `imageBuilder.taskImages.tag`. Nodes must be able to pull `build-image`, and BuildKit `frontend-v2`. Without internet access, copy both to a registry of yours, at the chart's `appVersion`, and point onebox at it:

  ```yaml
  imageBuilder:
    taskImages:
      repository: registry.example.com/imagebuilder   # holds build-image and frontend-v2
  ```

## Run BuildKit and a registry with the chart

`imageBuilder.bundled.enabled` runs a BuildKit daemon and a registry in onebox's namespace and points onebox at them:

```yaml
imageBuilder:
  enabled: true
  bundled:
    enabled: true
```

- BuildKit runs privileged and on the node's network, listening without TLS on port `imageBuilder.bundled.buildkit.hostPort` (`30234`) of its node, behind a Service on port `1234`.
- The registry listens on NodePort `imageBuilder.bundled.registry.nodePort` (`30000`) of every node and accepts anonymous pushes. BuildKit pushes to `localhost:30000/onebox` and nodes pull from there, since containerd and BuildKit accept plain HTTP for `localhost`. Onebox checks for existing images at the registry's in-cluster Service.
- Images are kept on an `emptyDir`, so they're rebuilt after the registry restarts. Set `imageBuilder.bundled.registry.storage` (for example `20Gi`) to keep them on a PersistentVolumeClaim instead; `helm uninstall` leaves the claim behind.

Any of `imageBuilder.buildkitURI`, `imageBuilder.repository`, and `imageBuilder.lookupURL` you set yourself wins over the bundled address. `lookupURL` points at the bundled registry only while `repository` does.

> [!WARNING] Single-user or evaluation clusters only
> Anything that can reach the bundled BuildKit can run builds as root on its node, and anything that can reach the registry can overwrite images. Don't use them on a shared cluster.

## Bring your own BuildKit and registry

On a shared cluster, run BuildKit rootless, and restrict access to it with a NetworkPolicy that admits only onebox's namespace: the `build-image` task connects to BuildKit without client TLS, so a BuildKit that requires mutual TLS can't be used. Use a registry with TLS. Then point onebox at them:

```yaml
imageBuilder:
  enabled: true
  buildkitURI: tcp://buildkit.buildkit.svc:1234            # as task pods reach BuildKit
  repository: registry.example.com/onebox                  # where nodes pull from
  lookupURL: https://registry.example.com/onebox           # where onebox checks
```

`lookupURL` defaults to `https://<repository>`; set it when onebox reaches the registry at another address.

Either way, onebox then creates the `system` project and registers the `build-image` task in its `production` domain, a few seconds after it starts. It registers the task again when `imageBuilder.taskImages` changes, or when an upgrade brings new images; otherwise there's nothing to do.

## Build an image

Use the remote builder for a run:

```shell
flyte --image-builder remote run my_task.py main
```

or set `image.builder: remote` in `.flyte/config.yaml`. The first run builds the image, which takes about half a minute for a small Python image, and later runs skip the build:

```text
i Image localhost:30000/onebox/my-image:3892709e... already exists, skipping build
```

## Gotchas

| Symptom | Cause and fix |
|---|---|
| `remote image builder is not enabled` | The `build-image` task isn't registered in `system`/`production` yet, or the CLI user can't read that project. Onebox registers it shortly after starting; while it can't, its log says `build-image task not registered yet` and why. |
| Builds fail with `exit code 255` while BuildKit loads the frontend | BuildKit can't run the `frontend-v2` image on its node's architecture. With a mirror, copy the image with all its architectures (for example `crane copy` or `docker buildx imagetools create`), not just one. |
| Every run rebuilds | Onebox can't read the registry at `imageBuilder.lookupURL`, or the path differs from `imageBuilder.repository`. They must name the same repository. |
| Task pods fail with `ErrImagePull` after a successful build | Nodes can't pull from `imageBuilder.repository`. It must resolve and be trusted from the node. |
