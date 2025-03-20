---
title: Defining launch plans
weight: 1
variants: +flyte +serverless +byoc +byok
---

# Defining launch plans

You can define a launch plan with the [`LaunchPlan` class]().
<!-- TODO: Add link to API -->

For example:

```python
import {{< key kit_import >}}

@{{< key kit_as >}}.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@{{< key kit_as >}}.workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)

{{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5}
)
```

In this example, we define a task `my_task` and a workflow `my_workflow`.
We then define a launch plan for `my_workflow`.
The launch plan is declared by calling `LaunchPlan.get_or_create` with the workflow name, launch plan name, and the desired default and fixed inputs. If you do not supply a launch plan name, the default launch plan (which has the same name as the workflow) is assumed.

> [!NOTE]
> In the above code the `LaunchPlan` object returned by `get_or_create()` is not assigned to a variable.
> However, you can assign the launch plan object to a variable and reference the variable elsewhere in your code, allowing you to control when the launch plan is invoked. For more details, see [Running launch plans)(running-launch-plans).

## Launch plan inputs

A launch plan can be defined with:

* Some (or all) workflow inputs unspecified.
  These must be provided at execution time.
  In the UI, they appear in the **Launch Workflow** dialog as empty input fields.

* Some (or all) workflow inputs specified as default, with values.
  These may be provided as overrides at execution time, but if not, the default values are used.
  In the UI, they appear in the **Launch Workflow** dialog as pre-filled input fields that can be changed.

* Some (or all) workflow inputs specified as fixed, with values.
  These cannot be overridden at execution time.
  They are not shown in the **Launch Workflow** dialog.

