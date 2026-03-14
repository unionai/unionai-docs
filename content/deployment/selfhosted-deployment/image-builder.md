---
title: Image builder
weight: 5
variants: -flyte -serverless -byoc +selfmanaged
---

# Image builder

The image builder enables {{< key product_name >}} to automatically build container images for your tasks when using the `flyte.Image` API. In self-hosted deployments, the image builder requires a one-time registration step after initial deployment.

## Prerequisites

- A running self-hosted deployment with both control plane and data plane healthy
- The `flyte` CLI installed (`pip install flyte` or `uv pip install flyte`)
- CLI access configured for your self-hosted environment (see [Authentication](./authentication))
- Image builder enabled in your data plane Helm values (`imageBuilder.enabled: true`)
- An account with permission to register tasks in the `system` project

## Register the build-image task

The `build-image` task must be registered in the `system/production` project before users can build images. This step must be repeated each time you upgrade to a new {{< key product_name >}} version.

### Step 1: Determine your appVersion

Find the `appVersion` from your deployed controlplane Helm chart:

```shell
helm list -n <controlplane-namespace> -o json | jq '.[0].app_version'
```

Or check the chart directly:

```shell
grep appVersion charts/controlplane/Chart.yaml
```

This returns a version like `2026.3.4`.

### Step 2: Register the task

From the root of the `cloud` repository, run:

```shell
UNION_IMAGE_NAME_PREFIX=public.ecr.aws/g1m2l3c1/imagebuilder \
UNION_IMAGE_TAG=<APP_VERSION> \
uv run flyte --config <your-config.yaml> deploy \
  --version "<APP_VERSION>" \
  --project system --domain production \
  imagebuild/flyte/build_image_task_cloud_v2.py build_image_task_env
```

Replace:
- `<APP_VERSION>` with the appVersion from Step 1 (e.g. `2026.3.4`)
- `<your-config.yaml>` with the path to your CLI config file

> [!NOTE]
> For staging environments, use the prefix `public.ecr.aws/g1m2l3c1/imagebuilder-staging` instead.

### Step 3: Verify

Confirm the task is registered:

```shell
uctl get task -p system -d production
```

You should see `build-image` listed.

## Updating

When you upgrade your self-hosted deployment to a new appVersion, repeat the registration steps with the new version. The SDK always uses the latest registered version.

## Troubleshooting

### "remote image builder is not enabled"

This error from the SDK means the `build-image` task is not registered in `system/production`. Follow the registration steps above.

### Build task fails with permission errors

Ensure the worker IAM role has permissions to push images to the container registry configured in your data plane Helm values (`imageBuilder.defaultRepository`).
