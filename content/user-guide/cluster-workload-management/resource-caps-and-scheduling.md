---
title: Resource caps and scheduling
description: Share clusters across teams with per-queue CPU, memory, and GPU caps, and choose how a queue schedules work when capacity is tight.
icon: sliders
weight: 4
variants: -flyte +union
---

# Resource caps and scheduling

> [!NOTE] Requires the `flyteplugins-union` plugin
> The queue CLI commands and Python objects on this page are provided by the
> `flyteplugins-union` package. Install it with `pip install flyteplugins-union`.

Two teams share one pool of GPU clusters. The research team launches a sweep
that asks for every H100 in the pool, and the inference team's nightly
evaluation, which needs four, waits for hours. Action concurrency limits do not fix
this. One action can ask for half a CPU and the next for sixty-four GPUs, so
the number of running actions says little about how much of the cluster a team
is using.

A resource cap limits the resources themselves. Give each team a queue and cap
the CPU, memory, and GPUs that the queue's scheduled work may use at once. Both
teams then run on the same clusters, and neither can take all of the capacity.

```bash
flyte create queue research \
  --run-concurrency 100 \
  --action-concurrency 1000 \
  --max-resources cpu=512 \
  --max-resources memory=4Ti \
  --max-accelerators H100=48 \
  --scheduling greedy_capacity

flyte create queue inference-eval \
  --run-concurrency 50 \
  --action-concurrency 500 \
  --max-resources cpu=128 \
  --max-accelerators H100=16 \
  --scheduling greedy_capacity
```

