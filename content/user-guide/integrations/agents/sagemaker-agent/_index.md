---
title: AWS SageMaker inference agent
weight: 1
variants: +flyte +serverless +byoc +byok
---

# AWS SageMaker inference agent

The AWS SageMaker inference agent allows you to deploy models, and create and trigger inference endpoints. You can also fully remove the SageMaker deployment.

## Installation

To use the AWS SageMaker inference agent, run the following command:

```
pip install flytekitplugins-awssagemaker
```

## Example usage

For a usage example, see [AWS SageMaker inference agent example](./sagemaker-agent-example.md).

## Local testing

To test the SageMaker inference agent locally, create a class for the agent task that inherits from [`AsyncAgentExecutorMixin`](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_agent.py#L278-382). This mixin can handle synchronous tasks and allows Flytekit to mimic FlytePropeller's behavior in calling the agent.

{{< if-variant byoc byok >}}
## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.
{{< /if-variant >}}