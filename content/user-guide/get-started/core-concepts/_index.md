---
title: Core concepts
description: 'The building blocks of every Flyte program: TaskEnvironments, tasks, runs, actions, and apps.'
icon: book
weight: 2
variants: +flyte +union
---

# Core concepts

The [Quickstart](../quickstart) ran a workflow without stopping to explain it. This section
explains it, one concept at a time, each with an example you can run yourself.

## How a Flyte program fits together

Four pieces do most of the work:

1. A **TaskEnvironment** declares the container image, the resources, and the secrets that a
   group of tasks share.
2. A **task** is a Python function you decorate with `@env.task`. It runs remotely, in that
   environment.
3. Calling a task creates a **run**, which tracks the whole execution from start to finish.
4. Every task execution inside that run is an **action**, recorded on its own so it can be
   retried, cached, and inspected separately.

Two more ideas sit on top. An **app** is a long-running service rather than a job that finishes,
and **projects and domains** decide where a run lives and what it is allowed to reach.

The pages below build on each other, so read them in order if you are new. The last one puts
every piece together in a project you can deploy.

{{< subpage-cards >}}
