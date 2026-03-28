---
title: User guide
weight: 1
variants: +flyte +union
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
> These are the Flyte **2.0** docs.
> To switch to [version 1.0]({{< docs_home flyte v1 >}}) or to the commercial product, [**Union.ai**]({{< docs_home union v2 >}}), use the selectors above.
>
> This documentation for open-source Flyte is maintained by Union.ai.

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}

# {{< key product_name >}}

{{< key product_name >}} empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With {{< key product_name >}} your team can:

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

{{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte v2 >}}).

{{< key product_name >}} provides all the features of Flyte, plus much more, in an environment where you keep your data and workflow code on your own infrastructure. {{< key product_name >}} is available as [BYOC]({{< docs_home union v2 >}}/deployment/byoc/_index) (Bring Your Own Cloud), where Union.ai manages the infrastructure for you, or [Self-managed]({{< docs_home union v2 >}}/deployment/selfmanaged/_index), where you manage the data plane yourself.

> [!NOTE]
> These are the Union.ai **2.0** docs.
> To switch to [version 1.0]({{< docs_home union v1 >}}) or to another product variant, use the selectors above.

{{< /markdown >}}
{{< /variant >}}

{{< note >}}
Want to try Flyte without installing anything? [Try Flyte 2 in your browser](https://flyte2intro.apps.demo.hosted.unionai.cloud/).
{{< /note >}}

{{< grid >}}

{{< link-card target="flyte-2" icon="lightbulb" title="Flyte 2" >}}
Flyte 2 represents a fundamental shift in how AI workflows are written and executed. Learn
more in this section.
{{< /link-card >}}

{{< link-card target="quickstart" icon="123" title="Quickstart" >}}
Install Flyte 2, configure your local IDE, create and run your first task, and inspect the results in 2 minutes.
{{< /link-card >}}
{{< /grid >}}
