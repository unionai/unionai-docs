---
title: AWS SageMaker agent example
weight: 1
variants: "+flyte +serverless +byoc +byok"
---

# AWS SageMaker agent example

## Deploy and serve an XGBoost model on AWS SageMaker using FastAPI

This example demonstrates how to deploy and serve an XGBoost model on SageMaker using FastAPI custom inference.

We train an XGBoost model on the Pima Indians Diabetes dataset and generate a `tar.gz` file to be stored in an S3 bucket.

{{< note >}}
The model artifact needs to be available in an S3 bucket for SageMaker to be able to access.
{{< /note >}}

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/sagemaker_inference_agent/sagemaker_inference_agent/sagemaker_inference_agent_example_usage.py
:language: python
:lines: 11-62
```

{{< note >}}
Replace `ghcr.io/flyteorg` with a container registry to which you can publish.
To upload the image to the local registry in the demo cluster, indicate the registry as `localhost:30000`.
{{< /note >}}

The above workflow generates a compressed model artifact that can be stored in an S3 bucket. Take note of the S3 URI.

To deploy the model on SageMaker, use the [`awssagemaker_inference.create_sagemaker_deployment`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.create_sagemaker_deployment.html#flytekitplugins.awssagemaker_inference.create_sagemaker_deployment) function.

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/sagemaker_inference_agent/sagemaker_inference_agent/sagemaker_inference_agent_example_usage.py
:language: python
:lines: 76-122
```

This function returns an imperative workflow responsible for deploying the XGBoost model, creating an endpoint configuration and initializing an endpoint. Configurations relevant to these tasks are passed to the `awssagemaker_inference.create_sagemaker_deployment` function.

An idempotence token ensures the generation of unique tokens for each configuration, preventing name collisions during updates.
By default, `idempotence_token` in `create_sagemaker_deployment` is set to `True`, causing the agent to append an idempotence token to the model name, endpoint config name, and endpoint.

- If a field value isn't provided (e.g., `ModelName`), the agent appends the idempotence token to the workflow name and uses that as the `ModelName`.
- You can also manually set the idempotence token by adding `{idempotence_token}` to the relevant fields in the configuration, e.g., `xgboost-{idempotence_token}`.

`sagemaker_image` should include the inference code, necessary libraries, and an entrypoint for model serving.

{{< note >}}
For more detailed instructions on using your custom inference image, refer to the [Amazon SageMaker documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html).
{{< /note >}}

If the plugin attempts to create a deployment that already exists, it will return the existing ARNs instead of raising an error.

{{< note >}}
When two executions run in parallel and attempt to create the same endpoint, one execution will proceed with creating the endpoint while both will wait until the endpoint creation process is complete.
{{< /note >}}

To receive inference requests, the container built with `sagemaker_image` must have a web server
listening on port 8080 and must accept POST and GET requests to the `/invocations` and `/ping` endpoints, respectively.

We define the FastAPI inference code as follows:

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/sagemaker_inference_agent/sagemaker_inference_agent/sagemaker_inference_agent_example_usage.py
:language: python
:lines: 155-208
```

Create a file named `serve` to serve the model. In our case, we are using FastAPI:

```shell
!/bin/bash

_term() {
echo "Caught SIGTERM signal!"
kill -TERM "$child" 2>/dev/null
}

trap _term SIGTERM

echo "Starting the API server"
uvicorn sagemaker_inference_agent_example_usage:app --host 0.0.0.0 --port 8080&

child=$!
wait "$child"
```

You can trigger the `sagemaker_deployment_wf` by providing the model artifact path, execution role ARN, and instance type.

Once the endpoint creation status changes to `InService`, the SageMaker deployment workflow succeeds.
You can then invoke the endpoint using the SageMaker agent as follows:

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/sagemaker_inference_agent/sagemaker_inference_agent/sagemaker_inference_agent_example_usage.py
:language: python
:lines: 237-246
```

The [`awssagemaker_inference.SageMakerInvokeEndpointTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerInvokeEndpointTask.html#flytekitplugins.awssagemaker_inference.SageMakerInvokeEndpointTask) invokes an endpoint asynchronously, resulting in an S3 location that will be populated with the output after it's generated. For instance, the inference_input file may include input like this: `[6, 148, 72, 35, 0, 33.6, 0.627, 50]`

To delete the deployment, you can instantiate a [`awssagemaker_inference.delete_sagemaker_deployment`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.delete_sagemaker_deployment.html#flytekitplugins.awssagemaker_inference.delete_sagemaker_deployment) function.

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/sagemaker_inference_agent/sagemaker_inference_agent/sagemaker_inference_agent_example_usage.py
:language: python
:lines: 255-266
```

You need to provide the endpoint name, endpoint config name, and the model name to execute this deletion, which removes the endpoint, endpoint config, and the model.

## Available tasks

You have the option to execute the SageMaker tasks independently. The following tasks are available for use:

- [`awssagemaker_inference.SageMakerModelTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerModelTask.html#flytekitplugins.awssagemaker_inference.SageMakerModelTask)
- [`awssagemaker_inference.SageMakerEndpointConfigTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerEndpointConfigTask.html#flytekitplugins.awssagemaker_inference.SageMakerEndpointConfigTask)
- [`awssagemaker_inference.SageMakerEndpointTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerEndpointTask.html#flytekitplugins.awssagemaker_inference.SageMakerEndpointTask)
- [`awssagemaker_inference.SageMakerDeleteEndpointTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerDeleteEndpointTask.html#flytekitplugins.awssagemaker_inference.SageMakerDeleteEndpointTask)
- [`awssagemaker_inference.SageMakerDeleteEndpointConfigTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerDeleteEndpointConfigTask.html#flytekitplugins.awssagemaker_inference.SageMakerDeleteEndpointConfigTask)
- [`awssagemaker_inference.SageMakerDeleteModelTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerDeleteModelTask.html#flytekitplugins.awssagemaker_inference.SageMakerDeleteModelTask)
- [`awssagemaker_inference.SageMakerInvokeEndpointTask`](https://docs.flyte.org/en/latest/api/flytekit/plugins/generated/flytekitplugins.awssagemaker_inference.SageMakerInvokeEndpointTask.html#flytekitplugins.awssagemaker_inference.SageMakerInvokeEndpointTask)

All tasks except the `awssagemaker_inference.SageMakerEndpointTask` inherit the `awssagemaker_inference.BotoTask`. The `awssagemaker_inference.BotoTask` provides the flexibility to invoke any [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) method. If you need to interact with the Boto3 APIs, you can use this task.
