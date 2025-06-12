---
title: Error handling
weight: 60
variants: +flyte +serverless +byoc +selfmanaged
---

# Error handling

One of the key features of Flyte 2 is the ability to recover from user-level errors in a workflow execution.
This includes out-of-memory errors and other exceptions.

This is a direct result of the fact that workflows are now written in regular Python, and provide you with all the power and flexibility of Python error handling.
Let's look at an example:

{{< code file="/external/migrate-to-unionai-examples-flyte2/error_handling.py" lang="python" >}}

In this code, we do the following:

* Import the necessary modules
* Set up the task environment. Note that we define our task environment with a resource allocation of 1 CPU and 250 MiB of memory.
* Define two tasks: one that will intentionally cause an out-of-memory (OOM) error, and another that will always succeed.
* Define the main task (the top level workflow task) that will handle the failure recovery logic.

The top `try...catch` block attempts to run the `oomer` task with a parameter that is likely to cause an OOM error.
If the error occurs, it catches the `flyte.errors.OOMError` and attempts to run the `oomer` task again with increased resources.

This type of dynamic error handling allows you to gracefully recover from user-level errors in your workflows.
