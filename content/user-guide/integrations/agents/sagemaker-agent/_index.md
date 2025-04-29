---
title: AWS SageMaker inference connector
weight: 2
variants: +flyte -serverless +byoc +byok
sidebar_expanded: false
---

# AWS SageMaker inference connector

The AWS SageMaker inference connector allows you to deploy models, and create and trigger inference endpoints. You can also fully remove the SageMaker deployment.

## Installation

To use the AWS SageMaker inference connector, run the following command:

```
pip install flytekitplugins-awssagemaker
```

## Example usage

For a usage example, see [AWS SageMaker inference connector example](./sagemaker-connector-example).

## Local testing

To test the SageMaker inference connector locally, create a class for the connector task that inherits from [`AsyncConnctorExecutorMixin`](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354). This mixin can handle synchronous tasks and allows {{< key kit_name >}} to mimic FlytePropeller's behavior in calling the connector.

{{< variant byoc byok >}}
{{< markdown >}}

## {{< key product_name >}} cluster deployment

After you have finished testing the connector locally, contact the {{< key product_name >}} team to enable it in your cluster.

{{< /markdown >}}
{{< /variant >}}
