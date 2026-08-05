---
title: Ray
weight: 1
variants: +flyte +union
---

# Ray

The Ray plugin lets you run [Ray](https://www.ray.io/) jobs natively on Kubernetes. Flyte provisions a transient Ray cluster for each task execution using [KubeRay](https://github.com/ray-project/kuberay) and tears it down on completion.

## When to use this plugin

- Distributed Python workloads (parallel computation, data processing)
- ML training with Ray Train or hyperparameter tuning with Ray Tune
- Ray Serve inference workloads
- Any workload that benefits from Ray's actor model or task parallelism

## Installation

```bash
pip install flyteplugins-ray
```

Your task image must also include a compatible version of Ray:

```python
image = (
    flyte.Image.from_debian_base(name="ray")
    .with_pip_packages("ray[default]==2.46.0", "flyteplugins-ray")
)
```

{{< variant union >}}
> [!NOTE]
For self-managed setups, refer to the [setup instructions](../../deployment/selfmanaged//configuration/plugins#ray) to enable the Ray plugin in your data plane.
{{< /variant >}}

## Configuration

Create a `RayJobConfig` and pass it as `plugin_config` to a `TaskEnvironment`:

```python
from flyteplugins.ray import HeadNodeConfig, RayJobConfig, WorkerNodeConfig

ray_config = RayJobConfig(
    head_node_config=HeadNodeConfig(ray_start_params={"log-color": "True"}),
    worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=2)],
    runtime_env={"pip": ["numpy", "pandas"]},
    enable_autoscaling=False,
    shutdown_after_job_finishes=True,
    ttl_seconds_after_finished=300,
)

ray_env = flyte.TaskEnvironment(
    name="ray_env",
    plugin_config=ray_config,
    image=image,
)
```

### `RayJobConfig` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `worker_node_config` | `List[WorkerNodeConfig]` | **Required.** List of worker group configurations |
| `head_node_config` | `HeadNodeConfig` | Head node configuration (optional) |
| `enable_autoscaling` | `bool` | Enable Ray autoscaler (default: `False`) |
| `runtime_env` | `dict` | Ray runtime environment (pip packages, env vars, etc.) |
| `address` | `str` | Connect to an existing Ray cluster instead of provisioning one |
| `shutdown_after_job_finishes` | `bool` | Shut down the cluster after the job completes (default: `False`) |
| `ttl_seconds_after_finished` | `int` | Seconds to keep the cluster after completion before cleanup |

### `WorkerNodeConfig` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `group_name` | `str` | **Required.** Name of this worker group |
| `replicas` | `int` | **Required.** Number of worker replicas |
| `min_replicas` | `int` | Minimum replicas (for autoscaling) |
| `max_replicas` | `int` | Maximum replicas (for autoscaling) |
| `ray_start_params` | `Dict[str, str]` | Ray start parameters for workers |
| `requests` | `Resources` | Resource requests per worker |
| `limits` | `Resources` | Resource limits per worker |
| `pod_template` | `PodTemplate` | Full pod template (mutually exclusive with `requests`/`limits`) |

### `HeadNodeConfig` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ray_start_params` | `Dict[str, str]` | Ray start parameters for the head node |
| `requests` | `Resources` | Resource requests for the head node |
| `limits` | `Resources` | Resource limits for the head node |
| `pod_template` | `PodTemplate` | Full pod template (mutually exclusive with `requests`/`limits`) |

### Connecting to an existing cluster

To connect to an existing Ray cluster instead of provisioning a new one, set the `address` parameter:

```python
ray_config = RayJobConfig(
    worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=2)],
    address="ray://existing-cluster:10001",
)
```

{{< variant union >}}

## Reusable Ray clusters

By default, every Ray task pays the full cluster cold-start cost: a new Ray cluster is provisioned for the task and torn down when it finishes. If your workload runs many Ray jobs with the same cluster configuration, you can instead share one long-lived Ray cluster across tasks by attaching a `flyte.ReusePolicy` (see [Reusable containers](../../user-guide/tasks/task-configuration/reusable-containers)) to the Ray `TaskEnvironment`:

```python
import flyte
from flyteplugins.ray import HeadNodeConfig, RayJobConfig, WorkerNodeConfig

ray_env = flyte.TaskEnvironment(
    name="ray_env",
    plugin_config=RayJobConfig(
        head_node_config=HeadNodeConfig(),
        worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=2)],
    ),
    image=image,
    reusable=flyte.ReusePolicy(
        replicas=1,     # one shared Ray cluster
        idle_ttl=300,   # tear the cluster down after 5 minutes of inactivity
        scope="global",  # share across all runs (see below)
    ),
)
```

The first task creates the shared cluster; once it is ready, every subsequent task with the same environment submits its Ray job directly to it, skipping cluster startup entirely. Each job still runs and reports under its own run identity.

The cluster's identity is derived from the task environment: its name, the Ray configuration, the container image and resources, any pod template, and the reuse policy itself. Tasks with an identical environment share one cluster; changing any of these (for example deploying a new image or code version) creates a fresh cluster rather than reusing a stale one.

### Reuse scope

The `scope` parameter controls how widely the shared cluster is reused:

| Scope | Behavior |
|-------|----------|
| `"global"` (default) | One cluster is shared by every run whose tasks use the same environment. The cluster survives across runs until it has been idle for `idle_ttl`. |
| `"run"` | Reuse is restricted to a single run: each run gets its own shared cluster, and tasks within that run share it. |

```python
# Each run gets its own Ray cluster, shared by the tasks in that run.
reusable = flyte.ReusePolicy(replicas=1, idle_ttl=300, scope="run")
```

### Cleanup

A shared cluster is never deleted when an individual task completes or is aborted — it is shut down automatically after it has been idle (no jobs running against it) for `idle_ttl`.

### Constraints

- `replicas` must be exactly `1` — one shared Ray cluster per environment.
- `concurrency` must be `1` (the default); Ray itself handles parallelism inside the cluster.
{{< /variant >}}

## Examples

The following example shows how to configure Ray in a `TaskEnvironment`. Flyte automatically provisions a Ray cluster for each task using this configuration:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/ray/ray_example.py" lang="python" >}}

The next example demonstrates how Flyte can create ephemeral Ray clusters and run a subtask that connects to an existing Ray cluster:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/ray/ray_existing_example.py" lang="python" >}}

## API reference

See the [Ray API reference](../../api-reference/integrations/ray/_index) for full details.
