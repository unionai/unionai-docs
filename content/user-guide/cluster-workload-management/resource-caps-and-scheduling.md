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
evaluation, which needs four, waits for hours. Concurrency limits do not fix
this. One action can ask for half a CPU and the next for sixty-four GPUs, so
counting actions says little about how much of the cluster a team is using.

Resource caps bound the resources themselves. Give each team its own queue, cap
the CPU, memory, and GPUs its scheduled work may use at once, and both teams draw from
the same clusters without either one taking all of it:

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

Use resource caps when several teams or workloads share clusters and you want
each one to have a ceiling. Use the [scheduling policy](#choose-a-scheduling-policy)
to decide what the queue does when the next action in line does not fit under
that ceiling.

This page covers the resource and scheduling settings of a queue. For creating,
draining, and deleting queues, see [Managing queues](./queues).

## What a cap bounds

A cap bounds the **summed resource requests** of the actions a queue has
dispatched and that have not finished yet. It counts what each action asks for
in its `resources`, not what the container ends up using.

- **The cap spans every cluster the queue routes to.** It is one budget for the
  queue, not a budget per cluster. The queue can accept
  as much work as its depth allows. The cap limits how much of it is scheduled
  at once: on a queue capped at 48 H100s, at most about 48 are scheduled at any
  moment, whether that work lands on one cluster or four. The rest waits in
  the queue.
- **Only the resources you name are capped.** `--max-resources cpu=512` caps CPU
  and leaves memory unlimited. A value of `0` is a hard cap that refuses every
  request for that resource. It does not mean "unset".
- **Caps are ceilings, not reservations.** A cap does not set capacity aside for
  a queue. The caps of queues that share clusters can add up to more than the
  clusters hold, which lets an idle team's share be used by a busy one.
- **Caps work alongside the other limits.** An action is dispatched only when it
  fits the queue's run concurrency, action concurrency, depth, and resource caps
  together.

There are two kinds of cap:

| Setting | Caps | Values |
|---|---|---|
| `max_resources` / `--max-resources` | `cpu`, `memory`, `ephemeral_storage` | Kubernetes quantities such as `64`, `500m`, `512Gi` |
| `max_accelerators` / `--max-accelerators` | GPUs and other accelerators, per type | A whole number of devices |

GPUs are always capped per accelerator type. There is no total `gpu` entry in
`max_resources`.

### Accelerator selectors

An accelerator cap names what it covers with a selector. A selector can be as
narrow as one partition size of one device or as wide as a whole device class:

| Selector | Covers | Example |
|---|---|---|
| Device | One accelerator model, across all its partitions | `H100`, `T4`, `nvidia-a100-80gb` |
| Device and partition | One partition size of one model | `A100/1g.5gb` |
| Class | Every device of that class | `nvidia_gpu`, `google_tpu`, `amazon_neuron`, `amd_gpu`, `habana_gaudi` |

You can write a device the same way a task does (`T4`, `A100 80G`) or by its
canonical name (`nvidia-t4`, `nvidia-a100-80gb`). The queue stores and prints
the canonical form, for example `nvidia_gpu/nvidia-h100`.

A queue can cap several accelerator types at once. Repeat `--max-accelerators`
once per type, or pass several entries in the Python mapping:

```bash
# At most 48 H100s, 16 A100s, and 32 T4s scheduled at once
flyte create queue research \
  --run-concurrency 100 \
  --action-concurrency 1000 \
  --max-accelerators H100=48 \
  --max-accelerators A100=16 \
  --max-accelerators T4=32
```

Each type has its own budget. A task that asks for T4s is counted against the T4
cap only, so a team that has used all of its H100s can still run T4 work.

A device counts against **every** cap that covers it, and the action must fit
all of them. This lets you combine a wide cap with narrow ones:

```bash
# At most 8 NVIDIA GPUs of any kind, of which at most 2 may be H100s
flyte create queue mixed-gpu \
  --run-concurrency 50 \
  --action-concurrency 500 \
  --max-accelerators nvidia_gpu=8 \
  --max-accelerators H100=2
```

An accelerator type that no cap covers is unlimited on that queue.

Every GPU is counted under a type. A task that asks for GPUs without naming one
is counted under the default GPU type configured for your organization. If no
default is configured either, the action fails as
[infeasible](#infeasible-requests-fail-fast) because there is nothing to count
it against.

## Set caps on a queue

Caps and the scheduling policy can be set when you create a queue or changed
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
  --max-accelerators H100=48 \
  --scheduling greedy_capacity

# Change the caps on an existing queue
flyte update queue research --max-resources cpu=768 --max-resources memory=6Ti
flyte update queue research --max-accelerators H100=64 --max-accelerators T4=32

# Remove the caps
flyte update queue research --clear-max-resources
flyte update queue research --clear-max-accelerators

# Change the scheduling policy
flyte update queue research --scheduling strict_fifo
```

`flyte update queue <name> --edit` opens the whole queue in your `$EDITOR`,
including `max_resources`, `max_accelerators`, and `scheduling`.

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
    max_accelerators={"H100": 48},
    scheduling="greedy_capacity",
)

# Change the caps on an existing queue
Queue.update("research", max_resources={"cpu": "768", "memory": "6Ti"})
Queue.update("research", max_accelerators={"H100": 64, "T4": 32})

# Remove the caps
Queue.update("research", max_resources={})
Queue.update("research", max_accelerators={})

# Change the scheduling policy
Queue.update("research", scheduling="strict_fifo")
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Console" >}}
{{< markdown >}}

Go to **Settings > Queues**, open the queue, and edit its resource caps and
scheduling policy there.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

> [!WARNING] An update replaces the whole cap
> `--max-resources` and `--max-accelerators` on `flyte update queue` replace the
> full set of caps of that kind. A resource you leave out becomes unlimited.
> To raise CPU on a queue that also caps memory, pass both again. The same goes
> for accelerators: to change the H100 cap on a queue that also caps T4s, pass
> both.
> In Python the same rule applies to the mapping you pass: `None` keeps the
> current caps, a mapping replaces them, and `{}` removes them.

### Changes apply to a live queue

You do not need to drain a queue to change its caps or its scheduling policy.
The scheduler picks up the new values shortly after the update and applies them
to everything it dispatches from then on:

- **Raising a cap** lets waiting actions through as soon as they fit.
- **Lowering a cap below what is in use** does not interrupt anything that is
  already running. The queue dispatches nothing new for that resource until
  enough work finishes to bring usage back under the cap.
- **Lowering a cap below what a single waiting action asks for** makes that
  action [infeasible](#infeasible-requests-fail-fast), and it fails instead of
  waiting.

## See how much of a cap is in use

A queue reports its usage next to its caps, so you can see how much of a team's
budget is in use by scheduled actions.

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

With a queue name, you get one bar per capped resource and per accelerator cap
(`used / cap` and a percentage), under the bars for run concurrency, action
concurrency, and depth. A resource the queue does not cap still shows what is in
flight, without a bar.

Without a name, `--watch` shows a dashboard with one row per queue: its pool,
scheduling policy, CPU and memory usage against their caps, GPUs in flight, runs,
actions, how many actions are waiting, and whether the head of the line is
blocked.

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

metrics = Queue.details("research")
print(metrics["in_flight_resources"], metrics["max_resources"])
print(metrics["accelerator_charges"], metrics["max_accelerators"])
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
`accelerator_charges` maps each accelerator cap to the devices counted against
it, with an `other` entry for devices no cap covers.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Choose a scheduling policy

The scheduling policy decides what a queue does when the next action in line
does not fit, either under the queue's caps or on the clusters it routes to.
There are two policies. Both consider actions in the order they were queued, and
they differ in what happens at the first action that does not fit.

> [!NOTE] Use `greedy_capacity` for most queues
> `greedy_capacity` is the recommended policy. It keeps capacity in use and keeps
> reusable containers busy. Choose `strict_fifo` only for queues that run
> gang-style jobs or that need strict first come, first served ordering.
>
> A new queue is created as `strict_fifo` unless you say otherwise, so pass
> `--scheduling greedy_capacity` (or `scheduling="greedy_capacity"` in Python)
> when you create it.

| | Greedy capacity (recommended) | Strict FIFO |
|---|---|---|
| Setting | `greedy_capacity` | `strict_fifo` |
| When the next action does not fit | Skips it and schedules the actions behind it that fit | Stops and waits for it |
| Order | First come, first served among the actions that fit | Exactly first come, first served |
| Idle capacity while work is waiting | No | Yes, while the head of the line is blocked |
| Can a large action be starved? | Yes, while smaller actions keep fitting | No |
| Reusable containers (warm pools) | Actions for a warm pool that is already running keep flowing | Actions for a warm pool wait behind the blocked head |
| Use it for | Most queues | Gang-style jobs and strict ordering |

### The two policies side by side

Take a queue capped at 8 GPUs with 6 in use, so 2 are free. Three actions are
waiting, in this order:

| Position | Action | Asks for | Greedy capacity | Strict FIFO |
|---|---|---|---|---|
| 1 | `train` | 4 GPUs | Waits. It does not fit in the 2 free GPUs. | Waits. It does not fit in the 2 free GPUs. |
| 2 | `evaluate` | 1 GPU | Scheduled now. | Waits behind `train`. |
| 3 | `embed` | 1 GPU | Scheduled now. | Waits behind `train`. |

Under greedy capacity the queue runs at 8 of 8 GPUs, and `train` starts once 4
GPUs are free at the same moment. Under strict FIFO the queue stays at 6 of 8
until 2 more GPUs free up, then `train` starts, and only then do `evaluate` and
`embed` get their turn.

### Greedy capacity

Set with `--scheduling greedy_capacity`. Recommended for most queues.

**How it works.** The queue walks the line in arrival order. When an action does
not fit, the queue moves on to the next one and schedules whatever does fit.

**Use it when:**

- The queue carries a mix of small and large actions.
- The work runs in reusable containers.
- You want the capacity you are paying for to stay in use.

**Trade-off.** A very large action can wait a long time when smaller ones keep
arriving and keep fitting. If a queue carries both, move the large jobs to their
own strict FIFO queue, or give them a
[`max_queued_time`](../tasks/task-configuration/retries-and-timeouts#max_queued_time-fail-fast-when-capacity-isnt-available)
so they fail instead of waiting indefinitely.

### Strict FIFO

Set with `--scheduling strict_fifo`.

**How it works.** The queue schedules actions strictly in arrival order. When
the action at the head of the line does not fit, nothing behind it is scheduled
until it does. This is head-of-line blocking, and it is the point of the policy:
as running work finishes, the freed capacity accumulates for the head instead of
going to smaller actions that arrived later.

**Use it when:**

- You run gang-style jobs. A distributed training job that needs 32 GPUs at once
  only starts when 32 are free together. Under greedy capacity, a steady stream
  of one-GPU actions can take each GPU as it frees up, and the large job never
  gets its turn.
- Order matters, and work must start in the order it was submitted.

**Trade-off.** Capacity sits idle while the head waits, and every action behind
it waits too, even the ones that would fit.

### Reusable containers (warm pools)

A [reusable environment](../tasks/task-configuration/reusable-containers) keeps
a pool of warm containers alive and runs many actions in them. A queue counts
those containers against its caps once, when the pool starts, and not once per
action:

- **The first action** of an environment starts the pool. It is counted like any
  other request, at the size of the containers the pool starts with, and it has
  to fit under the cap.
- **Every later action** that joins the running pool adds nothing to the cap,
  because the containers it runs in are already counted.

This is where the two policies differ most:

| | Greedy capacity | Strict FIFO |
|---|---|---|
| Actions for a warm pool that is already running | Skip past a blocked action and are scheduled, since they add nothing to the cap | Wait behind the blocked head like everything else |
| The warm pool while a large action is blocked | Stays busy | Sits idle, even though its next action would cost the queue nothing |
| An action that starts a new pool | Scheduled if the pool fits. If it does not, the queue moves on to the next action | Scheduled if the pool fits. If it does not, it blocks the line |

On a strict FIFO queue with little free capacity, one large job at the head of
the line can stall every reusable environment on the queue. If the wait lasts
longer than an environment's idle timeout, its containers shut down, and the
next action pays for a cold start again.

Put work that runs in reusable containers on a greedy capacity queue. If the
same team also runs gang-style jobs, give those their own strict FIFO queue
instead of mixing the two on one.

### When the line is blocked

A strict FIFO queue reports when its head is blocked and for how long.
`flyte get queue <name> --watch` shows a head-of-line banner with the number of
actions waiting behind it, and the `flyte get queue --watch` dashboard marks the
queue as blocked. In Python, `Queue.details` returns `head_blocked` and
`head_blocked_since`.

A blocked head clears on its own as running work finishes. If the queue should
not be waiting on its head in the first place, switch it:

```bash
flyte update queue research --scheduling greedy_capacity
```

The change applies to the live queue, and the actions that fit are scheduled
shortly after.

## Resource-aware scheduling

Queues schedule against what your clusters can actually run. When Union knows
each cluster's configuration (its node pools, the size of the nodes in each
pool, the accelerators they carry, and how far each pool can scale), a queue
uses it for every placement:

- **It only considers clusters that can run the action.** Each container the
  action asks for must fit on a node of some node pool in the cluster: its
  requests within one node's capacity, its accelerator offered by the pool, and
  its node selector compatible with the pool's labels.
- **It waits instead of overfilling a cluster.** An action that fits the
  cluster's node pools but not the room left at full scale stays queued under
  the queue's scheduling policy. On a `strict_fifo` queue it holds the line.
- **It spreads load.** Among the clusters with room, the action goes to the
  least loaded one.

> [!NOTE] Union needs your cluster configuration
> Resource-aware scheduling depends on Union knowing the node pools of each
> cluster. Union BYOC deployments already have this. For self-managed
> deployments, talk to the Union team to have your cluster configuration set
> up. Until it is, a queue treats a cluster as able to run anything and places
> work on any healthy cluster it routes to. Resource caps and the scheduling
> policy apply either way.

## Infeasible requests fail fast

Some requests can never run, however long they wait. Leaving them in the queue
hides the problem and, on a `strict_fifo` queue, would block everything behind
them forever. The scheduler fails these actions as soon as it sees them.

An action fails as infeasible when:

- **It asks for more than the queue's whole cap.** An action that requests 64
  CPUs on a queue capped at 32 would not fit even on an empty queue.
- **It asks for GPUs without a type** and no default GPU type is configured.

Once your cluster configuration is in place, the same check extends to the
clusters themselves. This is rolling out now. An action also fails as infeasible
when no cluster its queue routes to could ever run it:

- It asks for an accelerator that none of those clusters has.
- One of its containers is larger than any node those clusters can launch.
- Its total request is more than those clusters hold at full scale.

An infeasible action fails with the error code `INFEASIBLE`. It is not retried,
since a retry would ask for the same thing. The error message names the request
and what the queue or the clusters offer, so you can tell whether to shrink the
request, route the task to a different queue, or raise the cap.

This is different from waiting. An action that fits the cap and the clusters but
not the room available right now stays queued and runs once capacity frees up.
To bound that wait, set
[`max_queued_time`](../tasks/task-configuration/retries-and-timeouts#max_queued_time-fail-fast-when-capacity-isnt-available)
on the task.

## See also

- [Managing queues](./queues): create, drain, move, and delete queues.
- [Queues in Configure tasks](../tasks/task-configuration/queues): route work to
  a queue from task code.
- [Reusable containers](../tasks/task-configuration/reusable-containers): how
  reusable environments are sized.
