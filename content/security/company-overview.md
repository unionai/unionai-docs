---
title: Company overview
weight: 1
variants: -flyte +byoc +selfmanaged
---

Union.ai was founded to enable enterprises to build, deploy, and govern reliable AI/ML workflows at scale.
The platform is built on Flyte, a widely-adopted open-source workflow orchestration system **originally developed at Lyft** and now trusted by organizations including Spotify, LinkedIn, Freenome, and Lyft.

## Platform capabilities

* **Workflow orchestration:** Strongly-typed, reproducible workflows for ML training, data processing, and model deployment pipelines
* **Enterprise governance:** Role-based access control, audit trails, and compliance-ready deployment models
* **Kubernetes native:** Union AI's architecture integrates natively with Kubernetes, the industry-standard container orchestration system.
* **Multi-cloud support:** Deploy data planes on AWS, GCP, or Azure with consistent security guarantees
* **Observability:** Built-in metrics, logging, and cost tracking for full pipeline visibility
* **Agentic workflows:** Support for complex, multistep automated workflows and applications with guardrails

## Deployment models

Union.ai offers multiple deployment models to meet varying enterprise requirements:

| Deployment Model | Control plane | Data plane | Union Admin Permissions | Private Link Permissions | Best For |
| --- | --- | --- | --- | --- | --- |
| BYOC (Bring Your Own Cloud) | Union.ai hosted and managed | Customer cloud account hosted, Union.ai managed | Yes | Yes | Managed operation for enterprises that require strict data residency and a lower support overhead. |
| Self-Managed (Hybrid) | Union.ai hosted and managed | Customer cloud account hosted and managed | No | No | Organizations requiring full infrastructure control or those with specific compliance or unique infrastructure needs. |
| Self-Managed + Support | Union.ai hosted and managed | Customer cloud account hosted and managed | No | Yes | Self-managed deployments with Union-managed private connectivity for cluster management support. |
| Air-gapped | Union.ai hosted and managed | Customer cloud account hosted and managed (air-gapped) | No | No | Maximum isolation environments with no external connectivity requirements. |
| Air-gapped + Support | Union.ai hosted and managed | Customer cloud account hosted and managed (air-gapped) | No | Yes | Air-gapped deployments with Union-managed private connectivity for cluster management support. |
