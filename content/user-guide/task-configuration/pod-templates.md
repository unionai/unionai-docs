---
title: Pod templates
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Pod templates

The `pod_template` parameter in `TaskEnvironment` (and in the @env.task decorator, if you are overriding) allows you to customize the Kubernetes pod specification that will be used to run your tasks.
This provides fine-grained control over the underlying Kubernetes resources, enabling you to configure advanced pod settings like image pull secrets, environment variables, labels, annotations, and other pod-level configurations.

## Overview

Pod templates in Flyte allow you to:

- **Configure pod metadata**: Set custom labels and annotations for your pods.
- **Specify image pull secrets**: Access private container registries.
- **Set environment variables**: Configure container-level environment variables.
- **Customize pod specifications**: Define advanced Kubernetes pod settings.
- **Control container configurations**: Specify primary container settings.

The `pod_template` parameter accepts either a string reference or a `PodTemplate` object that defines the complete pod specification.

## Basic usage

Here's a complete example showing how to use pod templates with a `TaskEnvironment`:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/pod-templates/pod_template.py" fragment="pod-template" lang="python" >}}

## PodTemplate components

The `PodTemplate` class provides the following parameters for customizing your pod configuration:

```python
pod_template = flyte.PodTemplate(
    primary_container_name: str = "primary",
    pod_spec: Optional[V1PodSpec] = None,
    labels: Optional[Dict[str, str]] = None,
    annotations: Optional[Dict[str, str]] = None
)
```

### Parameters

- **`primary_container_name`** (`str`, default: `"primary"`): Specifies the name of the main container that will run your task code. This must match the container name defined in your pod specification.

- **`pod_spec`** (`Optional[V1PodSpec]`): A standard Kubernetes `V1PodSpec` object that defines the complete pod specification. This allows you to configure any pod-level setting including containers, volumes, security contexts, node selection, and more.

- **`labels`** (`Optional[Dict[str, str]]`): Key-value pairs used for organizing and selecting pods. Labels are used by Kubernetes selectors and can be queried to filter and manage pods.

- **`annotations`** (`Optional[Dict[str, str]]`): Additional metadata attached to the pod that doesn't affect pod scheduling or selection. Annotations are typically used for storing non-identifying information like deployment revisions, contact information, or configuration details.
