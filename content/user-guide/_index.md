---
title: User guide
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
> This documentation for open-source Flyte is maintained by Union.ai.
>
> You can switch to the documentation for the commercial versions with the selector above.

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}

# {{< key product_name >}} Serverless

The {{< key product_name >}} platform empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> {{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte >}}).
>
> {{< key product_name >}} Serverless provides [all the features of Flyte, plus much more](./introduction#-key-product_name--serverless)
> all in a turn-key, fully-managed, cloud environment.
> There is zero infrastructure to deal with, and you pay only for the resources you use.
> Your data and workflow code is stored safely and securely in the Union.ai cloud infrastructure.
>
> You can switch to another product version with the selector above.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc >}}
{{< markdown >}}

# {{< key product_name >}} BYOC

The {{< key product_name >}} platform empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> {{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte >}}).
>
> {{< key product_name >}} BYOC (Bring Your Own Cloud) provides [all the features of Flyte, plus much more](./introduction#-key-product_name--byoc)
> in an environment where you keep your data and workflow code on your infrastructure, while {{< key product_name >}} takes care of the management.
>
> You can switch to another product version with the selector above.

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

# {{< key product_name >}} Self-managed

The {{< key product_name >}} platform empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> {{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte >}}).
>
> {{< key product_name >}} Self-managed provides [all the features of Flyte, plus much more](./introduction#-key-product_name--self-managed)
> while letting you keep your data and workflow code on your infrastructure and under your own management.
>
> You can switch to another product version with the selector above.

{{< /markdown >}}
{{< /variant >}}

{{< grid >}}

{{< variant flyte >}}

{{< link-card target="introduction" icon="lightbulb" title="Introduction" >}}
Flyte is the leading open-source Kubernetes-native workflow orchestrator.
{{< /link-card >}}

{{< /variant >}}
{{< variant serverless byoc selfmanaged >}}

{{< link-card target="introduction" icon="lightbulb" title="Introduction" >}}
{{< key product_name >}} builds on the leading open-source workflow orchestrator, Flyte, to provide a powerful, scalable, and flexible platform for AI applications.
{{< /link-card >}}

{{< /variant >}}

{{< link-card target="getting-started" icon="123" title="Getting started" >}}
Build your first {{< key product_name >}} workflow, exploring the major features of the platform along the way.
{{< /link-card >}}

{{< link-card target="core-concepts" icon="mortarboard" title="Core concepts" >}}
Understand the core concepts of the {{< key product_name >}} platform.
{{< /link-card >}}

{{< link-card target="development-cycle" icon="arrow-repeat" title="Development cycle" >}}
Explore the {{< key product_name >}} development cycle from experimentation to production.
{{< /link-card >}}

{{< link-card target="data-input-output" icon="arrow-left-right" title="Data input/output" >}}
Manage the input and output of data in your {{< key product_name >}} workflow.
{{< /link-card >}}

{{< link-card target="programming" icon="code-slash" title="Programming" >}}
Learn about {{< key product_name >}}-specific programming constructs.
{{< /link-card >}}

{{< variant byoc selfmanaged >}}

{{< link-card target="administration" icon="person-add" title="Administration" >}}
{{< key product_full_name >}} administrators can manage users, projects, and resources.
{{< /link-card >}}

{{< link-card target="integrations" icon="tools" title="Integrations" >}}
{{< key product_full_name >}} integrates with your cloud resources and external services.
{{< /link-card >}}

{{< link-card target="faq" icon="question-circle" title="FAQ" >}}
Frequently asked questions.
{{< /link-card >}}

{{< /variant >}}

{{< /grid >}}
