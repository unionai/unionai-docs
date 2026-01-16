---
title: Flyte basics
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Flyte basics

Now that you've completed the [Quickstart](../quickstart) and [set up your local environment](../local-setup), let's explore Flyte's core concepts through working examples.

By the end of this section, you'll understand:

- **TaskEnvironment**: The container configuration that defines where and how your code runs
- **Tasks**: Python functions that execute remotely in containers
- **Runs and Actions**: How Flyte tracks and manages your executions
- **Apps**: Long-running services for APIs, dashboards, and inference endpoints

Each concept is introduced with a practical example you can run yourself.

## How Flyte works

When you run code with Flyte, here's what happens:

1. You define a **TaskEnvironment** that specifies the container image and resources
2. You decorate Python functions with `@env.task` to create **tasks**
3. When you execute a task, Flyte creates a **run** that tracks the execution
4. Each task execution within a run is an **action**

Let's explore each of these in detail.
