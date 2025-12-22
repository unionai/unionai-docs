---
title: Plugins
weight: 20
variants: +flyte +serverless +byoc +selfmanaged
---

# Task Plugins

Flyte tasks are pluggable by design, allowing you to extend task execution beyond simple containers to support specialized compute frameworks and integrations.

## Default Execution: Containers

By default, Flyte tasks execute as single containers in Kubernetes. When you decorate a function with `@env.task`, Flyte packages your code into a container and runs it on the cluster. For more advanced scenarios requiring multiple containers in a single pod (such as sidecars for logging or data mounting), you can use [pod templates](./pod-templates), which allow you to customize the entire Kubernetes pod specification.

## Compute Plugins

Beyond native container execution, Flyte provides **compute plugins** that enable you to run distributed computing frameworks directly on Kubernetes. These plugins create ephemeral clusters specifically for your task execution, spinning them up on-demand and tearing them down when complete.

### Available Compute Plugins

Flyte supports several popular distributed computing frameworks through compute plugins:

- **Spark**: Run Apache Spark jobs using the Spark operator
- **Ray**: Execute Ray workloads for distributed Python applications and ML training
- **Dask**: Scale Python workflows with Dask distributed
- **PyTorch**: Run distributed training jobs using PyTorch and Kubeflow's training operator

### How Compute Plugins Work

Compute plugins create temporary, isolated clusters within the same Kubernetes environment as Flyte:

1. **Ephemeral clusters**: Each task execution gets its own cluster, spun up on-demand
2. **Kubernetes operators**: Flyte leverages specialized Kubernetes operators (Spark operator, Ray operator, etc.) to manage cluster lifecycle
3. **Native containerization**: The same container image system used for regular tasks works seamlessly with compute plugins
4. **Per-environment configuration**: You can define the cluster shape (number of workers, resources, etc.) using `plugin_config` in your `TaskEnvironment`

### Using Compute Plugins

To use a compute plugin, you need to:

1. **Install the plugin package**: Each plugin has a corresponding Python package (e.g., `flyteplugins-ray` for Ray)
2. **Configure the TaskEnvironment**: Set the `plugin_config` parameter with the plugin-specific configuration
3. **Write your task**: Use the framework's native APIs within your task function

#### Example: Ray Plugin

Here's how to run a distributed Ray task:

```python
import ray
from flyteplugins.ray.task import HeadNodeConfig, RayJobConfig, WorkerNodeConfig
import flyte

# Define your Ray computation
@ray.remote
def compute_square(x):
    return x * x

# Configure the Ray cluster
ray_config = RayJobConfig(
    head_node_config=HeadNodeConfig(ray_start_params={"log-color": "True"}),
    worker_node_config=[WorkerNodeConfig(group_name="ray-workers", replicas=2)],
    runtime_env={"pip": ["numpy", "pandas"]},
    enable_autoscaling=False,
    shutdown_after_job_finishes=True,
    ttl_seconds_after_finished=300,
)

# Create a task environment with Ray plugin configuration
image = (
    flyte.Image.from_debian_base(name="ray")
    .with_pip_packages("ray[default]==2.46.0", "flyteplugins-ray")
)

ray_env = flyte.TaskEnvironment(
    name="ray_env",
    plugin_config=ray_config,
    image=image,
    resources=flyte.Resources(cpu=(3, 4), memory=("3000Mi", "5000Mi")),
)

# Use the Ray cluster in your task
@ray_env.task
async def distributed_compute(n: int = 10) -> list[int]:
    futures = [compute_square.remote(i) for i in range(n)]
    return ray.get(futures)
```

When this task runs, Flyte will:
1. Spin up a Ray cluster with 1 head node and 2 worker nodes
2. Execute your task code in the Ray cluster
3. Tear down the cluster after completion

### Using Plugins on Union

Most compute plugins are enabled by default on Union or can be enabled upon request. Contact your Account Manager to confirm plugin availability or request specific plugins for your deployment.

## Backend Integrations

Beyond compute plugins, Flyte also supports **integrations** with external SaaS services and internal systems through **connectors**. These allow you to seamlessly interact with:

- **Data warehouses**: Snowflake, BigQuery, Redshift
- **Data platforms**: Databricks
- **Custom services**: Your internal APIs and services

Connectors enable Flyte to delegate task execution to these external systems while maintaining Flyte's orchestration, observability, and data lineage capabilities. See the [connectors documentation](#) for more details on available integrations.

## Next Steps

For detailed guides on each compute plugin, including configuration options, best practices, and advanced examples, see the [Plugins section](#) of the documentation. Each plugin guide covers:

- Installation and setup
- Configuration options
- Resource management
- Advanced use cases
- Troubleshooting tips
