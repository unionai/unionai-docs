---
title: Extending tasks with K8s PodTemplates
weight: 110
variants: +flyte +serverless +byoc +selfmanaged
---

Flyte is built on Kubernetes and leverages its powerful container orchestration capabilities. One of the key features is the ability to use Kubernetes pods, which can run multiple containers in an isolated group. Pod templates allow you to customize how your tasks run on Kubernetes, enabling advanced use cases like sidecars, volume mounts, and cluster-specific configurations.

## What are Pod Templates?

A Kubernetes [pod](https://kubernetes.io/docs/concepts/workloads/pods/) is a group of one or more containers that share storage and network resources. While Flyte automatically runs your task code in a container, pod templates let you customize the entire pod specification, including:

- **Multiple containers**: Add sidecar containers for metrics, logging, data mounting, or specialized services
- **Volume mounts**: Attach persistent storage or mount cloud storage like GCS or S3
- **Labels and annotations**: Add Kubernetes metadata for monitoring, routing, or cluster policies
- **Resource management**: Configure resource requests, limits, and affinities
- **Secrets and config**: Inject secrets, environment variables, or config maps

## How It Works

When you define a pod template:

1. **Primary container**: Flyte automatically injects your task code into the container specified by `primary_container_name` (default: `"primary"`)
2. **Automatic monitoring**: Flyte watches the primary container and exits the entire pod when it completes
3. **Image handling**:
   - The image for your task environment is built automatically by Flyte
   - Images for other containers (sidecars) must be provided by you
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

## Basic Pod Template

Here's a simple example showing how to add labels, annotations, and environment variables:

```python
from kubernetes.client import V1Container, V1EnvVar, V1PodSpec
import flyte

# Define the pod template
pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    labels={"team": "ml-platform", "environment": "production"},
    annotations={"monitoring": "enabled"},
    pod_spec=V1PodSpec(
        containers=[
            V1Container(
                name="primary",
                env=[V1EnvVar(name="LOG_LEVEL", value="INFO")]
            )
        ],
    ),
)

# Use the pod template in your task environment
env = flyte.TaskEnvironment(
    name="my-env",
    pod_template=pod_template,
    image=flyte.Image.from_debian_base(),
)

@env.task
async def my_task(data: str) -> str:
    return f"Processed {data}"
```

## Volume Mounts

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

## Sidecar Containers

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

## Image Pull Secrets

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

## Common Use Cases

### Cluster-Specific Configuration

Often, pod templates are used to configure Kubernetes-specific settings required by your cluster, even when not using multiple containers:

```python
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

### GCS/S3 Volume Mounts

Mount cloud storage directly into your pod for efficient data access:

```python
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

### Specialized Sidecars

Run specialized services like Nvidia NIMs or other pre-built containers:

```python
pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    pod_spec=V1PodSpec(
        containers=[
            V1Container(name="primary"),
            V1Container(
                name="nvidia-nim",
                image="nvcr.io/nvidia/nim:latest",
                # Configure as needed
            ),
        ],
    ),
)
```

## PodTemplate Structure

The `flyte.PodTemplate` class accepts:

| Parameter | Type | Description |
|-----------|------|-------------|
| `pod_spec` | `V1PodSpec` | Kubernetes pod specification |
| `primary_container_name` | `str` | Name of the container where task code runs (default: `"primary"`) |
| `labels` | `dict[str, str]` | Pod labels for organization and selection |
| `annotations` | `dict[str, str]` | Pod annotations for metadata and integrations |

## Important Notes

1. **Local execution**: Pod templates only apply to remote execution. When running locally (`mode="local"`), only your task code executes.

2. **Image building**:
   - Flyte automatically builds and manages the image for your task environment
   - Images for sidecar containers must be pre-built and available in a registry

3. **Primary container**: Your task code is automatically injected into the container with `primary_container_name`. This container must be defined in the `pod_spec.containers` list.

4. **Lifecycle management**: Flyte monitors the primary container and terminates the entire pod when it exits, ensuring sidecar containers don't run indefinitely.

5. **Kubernetes knowledge**: While Flyte simplifies pod configuration, understanding [Kubernetes pod concepts](https://kubernetes.io/docs/concepts/workloads/pods/) is helpful for advanced use cases.

## Best Practices

1. **Start simple**: Begin with basic labels and annotations before adding complex sidecars
2. **Test locally first**: Verify your task logic works locally before adding pod customizations
3. **Use env-specific templates**: Different environments (dev, staging, prod) may need different pod configurations
4. **Resource limits**: Always set resource requests and limits for sidecars to prevent cluster issues
5. **Security**: Use image pull secrets and least-privilege service accounts

## Learn More

- [Kubernetes Pods Documentation](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Kubernetes Python Client](https://github.com/kubernetes-client/python)
- [V1PodSpec Reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#podspec-v1-core)

