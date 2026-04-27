---
title: BYOC deployment
weight: 1
variants: -flyte +union
---

# BYOC deployment

The BYOC (Bring Your Own Cloud) deployment offers a fully managed, turnkey solution where all infrastructure management is offloaded to Union.ai.

The **data plane** resides in your cloud provider account but is managed by Union.ai, who handle deployment, monitoring, Kubernetes upgrades, and all other operational aspects of the platform. BYOC supports data planes on Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure.

The **control plane** resides in the Union.ai AWS account and is administered by Union.ai. Data separation is maintained between the data plane and the control plane, with no control plane access to the code, input/output, images or logs in the data plane.
