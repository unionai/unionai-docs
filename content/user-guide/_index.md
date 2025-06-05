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

# Flyte OSS

Flyte OSS is a free and open source platform that provides a full suite of powerful features for orchestrating AI workflows.
You deploy and manage Flyte OSS yourself, on your own cloud infrastructure.

> [!NOTE]
> This documentation for Flyte OSS is maintained by Union.ai.
> You can switch to the documentation for the commercial versions with the selector above.

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}

# {{< key product_name >}} Serverless

Union.ai Serverless provides [all the features of Flyte OSS, plus much more](./about-union#-key-product_name--serverless),
all in a turn-key, fully-managed, cloud environment.
There is zero infrastructure to deal with, and you pay only for the resources you use.
Your data and workflow code is stored safely and securely in Union.ai’s cloud infrastructure.

> [!NOTE]
> You can switch to another product version with the selector above.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc >}}
{{< markdown >}}

# {{< key product_name >}} BYOC

{{< key product_name >}} BYOC (Bring Your Own Cloud) provides [all the features of Flyte, plus much more](./about-union#-key-product_name--byoc) in an environment where you keep your data and workflow code on your infrastructure, while {{< key product_name >}} takes care of the management.

> [!NOTE]
> You can switch to another product version with the selector above.

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

# {{< key product_name >}} Self-managed

{{< key product_name >}} Self-managed provides [all the features of Flyte, plus much more](./about-union#-key-product_name--self-managed) while letting you keep your data and workflow code on your infrastructure and under your own management.

> [!NOTE]
> You can switch to another product version with the selector above.

{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

Flyte is an open-source, Kubernetes-native workflow orchestrator implemented in Go.

Flyte empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.


{{< /markdown >}}
{{< /variant >}}
{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

The {{< key product_name >}} platform empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale or compliance.

{{< /markdown >}}
{{< /variant >}}

{{< grid >}}
{{< link-card target="about-flyte-2" icon="lightbulb" title="About Flyte 2" >}}
Flyte 2 provides a new and powerful way author and run workflows and apps on your Flyte OSS or Union cluster.
{{< /link-card >}}

{{< link-card target="getting-started" icon="123" title="Getting started" >}}
Build your first Flyte workflow, exploring the major features of the platform along the way.
{{< /link-card >}}

{{< /grid >}}
