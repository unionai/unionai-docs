---
title: Platform deployment
weight: 4
variants: -flyte -serverless +byoc +selfmanaged
top_menu: true
mermaid: true
sidebar_expanded: true
---

# Platform deployment

The Union.ai platform uses a split control plane / data plane model.
In both BYOC and Self-managed products, your code, input and output data, container images and logs reside entirely on the data plane, which runs in your cloud account, while the control plane runs on Union.ai's cloud account, providing the workflow orchestration logic.

BYOC and Self-managed differ only in _who manages the data plane_: With BYOC, Union.ai manages your data plane (in your account) for you. With Self-managed you manage the data plane entirely yourself.

{{< variant byoc >}}
{{< markdown >}}

> [!NOTE]
> These are the BYOC docs. You can switch to the Union.ai Self-managed docs with the product selector above.

## Union.ai BYOC

Union.ai BYOC is a fully "serverless in your cloud", turnkey product that enables you to offload all infrastructure management to Union.ai, who will handle deployment, monitoring, Kubernetes upgrades, and all other operational aspects of the platform.

Union.ai BYOC supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure.

{{< /markdown >}}
{{< /variant >}}

{{< variant selfmanaged >}}
{{< markdown >}}

> [!NOTE]
> These are the Self-managed docs. You can switch to the Union.ai BYOC docs with the product selector above.

## Union.ai Self-managed

Union.ai Self-managed allows you to manage the data plane yourself on cloud infrastructure that you control and maintain.
In this model, Union.ai only manages the control plane scaling and resiliency.
Your platform team manages data plane hardware, upgrades and permissions.
You do not need to provide any permissions to the Union.ai system to create a data plane.

Union.ai Self-managed supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure and Oracle Compute Infrastructure (OCI).

{{< /markdown >}}
{{< /variant >}}

{{< variant byoc selfmanaged >}}
{{< markdown >}}

## Control plane

Union.ai operates the control plane in its own cloud infrastructure in Amazon Web Services (AWS).
The control plane holds:

* Workload execution state information
* Names of tasks and other deployed entities
* Pointers to object storage locations in the data plane (but not any user data)
* Union.ai IDP

## Data plane

The data plane runs in your cloud account and VPC. It is composed of the required services to run and monitor workflows:

* Kubernetes cluster
* Object storage bucket
* Container image registry
* Secrets manager
* Logging solution
* IAM role with proper access

When you run your workflow:

1. Your code is sent to the object storage bucket
2. Container images are built on a builder node and pushed to the registry
3. Pods are created and assume the IAM role
4. Container images are pulled down from the registry for each pod as needed
5. Containers load their inputs from, and save their outputs to, the object store

All of this happens in the data plane, with the control plane aware only of the workflow execution state, and not the code, data, logs, secrets, or any other proprietary information. The data plane communicates with the control plane through an outgoing port through a zero trust proxy. There is no open incoming port to the data plane.

{{< /markdown >}}
{{< /variant >}}

{{< variant selfmanaged >}}
{{< grid >}}

{{< link-card target="../deployment/cluster-recommendations" icon="box" title="Installation" >}}
Installing {{< key product_name >}}
{{< /link-card >}}

{{< /grid >}}
{{< /variant >}}
