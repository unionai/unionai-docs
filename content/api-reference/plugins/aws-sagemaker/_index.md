---
title: AWS SageMaker
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: AWS SageMaker
  title_expanded: AWS SageMaker Plugin
  name: flytekitplugins-awssagemaker
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: Flytekit AWS SageMaker Plugin
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.awssagemaker_inference
  install_requires:
  - flytekit>1.14.6
  - aioboto3>=12.3.0
  - xxhash
  license: apache2
  python_requires: '>=3.10'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Programming Language :: Python :: 3.12'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  entry_points:
    flytekit.plugins:
    - awssagemaker_inference=flytekitplugins.awssagemaker_inference
  folder: flytekit-aws-sagemaker
---


The plugin currently features a SageMaker deployment agent.

## Inference

The deployment agent enables you to deploy models, create and trigger inference endpoints.
Additionally, you can entirely remove the SageMaker deployment using the `delete_sagemaker_deployment` workflow.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-awssagemaker
```

Here is a sample SageMaker deployment workflow:

```python
from flytekitplugins.awssagemaker_inference import create_sagemaker_deployment


REGION = os.getenv("REGION")
MODEL_NAME = "xgboost"
ENDPOINT_CONFIG_NAME = "xgboost-endpoint-config"
ENDPOINT_NAME = "xgboost-endpoint"

sagemaker_deployment_wf = create_sagemaker_deployment(
    name="sagemaker-deployment",
    model_input_types=kwtypes(model_path=str, execution_role_arn=str),
    model_config={
        "ModelName": MODEL_NAME,
        "PrimaryContainer": {
            "Image": "{images.deployment_image}",
            "ModelDataUrl": "{inputs.model_path}",
        },
        "ExecutionRoleArn": "{inputs.execution_role_arn}",
    },
    endpoint_config_input_types=kwtypes(instance_type=str),
    endpoint_config_config={
        "EndpointConfigName": ENDPOINT_CONFIG_NAME,
        "ProductionVariants": [
            {
                "VariantName": "variant-name-1",
                "ModelName": MODEL_NAME,
                "InitialInstanceCount": 1,
                "InstanceType": "{inputs.instance_type}",
            },
        ],
        "AsyncInferenceConfig": {
            "OutputConfig": {"S3OutputPath": os.getenv("S3_OUTPUT_PATH")}
        },
    },
    endpoint_config={
        "EndpointName": ENDPOINT_NAME,
        "EndpointConfigName": ENDPOINT_CONFIG_NAME,
    },
    images={"deployment_image": custom_image},
    region=REGION,
)


@workflow
def model_deployment_workflow(
    model_path: str = os.getenv("MODEL_DATA_URL"),
    execution_role_arn: str = os.getenv("EXECUTION_ROLE_ARN"),
) -> str:
    return sagemaker_deployment_wf(
        model_path=model_path,
        execution_role_arn=execution_role_arn,
        instance_type="ml.m4.xlarge",
    )
```
