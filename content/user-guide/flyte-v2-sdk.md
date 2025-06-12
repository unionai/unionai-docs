---
title: Flyte v2 SDK
weight: 20
variants: +flyte +serverless +byoc +selfmanaged
---

# Introduction

The Flyte v2 SDK is the new toolkit for authoring workflows in Union.ai and Flyte v2.

## What has changed?

The SDK introduces several key improvements:

### Pure Python execution

* The SDK allows you to write workflows in pure Python, enabling a more natural and flexible development experience.
* In the previous Flytekit SDK, individual tasks were written in Python, but the workflow DAG was defined in a python-like, but not Python-native DSL (`@workflow`) which restricted users to static behavior (no loops, try-catch, or dynamic branching).
* In Flyte SDK 2, you can define both tasks and "workflows" using standard Python.
* In fact, your "workflow" is now just another task, which simply calls other tasks in a specific order.

### Radically simplified API

* The API has been streamlined to make it easier to understand and use.
* The new API is more intuitive, with fewer abstractions and a focus on simplicity.
* This makes it easier for developers to get started and build complex workflows without getting bogged down in unnecessary complexity.

### Task Environments

* Tasks are defined within Environments, which encapsulate the context and resources needed for execution.

### Workflows are now tasks

* Because workflows can now be written in pure Python, they no longer require a separate construct.
* You simply define your workflow as a function (with a `@task` decorator) and have it call other tasks.
* You can still think of it abstractly as a workflow, but it is now implemented (and coded) as a top-level task that orchestrates other tasks.
