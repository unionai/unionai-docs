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
    .with_apt_packages("wget")
    .with_pip_packages("ray[default]==2.46.0", "flyteplugins-ray")
)
```

> [!WARNING] Your image must include `wget`
> KubeRay's readiness and liveness probes for the head and worker pods shell out to `wget`
> to poll the raylet and GCS health endpoints. If the image has no `wget`, both
> probes fail permanently with `wget: command not found`, the head pod never
> reports `Ready`, the workers stay parked in their `wait-gcs-ready` init
> container, and the job is never submitted. Install it with
> `.with_apt_packages("wget")`, or use a base image that already ships it.

{{< variant union >}}
{{< markdown >}}
> [!NOTE]
> For self-managed setups, refer to the [setup instructions](../../deployment/selfmanaged/configuration/plugins#ray) to enable the Ray plugin in your data plane.
{{< /markdown >}}
{{< /variant >}}

## Configuration

Create a `RayJobConfig` and pass it as `plugin_config` to a `TaskEnvironment`:

```python
import flyte
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
| `autoscaler_options` | `AutoscalerOptionsConfig` | Tune the autoscaler sidecar. Has no effect unless `enable_autoscaling` is `True` |
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

The head node runs the Ray dashboard, which starts nine subprocess modules on
top of GCS and the raylet. Give it 2 CPU and 4Gi of memory:

```python
ray_config = RayJobConfig(
    head_node_config=HeadNodeConfig(requests=flyte.Resources(cpu=2, memory="4Gi")),
    worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=2)],
)
```

Under-provisioning the head node is a common cause of a cluster that never becomes
ready: if the dashboard cannot start, `ray start --head` fails and KubeRay recycles
the head pod in a loop. A head pod at 1 CPU and 1000Mi has been observed failing
this way.

### `AutoscalerOptionsConfig` parameters

Setting `enable_autoscaling=True` runs the Ray autoscaler with KubeRay's defaults. Pass `autoscaler_options` to tune it:

```python
import flyte
from flyteplugins.ray import AutoscalerOptionsConfig, RayJobConfig, WorkerNodeConfig

ray_config = RayJobConfig(
    worker_node_config=[
        WorkerNodeConfig(group_name="ray-group", replicas=1, min_replicas=1, max_replicas=5)
    ],
    enable_autoscaling=True,
    autoscaler_options=AutoscalerOptionsConfig(
        upscaling_mode=AutoscalerOptionsConfig.UpscalingMode.CONSERVATIVE,
        idle_timeout_seconds=120,
        resources=flyte.Resources(cpu=("500m", "1"), memory=("512Mi", "1Gi")),
    ),
)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `upscaling_mode` | `AutoscalerOptionsConfig.UpscalingMode` | Rate limiting on adding nodes. `CONSERVATIVE` holds the number of pending worker pods to at most the current cluster size. `DEFAULT` and `AGGRESSIVE` are the same setting: no rate limit. Leaving the field unset, or passing `UNSPECIFIED`, also means no rate limit |
| `idle_timeout_seconds` | `int` | Seconds a node may sit idle before the autoscaler removes it (default: 60). An explicit `0` is dropped and the default applies |
| `image` | `str` | Container image for the autoscaler sidecar |
| `env` | `Dict[str, str]` | Environment variables for the autoscaler container |
| `resources` | `Resources` | Requests and limits for the autoscaler sidecar |

Every field is optional. Leaving `upscaling_mode`, `idle_timeout_seconds`, `image`, or `env` unset keeps the KubeRay default. `resources` is the exception: whenever you pass `autoscaler_options`, whatever you give for `resources` replaces the sidecar's default 500m CPU and 512Mi memory requests and limits outright. Omit it and the sidecar runs with no requests or limits at all; set only a request and it also loses the default limits. Set `resources` explicitly, on both sides. It accepts tuples to set a request and a limit together, as in `flyte.Resources(cpu=("500m", "1"))`.

> [!NOTE] The options do not switch autoscaling on
> `autoscaler_options` only configures the autoscaler sidecar, and the sidecar is created only when `enable_autoscaling` is `True`. Passing options on their own changes nothing.

### Connecting to an existing cluster

To connect to an existing Ray cluster instead of provisioning a new one, set the `address` parameter:

```python
ray_config = RayJobConfig(
    worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=2)],
    address="ray://existing-cluster:10001",
)
```

{{< variant union >}}
{{< markdown >}}

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

The cluster's identity is derived from the task environment: its name, the Ray configuration, the container image and resources, any pod template, the security context (service account and secrets), the code bundle, and the reuse policy itself. Tasks with an identical environment share one cluster; changing any of these (for example deploying a new image or code version, or switching service account) creates a fresh cluster rather than reusing a stale one.

> [!NOTE]
> `ReusePolicy` logs a recommendation to use at least two replicas to avoid starvation. That advice applies to reusable containers, not to reusable Ray clusters, which require exactly one shared cluster and let Ray schedule work across its nodes. You can ignore the warning here.

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

A shared cluster is never deleted when an individual task completes or is aborted. It is shut down automatically after it has been idle (no jobs running against it) for `idle_ttl`.

### Constraints

- `replicas` must be `1`: one shared Ray cluster per environment. An autoscaling range whose maximum is greater than `1`, such as `(1, 3)`, is rejected.
- `concurrency` must be `1` (the default). Ray itself handles parallelism inside the cluster.
- `shutdown_after_job_finishes` and `ttl_seconds_after_finished` must not be set on the `RayJobConfig`. The shared cluster has to outlive the individual jobs that run on it, so `idle_ttl` governs its shutdown instead. The `RayJobConfig` example under [Configuration](#configuration) above sets both, so drop them when you add a reuse policy.
{{< /markdown >}}
{{< /variant >}}

## Examples

The following example shows how to configure Ray in a `TaskEnvironment`. Flyte automatically provisions a Ray cluster for each task using this configuration:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/ray/ray_example.py" lang="python" >}}

The next example demonstrates how Flyte can create ephemeral Ray clusters and run a subtask that connects to an existing Ray cluster:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/ray/ray_existing_example.py" lang="python" >}}

## API reference

See the [Ray API reference](../../api-reference/integrations/ray/_index) for full details.
