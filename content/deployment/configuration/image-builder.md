---
title: ImageBuilder
weight: 2
variants: -flyte -serverless -byoc +selfmanaged
---

# ImageBuilder

Union Image Builder supports the ability to build container images within the dataplane. Subsequently enabling the use of the `union` builder type within defined [ImageSpecs](../../user-guide/development-cycle/image-spec.md).

```python
image_spec = union.ImageSpec(
    builder="union",
    name="say-hello-image",
)
```

By default, image builder is disabled.

## Requirements

* Union requires that a `production` domain exists.

## Configuration

Image Builder is configured directly through halm values.

```yaml
imageBuilder:

  # Enable image builder
  enabled: true

  # -- The config map build-image container task attempts to reference.
  # -- Should not change unless coordinated with Union technical support.
  targetConfigMapName: "build-image-config"

  # -- The URI of the buildkitd service. Used for externally managed buildkitd services.
  # -- Leaving empty and setting imageBuilder.buildkit.enabled to true will create a buildkitd service and configure the Uri appropriately.
  # -- E.g. "tcp://buildkitd.buildkit.svc.cluster.local:1234"
  buildkitUri: ""

  # -- The default repository to publish images to "registry" is not specified with imagespec.
  # -- Note, the build-image task will fail unless "registry" is specified or a default repository is provided.
  defaultRepository: ""

  # -- How build-image task and operator proxy will attempt to authenticate against the default #    repository.
  # -- Supported values are "noop", "google", "aws", "azure"
  # -- "noop" no authentication is attempted
  # -- "google" uses docker-credential-gcr to authenticate to the default registry
  # -- "aws" uses docker-credential-ecr-login to authenticate to the default registry
  # -- "azure" uses az acr login to authenticate to the default registry. Requires Azure Workload Identity to be enabled.
  authenticationType: "noop"

  buildkit:

    # -- Enable buildkit service within this release.
    enabled: true

    # Configuring Union managed buildkitd Kubernetes resources.
    ...
```

## Authentication

### AWS

By default, Union is intended to be configured to use [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) for authentication. Setting `authenticationType` to `aws` configures Union image builder related services to use AWS default credential chain. Additionally, Union image builder uses [`docker-credential-ecr-login`](https://github.com/awslabs/amazon-ecr-credential-helper) to authenticate to the ecr repository configured with `defaultRepository`.

`defaultRepository` should be the full qualified ecr repository namem `<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<REPOSITORY_NAME>`.

Therefore, it is necessary to configure the user role with permissions the following permissions.

```json
{
  "Effect": "Allow",
  "Action": [
    "ecr:GetAuthorizationToken"
  ],
  "Resource": "*"
},
{
  "Effect": "Allow",
  "Action": [
    "ecr:BatchCheckLayerAvailability",
    "ecr:BatchGetImage",
    "ecr:GetDownloadUrlForLayer"
  ],
  "Resource": "*"
  // Or
  // "Resource": "arn:aws:ecr:<AWS_REGION>:<AWS_ACCOUNT_ID>:repository/<REPOSITORY>"
}
```

Simarly, the `operator-proxy` requires the following permissions

```json
{
  "Effect": "Allow",
  "Action": [
    "ecr:GetAuthorizationToken"
  ],
  "Resource": "*"
},
{
  "Effect": "Allow",
  "Action": [
    "ecr:DescribeImages"
  ],
  "Resource": "arn:aws:ecr:<AWS_REGION>:<AWS_ACCOUNT_ID>:repository/<REPOSITORY>"
}
```

#### AWS Cross Account access

Access to repositories that do not exist in the same AWS account as the data plane requires additional ECR resource-based permissions. An ECR policy like the following is required if the configured `defaultRepository` or ImageSpec's `registry` exists in an AWS account different from the dataplane's.

```json
{
  "Statement": [
    {
      "Sid": "AllowPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<user-role>",
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<node-role>",
          // ... Additional roles that require image pulls
        ]
      },
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ]
    },
    {
      "Sid": "AllowDescribeImages",
      "Action": [
        "ecr:DescribeImages"
      ],
      "Principal": {
        "AWS": [
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<operator-proxy-role>",
        ]
      },
      "Effect": "Allow"
    },
    {
      "Sid": "ManageRepositoryContents"
      // ...
    }
  ],
  "Version": "2012-10-17"
}
```

In order to support a private ImageSpec `base_image` the following permissions are required.

```json
{
  "Statement": [
    {
      "Sid": "AllowPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<user-role>",
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<node-role>",
          // ... Additional roles that require image pulls
        ]
      },
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ]
    },
  ]
}
```

### Google Cloud Platform

By default, GCP uses [Kubernetes Service Accounts to GCP IAM](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) for authentication. Setting `authenticationType` to `google` configures Union image builder related services to use GCP default credential chain. Additionally, Union image builder uses [`docker-credential-gcr`](https://github.com/GoogleCloudPlatform/docker-credential-gcr) to authenticate to the google artifact registries referenced by `defaultRepository`.

`defaultRepository` should be the full name to the repository in combination with an optional image name prefix. `<GCP_LOCATION>-docker.pkg.dev/<GCP_PROJECT_ID>/<REPOSITORY_NAME>/<IMAGE_PREFIX>`.

It is necessary to configure the GCP user service account with `iam.serviceAccounts.signBlob` project level permissions.

#### GCP Cross Project access

Access to registries that do not exist in the same GCP project as the data plane requires additional GCP permissions.

* Configure the user "role" service account with the `Artifact Registry Writer`.
* Configure the GCP worker node and union-operator-proxy service accounts with the `Artifact Registry Reader` role.

### Azure

By default, Union is designed to use Azure [Workload Identity Federation](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster) for authentication using [user-assigned managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp) in place of AWS IAM roles.

* Configure the user "role" user-assigned managed identity with the `AcrPush` role.
* Configure the Azure kubelet identity id and operator-proxy user-assigned managed identities with the `AcrPull` role.
