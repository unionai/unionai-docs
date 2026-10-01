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
flyte update queue research --max-accelerators H100=64

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
Queue.update("research", max_accelerators={"H100": 64})

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
> To raise CPU on a queue that also caps memory, pass both again.
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
Both policies consider actions in the order they were queued. They differ in
what happens at the first action that does not fit.

| | `strict_fifo` | `greedy_capacity` |
|---|---|---|
| When the next action does not fit | The queue stops and waits for it | The queue skips it and keeps going |
| Order of dispatch | Exactly first come, first served | First come, first served among the actions that fit |
| Can a large action be starved? | No | Yes, while smaller actions keep fitting |
| Can small actions be stuck behind a large one? | Yes | No |
| Use it for | Gang-style jobs and strict ordering | Most queues |

`strict_fifo` is the default for a new queue. Pass `--scheduling greedy_capacity`
(or `scheduling="greedy_capacity"` in Python) to choose the other policy.

### `strict_fifo`

The queue dispatches actions strictly in arrival order. When the action at the
head of the line does not fit, nothing behind it is dispatched until it does.
This is head-of-line blocking, and it is the point of the policy: as running
work finishes, the freed capacity accumulates for the head instead of being
handed to smaller actions that arrived later.

Use `strict_fifo` when:

- **You run gang-style jobs.** A distributed training job that needs 32 GPUs at
  once only starts when 32 are free together. Under `greedy_capacity` a steady
  stream of one-GPU actions can keep taking each GPU as it frees up, and the
  large job never gets its turn.
- **Order matters.** Work must start in the order it was submitted.

The cost is idle capacity. While the head waits, actions behind it wait too,
even when they would fit. That includes actions for a
[reusable environment](#how-the-policies-treat-reusable-environments) that is
already running.

### `greedy_capacity`

The queue still walks the line in arrival order, but when an action does not
fit it moves on to the next one and dispatches whatever does fit. Capacity is
not left idle while something that could use it is waiting.

This is the right choice for most queues: mixed workloads, many small and
medium actions, and anything built on reusable environments. The trade-off is
that a very large action can wait a long time when smaller ones keep arriving
and keep fitting. If a queue carries both, either move the large jobs to their
own `strict_fifo` queue or give them a
[`max_queued_time`](../tasks/task-configuration/retries-and-timeouts#max_queued_time-fail-fast-when-capacity-isnt-available)
so they fail instead of waiting indefinitely.

### How the policies treat reusable environments

A [reusable environment](../tasks/task-configuration/reusable-containers) keeps
a set of containers alive and runs many actions in them. A queue counts those
containers against its caps once, when the environment starts, and not once per
action. An action that joins an environment that is already running adds nothing
to the cap, because the containers it runs in are already counted.

The two policies treat those actions differently:

- Under **`greedy_capacity`**, the queue skips the blocked action and dispatches
  the actions behind it that fit. Actions for a running reusable environment
  add nothing to the cap, so they keep flowing while a large action waits for
  room.
- Under **`strict_fifo`**, they wait behind the blocked head like everything
  else. When capacity is low, a reusable environment can sit idle behind one
  large job even though running its next action would cost the queue nothing.

### When the line is blocked

A `strict_fifo` queue reports when its head is blocked and for how long.
`flyte get queue <name> --watch` shows a head-of-line banner with the number of
actions waiting behind it, and the `flyte get queue --watch` dashboard marks the
queue as blocked. In Python, `Queue.details` returns `head_blocked` and
`head_blocked_since`.

A blocked head clears on its own as running work finishes. If the queue should
not have been holding the line in the first place, switch it:

```bash
flyte update queue research --scheduling greedy_capacity
```

The change applies to the live queue, and the actions that fit are dispatched
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
