---
title: AWS SageMaker Inference Connector
weight: 1
variants: +flyte -serverless -byoc -byok
sidebar_expanded: false
---

# AWS SageMaker Inference Connector

The AWS SageMaker inference connector allows you to deploy models, and create and trigger inference endpoints.
You can also fully remove the SageMaker deployment.

## Installation

To use the AWS SageMaker inference connector, run the following command:

```shell
$ pip install flytekitplugins-awssagemaker
```

## Example usage

For a usage example, see [AWS SageMaker inference connector example usage](./sagemaker-inference-connector-example-usage)

## Local testing

To test an connector locally, create a class for the connector task that inherits from
[SyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L304)
or [AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
These mixins can handle synchronous and synchronous tasks, respectively,
and allow flytekit to mimic FlytePropeller's behavior in calling the connector.

<!-- TODO add back when page correctly relocated
For more information,
see "[Testing connectors locally](https://docs.flyte.org/en/latest/flyte_connectors/testing_connectors_in_a_local_python_environment.html)".
-->
## Flyte deployment configuration

> [!NOTE]
> If you are using a managed deployment of Flyte,
> you will need to contact your deployment administrator to configure connectors in your deployment.

To enable the AWS SageMaker inference connector in your Flyte deployment, refer to the
[AWS SageMaker inference connector setup guide](../../../deployment/flyte-connectors/sagemaker-inference).
