---
title: Image builder
weight: 8
variants: -flyte +union
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

### Step 2: Create the task definition file

Create a file named `build_image_task.py` with the following contents:

```python
import os

from kubernetes.client import (
    V1PodSpec,
    V1Container,
    V1EnvVar,
    V1VolumeMount,
    V1EnvVarSource,
    V1ObjectFieldSelector,
    V1ConfigMapKeySelector,
    V1Volume,
    V1ProjectedVolumeSource,
    V1VolumeProjection,
    V1ServiceAccountTokenProjection,
    V1ConfigMapVolumeSource,
    V1KeyToPath,
)

import flyte
from flyte.extras import ContainerTask


# Statically assigned name intended to match Union operator static name.
_DEFAULT_CONFIGMAP_NAME = "build-image-config"
_STORAGE_YAML_KEY = "storage.yaml"
_CONFIG_DIR = "/etc/union/config"

# The config map storing build image configuration.
config_map_name = os.getenv("CONFIG_MAP_NAME", _DEFAULT_CONFIGMAP_NAME)

log_level = os.getenv("LOG_LEVEL", "5")  # Default to Warn

union_image_name_prefix = "public.ecr.aws/g1m2l3c1/imagebuilder-staging"

app_version = os.getenv("APP_VERSION", None)
if app_version is None:
    raise ValueError("APP_VERSION environment variable must be set")

build_image_task = ContainerTask(
    name="build-image",
    cache=flyte.Cache(behavior="auto"),
    image=f"{union_image_name_prefix}/build-image:{app_version}",
    inputs={"spec": str, "context": str, "target_image": str},
    outputs={"fully_qualified_image": str},
    pod_template=flyte.PodTemplate(
        primary_container_name="main",
        pod_spec=V1PodSpec(
            containers=[
                V1Container(
                    name="main",
                    image_pull_policy="Always",
                    termination_message_policy="FallbackToLogsOnError",
                    volume_mounts=[
                        V1VolumeMount(
                            mount_path="/var/run/secrets/union/registry",
                            name="registry-token",
                            read_only=True,
                        ),
                        V1VolumeMount(
                            name="config-volume",
                            mount_path=f"{_CONFIG_DIR}/{_STORAGE_YAML_KEY}",
                            sub_path=_STORAGE_YAML_KEY,
                        ),
                    ],
                    env=[
                        V1EnvVar(
                            name="ORGANIZATION",
                            value_from=V1EnvVarSource(
                                field_ref=V1ObjectFieldSelector(
                                    field_path="metadata.labels['organization']"
                                )
                            ),
                        ),
                        V1EnvVar(
                            name="UNION_BUILDKIT_URI",
                            value_from=V1EnvVarSource(
                                config_map_key_ref=V1ConfigMapKeySelector(
                                    name=config_map_name,
                                    key="buildkit-uri",
                                )
                            ),
                        ),
                        V1EnvVar(
                            name="UNION_DEFAULT_REPOSITORY",
                            value_from=V1EnvVarSource(
                                config_map_key_ref=V1ConfigMapKeySelector(
                                    name=config_map_name,
                                    key="default-repository",
                                )
                            ),
                        ),
                        V1EnvVar(
                            name="UNION_REGISTRY_AUTHENTICATION_TYPE",
                            value_from=V1EnvVarSource(
                                config_map_key_ref=V1ConfigMapKeySelector(
                                    name=config_map_name,
                                    key="authentication-type",
                                )
                            ),
                        ),
                        V1EnvVar(
                            name="UNION_IMAGE_NAME_PREFIX",
                            value=union_image_name_prefix,
                        ),
                        V1EnvVar(
                            name="FLYTE_INTERNAL_OPTIMIZE_IMAGE",
                            value_from=V1EnvVarSource(
                                config_map_key_ref=V1ConfigMapKeySelector(
                                    name=config_map_name,
                                    key="enable-image-optimization",
                                    optional=True,
                                )
                            ),
                        ),
                    ],
                ),
            ],
            volumes=[
                V1Volume(
                    name="registry-token",
                    projected=V1ProjectedVolumeSource(
                        sources=[
                            V1VolumeProjection(
                                service_account_token=V1ServiceAccountTokenProjection(
                                    audience="registry",
                                    expiration_seconds=7200,
                                    path="token",
                                )
                            )
                        ]
                    ),
                ),
                V1Volume(
                    name="config-volume",
                    config_map=V1ConfigMapVolumeSource(
                        name=config_map_name,
                        items=[
                            V1KeyToPath(
                                key=_STORAGE_YAML_KEY,
                                path=_STORAGE_YAML_KEY,
                            )
                        ],
                    ),
                ),
            ],
        ),
    ),
    command=[
        "imagebuild",
        "--logger.formatter.type=text",
        f"--logger.level={log_level}",
        "--context",
        "{{.inputs.context}}",
        "--frontend",
        f"{union_image_name_prefix}/frontend-v2:{app_version}",
        "--remote-outputs-prefix",
        "{{.outputPrefix}}",
        "--spec",
        "{{.inputs.spec}}",
        "--target-image",
        "{{.inputs.target_image}}",
        "--optimize",
    ],
)

build_image_task_env = flyte.TaskEnvironment.from_task(
    "build_image_task", build_image_task
)
```

