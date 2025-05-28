---
title: SageMaker connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: false
---

# SageMaker connector

The SageMaker connector allows you to deploy models, and create and trigger inference endpoints.
You can also fully remove the SageMaker deployment.

## Installation

To use the SageMaker connector, run the following command:

```shell
$ pip install flytekitplugins-awssagemaker
```

## Example usage

{{< variant flyte >}}
{{< markdown >}}

For an example query, see [SageMaker connector example usage](./sagemaker-inference-connector-example-usage)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

For an example query, see [SageMaker connector example usage](./sagemaker-inference-connector-example-usage-union)

{{< /markdown >}}
{{< /variant >}}

## Local testing

To test an connector locally, create a class for the connector task that inherits from
[SyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L304)
or [AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
These mixins can handle synchronous and synchronous tasks, respectively, and allow the SDK to mimic the system's behavior in calling the connector.

For more information, see [Testing connectors locally](../#testing-your-connector-locally).

{{< variant flyte >}}
{{< markdown >}}

## Flyte deployment configuration

To enable the AWS SageMaker inference connector in your Flyte deployment, refer to the [AWS SageMaker inference connector setup guide](../../../deployment/flyte-connectors/sagemaker-inference).

{{< /markdown >}}
{{< /variant >}}
