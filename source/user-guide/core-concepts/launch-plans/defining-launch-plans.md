# Defining launch plans

You can define a launch plan with the [`flytekit.LaunchPlan` class](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.LaunchPlan.html#flytekit.LaunchPlan).

For example:

```{literalinclude} ../../../_static/includes/core-concepts/launch-plans/defining-launch-plans/example_1.py
:language: python
```

In this example, we define a task `my_task` and a workflow `my_workflow`.
We then define a launch plan for `my_workflow`.
The launch plan is declared by calling `LaunchPlan.get_or_create` with the workflow name, launch plan name, and the desired default and fixed inputs. If you do not supply a launch plan name, the default launch plan (which has the same name as the workflow) is assumed.

```{note}
In the above code the `LaunchPlan` object returned by `get_or_create()` is not assigned to a variable.
However, you can assign the launch plan object to a variable and reference the variable elsewhere in your code, allowing you to control when the launch plan is invoked. For more details, see [Running Launch Plans)(running-launch-plans).
```

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