### Step 3: Register the task

From the directory containing `build_image_task.py`, run:

```shell
APP_VERSION=<APP_VERSION> \
uv run flyte --config <your-config.yaml> deploy \
  --version "<APP_VERSION>" \
  --project system --domain production \
  build_image_task.py build_image_task_env
```

Replace:
- `<APP_VERSION>` with the appVersion from Step 1 (e.g. `2026.3.4`)
- `<your-config.yaml>` with the path to your CLI config file

### Step 4: Verify

Confirm the task is registered:

```shell
flyte --config <your-config.yaml> get task -p system -d production
```

You should see `build-image` listed.

## Updating

When you upgrade your self-hosted deployment to a new appVersion, repeat the registration steps with the new version. The SDK always uses the latest registered version.

## Restricted network environments

If your buildkit pods do not have egress to public container registries or the internet (e.g. due to network policies, firewall rules, or air-gapped infrastructure), additional configuration is required.

### Container image access

The image builder needs to pull three images during a build:

| Image | Purpose | Default source |
|-------|---------|---------------|
| `frontend-v2` | Buildkit gateway frontend | `public.ecr.aws/...` (Union) |
| `build-image` | Build task executor | `public.ecr.aws/...` (Union) |
| Base image (e.g. `python:3.12-slim`) | User's base image | Docker Hub or custom registry |

If buildkit cannot reach public registries, you must mirror these images to an internal registry that buildkit can access. Update the `union_image_name_prefix` in your `build_image_task.py` to point to your internal registry, and use `Image.from_base()` with an image URI from your internal registry.

> [!NOTE]
> Starting with version `2026.3.7`, the `uv` package manager binary is baked into the `frontend-v2` image. Previous versions pulled `ghcr.io/astral-sh/uv` as a separate image during builds, which required additional mirroring.

### Python version constraints

When using a custom base image via `Image.from_base()`, the Python version in your base image must match the Python version in your image specification. The image builder does not download Python interpreters from the internet — it uses only the Python already installed in the base image.

If there is a version mismatch, the build will fail with:

```
error: No interpreter found for Python 3.13 in managed installations or search path
hint: A managed Python download is available for Python 3.13, but Python downloads are set to 'never'
```

To resolve this, ensure your `python_version` matches what is installed in your base image:

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

The image builder runs `pip install` or `uv pip install` to install Python packages during builds. If your buildkit pods cannot reach `pypi.org`, you must configure a private package index. You can do this by including a `pip.conf` or setting the `PIP_INDEX_URL` environment variable in your base image:

```dockerfile
# In your custom base image Dockerfile
ENV PIP_INDEX_URL=https://your-artifactory.example.com/api/pypi/pypi-remote/simple
ENV PIP_TRUSTED_HOST=your-artifactory.example.com
```

## Troubleshooting

### "remote image builder is not enabled"

This error from the SDK means the `build-image` task is not registered in `system/production`. Follow the registration steps above.

### Build task fails with permission errors

Ensure the worker IAM role has permissions to push images to the container registry configured in your data plane Helm values (`imageBuilder.defaultRepository`).
