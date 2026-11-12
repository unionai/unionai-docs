---
title: Gang scheduling for multi-node training
icon: diagram-3
description: Show that a distributed training job is only useful when every worker starts together, and that the workers a cluster cannot fit stay off the GPUs until the whole job can run.
weight: 2
variants: -flyte +union
---

# Gang scheduling for multi-node training

A distributed training job is only useful when *every* worker is running. If a scheduler starts
some workers and not the rest, the started workers sit on expensive GPUs doing nothing, and two jobs
that compete for the same GPUs can both end up half-started, each waiting on the other to free the
hardware it needs.

**Gang scheduling** admits a multi-worker job as one unit: all of its workers start together, or none
of them start. This tutorial runs a demo that makes that behavior visible. It submits two GPU training
jobs at the same moment, sized so the cluster can fit one job but not both, and then *measures* from
the workers' own timestamps whether each job started as a whole gang.

Full code is available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/gang_scheduling).

> [!TIP]
> This demo is a companion to [Distributed LLM pretraining](../distributed-pretraining/_index), which
> shows a full multi-node FSDP run inside a `ClusteredTaskEnvironment`. This one zooms in on the
> scheduling guarantee those runs rely on. For the framework itself, see the [Clustered task environment](../../../user-guide/tasks/task-configuration/clustered-task-environment) guide.

## The problem: partial starts

Think of a training job as a gang of workers that must run together. Rank 0 and rank 1 need rank 2 to
exchange gradients; a worker whose peers never arrive does nothing but hold its GPU. Without gang
scheduling:

- **GPU stranding.** A cluster can start some workers of a job and not the rest. Those workers hold
  GPUs and wait forever for peers that cannot fit.
- **Deadlock.** Two jobs that each need more GPUs than are free can each get a partial share—half of
  job A starts, half of job B starts, and each waits on the other forever.

Gang scheduling fixes this by treating the whole group as indivisible. The scheduler puts the workers
on a queue and only admits them when every worker can be placed at once.

## What the demo does

The demo submits two training jobs, `team-a` and `team-b`, at the same moment. Together they need more
GPUs than the pool has, so only one can run at a time. On Union, one gang is admitted as a whole and
all of its workers start together; the other stays queued without starting a single worker or holding a
GPU, then starts as a whole once the first gang releases its GPUs.

To make the guarantee observable, each worker records three timestamps while it runs and the driver
collects them into a report that draws one timeline per worker and runs two checks:

1. **Every gang started together** — the workers of each job started within seconds of each other.
2. **The waiting gang started no workers early** — no worker of the waiting job was up until the whole
   first job finished training.

## Requirements

- A Union cluster with gang scheduling turned on and a queue the jobs can use (`shared` by default).
- `flyte>=2.11.2` and a Flyte config pointing at that cluster.
- A GPU pool that can fit one job but not two: `GANG_WORKERS ≤ GPUs < 2 × GANG_WORKERS`, within both
  the node pool's capacity and the queue's quota. If both jobs fit, they run side by side and the
  report says so. If one job cannot fit at all, it is rejected as infeasible.

See [Resource caps and scheduling](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling)
for how queues admit gang-style jobs, and
[Managing queues](../../../user-guide/clusters-and-queues/queues) to create the queue.

## Run it

The driver task submits both gangs and renders the report, so you only point one command at the
cluster. Three knobs control the run:

{{< code file="/unionai-examples/v2/tutorials/gang_scheduling/main.py" fragment="knobs" lang="python" >}}

| Knob | Default | Meaning |
| --- | --- | --- |
| `GANG_WORKERS` | `3` | Workers (pods, one GPU each) per job |
| `GANG_GPU` | `L4:1` | Accelerator per worker. Set to `""` for a CPU-only rehearsal |
| `GANG_QUEUE` | `shared` | The queue the jobs are submitted to |

Run it with GPUs:

```bash
GANG_WORKERS=3 GANG_GPU=L4:1 uv run --script main.py
```

The script prints the run URL. One run takes about 5 to 8 minutes: GPU nodes start, `team-a` trains
for about 90 seconds, then `team-b` trains.

To rehearse without GPUs, use `GANG_GPU="" uv run --script main.py`. On CPU the two jobs usually fit
side by side, so you see the gang start but not the waiting.

## Turning on gang scheduling

