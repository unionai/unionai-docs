---
title: Image builder
description: Build task images inside your cluster with BuildKit, push them to a registry your nodes pull from, and reuse them across runs.
icon: hammer
weight: 9
variants: -flyte +union
---

# Image builder

With the image builder, the SDK builds a task's container image inside your cluster instead of on the machine that runs `flyte run`. It runs a `build-image` task that sends the build to BuildKit and pushes the result to a registry. Before building, the SDK asks onebox whether the image already exists, so an image is built once and reused. You install BuildKit and the registry; onebox registers the `build-image` task itself. Onebox doesn't depend on any of them to start.

## Requirements

- **BuildKit**, reachable from task pods. BuildKit runs privileged, or rootless on kernels 5.11 and later.
- **A registry** that:
  - BuildKit can push to without credentials;
  - your nodes can pull from, at the same address BuildKit pushed to;
  - onebox can read anonymously, possibly at a different address.

  Registries that require credentials aren't supported.
- **Access to the build task's images.** The `build-image` task runs the `build-image` image and has BuildKit use the `frontend-v2` image, both published by Union at `public.ecr.aws/g1m2l3c1/imagebuilder-canary`, for amd64 and arm64. Nodes must be able to pull `build-image`, and BuildKit `frontend-v2`. Without internet access, copy both to a registry of yours, at the tag in the chart's `imageBuilder.taskImages.tag`, and point onebox at it:

  ```yaml
  imageBuilder:
    taskImages:
      repository: registry.example.com/imagebuilder   # holds build-image and frontend-v2
      tag: <tag>
  ```

  > [!NOTE] Canary images
  > Onebox currently uses Union's canary builds of these images, because the production builds (`imagebuilder`) don't include arm64 yet. A later chart switches to the production images. The tag names a single build, so the images don't change under you.

## Example: k3d

On a single-node k3d cluster, BuildKit and the kubelet both run on the node, so a registry exposed on a NodePort is `localhost:30500` to both, and containerd and BuildKit accept plain HTTP for `localhost`.

> [!WARNING] Local clusters only
> BuildKit here is privileged, on the node's network, and listening without TLS, and the registry accepts anonymous pushes. Anything that can reach them can run builds as root on the node or overwrite images. On a shared cluster, run BuildKit with mutual TLS (`--tlscacert`, `--tlscert`, `--tlskey`) or rootless, restrict access with a NetworkPolicy, and use a registry with TLS.

```yaml
# image-builder.yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: registry}
spec:
  selector: {matchLabels: {app: registry}}
  template:
    metadata: {labels: {app: registry}}
    spec:
      containers:
        - name: registry
          image: mirror.gcr.io/library/registry:2
          volumeMounts: [{name: data, mountPath: /var/lib/registry}]
      volumes: [{name: data, emptyDir: {}}]
---
apiVersion: v1
kind: Service
metadata: {name: registry}
spec:
  type: NodePort
  selector: {app: registry}
  ports: [{port: 5000, nodePort: 30500}]
---
apiVersion: apps/v1
kind: Deployment
metadata: {name: buildkit}
spec:
  selector: {matchLabels: {app: buildkit}}
  template:
    metadata: {labels: {app: buildkit}}
    spec:
      hostNetwork: true
      dnsPolicy: ClusterFirstWithHostNet
      containers:
        - name: buildkit
          image: moby/buildkit:buildx-stable-1
          args: [--addr, unix:///run/buildkit/buildkitd.sock, --addr, tcp://0.0.0.0:30234]
          securityContext: {privileged: true}
---
apiVersion: v1
kind: Service
metadata: {name: buildkit}
spec:
  selector: {app: buildkit}
  ports: [{port: 1234, targetPort: 30234}]
```

```shell
kubectl -n union apply -f image-builder.yaml
```

Turn the image builder on in onebox's values:

```yaml
imageBuilder:
  enabled: true
  buildkitURI: tcp://buildkit.union.svc:1234
  repository: localhost:30500/onebox                       # where nodes pull from
  lookupURL: http://registry.union.svc:5000/onebox         # where onebox checks
```

Onebox then creates the `system` project and registers the `build-image` task in its `production` domain, a few seconds after it starts. It registers the task again when `imageBuilder.taskImages` changes, or when an upgrade brings new images; otherwise there's nothing to do.

## Build an image

Use the remote builder for a run:

```shell
flyte --image-builder remote run my_task.py main
```

or set `image.builder: remote` in `.flyte/config.yaml`. The first run builds the image, which takes about half a minute for a small Python image, and later runs skip the build:

```text
i Image localhost:30500/onebox/my-image:3892709e... already exists, skipping build
```

## Gotchas

| Symptom | Cause and fix |
|---|---|
| `remote image builder is not enabled` | The `build-image` task isn't registered in `system`/`production` yet, or the CLI user can't read that project. Onebox registers it shortly after starting; while it can't, its log says `build-image task not registered yet` and why. |
| Builds fail with `exit code 255` while BuildKit loads the frontend | BuildKit can't run the `frontend-v2` image on its node's architecture. With a mirror, copy the image with all its architectures (for example `crane copy` or `docker buildx imagetools create`), not just one. |
| Every run rebuilds | Onebox can't read the registry at `imageBuilder.lookupURL`, or the path differs from `imageBuilder.repository`. They must name the same repository. |
| Task pods fail with `ErrImagePull` after a successful build | Nodes can't pull from `imageBuilder.repository`. It must resolve and be trusted from the node. |
