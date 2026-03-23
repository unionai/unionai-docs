---
title: Company overview
weight: 1
variants: -flyte +byoc +selfmanaged
---

# Company overview

Union.ai was founded to enable enterprises to build, deploy, and govern reliable AI/ML workflows at scale.
The platform is built on Flyte, a widely-adopted open-source workflow orchestration system originally developed at Lyft and now trusted by organizations including Spotify, LinkedIn, Freenome, Artera, and Lyft.

## Platform capabilities

* **Workflow orchestration:** Strongly-typed, reproducible workflows for ML training, data processing, and model deployment pipelines
* **Enterprise governance:** Role-based access control, audit trails, and compliance-ready deployment models
* **Kubernetes native:** Union AI's architecture integrates natively with Kubernetes, the industry-standard container orchestration system.
* **Multi-cloud support:** Deploy compute planes on AWS, GCP, or Azure with consistent security guarantees
* **Observability:** Built-in metrics, logging, and cost tracking for full pipeline visibility
* **Agentic workflows:** Support for complex, multistep automated workflows and applications with guardrails

## Deployment models

{{< variant selfmanaged >}}
{{< markdown >}}
Union.ai offers multiple deployment models to meet varying enterprise requirements. This document addresses the security concerns of the self-managed deployment, where the customer operates their compute plane independently.
{{< /markdown >}}
{{< /variant >}}
{{< variant byoc >}}
{{< markdown >}}
Union.ai offers multiple deployment models to meet varying enterprise requirements. This document addresses the security concerns of the BYOC (Bring Your Own Cloud) deployment, where Union.ai manages the Kubernetes cluster in the customer's cloud account.
{{< /markdown >}}
{{< /variant >}}
