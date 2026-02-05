---
title: Platform deployment
weight: 4
variants: -flyte -serverless +byoc +selfmanaged
top_menu: true
mermaid: true
sidebar_expanded: true
---

# Platform deployment

{{< variant byoc selfmanaged >}}
{{< markdown >}}

The {{< key product_name >}} platform uses a split control plane / data plane model. Workflow orchestration logic resides on the control plane while all user code and data resides on the data plane.

## Control plane

Union.ai operates the control plane in its own cloud infrastructure in Amazon Web Services (AWS).
The control plane holds:

* Workload execution state information
* Names of tasks and other deployed entities
* Pointers to object storage locations in the data plane (but not any user data).
* Union.ai IDP

## Data plane

The data plane runs in your cloud account and VPC. It is composed of the required services to run and monitor workflows:

* Kubernetes cluster
* Object storage bucket
* Container image registry
* Secrets manager
* Logging solution
* IAM role with proper access.

When you run the tasks of your workflow:

1. Your code is sent to the object storage bucket.
2. Container images are built on a builder node and pushed to the registry.
3. Pods are created and assume the IAM role.
4. Container images are pulled down from the registry for each pod as needed.
5. Containers load their inputs from, and save their outputs to, the object store.

All of this happens in the data plane, with the control plane aware only of the workflow execution state, and not the code, data, logs, secrets, or any other proprietary information. The data plane communicates with the control plane through an outgoing port through a zero trust proxy. There is no open incoming port to the data plane.

{{< /markdown >}}
{{< /variant >}}

{{< variant byoc >}}
{{< markdown >}}

## Union.ai BYOC

Union.ai BYOC is a fully "serverless in your cloud", turnkey product that enables you to offload all infrastructure management to Union.ai, who will handle deployment, monitoring, Kubernetes upgrades, and all other operational aspects of the platform.

Union.ai BYOC supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure.

{{< /markdown >}}
{{< /variant >}}

{{< variant selfmanaged >}}
{{< markdown >}}

## Union.ai Self-managed

Union.ai Self-managed allows you to manage the data plane yourself on cloud infrastructure that you control and maintain.
In this model, Union.ai only manages the control plane scaling and resiliency.
Your platform team manages data plane hardware, upgrades and permissions.
You do not need to provide any permissions to the Union.ai system to create a data plane.

Union.ai Self-managed supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure and Oracle Compute Infrastructure (OCI).

{{< /markdown >}}
{{< grid >}}

{{< link-card target="../deployment/cluster-recommendations" icon="box" title="Installation" >}}
Installing {{< key product_name >}}
{{< /link-card >}}

{{< /grid >}}
{{< /variant >}}
