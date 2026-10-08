---
title: Image builder
description: Build task images inside your cluster with BuildKit, push them to a registry your nodes pull from, and reuse them across runs.
icon: hammer
weight: 9
variants: -flyte +union
---

# Image builder

With the image builder, the SDK builds a task's container image inside your cluster instead of on the machine that runs `flyte run`. It runs a `build-image` task that sends the build to BuildKit and pushes the result to a registry. Before building, the SDK asks onebox whether the image already exists, so an image is built once and reused. BuildKit, the registry, and the build task are installed separately; onebox doesn't depend on them to start.

## Requirements

- **BuildKit**, reachable from task pods. BuildKit runs privileged, or rootless on kernels 5.11 and later.
- **A registry** that:
  - BuildKit can push to without credentials;
  - your nodes can pull from, at the same address BuildKit pushed to;
  - onebox can read anonymously, possibly at a different address.

  Registries that require credentials aren't supported.
- **The `build-image` task**, deployed once into the `system` project's `production` domain. It runs the `build-image` image and uses the `frontend-v2` BuildKit frontend image, both from the Union image builder. The frontend image must be in a registry BuildKit can pull from.

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

Turn the image builder on in onebox's values, and add the `system` project:

```yaml
imageBuilder:
  enabled: true
  buildkitURI: tcp://buildkit.union.svc:1234
  repository: localhost:30500/onebox                       # where nodes pull from
  lookupURL: http://registry.union.svc:5000/onebox         # where onebox checks
seedProjects: [default, system]
```

Then push the `build-image` and `frontend-v2` images to the registry, and deploy the build task with the `imagebuild/flyte/build_image_task_cloud_v2.py` definition, pointing it at those images:

```shell
UNION_IMAGE_NAME_PREFIX=localhost:30500/onebox-system UNION_IMAGE_TAG=<tag> \
  flyte deploy --project system --domain production --version <tag> \
  build_image_task_cloud_v2.py build_image_task_env
```

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
| `remote image builder is not enabled` | The `build-image` task isn't deployed in `system`/`production`, or the CLI user can't read that project. |
| Every run rebuilds | Onebox can't read the registry at `imageBuilder.lookupURL`, or the path differs from `imageBuilder.repository`. They must name the same repository. |
| Task pods fail with `ErrImagePull` after a successful build | Nodes can't pull from `imageBuilder.repository`. It must resolve and be trusted from the node. |