The [scheduling policy](#choose-a-scheduling-policy) decides what a queue does
when the next action in line does not fit under its caps.

This page covers a queue's resource and scheduling settings. To create, drain,
or delete queues, see [Managing queues](./queues).

## What a cap limits

A cap limits the total resources requested by the actions a queue has scheduled
and that have not finished. It adds up what each action asks for in its
`resources`. Actual usage inside the container does not count.

A queue has one cap for all the clusters it routes to. A queue still accepts as
much work as its depth allows, and the cap limits how much of that work is
scheduled at once. On a queue capped at 48 H100s, at most about 48 H100s are
scheduled at any moment, on one cluster or spread over four. The rest of the
work waits in the queue.

A cap applies only to the resources you name. `--max-resources cpu=512` caps CPU
and leaves memory unlimited.

A cap does not reserve capacity. The caps of queues that share clusters can add
up to more than the clusters have, so a busy team can use capacity that an idle
team is not using.

An action is scheduled only when it fits under the queue's run concurrency,
action concurrency, depth, and resource caps together.

There are three cap settings:

| Python | CLI | Limits | Values |
|---|---|---|---|
| `max_resources` | `--max-resources` | `cpu`, `memory`, `ephemeral_storage` | Kubernetes quantities such as `64`, `500m`, `512Gi` |
| `max_gpus` | `--max-gpus` | GPUs requested without a device type | A whole number of GPUs |
| `max_accelerators` | `--max-accelerators` | GPUs and other accelerators, per device type | A whole number of devices for each type |

## Cap GPUs and accelerators

A task asks for a GPU in one of two ways. It names a device, such as `H100:1`,
or it asks for a GPU of any type with `gpu=1`. A queue has a separate setting
for each.

### GPUs of a named type

`--max-accelerators` caps one device type. Repeat it to cap several types on the
same queue:

```bash
# At most 48 H100s, 16 A100s, and 32 T4s scheduled at once
flyte create queue research \
  --run-concurrency 100 \
  --action-concurrency 1000 \
  --max-accelerators H100=48 \
  --max-accelerators A100=16 \
  --max-accelerators T4=32
```

Each type has its own cap. A task that asks for T4s counts against the T4 cap
only, so a team that has reached its H100 cap can still run T4 work. A type you
do not name is unlimited.

Name a device the way a task does (`T4`, `A100 80G`, `V6E`) or by its canonical
name (`nvidia-t4`, `nvidia-a100-80gb`, `google-tpu-v6e`). The queue stores and
prints the canonical name, for example `nvidia_gpu/nvidia-h100`. To cap one
partition size of a device, add the partition: `A100/1g.5gb=4`.

### GPUs without a type

`--max-gpus` caps the GPUs requested without a device type:

```bash
# At most 8 GPUs of any type, and separately at most 10 H100s
flyte create queue mixed-gpu \
  --run-concurrency 50 \
  --action-concurrency 500 \
  --max-gpus 8 \
  --max-accelerators H100=10
```

The two caps are independent. A task that asks for `gpu=1` counts against
`--max-gpus`. A task that asks for `H100:1` counts against the H100 cap and not
against `--max-gpus`. In the example, the queue can have 8 untyped GPUs and 10
H100s scheduled at the same time.

Only NVIDIA GPUs can be requested without a type, so `--max-gpus` applies to
NVIDIA GPUs. Tasks that use TPUs or other accelerators always name the device,
and you cap those with `--max-accelerators`.

Two cases change which cap an untyped request counts against:

- The scheduler chooses the device for an untyped request. If it chooses a
  device that has its own cap, the request counts against that cap as well. On a
  cluster with T4, L4, and A10G nodes and a queue that caps L4s, a `gpu=1` task
  that lands on an L4 counts against both `--max-gpus` and the L4 cap.
- If your organization has a default GPU type in its settings, an untyped
  request is treated as a request for that type. It counts against that type's
  cap in `--max-accelerators`.

## Set caps on a queue

Set caps and the scheduling policy when you create a queue, or change them
later.

{{< tabs "set-caps" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
# Create a queue with caps
flyte create queue research \
  --run-concurrency 100 \
  --action-concurrency 1000 \
  --max-resources cpu=512 \
  --max-resources memory=4Ti \
  --max-gpus 8 \
  --max-accelerators H100=48 \
  --scheduling greedy_capacity

# Change the caps on an existing queue
flyte update queue research --max-resources cpu=768 --max-resources memory=6Ti
flyte update queue research --max-gpus 16
flyte update queue research --max-accelerators H100=64 --max-accelerators T4=32

# Remove the caps
flyte update queue research --clear-max-resources
flyte update queue research --clear-max-gpus
flyte update queue research --clear-max-accelerators

# Change the scheduling policy
flyte update queue research --scheduling strict_fifo
```

`flyte update queue <name> --edit` opens the whole queue in your `$EDITOR`,
including `max_resources`, `max_gpus`, `max_accelerators`, and `scheduling`.

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

# Create a queue with caps
Queue.create(
    "research",
    run_concurrency=100,
    action_concurrency=1000,
    max_resources={"cpu": "512", "memory": "4Ti"},
    max_gpus=8,
    max_accelerators={"H100": 48},
    scheduling="greedy_capacity",
)

# Change the caps on an existing queue
Queue.update("research", max_resources={"cpu": "768", "memory": "6Ti"})
Queue.update("research", max_gpus=16)
Queue.update("research", max_accelerators={"H100": 64, "T4": 32})

# Remove the caps
Queue.update("research", max_resources={})
Queue.update("research", clear_max_gpus=True)
Queue.update("research", max_accelerators={})

# Change the scheduling policy
Queue.update("research", scheduling="strict_fifo")
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Console" >}}
{{< markdown >}}

Go to **Settings > Queues**, open the queue, and edit its resource caps and
scheduling policy.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

> [!WARNING] An update replaces every cap of the same kind
> `--max-resources` on `flyte update queue` replaces all of the queue's resource
> caps, so a resource you leave out becomes unlimited. To raise CPU on a queue
> that also caps memory, pass both. `--max-accelerators` works the same way for
> device types: to change the H100 cap on a queue that also caps T4s, pass both.
> The three settings do not affect each other. Changing `--max-accelerators`
> leaves `--max-gpus` and `--max-resources` as they are.
>
> In Python, passing `None` for `max_resources` or `max_accelerators` keeps the
> current caps, a mapping replaces them, and `{}` removes them.

### Changes apply to a live queue

You can change a queue's caps and scheduling policy without draining it. The
scheduler picks up the new values shortly after the update and uses them for
everything it schedules from then on.

If you raise a cap, waiting actions are scheduled as soon as they fit. If you
lower a cap below what is in use, running actions are not interrupted, and the
queue schedules nothing new for that resource until enough work finishes to
bring usage under the cap. If you lower a cap below what a single waiting action
asks for, that action becomes [infeasible](#infeasible-requests-fail-fast) and
fails.

## See how much of a cap is in use

A queue reports usage next to each cap.

{{< tabs "watch-caps" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
# One queue: settings plus a usage bar for each cap
flyte get queue research

# The same view, updating live
flyte get queue research --watch

# Every live queue in one table
flyte get queue --watch

# Only the queues in one or more pools
flyte get queue --watch --pool gpu-pool
```

With a queue name, the output has a bar for each cap showing `used / cap` and a
percentage: one per capped resource, one named `gpus` for `--max-gpus`, and one
per capped device type. They follow the bars for run concurrency, action
concurrency, and depth. A resource without a cap shows its usage with no bar.

Without a name, `--watch` shows one row per queue with its pool, scheduling
policy, CPU and memory usage against their caps, GPUs in use, runs, actions, the
number of waiting actions, and whether the head of the line is blocked.

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

metrics = Queue.details("research")
print(metrics["in_flight_resources"], metrics["max_resources"])
print(metrics["accelerator_charges"], metrics["max_gpus"], metrics["max_accelerators"])
print(metrics["scheduling"], metrics["head_blocked"])

# Stream one queue
for metrics in Queue.watch("research"):
    print(metrics["in_flight_resources"])

# Stream every live queue in the given pools (all pools when omitted)
for snapshot in Queue.watch_pool(pools=["gpu-pool"]):
    for metrics in snapshot:
        print(metrics["pool"], metrics["name"], metrics["in_flight_resources"])
```

`in_flight_resources` and `max_resources` are `{name: quantity}` mappings.
`accelerator_charges` maps each GPU cap to the number of devices counted against
it. Devices with no cap are counted under `other`.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Choose a scheduling policy

The scheduling policy decides what a queue does when the next action in line
does not fit, under the queue's caps or on the clusters it routes to. Both
policies consider actions in the order they were queued.

> [!NOTE] Use `greedy_capacity` for most queues
> `greedy_capacity` keeps capacity in use and keeps reusable containers busy.
> Choose `strict_fifo` for queues that run gang-style jobs or that need strict
> first come, first served ordering.
>
> A new queue is created as `strict_fifo` unless you pass
> `--scheduling greedy_capacity`, or `scheduling="greedy_capacity"` in Python.

| | Greedy capacity (recommended) | Strict FIFO |
|---|---|---|
| Setting | `greedy_capacity` | `strict_fifo` |
| When the next action does not fit | Skips it and schedules the actions behind it that fit | Stops and waits for it |
| Order | First come, first served among the actions that fit | Exactly first come, first served |
| Idle capacity while work is waiting | No | Yes, while the head of the line is blocked |
| Can a large action be starved? | Yes, while smaller actions keep fitting | No |
| Reusable containers (warm pools) | Actions for a running warm pool keep being scheduled | Actions for a running warm pool wait behind the blocked head |
| Use it for | Most queues | Gang-style jobs and strict ordering |

### An example

A queue is capped at 8 GPUs and 6 are in use, so 2 are free. Three actions are
waiting, in this order:

| Position | Action | Asks for | Greedy capacity | Strict FIFO |
|---|---|---|---|---|
| 1 | `train` | 4 GPUs | Waits. It does not fit in the 2 free GPUs. | Waits. It does not fit in the 2 free GPUs. |
| 2 | `evaluate` | 1 GPU | Scheduled now. | Waits behind `train`. |
| 3 | `embed` | 1 GPU | Scheduled now. | Waits behind `train`. |

Under greedy capacity the queue runs at 8 of 8 GPUs, and `train` starts once 4
GPUs are free at the same moment. Under strict FIFO the queue stays at 6 of 8
until 2 more GPUs free up. Then `train` starts, followed by `evaluate` and
`embed`.

### Greedy capacity

Set with `--scheduling greedy_capacity`.

The queue goes through the line in arrival order. When an action does not fit,
the queue moves on to the next one and schedules every action that fits.

Use it for queues that carry a mix of small and large actions, for work that
runs in reusable containers, and when you want the capacity you pay for to stay
in use.

A very large action can wait a long time when smaller ones keep arriving and
keep fitting. If a queue carries both, move the large jobs to their own strict
FIFO queue, or give them a
[`max_queued_time`](../tasks/task-configuration/retries-and-timeouts#max_queued_time-fail-fast-when-capacity-isnt-available)
so they fail after a set wait.

### Strict FIFO

Set with `--scheduling strict_fifo`.

The queue schedules actions strictly in arrival order. When the action at the
head of the line does not fit, the queue schedules nothing behind it until it
does. As running work finishes, the freed capacity accumulates for the head of
the line, and later, smaller actions cannot take it.

Use it for gang-style jobs. A distributed training job that needs 32 GPUs at
once starts only when 32 are free together. Under greedy capacity, a steady
stream of one-GPU actions can take each GPU as it frees up, and the large job
never starts. Also use it when work must start in the order it was submitted.

Capacity sits idle while the head of the line waits, and every action behind it
waits too, including the ones that would fit.

### Reusable containers (warm pools)

A [reusable environment](../tasks/task-configuration/reusable-containers) keeps
a pool of warm containers alive and runs many actions in them. A queue counts
those containers against its caps once, when the pool starts. The first action
of an environment starts the pool, and it has to fit under the cap at the size
of the containers the pool starts with. Later actions that join the running pool
add nothing to the cap.

| | Greedy capacity | Strict FIFO |
|---|---|---|
| Actions for a warm pool that is already running | Scheduled past a blocked action, since they add nothing to the cap | Wait behind the blocked head |
| The warm pool while a large action is blocked | Stays busy | Sits idle |
| An action that starts a new pool | Scheduled if the pool fits. If it does not fit, the queue moves on to the next action | Scheduled if the pool fits. If it does not fit, it blocks the line |

On a strict FIFO queue with little free capacity, one large job at the head of
the line stalls every reusable environment on the queue. If the wait lasts
longer than an environment's idle timeout, its containers shut down and the next
action starts cold.

Put work that runs in reusable containers on a greedy capacity queue. If the
same team also runs gang-style jobs, give those jobs their own strict FIFO
queue.

### When the line is blocked

A strict FIFO queue reports when its head is blocked and for how long.
`flyte get queue <name> --watch` shows a head-of-line banner with the number of
actions waiting behind it, and the `flyte get queue --watch` table marks the
queue as blocked. In Python, `Queue.details` returns `head_blocked` and
`head_blocked_since`.

A blocked head clears as running work finishes. To let the waiting actions that
fit run now, switch the policy:

```bash
flyte update queue research --scheduling greedy_capacity
```

## Resource-aware scheduling

When Union knows each cluster's configuration, a queue schedules against what
the clusters can run. The configuration is the cluster's node pools, the size of
the nodes in each pool, the accelerators they have, and how far each pool can
scale. With it, the scheduler does the following for every action:

- It considers only the clusters that can run the action. Each container the
  action asks for must fit on a node of some node pool in the cluster: its
  requests fit one node, the pool has its accelerator, and its node selector is
  compatible with the pool's labels.
- It waits when a cluster is full. An action that fits a cluster's node pools
  but not the room left at full scale stays queued under the queue's scheduling
  policy. On a strict FIFO queue it blocks the line.
- Among the clusters with room, it places the action on the least loaded one.

> [!NOTE] Union needs your cluster configuration
> Union BYOC deployments already have this configuration. For self-managed
> deployments, talk to the Union team to set it up. Until then, a queue treats a
> cluster as able to run anything and places work on any healthy cluster it
> routes to. Resource caps and the scheduling policy apply either way.

## Infeasible requests fail fast

Some requests can never run, however long they wait. An action that asks for 64
CPUs on a queue capped at 32 does not fit even when the queue is empty. On a
strict FIFO queue it would also block everything behind it. The scheduler fails
such an action as soon as it sees it.

With your cluster configuration in place, the same check extends to the
clusters, and this is rolling out now. An action also fails as infeasible when
no cluster its queue routes to could ever run it:

- It asks for an accelerator that none of those clusters has.
- One of its containers is larger than any node those clusters can launch.
- Its total request is more than those clusters have at full scale.

An infeasible action fails with the error code `INFEASIBLE` and is not retried.
The error message names the request and what the queue or the clusters offer.
Reduce the request, route the task to a different queue, or raise the cap.

An action that fits the cap and the clusters, but not the room available right
now, stays queued and runs once capacity frees up. To limit that wait, set
[`max_queued_time`](../tasks/task-configuration/retries-and-timeouts#max_queued_time-fail-fast-when-capacity-isnt-available)
on the task.

## See also

- [Managing queues](./queues): create, drain, move, and delete queues.
- [Queues in Configure tasks](../tasks/task-configuration/queues): route work to
  a queue from task code.
- [Reusable containers](../tasks/task-configuration/reusable-containers): how
  reusable environments are sized.
