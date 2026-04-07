---
title: Platform deployment
weight: 4
variants: +flyte +union
top_menu: true
tier2_band: "+union -flyte"
mermaid: true
sidebar_expanded: true
---

# Platform deployment

{{< variant union >}}
{{< markdown >}}

The Union.ai platform uses a split-plane model with separate control and data planes.

In both BYOC and Self-managed deployments, your code, input and output data, container images and logs reside entirely on the **data plane**, which runs in your cloud account, while the **control plane** runs on Union.ai's cloud account, providing the workflow orchestration logic.

The **control plane** does not have access to the code, data, images, or logs in the **data plane**.

If you choose a **Self-managed deployment**, your data isolation is further enhanced by the fact that you manage your data plane entirely on your own, without providing any access to Union.ai customer support.

If you choose a **BYOC deployment**, Union.ai manages the Kubernetes cluster in your data plane for you. The data isolation of the control vs. data plane is still enforced — for example, Union.ai has no access to your object storage or logs. However, Union.ai customer support will have some access to your cluster, though strictly for upgrades, provisioning, and other actions related to maintaining cluster health.

## Deployment options

Union.ai offers two deployment models:

### BYOC (Bring Your Own Cloud)

The BYOC deployment offers a fully "serverless in your cloud", turnkey solution where all infrastructure management is offloaded to Union.ai:

* The **data plane** resides in your cloud provider account but is managed by Union.ai, who handle deployment, monitoring, Kubernetes upgrades, and all other operational aspects of the platform. BYOC supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure.

* The **control plane** resides in the Union.ai AWS account and is administered by Union.ai. Data separation is maintained between the data plane and the control plane, with no control plane access to the code, input/output, images or logs in the data plane.

### Self-managed

The Self-managed deployment allows you to manage the data plane yourself on cloud infrastructure that you control and maintain:

* The **data plane** resides in your cloud provider account and is managed by you. Your team handles deployment, monitoring, Kubernetes upgrades, and all other operational aspects of the platform. You do not need to provide any permissions to Union.ai. Self-managed supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, and Oracle Compute Infrastructure (OCI).

* The **control plane** resides in the Union.ai AWS account and is administered by Union.ai. As with BYOC, data separation is maintained between the data plane and the control plane.

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

## Control plane

Union.ai operates the control plane in its own cloud infrastructure in Amazon Web Services (AWS).
The control plane has access to:

* Workflow execution state information
* Names of tasks and other deployed entities
* Pointers to object storage locations in the data plane (but not any user data)
* Union.ai IDP

{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

Flyte is an open-source workflow orchestration platform that you deploy and manage on your own infrastructure. This section covers planning, installing, configuring, and operating a Flyte backend.

The sections below cover the full scope of running Flyte in production:

* **Flyte deployment** — Planning and installing Flyte on Kubernetes (single-cluster or multi-cluster setups).
* **Flyte configuration** — Configuring authentication, secrets, notifications, monitoring, GPUs, pod templates, and other runtime settings.
* **Flyte connectors** — Integrating with external services such as Airflow, BigQuery, Databricks, Snowflake, and more.
* **Flyte plugins** — Native backend plugins for Kubernetes operators, Spark, Athena, SageMaker, and other compute backends.
* **Configuration reference** — Full reference for FlyteAdmin, FlytePropeller, DataCatalog, and Scheduler config files.

{{< /markdown >}}
{{< /variant >}}
