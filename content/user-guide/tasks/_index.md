---
title: Tasks
description: Configure, build, and deploy the durable batch workloads that everything else is made of.
icon: gear
weight: 2
variants: +flyte +union
---

# Tasks

A task is a Python function that runs remotely in a container. Tasks are the unit of work in Flyte: they are versioned, cached, retried, and recorded, so a run you start today can be reproduced and inspected later.

Every task belongs to a `TaskEnvironment`, which declares the container image, the resources, and the secrets the task needs. You define the environment once and reuse it across the tasks that share it.

```python
env = flyte.TaskEnvironment(name="etl", image=flyte.Image.from_debian_base())

@env.task
def extract(url: str) -> str:
    ...
```

Tasks compose. Calling one task from another builds the graph as your code executes, so fanout, branching, and error handling are ordinary Python rather than a separate DSL.

A task usually runs in a single container, but it doesn't have to. For distributed workloads such as multi-node model training, a `flyte.clustered.ClusteredTaskEnvironment` runs one task across a gang of pods at once, wiring up a `torchrun` rendezvous so your task body executes on every worker:

```python
import flyte
from flyte.clustered import ClusteredTaskEnvironment, TorchRun

env = ClusteredTaskEnvironment(
    name="ddp_env",
    image=flyte.Image.from_debian_base().with_pip_packages("torch"),
    replicas=2,            # number of pods (nodes)
    nproc_per_node=1,      # worker processes per pod
    runtime=TorchRun(),
)

@env.task
async def train() -> float:
    import torch.distributed as dist
    dist.init_process_group()  # RANK / WORLD_SIZE / MASTER_ADDR already set
    ...
```

See [Clustered task environment](./task-configuration/clustered-task-environment) for the full guide.

The three sections below follow the order you meet them in: describe the environment a task runs in, write the task logic, then get it onto a cluster.

{{< grid >}}

{{< link-card target="task-configuration" icon="gear" title="Configure tasks" >}}
Define `TaskEnvironment`s for container images, resources, secrets, caching, retries, and more; use triggers for schedules.
{{< /link-card >}}

{{< link-card target="task-programming" icon="code" title="Build tasks" >}}
Compose tasks with fanout, parallelism, error handling, traces, files, and DataFrames.
{{< /link-card >}}

{{< link-card target="task-deployment" icon="rocket" title="Run and deploy tasks" >}}
Use `flyte run` for iteration or `flyte deploy` to register a stable task version.
{{< /link-card >}}

{{< /grid >}}

## Related

Tasks are also the substrate for the other two building blocks. An app serves a task's results over HTTP; an agent drives tasks in a loop.

{{< grid >}}

{{< link-card target="../apps" icon="window" title="Apps" >}}
Long-running services for dashboards, APIs, and model endpoints.
{{< /link-card >}}

{{< link-card target="../agents" icon="robot" title="Agents" >}}
Durable, self-healing agents built from tasks and apps.
{{< /link-card >}}

{{< /grid >}}
