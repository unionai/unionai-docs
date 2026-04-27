---
title: Self-managed deployment
weight: 2
variants: -flyte +union
---

# Self-managed deployment

The self-managed deployment allows you to manage the data plane yourself on cloud infrastructure that you control and maintain.

The **data plane** resides in your cloud provider account and is managed by you. Your team handles deployment, monitoring, Kubernetes upgrades, and all other operational aspects of the platform. You do not need to provide any permissions to Union.ai. Self-managed supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, and Oracle Compute Infrastructure (OCI).

The **control plane** resides in the Union.ai AWS account and is administered by Union.ai. As with BYOC, data separation is maintained between the data plane and the control plane.
