---
title: Image Builder
variants: -flyte -serverless +byoc +selfmanaged
weight: 2
---

# Image Builder

Union Image Builder supports the ability to build container images within the dataplane. For details about this feature, please visit [Image Builder](../../../deployment/configuration/image-builder.md).

## Authentication

By default, GCP uses [Kubernetes Service Accounts to GCP IAM](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) for authentication. Setting `authenticationType` to `google` configures Union image builder related services to use GCP default credential chain. Additionally, Union image builder uses [`docker-credential-gcr`](https://github.com/GoogleCloudPlatform/docker-credential-gcr) to authenticate to the google artifact registries referenced by `defaultRepository`.

`defaultRepository` should be the full name to the repository in combination with an optional image name prefix. `<GCP_LOCATION>-docker.pkg.dev/<GCP_PROJECT_ID>/<REPOSITORY_NAME>/<IMAGE_PREFIX>`.

It is necessary to configure the GCP user service account with `iam.serviceAccounts.signBlob` project level permissions.

### GCP Cross Project access

Access to registries that do not exist in the same GCP project as the data plane requires additional GCP permissions.

- Configure the user "role" service account with the `Artifact Registry Writer`.
- Configure the GCP worker node and union-operator-proxy service accounts with the `Artifact Registry Reader` role.