Gang scheduling is opt-in per job, and it is one line on the task's environment. Each training job is a
`ClusteredTaskEnvironment` that launches `replicas` identical workers and bootstraps `torchrun` inside them. The whole opt-in is
the queue label on the pod template:

{{< code file="/unionai-examples/v2/tutorials/gang_scheduling/main.py" fragment="gang-env" lang="python" >}}

Most of this is the ordinary clustered-environment setup you would use for any distributed job:
`replicas=WORKERS` pods, one GPU each via `resources`, a PyTorch distributed runtime, and a failure
policy that recreates the group rather than leaving it half-alive. The single line that turns on gang
scheduling is the label:

```python
pod_template=flyte.PodTemplate(labels={"kueue.x-k8s.io/queue-name": QUEUE})
```

With that label present, the cluster's queue admits the whole JobSet as one gang—never a subset. A
job that references a queue also inherits that queue's [resource caps and priority](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling), so a queue is exactly how a team caps the GPUs its
training jobs can use.

## The training function

Each worker records its own timestamps so the driver can later reconstruct the timeline. The training
loop itself is ordinary PyTorch DDP—there is nothing gang-specific about it:

{{< code file="/unionai-examples/v2/tutorials/gang_scheduling/main.py" fragment="train" lang="python" >}}

The details worth noticing:

- **`container_started()` reads `/proc`** rather than `time.time()` at the top of `train`. `torchrun`'s
  static rendezvous waits for every pod before it runs your function, so a timestamp taken when `train`
  begins would hide a pod that came up early and sat waiting for the rest. Reading PID 1's start time
  from `/proc/1/stat` captures when the container actually started—the exact moment a worker began
  occupying its GPU.
- **`dist.barrier()` after `init_process_group`** marks the moment every worker of the gang has joined.
  `init_process_group` is not a barrier on NCCL; the barrier is what guarantees all peers are connected.
- **`dist.all_gather_object`** exchanges every worker's `Worker` record so rank 0's return value—the
  task output—carries the whole gang's timestamps. Flyte keeps rank 0's output for a clustered task.

## The driver and the report

The driver submits both gangs at once with `asyncio.gather`, then renders and flushes the report:

{{< code file="/unionai-examples/v2/tutorials/gang_scheduling/main.py" fragment="driver" lang="python" >}}

`train.override(short_name=...)` reuses one task definition for both `team-a` and `team-b` under
distinct names in the run graph. The two calls happen together, so whatever ordering the scheduler
imposes is visible, not an artifact of submission order.

The report draws every worker on one timeline and reduces the three timestamps to a verdict:

- **Every gang started together.** The workers of one job should start within seconds of each other
  (`START_SKEW_TOLERANCE_S`, 60 s by default). The faint part at the start of each bar is how long a
  worker waited for its peers; when gang admission works, it stays seconds long.
- **The waiting gang started no workers early.** No bar of the waiting gang should begin until every
  bar of the other gang has ended. If the two gangs overlapped, the report reports `info` (both fit at
  once) rather than pretending there was a queue.

Because the report relies on timestamps the workers recorded themselves, it is not a check of "the UI
looked right"—it is a measurement of the scheduling behavior from the pods' own perspective, and it will
*fail* loudly if gang scheduling is off.

## Reading the report

Once the driver finishes, open its **report tab**. You should see:

- One row per worker, colored by team.
- **Every gang started together.** All of a job's bars begin at the same point; each faint
  "up, waiting for peers" segment stays a few seconds long.
- **The waiting gang started no workers early.** No bar of the waiting gang starts until every bar of
  the other gang has ended, and both checks read `pass`.
- The run graph (while the run is live) shows one job transitioning through *waiting for gang
  admission* to *k/N workers ready* to *Running* only once every worker is ready, while the other job
  stays queued with no pods.

If a check reads `fail`, the timestamps tell you what happened: which worker came up early, how long it
sat, and when its gang actually began training.

## Related

- [Distributed LLM pretraining](../distributed-pretraining/_index) — a full multi-node FSDP pipeline in a `ClusteredTaskEnvironment`.
- [Clustered task environment](../../../user-guide/tasks/task-configuration/clustered-task-environment) — how a clustered task starts a gang of pods on the backend.
- [Resource caps and scheduling](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling) — how queues enforce gang-style admission, caps, and priority.
- [Managing queues](../../../user-guide/clusters-and-queues/queues) — creating and routing queues administratively.
