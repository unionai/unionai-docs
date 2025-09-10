---
title: User guide
description: "Complete guide to Union.ai and Flyte workflow orchestration platform. Learn to build, deploy, and manage AI workflows with our comprehensive documentation."
keywords: ["AI workflows", "workflow orchestration", "machine learning", "data pipelines", "Flyte", "Union.ai", "MLOps", "data processing"]
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
top_menu: true
site_root: true
sidebar_expanded: true
---

{{< variant flyte >}}
{{< markdown >}}

# Flyte

Flyte is a free and open source platform that provides a full suite of powerful features for orchestrating AI workflows.
Flyte empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.
You deploy and manage Flyte yourself, on your own cloud infrastructure.

> [!NOTE]
> These are the Flyte **2.0 beta** docs.
> To switch to [version 1.0]({{< docs_home flyte v1 >}}) or to the commercial product, [**Union.ai**]({{< docs_home byoc v2 >}}), use the selectors above.
>
> This documentation for open-source Flyte is maintained by Union.ai.

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}

# {{< key product_name >}} Serverless

{{< key product_name >}} empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With {{< key product_name >}} your team can:

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> These are the Union.ai **2.0 beta** docs.
> To switch to [version 1.0]({{< docs_home serverless v1 >}}) or to another product variant, use the selectors above.
>
> {{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte v2 >}}).
>
> {{< key product_name >}} Serverless provides all the features of Flyte, plus much more,
> all in a turn-key, fully-managed, cloud environment.
> There is zero infrastructure to deal with, and you pay only for the resources you use.
> Your data and workflow code is stored safely and securely in the Union.ai cloud infrastructure.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc >}}
{{< markdown >}}

# {{< key product_name >}} BYOC

{{< key product_name >}} empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With {{< key product_name >}} your team can:

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> These are the Union.ai **2.0 beta** docs.
> To switch to [version 1.0]({{< docs_home byoc v1 >}}) or to another product variant, use the selectors above.
>
> {{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte v2 >}}).
>
> {{< key product_name >}} BYOC (Bring Your Own Cloud) provides all the features of Flyte, plus much more
> in an environment where you keep your data and workflow code on your infrastructure, while {{< key product_name >}} takes care of the management.

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

# {{< key product_name >}} Self-managed

{{< key product_name >}} empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With {{< key product_name >}} your team can:

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> These are the Union.ai **2.0 beta** docs.
> To switch to [version 1.0]({{< docs_home selfmanaged v1 >}}) or to another product variant, use the selectors above.
>
> {{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte v2 >}}).
>
> {{< key product_name >}} Self-managed provides all the features of Flyte, plus much more
> while letting you keep your data and workflow code on your infrastructure and under your own management.

{{< /markdown >}}
{{< /variant >}}

{{< grid >}}

{{< link-card target="flyte-2" icon="lightbulb" title="Flyte 2" >}}
Flyte 2 represents a fundamental shift in how AI workflows are written and executed. Learn
more in this section.
{{< /link-card >}}

{{< link-card target="getting-started" icon="123" title="Getting started" >}}
Install Flyte 2, configure your local IDE, create and run your first task, and inspect the results in 2 minutes.
{{< /link-card >}}
{{< /grid >}}
