# Workflow structure

## When should I decompose tasks?

There are several reasons why one may choose to decompose a task into smaller tasks. Doing so may result in better computational performance, improved cache performance, and taking advantage of interruptible tasks. However, decomposition comes at the cost of the overhead among tasks, including spinning up nodes and downloading data. In some cases, these costs may be remediated by using Union Actors.

Firstly, decomposition provides support for heterogeneous environments among the operations in the task. For example, you may have some large task that trains a machine learning model and then uses the model to run batch inference on your test data. However, training a model typically requires significantly more memory than inference. For that reason, given large enough scale, it could actually be beneficial to decompose this large task into two tasks that (1) train a model and then (2) run batch inference. By doing so, you could request significantly less memory for the second task in order to save on the expense of this workflow. If you are working with even more data, then you might benefit from decomposing the batch inference task via map_task such that you may further parallelize this operation, substantially reducing the runtime of this step. Generally speaking, decomposition provides infrastructural flexibility regarding the ability to define resources, dependencies, and execution parallelism.

Secondly, you may decompose large tasks into smaller tasks to enable “fine-grained” caching. In other words, each unique task provides an automated “checkpoint” system. Thus, by breaking down a large workflow into its many natural tasks, one may minimize redundant work among multiple serial workflow executions. This is especially useful during rapid, iterative development, during which a user may attempt to run the same workflow multiple times in a short period of time. “Fine-grained” caching will dramatically improve productivity while executing workflows both locally and remotely.

Lastly, one may utilize “fine-grained” caching to leverage interruptible tasks. Interruptible tasks will attempt to run on spot instances or spot VMs, where possible. These nodes are interruptible, meaning that the task may occasionally fail due to another organization willing to pay more to use it. However, these spot instances can be substantially cheaper than their non-interruptible counterparts (on-demand instances / VMs). By utilizing “fine-grained” caching, one may reap the significant cost savings on interruptible tasks while minimizing the effects of having their tasks being interrupted.

## When should I parallelize tasks?

## When should I use caching?
