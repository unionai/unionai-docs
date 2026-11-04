---
title: Pretraining
description: Train a model from scratch across many GPUs and nodes, with data prep cached and sized separately from the training job.
icon: stack
weight: 1
variants: +flyte +union
---

# Pretraining

Pretraining runs one training loop across more GPUs than a single machine holds. Flyte launches the nodes as one group, wires up `torch.distributed`, and runs the data pipeline and the driver on cheaper hardware next to it.

## Split the job by hardware

A pretraining run has three kinds of work with very different needs. Give each its own environment:

```python
import flyte
from flyte.clustered import ClusteredTaskEnvironment, TorchRun

image = flyte.Image.from_debian_base().with_pip_packages("torch", "datasets")

data_env = flyte.TaskEnvironment(
    name="data",
    image=image,
    resources=flyte.Resources(cpu=16, memory="64Gi", disk="200Gi"),
    cache="auto",
)

train_env = ClusteredTaskEnvironment(
    name="pretrain",
    image=image,
    resources=flyte.Resources(cpu=64, memory="512Gi", gpu="H200:8", shm="16Gi"),
    replicas=4,
    nproc_per_node=8,
    runtime=TorchRun(),
)

driver_env = flyte.TaskEnvironment(
    name="driver",
    image=image,
    resources=flyte.Resources(cpu=2, memory="4Gi"),
    depends_on=[data_env, train_env],
)
```

- **Data loading** gets CPUs, memory, and disk for tokenization, and no GPU. `cache="auto"` means a second training run on the same dataset reuses the tokenized shards instead of rebuilding them.
- **Training** gets the GPUs: 4 nodes with 8 GPUs each. Set `shm` explicitly, because NCCL and PyTorch data loaders use shared memory, and the container default is small.
- **The driver** gets two CPUs. `depends_on` deploys the other two environments with it, so a single `flyte run` deploys all three.

## Run torchrun across nodes

`flyte.clustered.ClusteredTaskEnvironment` runs a task on `replicas` identical pods, each starting `nproc_per_node` processes with torchrun:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/ddp_train.py" fragment="env" lang=python >}}

`resources` applies to each pod, so 2 replicas with `gpu="H100:8"` and `nproc_per_node=8` is a 16-GPU job. Inside the task, torchrun has already set `RANK`, `WORLD_SIZE`, and `MASTER_ADDR`, and `flyte.ctx()` exposes the same topology to your code:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/ddp_train.py" fragment="task" lang=python >}}

Every rank runs the same function. Return a value of the declared type from every rank; Flyte keeps rank 0's output. Frameworks that read the torchrun environment, such as Lightning, Hugging Face Accelerate, and DeepSpeed, work unchanged. For FSDP and Lightning versions of this task, and the prerequisites on the cluster, see [Clustered task environment](../tasks/task-configuration/clustered-task-environment). For JAX, set `runtime=JaxRun()` and `nproc_per_node=1`: JAX runs one process per node that owns every local GPU.

## Save checkpoints to your object store

A pretraining run can take days, so save progress as it trains. Write to `flyte.ctx().checkpoint` from rank 0 only, so the ranks don't write the same file:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/fsdp_train.py" fragment="checkpoint" lang=python >}}

The checkpoint lives in your object store, not on the pod, so it survives a restart of the whole group and a retry of the task. Load it at the start of the task to continue from the last save. See [Resilient training](./resilient-training).

## Schedule all nodes together

A multi-node job can't start until every node is available. If pods start one at a time, the first nodes sit idle while the rest wait for capacity. Admit the job as one gang through a Kueue queue on the cluster:

{{< code file="/unionai-examples/v2/tutorials/gang_scheduling/main.py" fragment="gang-env" lang=python >}}

If a higher-priority job can preempt yours after it starts, set `failure_policy=ClusterFailurePolicy(resume_after_preemption=True)`, so the job waits to be readmitted and resumes from its checkpoint without using a retry. See [Resilient training](./resilient-training#restart-a-multi-node-job).

{{< variant union >}}
{{< markdown >}}

On {{< key product_name >}}, a [queue](../tasks/task-configuration/queues) also caps the GPUs a team's training jobs can use and sets their priority. See [Resource caps and scheduling](../clusters-and-queues/resource-caps-and-scheduling).

{{< /markdown >}}
{{< /variant >}}

## Profile a training step

To find out whether a step is bound by compute, communication, or data loading, capture an NVIDIA Nsight Systems profile from the task. See the [Nsight integration](../../integrations/nsight/_index).

## Related

- [Distributed LLM pretraining](../../tutorials/frontier-ai/distributed-pretraining/_index): a GPT model pretrained on multiple H200 nodes, end to end.
- [Fine-tuning a VLM](../../tutorials/computer-vision/qwen-vl-finetuning/_index): multi-node DeepSpeed training with checkpoints you can resume from.
- [PyTorch](../../integrations/pytorch/_index): the `Elastic` plugin config, an alternative to the clustered environment.
- [Ray](../../integrations/ray/_index): run a Ray cluster from a task.
- [Weights & Biases distributed training](../../integrations/wandb/distributed_training): log from every rank.
