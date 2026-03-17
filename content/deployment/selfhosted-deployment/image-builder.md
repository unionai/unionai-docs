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

union_image_name_prefix = os.getenv("UNION_IMAGE_NAME_PREFIX", None)
if union_image_name_prefix is None:
    raise ValueError("UNION_IMAGE_NAME_PREFIX environment variable must be set")

union_image_tag = os.getenv("UNION_IMAGE_TAG", None)
if union_image_tag is None:
    raise ValueError("UNION_IMAGE_TAG environment variable must be set")

build_image_task = ContainerTask(
    name="build-image",
    cache=flyte.Cache(behavior="auto"),
    image=f"{union_image_name_prefix}/build-image:{union_image_tag}",
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
        f"{union_image_name_prefix}/frontend-v2:{union_image_tag}",
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
UNION_IMAGE_NAME_PREFIX=public.ecr.aws/g1m2l3c1/imagebuilder \
UNION_IMAGE_TAG=<APP_VERSION> \
uv run flyte --config <your-config.yaml> deploy \
  --version "<APP_VERSION>" \
  --project system --domain production \
  build_image_task.py build_image_task_env
```

Replace:
- `<APP_VERSION>` with the appVersion from Step 1 (e.g. `2026.3.4`)
- `<your-config.yaml>` with the path to your CLI config file

> [!NOTE]
> For staging environments, use the prefix `public.ecr.aws/g1m2l3c1/imagebuilder-staging` instead.

### Step 4: Verify

Confirm the task is registered:

```shell
flyte --config <your-config.yaml> get task -p system -d production
```

You should see `build-image` listed.

## Updating

When you upgrade your self-hosted deployment to a new appVersion, repeat the registration steps with the new version. The SDK always uses the latest registered version.

## Troubleshooting

### "remote image builder is not enabled"

This error from the SDK means the `build-image` task is not registered in `system/production`. Follow the registration steps above.

### Build task fails with permission errors

Ensure the worker IAM role has permissions to push images to the container registry configured in your data plane Helm values (`imageBuilder.defaultRepository`).
