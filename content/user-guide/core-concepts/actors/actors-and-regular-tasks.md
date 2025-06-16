---
title: Actors and regular tasks
weight: 1
variants: -flyte +serverless +byoc +selfmanaged
---

# Actors and regular tasks

When deciding whether to use actors or traditional tasks in your workflows, it's important to consider the benefits
and trade-offs. This page outlines key scenarios where actors shine and where they may not be the best fit.

| When to Use Actors | When Not to Use Actors |
| ------------------ | ---------------------- |
| **Short Running Tasks** Traditional tasks spin up a new container and pod for each task, which adds overhead. Actors allow tasks to run on the same container, removing the repeated cost of pod creation, image pulling, and initialization. Actors offer the most benefit for short running tasks where the startup overhead is a larger component of total task runtime. | **Long Running Tasks** For long running tasks, container initialization overhead is minimal, therefore the performance benefits of actors become negligible when task runtime significantly exceeds startup time. |
| **Map Tasks with Large Input Arrays** Map tasks by default share the same image and resource definitions, making them a great use case for actors. Actors provide the greatest benefit when the input array is larger than the desired concurrency. For example, consider an input array with 2,000 entries and a concurrency level of 50. Without actors, map tasks would spin up 2,000 individual containers—one for each entry. With actors, only 50 containers are needed, corresponding to the number of replicas, dramatically reducing overhead. | **Map Tasks with Small Input Arrays** In a map task where the number of actor replicas matches the input array size, the same number of pods and container are initialized when a map task is used without an actor. For example, if there are 10 inputs and 10 replicas, 10 pods are created, resulting in no reduction in overhead. |
| **State Management and Efficient Initialization** Actors excel when state persistence between tasks is valuable. You can use `@actor_cache` to cache Python objects. For example, this lets you load a large model or dataset into memory once per replica, and access it across tasks run on that replica. You can also serve a model or initialize shared resources in an init container. Each task directed to that actor replica can then reuse the same model or resource. | **Strict Task Isolation Is Critical** While actors clear Python caches, global variables, and custom environment variables after each task, they still share the same container. The shared environment introduces edge cases where you could intentionally or unintentionally impact downstream tasks. For example, if you write to a file in one task, that file will remain mutated for the next task that is run on that actor replica. If strict isolation between tasks is a hard requirement, regular tasks provide a safer option. |
| **Shared Dependencies and Resources** If multiple tasks can use the same container image and have consistent resource requirements, actors are a natural fit. | |

# Efficiency Gains from Actors with Map Tasks

Let's see how using Actors with map tasks can cut runtime in half!

We compare three scenarios:

1. **Regular map tasks without specifying concurrency.** This is the fasted expected configuration as flyte will spawn as many pods as there are elements in the input array, allowing Kubernetes to manage scheduling based on available resources.
2. **Regular map tasks with fixed concurrency.** This limits the number of pods that are alive at any given time.
3. **Map tasks with Actors.** Here we set the number of replicas to match the concurrency of the previous example.

These will allow us to compare actors to vanilla map tasks when both speed is maximized and when alive pods are matched one-to-one.

## "Hello World" Benchmark

This benchmark simply runs a task that returns "Hello World", which is a near instantaneous task.

| Task Type      | Concurrency/Replicas | Duration (seconds) |
| -------------- | -------------------- | ------------------ |
| Without Actors | unbound              | 111                |
| Without Actors | 25                   | 1195               |
| With Actors    | 25                   | 42                 |

**Key Takeaway:** For near instantaneous tasks, using a 25-replica Actor with map tasks reduces runtime by 96% if live pods are matched, and 62% when map task concurrency is unbounded.

## "5s Sleep" Benchmark

This benchmark simply runs a task that sleeps for five seconds.

| Task Type      | Concurrency/Replicas | Duration (seconds) |
| -------------- | -------------------- | ------------------ |
| Without Actors | unbound              | 174                |
| Without Actors | 100                  | 507                |
| With Actors    | 100                  | 87                 |

**Key Takeaway:** For five-second long tasks, using a 100-replica Actor with map tasks reduces runtime by 83% if live pods are matched, and 50% when map task concurrency is unbounded.

If you have short running map tasks, you can cut your runtime in half. If you are already using concurrency limits on your map tasks, you can expect even better improvements!
