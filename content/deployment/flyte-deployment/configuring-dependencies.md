---
title: Flyte components
weight: 1
variants: +flyte -serverless -byoc -byok
top_menu: false
---

# Components of a Flyte deployment


A Flyte cluster is composed of 3 logical planes as described in the table:

| Plane  | Description  | Component  | 
|---|---|---|
| User plane  | Tools to interact with the API  | `flytekit` SDK, `flytectl`, and `pyflyte`  | 
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
It runs each Flyte component as a highly-available Deployment. The main difference with the flyte-binary chart include is that flyte-core supports scaling out each Flyte component independently.
Most often and when reaching very large scale, you'd need to scale out the dataplane (`flytepropeller`) using one of the supported sharding strategies.

- Scale out individual Flyte components

Flyte uses `Helm <https://helm.sh/>`__ as the K8s release packaging solution. The core Flyte
team maintains Helm charts that correspond with the latter two deployment paths.

## Additional resources

### Terraform reference implementations

### Support

