---
title: Image builder
weight: 5
variants: -flyte +union
---

# Image builder

The image builder lets {{< key product_name >}} automatically build container images for your tasks when you use the `flyte.Image` API. In self-hosted deployments, the controlplane Helm chart registers the required `build-image` task automatically as part of `helm install` / `helm upgrade` — operators don't need to run anything by hand for the common case.

> [!NOTE]
> Chart-side auto-registration is available **as of helm-charts `2026.7.8`**. On older chart versions, operators must run `flyte deploy ... build_image_task.py` after each `helm upgrade` — see [Manual registration](#manual-registration).

## How it works

When you install or upgrade the controlplane chart, a post-install Helm hook Job runs in the controlplane namespace and:

1. Ensures the `system` project exists.
2. Registers the `build-image` task in `system/production` at the chart's `appVersion`.

The Job pins the task version to the chart's `appVersion`, so every `helm upgrade` re-registers `build-image` with task images matching the deployed chart. The hook Job auto-deletes after a successful run (`helm.sh/hook-delete-policy: hook-succeeded`); the underlying `build-image` task definition remains in flyteadmin.

## Prerequisites

- A running self-hosted deployment with control plane and data plane healthy.
- Image builder enabled in your data plane Helm values (`imageBuilder.enabled: true`).
- (Optional, only if changing defaults) The controlplane chart values described in [Configuration](#configuration) below.

## Configuration

The controlplane chart exposes the bootstrap behavior under `imageBuilder.bootstrap`:

```yaml
imageBuilder:
  bootstrap:
    enabled: true                                       # set to false to disable auto-registration
    image: python:3.13-slim                              # container the hook Job runs in
    unionImageNamePrefix: public.ecr.aws/g1m2l3c1/imagebuilder-staging
    project: system                                      # target project for the task
    domain: production                                   # target domain
    clientSecretName: service-shared-secret              # K8s Secret holding `client_secret`
```

Defaults are correct for stock {{< key product_name >}} deployments. Customize when:

- **Mirroring images to a private registry** — set `unionImageNamePrefix` to your mirror (see [Restricted network environments](#restricted-network-environments)).
- **Managing `build-image` registration yourself** — set `enabled: false` and follow [Manual registration](#manual-registration).
- **Non-default secret name** — point `clientSecretName` at the Secret holding the `INTERNAL_CLIENT_ID`'s `client_secret` value.

## Verify

After install/upgrade, confirm the task is registered:

```shell
flyte --config <your-config.yaml> get task -p system -d production
```

You should see `build-image` listed at the chart's `appVersion`.

## Restricted network environments

If your buildkit pods do not have egress to public container registries or the internet (network policies, firewall rules, air-gapped infrastructure), additional configuration is required.

### Container image access

The image builder needs to pull three images during a build:

| Image | Purpose | Default source |
|-------|---------|---------------|
| `frontend-v2` | Buildkit gateway frontend | `public.ecr.aws/...` (Union) |
| `build-image` | Build task executor | `public.ecr.aws/...` (Union) |
| Base image (e.g. `python:3.12-slim`) | User's base image | Docker Hub or custom registry |

If buildkit cannot reach public registries, mirror these images to an internal registry that buildkit can access. Then set `imageBuilder.bootstrap.unionImageNamePrefix` in your controlplane Helm values to point at your mirror, and use `Image.from_base()` with an image URI from your internal registry.

> [!NOTE]
> Starting with version `2026.3.7`, the `uv` package manager binary is baked into the `frontend-v2` image. Previous versions pulled `ghcr.io/astral-sh/uv` as a separate image during builds, which required additional mirroring.

### Python version constraints

When using a custom base image via `Image.from_base()`, the Python version in your base image must match the Python version in your image specification. The image builder does not download Python interpreters from the internet — it uses only the Python already installed in the base image.

If there is a version mismatch, the build will fail with:

```
error: No interpreter found for Python 3.13 in managed installations or search path
hint: A managed Python download is available for Python 3.13, but Python downloads are set to 'never'
```

To resolve, ensure your `python_version` matches what is installed in your base image:

```python
# Base image has Python 3.12 installed
image = Image.from_base("your-registry.example.com/python:3.12-slim")
```

### AWS VPC endpoints

For AWS deployments where pods cannot reach public endpoints, configure VPC interface endpoints for ECR so that buildkit can push and pull images through private network paths:

- `com.amazonaws.<region>.ecr.api` — ECR API (authentication, image metadata)
- `com.amazonaws.<region>.ecr.dkr` — ECR Docker registry (image push/pull)
- `com.amazonaws.<region>.s3` — S3 Gateway endpoint (ECR stores image layers in S3)

The ECR interface endpoints must have private DNS enabled and a security group that allows inbound traffic from the VPC CIDR blocks (including any secondary CIDRs used by EKS pod networking).

### Package index access

The image builder runs `pip install` or `uv pip install` to install Python packages during builds. If your buildkit pods cannot reach `pypi.org`, configure a private package index by including a `pip.conf` or setting the `PIP_INDEX_URL` environment variable in your base image:

```dockerfile
# In your custom base image Dockerfile
ENV PIP_INDEX_URL=https://your-artifactory.example.com/api/pypi/pypi-remote/simple
ENV PIP_TRUSTED_HOST=your-artifactory.example.com
```

## Manual registration

Set `imageBuilder.bootstrap.enabled: false` in the controlplane chart values to disable the automated registration. You then take ownership of registering `build-image` yourself.

The task definition is published in the chart at `charts/controlplane/files/build_image_task.py`. To register it manually:

```shell
APP_VERSION=$(helm list -n <controlplane-namespace> --filter '^unionai-controlplane$' -o json | jq -r '.[0].app_version')

UNION_IMAGE_NAME_PREFIX=public.ecr.aws/g1m2l3c1/imagebuilder-staging \
APP_VERSION="${APP_VERSION}" \
uv run flyte --config <your-config.yaml> deploy \
  --version "${APP_VERSION}" \
  --project system --domain production \
  build_image_task.py build_image_task_env
```

Repeat after every `helm upgrade` so the registered task tracks the deployed `appVersion`. (Or leave `bootstrap.enabled: true` and let the chart do it.)

## Troubleshooting

### "remote image builder is not enabled"

This error from the SDK means the `build-image` task is not registered in `system/production`. Check whether the bootstrap Job ran:

```shell
kubectl -n <controlplane-namespace> logs job/<release-name>-bootstrap-build-image
```

The Job auto-deletes on success; if you see no Job at all and `flyte get task -p system -d production` doesn't list `build-image`, force a re-run via `helm upgrade --reuse-values` or sync the controlplane Application in ArgoCD.

If `bootstrap.enabled: false`, see [Manual registration](#manual-registration).

### Build task fails with permission errors

Ensure the worker IAM role has permissions to push images to the container registry configured in your data plane Helm values (`imageBuilder.defaultRepository`). See [Infrastructure requirements → Identity and workload binding](./infrastructure-requirements#identity-and-workload-binding) for the per-cloud IAM tables.
