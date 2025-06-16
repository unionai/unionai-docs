---
title: AWS Sagemaker plugin
weight: 4
variants: +flyte -serverless -byoc -selfmanaged
---

# Sagemaker Plugin Setup


This guide gives an overview of how to set up Sagemaker in your Flyte deployment.

> The Sagemaker plugin needs Flyte deployment in AWS cloud; sandbox/GCP/Azure won't work.

## Prerequisites

* Flyte cluster in [AWS](https://docs.flyte.org/en/latest/deployment/aws/index.html#deployment-aws)
* [AWS role set up for SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html)
* [AWS SageMaker K8s operator](https://github.com/aws/amazon-sagemaker-operator-for-k8s) is installed in your k8s cluster
* Correct kubeconfig and Kubernetes context
* Correct FlyteCTL config at `~/.flyte/config.yaml`

## Specify Plugin Configuration

Create a file named ``values-override.yaml`` and add the following config to it.
Please make sure that the propeller has the correct service account for Sagemaker.

```yaml
    configmap:
      enabled_plugins:
        # -- Tasks specific configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#GetConfig)
        tasks:
          # -- Plugins configuration, [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#TaskPluginConfig)
          task-plugins:
            # -- [Enabled Plugins](https://pkg.go.dev/github.com/flyteorg/flyteplugins/go/tasks/config#Config).
            # plugins
            enabled-plugins:
              - container
              - sidecar
              - k8s-array
              - sagemaker_training
              - sagemaker_hyperparameter_tuning
            default-for-task-types:
              container: container
              sidecar: sidecar
              container_array: k8s-array
```
## Upgrade the Flyte Helm release

```bash
helm upgrade -n flyte -f values-override.yaml flyteorg/flyte-core
```

## Register the Sagemaker plugin example


```bash
flytectl register files https://github.com/flyteorg/flytesnacks/releases/download/v0.3.0/snacks-cookbook-integrations-aws-sagemaker_training.tar.gz --archive -p flytesnacks -d development
```

### Launch an execution

#### Flyte console UI

* Navigate to Flyte Console's UI (e.g. `sandbox <http://localhost:30081/console>`_) and find the workflow.
* Click on `Launch` to open up the launch form.
* Submit the form.

#### flytectl

Retrieve an execution form in the form of a YAML file:

```bash
flytectl get launchplan --config ~/.flyte/flytectl.yaml \
    --project flytesnacks \
    --domain development \
    sagemaker_training.sagemaker_custom_training.mnist_trainer \
    --latest \
    --execFile exec_spec.yaml
 ```
Launch! 🚀

```bash
flytectl --config ~/.flyte/flytectl.yaml create execution \
    -p <project> -d <domain> --execFile ~/exec_spec.yaml
```
