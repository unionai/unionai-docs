---
title: Planning your deployment
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
---

# Components of a Flyte deployment


A Flyte cluster is composed of 3 logical planes as described in the table:

| Plane  | Description  | Component  |
|---|---|---|
| User plane  | Tools to interact with the API  | `flytekit`, `flytectl`, and `pyflyte`  |
| Control plane  | Processes incoming requests, implements core logic, maintains metadata and resource inventory.  | `flyteadmin`, `datacatalog`, and `flytescheduler`.  |
| Data plane  | It fulfills execution requests, including instantiating plugins/connectors.  | `flytepropeller`, `clusterresourcessync`   |

# External dependencies
Regardless of the deployment path you choose, Flyte relies on a few elements to operate.

## Kubernetes cluster
It's recommended to a [supported Kubernetes version](https://kubernetes.io/releases/version-skew-policy/#supported-versions) . Flyte doesn't impose a requirement on the provider or method you use to stand up the K8s cluster: it can be anything from `k3s` on edge devices to massive K8s environments in the cloud or on-prem bare metal.

## Relational Database

Both `flyteadmin` and `datacatalog` rely on a PostgreSQL 12+ instance to store persistent records.

## Object store

Core Flyte components such as `flyteadmin`, `flytepropeller`, `datacatalog`, and user runtime containers -spawned for each execution- rely on an object store to hold files.

A Flyte deployment requires at least one storage bucket from an S3-compliant provider with the following minimum permissions:

- DeleteObject
- GetObject
- ListBucket
- PutObject

## Optional dependencies

Flyte can be operated without the following elements, but is prepared to use them if available for better integration with your current infrastructure:

### Ingress controller


Flyte operates with two protocols: `HTTP` for the UI and `gRPC` for the client-to-control-plane communication. You can expose both ports through `port-forward` which is typically a temporary measure, or expose them in a stable manner using Ingress. For a Kubernetes Ingress resource to be properly materialized, it needs an Ingress controller already installed in the cluster.
The Flyte Helm charts can trigger the creation of the Ingress resource but the config needs to be reconciled by an Ingress controller (doesn't ship with Flyte).
The Flyte community has used the following controllers succesfully:

| Environment  | Controller  | Example configuration  |
|---|---|---|
| AWS  | ALB  | [flyte-binary config](https://github.com/flyteorg/flyte/blob/754ab74b29f5fee665fd1cfde38fccccd95af8bd/charts/flyte-binary/eks-starter.yaml#L108-L120) / [flyte-core config](https://github.com/flyteorg/flyte/blob/754ab74b29f5fee665fd1cfde38fccccd95af8bd/charts/flyte-core/values-eks.yaml#L142-L160)  |
| GCP  | NGINX  | [flyte-core example config](https://github.com/flyteorg/flyte/blob/754ab74b29f5fee665fd1cfde38fccccd95af8bd/charts/flyte-core/values-gcp.yaml#L160-L173)  |
| Azure  | NGINX | [flyte-core example config](https://github.com/flyteorg/flyte/blob/754ab74b29f5fee665fd1cfde38fccccd95af8bd/charts/flyte-core/values-gcp.yaml#L160-L173)   |
| On-prem | NGINX, Traefik |

### DNS
To register and run workflows in Flyte, your client (the CLI in your machine or an external system) needs to connect to the Flyte control plane through an endpoint. When you do `port-forward`, you typically access Flyte through `localhost`. For a production environment is recommended to use a valid DNS entry that points to your Ingress host name.

### SSL/TLS

Use a valid certificate to secure the communication between your client and the Flyte control plane. For Flyte, `insecure: true` means no certificate is installed. You can even use self-signed certificates (which counts as `insecure: false`) adding the `insecureSkipVerify: true` key to the local `config.yaml` file. That will inform Flyte to skip verifying the certificate chain.

## Helm chart variants

### Sandbox
It packages Flyte and all its dependencies into a single container that runs locally.
When you run `flytectl demo start` it creates the container using any OCI-compliant container engine you have available in your local system.

### flyte-binary
It packages all the Flyte components in a single Pod and is designed to scale up by adding more compute resources to the Deployment.
It doesn't implement the dependencies so you have to provision the storage bucket, Kubernetes cluster and database before installing it.
The repo includes [example values files](https://github.com/flyteorg/flyte/tree/master/charts/flyte-binary) for different environments.

> The [Flyte the Hard Way](https://github.com/davidmirror-ops/flyte-the-hard-way) community-maintained guide walks you through the semiautomated process to prepare the dependencies to install `flyte-binary`

### flyte-core
It runs each Flyte component as a highly-available Deployment. The main difference with the flyte-binary chart is that flyte-core supports scaling out each Flyte component independently.

## Additional resources

### Terraform reference implementations

{{< key product_name >}} maintains a [Terraform codebase](https://github.com/unionai-oss/deploy-flyte) you can use to automatically configure all the dependencies and install Flyte in AWS, GCP, or Azure.

### Support

Reach out to the [#flyte-deployment](https://flyte-org.slack.com/archives/C01P3B761A6) community channel if you have questions during the deployment process.

[{{< key product_name >}}](https://www.union.ai/contact) also offers paid Install Assist and different tiers of support services.
