---
title: Task hardware environment
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Task hardware environment

## Customizing task resources

{{< variant serverless >}}
{{< markdown >}}

You can customize the hardware environment in which your task code executes through configuration in the `@{{< key kit_as >}}.task` decorator by specifying `requests` and `limits` on:

* CPU number
* GPU number
* Memory size
* Ephemeral storage size

See [Customizing task resources](./customizing-task-resources) for details.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

You can customize the hardware environment in which your task code executes.

Depending on your needs, there are two different of ways to define and register tasks with their own custom hardware requirements:

* Configuration in the `@{{< key kit_as >}}.task` decorator
* Defining a `PodTemplate`

### Using the `@{{< key kit_as >}}.task` decorator

You can specify `requests` and `limits` on:

* CPU number
* GPU number
* Memory size
* Ephemeral storage size

See [Customizing task resources](./customizing-task-resources) for details.

### Using PodTemplate

If your needs are more complex, you can use Kubernetes-level configuration to constrain a task to only run on a specific machine type.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

This requires that you set up the required machine types and node groups with the appropriate node assignment configuration (node selector labels, node affinities, taints, tolerations, etc.)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

This requires that you coordinate with {{< key product_name >}} to set up the required machine types and node groups with the appropriate node assignment configuration (node selector labels, node affinities, taints, tolerations, etc.)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

In your task definition you then use a `PodTemplate` that that uses the matching node assignment configuration to make sure that the task will only be scheduled on the appropriate machine type.

### `pod_template` and `pod_template_name` @{{< key kit_as >}}.task parameters

The `pod_template` parameter can be used to supply a custom Kubernetes `PodTemplate` to the task.
This can be used to define details about node selectors, affinity, tolerations, and other Kubernetes-specific settings.

The `pod_template_name` is a related parameter that can be used to specify the name of an already existing `PodTemplate` resource which will be used in this task.

For details see [Configuring task pods with Kubernetes PodTemplates]().
<!-- TODO: Add link to API -->

{{< /markdown >}}
{{< /variant >}}

## Accelerators

If you specify GPUs, you can also specify the type of GPU to be used by setting the `accelerator` parameter.
See [Accelerators](./accelerators) for more information.

## Task-level monitoring

You can also monitor the hardware resources used by a task.
See [Task-level monitoring](./task-level-monitoring) for details.
