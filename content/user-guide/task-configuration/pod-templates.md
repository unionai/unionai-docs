---
title: Pod templates
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Pod templates

Flyte is built on Kubernetes and leverages its powerful container orchestration capabilities. A Kubernetes [pod](https://kubernetes.io/docs/concepts/workloads/pods/) is a group of one or more containers that share storage and network resources. While Flyte automatically runs your task code in a container, pod templates let you customize the entire pod specification for advanced use cases.

The `pod_template` parameter in `TaskEnvironment` allows you to:

- **Add sidecar containers**: Run metrics exporters, service proxies, or specialized services alongside your task
- **Mount volumes**: Attach persistent storage or cloud storage like GCS or S3
- **Configure metadata**: Set custom labels and annotations for monitoring, routing, or cluster policies
- **Manage resources**: Configure resource requests, limits, and affinities
- **Inject configuration**: Add secrets, environment variables, or config maps
- **Access private registries**: Specify image pull secrets

## How it works

When you define a pod template:

1. **Primary container**: Flyte automatically injects your task code into the container specified by `primary_container_name` (default: `"primary"`)
2. **Automatic monitoring**: Flyte watches the primary container and exits the entire pod when it completes
3. **Image handling**: The image for your task environment is built automatically by Flyte; images for sidecar containers must be provided by you
4. **Local execution**: When running locally, only the task code executes—additional containers are not started

## Requirements

To use pod templates, install the Kubernetes Python client:

```bash
pip install kubernetes
```

Or add it to your image dependencies:

```python
image = flyte.Image.from_debian_base().with_pip_packages("kubernetes")
```

## Basic usage

Here's a complete example showing how to configure labels, annotations, environment variables, and image pull secrets:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/pod-templates/pod_template.py" fragment="pod-template" lang="python" >}}

## PodTemplate parameters

The `PodTemplate` class provides the following parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `primary_container_name` | `str` | Name of the container where task code runs (default: `"primary"`). Must match a container in `pod_spec`. |
| `pod_spec` | `V1PodSpec` | Kubernetes pod specification for configuring containers, volumes, security contexts, and more. |
| `labels` | `dict[str, str]` | Pod labels for organization and selection by Kubernetes selectors. |
| `annotations` | `dict[str, str]` | Pod annotations for metadata and integrations (doesn't affect scheduling). |

## Volume mounts

Pod templates are commonly used to mount volumes for persistent storage or cloud storage access:

```python
from kubernetes.client import (
    V1Container,
    V1PodSpec,
    V1Volume,
    V1VolumeMount,
    V1CSIVolumeSource,
)
import flyte

pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    pod_spec=V1PodSpec(
        containers=[
            V1Container(
                name="primary",
                volume_mounts=[
                    V1VolumeMount(
                        name="data-volume",
                        mount_path="/mnt/data",
                        read_only=False,
                    )
                ],
            )
        ],
        volumes=[
            V1Volume(
                name="data-volume",
                csi=V1CSIVolumeSource(
                    driver="your-csi-driver",
                    volume_attributes={"key": "value"},
                ),
            )
        ],
    ),
)

env = flyte.TaskEnvironment(
    name="volume-example",
    pod_template=pod_template,
    image=flyte.Image.from_debian_base(),
)

@env.task
async def process_data() -> str:
    # Access mounted volume
    with open("/mnt/data/input.txt", "r") as f:
        data = f.read()
    return f"Processed {len(data)} bytes"
```

### GCS/S3 volume mounts

Mount cloud storage directly into your pod for efficient data access:

```python
from kubernetes.client import V1Container, V1PodSpec, V1Volume, V1VolumeMount, V1CSIVolumeSource
import flyte

# GCS example with CSI driver
pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    annotations={
        "gke-gcsfuse/volumes": "true",
        "gke-gcsfuse/cpu-limit": "2",
        "gke-gcsfuse/memory-limit": "1Gi",
    },
    pod_spec=V1PodSpec(
        containers=[
            V1Container(
                name="primary",
                volume_mounts=[V1VolumeMount(name="gcs", mount_path="/mnt/gcs")],
            )
        ],
        volumes=[
            V1Volume(
                name="gcs",
                csi=V1CSIVolumeSource(
                    driver="gcsfuse.csi.storage.gke.io",
                    volume_attributes={"bucketName": "my-bucket"},
                ),
            )
        ],
    ),
)
```

## Sidecar containers

Add sidecar containers to run alongside your task. Common use cases include:

- **Metrics exporters**: Prometheus, Datadog agents
- **Service proxies**: Istio, Linkerd sidecars
- **Data services**: Databases, caches, or specialized services like Nvidia NIMs

```python
from kubernetes.client import V1Container, V1PodSpec
import flyte

pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    pod_spec=V1PodSpec(
        containers=[
            # Primary container (where your task code runs)
            V1Container(name="primary"),

            # Sidecar container
            V1Container(
                name="metrics-sidecar",
                image="prom/pushgateway:latest",
                ports=[{"containerPort": 9091}],
            ),
        ],
    ),
)

env = flyte.TaskEnvironment(
    name="sidecar-example",
    pod_template=pod_template,
    image=flyte.Image.from_debian_base().with_pip_packages("requests"),
)

@env.task
async def task_with_metrics() -> str:
    import requests

    # Send metrics to sidecar
    requests.post("http://localhost:9091/metrics", data="my_metric 42")

    # Your task logic
    return "Task completed with metrics"
```

## Image pull secrets

Configure private registry access:

```python
from kubernetes.client import V1Container, V1PodSpec, V1LocalObjectReference
import flyte

pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    pod_spec=V1PodSpec(
        containers=[V1Container(name="primary")],
        image_pull_secrets=[V1LocalObjectReference(name="my-registry-secret")],
    ),
)
```

## Cluster-specific configuration

Pod templates are often used to configure Kubernetes-specific settings required by your cluster, even when not using multiple containers:

```python
import flyte

pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    annotations={
        "iam.amazonaws.com/role": "my-task-role",  # AWS IAM role
        "cluster-autoscaler.kubernetes.io/safe-to-evict": "false",
    },
    labels={
        "cost-center": "ml-team",
        "project": "recommendations",
    },
)
```

## Important notes

1. **Local execution**: Pod templates only apply to remote execution. When running locally, only your task code executes.

2. **Image building**: Flyte automatically builds and manages the image for your task environment. Images for sidecar containers must be pre-built and available in a registry.

3. **Primary container**: Your task code is automatically injected into the container matching `primary_container_name`. This container must be defined in the `pod_spec.containers` list.

4. **Lifecycle management**: Flyte monitors the primary container and terminates the entire pod when it exits, ensuring sidecar containers don't run indefinitely.

## Best practices

1. **Start simple**: Begin with basic labels and annotations before adding complex sidecars
2. **Test locally first**: Verify your task logic works locally before adding pod customizations
3. **Use environment-specific templates**: Different environments (dev, staging, prod) may need different pod configurations
4. **Set resource limits**: Always set resource requests and limits for sidecars to prevent cluster issues
5. **Security**: Use image pull secrets and least-privilege service accounts

## Learn more

- [Kubernetes Pods Documentation](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Kubernetes Python Client](https://github.com/kubernetes-client/python)
- [V1PodSpec Reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#podspec-v1-core)
