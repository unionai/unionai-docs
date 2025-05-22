---
title: Chaining entities
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Chaining Entities

{{< key product_name >}} offers a mechanism for chaining entities using the `>>` operator. This is particularly valuable when chaining tasks and subworkflows without the need for data flow between the entities.

## Tasks

Let’s establish a sequence where `t1()` occurs after `t0()`, and `t2()` follows `t1()`.

```python
import {{< key kit_import >}}

@{{< key kit_as >}}.task
def t2():
    print("Running t2")
    return


@{{< key kit_as >}}.task
def t1():
    print("Running t1")
    return


@{{< key kit_as >}}.task
def t0():
    print("Running t0")
    return

# Chaining tasks
@{{< key kit_as >}}.workflow
def chain_tasks_wf():
    t2_promise = t2()
    t1_promise = t1()
    t0_promise = t0()

    t0_promise >> t1_promise
    t1_promise >> t2_promise
```

## Subworkflows

Just like tasks, you can chain subworkflows.

```python
@{{< key kit_as >}}.workflow
def sub_workflow_1():
    t1()


@{{< key kit_as >}}.workflow
def sub_workflow_0():
    t0()


@{{< key kit_as >}}.workflow
def chain_workflows_wf():
    sub_wf1 = sub_workflow_1()
    sub_wf0 = sub_workflow_0()

    sub_wf0 >> sub_wf1
```

> [!NOTE]
> Chaining tasks and subworkflows is not supported in local Python environments.
