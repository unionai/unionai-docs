---
title: Launch plans
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Launch plans

A launch plan is a template for a workflow invocation.
It brings together:

* A [workflow](../workflows)
* A (possibly partial) set of inputs required to initiate that workflow
* Optionally, [notifications](./notifications) and [schedules](./schedules)

When invoked, the launch plan starts the workflow, passing the inputs as parameters.
If the launch plan does not contain the entire set of required workflow inputs, additional input arguments must be provided at execution time.

## Default launch plan

Every workflow automatically comes with a *default launch plan*.
This launch plan does not define any default inputs, so they must all be provided at execution time.
A default launch plan always has the same name as its workflow.

## Launch plans are versioned

Like tasks and workflows, launch plans are versioned.
A launch plan can be updated to change, for example, the set of inputs, the schedule, or the notifications.
Each update creates a new version of the launch plan.

## Custom launch plans

Additional launch plans, other than the default one, can be defined for any workflow.
In general, a given workflow can be associated with multiple launch plans, but a given launch plan is always associated with exactly one workflow.

## Viewing launch plans for a workflow

To view the launch plans for a given workflow, in the UI, navigate to the workflow's page and click **Launch Workflow**.
You can choose which launch plan to use to launch the workflow from the **Launch Plan** dropdown menu.
The default launch plan will be selected by default. If you have not defined any custom launch plans for the workflow, only the default plan will be available.
If you have defined one or more custom launch plans, they will be available in the dropdown menu along with the default launch plan.
For more details, see [Running launch plans](./running-launch-plans).

## Registering a launch plan

### Registering a launch plan on the command line

In most cases, launch plans are defined alongside the workflows and tasks in your project code and registered as a bundle with the other entities using the CLI (see [Running your code](../../development-cycle/running-your-code)).

### Registering a launch plan in Python with `{{< key kit_remote >}}`

As with all {{< key product_name >}} command line actions, you can also perform registration of launch plans programmatically with [`{{< key kit_remote >}}`](../../development-cycle/union-remote), specifically, `{{< key kit_remote >}}.register_launch_plan`.

### Results of registration

When the code above is registered to {{< key product_name >}}, it results in the creation of four objects:

* The task `workflows.launch_plan_example.my_task`
* The workflow `workflows.launch_plan_example.my_workflow`
* The default launch plan `workflows.launch_plan_example.my_workflow` (notice that it has the same name as the workflow)
* The custom launch plan `my_workflow_custom_lp` (this is the one we defined in the code above)

### Changing a launch plan

Launch plans are changed by altering their definition in code and re-registering.
When a launch plan with the same project, domain, and name as a preexisting one is re-registered, a new version of that launch plan is created.
