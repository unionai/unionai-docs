# AWS SageMaker inference connector

The AWS SageMaker inference connector allows you to deploy models, and create and trigger inference endpoints. You can also fully remove the SageMaker deployment.

## Installation

To use the AWS SageMaker inference connector, run the following command:

```
pip install flytekitplugins-awssagemaker
```

## Example usage

For a usage example, see [AWS SageMaker inference connector example](./sagemaker-connector-example.md).

## Local testing

To test the SageMaker inference connector locally, create a class for the connector task that inherits from [`AsyncConnectorExecutorMixin`](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_connector.py#L278-382). This mixin can handle synchronous tasks and allows Flytekit to mimic FlytePropeller's behavior in calling the connector.

{@@ if byoc @@}
## Union cluster deployment

After you have finished testing the connector locally, contact the Union team to enable it in your cluster.
{@@ endif @@}