---
title: User Guide
weight: 1
top_menu: true
site_root: true
---

# User guide

{{< if-variant serverless >}}

> **Union Serverless**
> These docs are for [**Union Serverless**](./about-union.md#union-serverless).
> Switch to [Union BYOC](https://docs.union.ai/byoc) with the version selector above.

{{< /if-variant >}}

{{< if-variant byoc >}}

> **Union BYOC**
> These docs are for [**Union BYOC**](./about-union.md#union-byoc).
> Switch to [Union Serverless](https://docs.union.ai/byoc) with the version selector above.

{{< /if-variant >}}

The Union platform empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

- Run complex AI workloads with performance, scale, and efficiency.
- Achieve millisecond-level execution times with reusable containers.
- Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale or compliance.

{{< grid >}}

{{< link-card target="about-union" icon="building" title="About Union" >}}
Union builds on the leading OSS orchestrator, Flyte, to provide a powerful, scalable, and flexible platform for AI workflows.
{{< /link-card >}}

{{< link-card target="getting-started" icon="file" title="Getting Started" >}}
Build your first Union workflow, exploring the major features of the platform along the way.
{{< /link-card >}}

{{< link-card target="core-concepts" icon="board" title="Core Concepts" >}}
Understand the core concepts of the Union platform.
{{< /link-card >}}

{{< link-card target="development-cycle" icon="iterations" title="Development Cycle" >}}
Explore the Union development cycle from experimentation to production.
{{< /link-card >}}

{{< link-card target="data-input-output" icon="arrow-switcg" title="Data Input/Output" >}}
Manage the input and output of data in your Union workflow.
{{< /link-card >}}

{{< if-variant variants=byoc nested=true >}}

{{< link-card target="administration" icon="person" title="Administration" >}}
Union BYOC administrators can manage users, projects, and resources.
{{< /link-card >}}

{{< link-card target="integrations" icon="gear" title="Integrations" >}}
Union BYOC integrates with your cloud resources and external services.
{{< /link-card >}}

{{< link-card target="faq" icon="question" title="FAQ" >}}
Frequently asked questions.
{{< /link-card >}}

{{< /if-variant >}}

{{< /grid >}}