---
title: Building workflows
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Building workflows

## When should I decompose tasks?

There are several reasons why one may choose to decompose a task into smaller tasks.
Doing so may result in better computational performance, improved cache performance, and taking advantage of interruptible tasks.
However, decomposition comes at the cost of the overhead among tasks, including spinning up nodes and downloading data.
In some cases, these costs may be remediated by using [Actors](../core-concepts/actors).

### Differing runtime requirements

Firstly, decomposition provides support for heterogeneous environments among the operations in the task.
For example, you may have some large task that trains a machine learning model and then uses the model to run batch inference on your test data.
However, training a model typically requires significantly more memory than inference.
For that reason, given large enough scale, it could actually be beneficial to decompose this large task into two tasks that (1) train a model and then (2) run batch inference.
By doing so, you could request significantly less memory for the second task in order to save on the expense of this workflow.
If you are working with even more data, then you might benefit from decomposing the batch inference task via `map_task` such that you may further parallelize this operation, substantially reducing the runtime of this step.
Generally speaking, decomposition provides infrastructural flexibility regarding the ability to define resources, dependencies, and execution parallelism.

### Improved cache performance

Secondly, you may decompose large tasks into smaller tasks to enable “fine-grained” caching.
In other words, each unique task provides an automated “checkpoint” system.
Thus, by breaking down a large workflow into its many natural tasks, one may minimize redundant work among multiple serial workflow executions.
This is especially useful during rapid, iterative development, during which a user may attempt to run the same workflow multiple times in a short period of time.
“Fine-grained” caching will dramatically improve productivity while executing workflows both locally and remotely.

### Take advantage of interruptible tasks

Lastly, one may utilize “fine-grained” caching to leverage interruptible tasks.
Interruptible tasks will attempt to run on spot instances or spot VMs, where possible.
These nodes are interruptible, meaning that the task may occasionally fail due to another organization willing to pay more to use it.
However, these spot instances can be substantially cheaper than their non-interruptible counterparts (on-demand instances / VMs).
By utilizing “fine-grained” caching, one may reap the significant cost savings on interruptible tasks while minimizing the effects of having their tasks being interrupted.

## When should I parallelize tasks?

In general, parallelize early and often.
A lot of {{< key product_name >}}’s powerful ergonomics like caching and workflow recovery happen at the task level, as mentioned above.
Decomposing into smaller tasks and parallelizing enables for a performant and fault-tolerant workflow.

One caveat is for very short duration tasks, where the overhead of spinning up a pod and cleaning it up negates any benefits of parallelism.
With reusable containers via [Actors](../core-concepts/actors), however, these overheads are transparently obviated, providing the best of both worlds at the cost of some up-front work in setting up that environment.
In any case, it may be useful to batch the inputs and outputs to amortize any overheads.
Please be mindful to keep the sequencing of inputs within a batch, and of the batches themselves, to ensure reliable cache hits.

### Parallelization constructs

The two main parallelization constructs in {{< key product_name >}} are the [map task](../core-concepts/tasks/task-types#map-tasks) and the [dynamic workflow](../core-concepts/workflows/dynamic-workflows).
They accomplish roughly the same goal but are implemented quite differently and have different advantages.

Dynamic tasks are more akin to a `for` loop, iterating over inputs sequentially.
The parallelism is controlled by the overall workflow parallelism.

Map tasks are more efficient and have no such sequencing guarantees.
They also have their own concurrency setting separate from the overall workflow and can have a minimum failure threshold of their constituent tasks.
A deeper explanation of their differences is available [here]() while examples of how to use them together can be found [here]().

## When should I use caching?

Caching should be enabled once the body of a task has stabilized.
Cache keys are implicitly derived from the task signature, most notably the inputs and outputs.
If the body of a task changes without a modification to the signature, and the same inputs are used, it will produce a cache hit.
This can result in unexpected behavior when iterating on the core functionality of the task and expecting different inputs downstream.
Moreover, caching will not introspect the contents of a `FlyteFile` for example.
If the same URI is used as input with completely different contents, it will also produce a cache hit.
For these reasons, it’s wise to add an explicit cache key so that it can be invalidated at any time.

Despite these caveats, caching is a huge time saver during workflow development.
Caching upstream tasks enable a rapid run through of the workflow up to the node you’re iterating on.
Additionally, caching can be valuable in complex parallelization scenarios where you’re debugging the failure state of large map tasks, for example.
In production, if your cluster is under heavy resource constraints, caching can allow a workflow to complete across re-runs as more and more tasks are able to return successfully with each run.
While not an ideal scenario, caching can help soften the blow of production failures.
With these caveats in mind, there are very few scenarios where caching isn’t warranted.

