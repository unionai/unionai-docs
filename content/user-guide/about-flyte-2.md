---
title: About Flyte SDK 2
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# About Flyte SDK 2

Flyte SDK 2 is the new toolkit for deploying and managing your Union .aiinstance.

## What has changed?

Flyte 2 introduces several key improvements:

### Pure Python Execution

* The SDK allows you to write workflows in pure Python, enabling a more natural and flexible development experience.
* In the old Flytekit, individual tasks were written in Python, but the workflow DAG was defined as in a Python-like DSL which lacked the power and flexibility of Python.
* In Flyte SDK 2, you can define both tasks and "workflows" using standard Python.
* In fact, your "workflow" is now just another task, which simply calls other tasks in a specific order.

### Radically simplified API

* The API has been streamlined to make it easier to use and understand.
* The new API is more intuitive, with fewer abstractions and a focus on simplicity.
* This makes it easier for developers to get started and build complex workflows without getting bogged down in unnecessary complexity.

### Task Environments

* Tasks are defined within environments, which encapsulate the context and resources needed for execution.

### Workflows are now Tasks

* Because workflows can now be written in pure Python, they no longer require a separate construct
* You simply define your workflow as a function (with a `@task` decorator) and have it call other tasks.
* You can still think of it abstractly as a workflow, but it is now implemented (and coded) as a top-level task that orchestrates other tasks.
