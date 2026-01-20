---
title: Scale your runs
weight: 11
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Scale your runs

This guide helps you understand and optimize the performance of your Flyte workflows. Whether you're building latency-sensitive applications or high-throughput data pipelines, these docs will help you make the right architectural choices.

## Understanding Flyte execution

Before optimizing performance, it's important to understand how Flyte executes your workflows:

- **[Data flow](./data-flow)**: Learn how data moves between tasks, including inline vs. reference data types, caching mechanisms, and storage configuration.
- **[Life of a run](./life-of-a-run)**: Understand what happens when you invoke `flyte.run()`, from code analysis and image building to task execution and state management.

## Performance optimization

Once you understand the fundamentals, dive into performance tuning:

- **[Scale your workflows](./scale-your-workflows)**: A comprehensive guide to optimizing workflow performance, covering latency vs. throughput, task overhead analysis, batching strategies, reusable containers, and more.

## Key concepts for scaling

When scaling your workflows, keep these principles in mind:

1. **Task overhead matters**: The overhead of creating a task (uploading data, enqueuing, creating containers) should be much smaller than the task runtime.
2. **Batch for throughput**: For large-scale data processing, batch multiple items into single tasks to reduce overhead.
3. **Reusable containers**: Eliminate container startup overhead and enable concurrent execution with reusable containers.
4. **Traces for lightweight ops**: Use traces instead of tasks for lightweight operations that need checkpointing.
5. **Limit fanout**: Keep the total number of actions per run below 50k (target 10k-20k for best performance).
6. **Choose the right data types**: Use reference types (files, directories, DataFrames) for large data and inline types for small data.

For detailed guidance on each of these topics, see [Scale your workflows](./scale-your-workflows).
