---
title: User guide
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
top_menu: true
site_root: true
sidebar_expanded: true
---

{{< variant byoc >}}
{{< markdown >}}

# {{< key product_name >}} BYOC

{{< key product_name >}} BYOC (Bring Your Own Cloud) provides all the features of Flyte OSS, plus much more in an environment where you keep your data and workflow code on your infrastructure, while {{< key product_name >}} takes care of the management.

> [!NOTE]
> You can switch to another product version with the selector above.

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

# {{< key product_name >}} Self-managed

{{< key product_name >}} Self-managed provides all the features of Flyte OSS, plus much more while letting you keep your data and workflow code on your infrastructure and under your own management.

> [!NOTE]
> You can switch to another product version with the selector above.

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
Build your first Flyte workflow
{{< /link-card >}}

{{< link-card target="task-environment" icon="thermometer-sun" title="Task environment" >}}
Task environments define the resources and dependencies for your tasks.
{{< /link-card >}}

{{< link-card target="container-images" icon="123" title="Container images" >}}
Each task runs in its own container, and every container needs a container image to define it.
{{< /link-card >}}

{{< link-card target="error-handling" icon="bug" title="Error handling" >}}
Dynamically adjust your settings and retry when you run out of memory, or other resources.
{{< /link-card >}}

{{< link-card target="files-and-directories" icon="folder2-open" title="Files and directories" >}}
Pass files and directories between tasks without worrying about transferring data from one container to the next.
{{< /link-card >}}

{{< link-card target="dataclasses" icon="clipboard-data" title="Dataclasses" >}}
Work with Python dataclasses to define your data types.
{{< /link-card >}}

{{< link-card target="notebooks" icon="journal-album" title="Notebooks" >}}
Run your workflows in Jupyter notebooks.
{{< /link-card >}}

{{< link-card target="scaling" icon="graph-up-arrow" title="Scaling" >}}
Scale effortlessly using native Python contructs.
{{< /link-card >}}

{{< link-card target="considerations" icon="cone-striped" title="Considerations" >}}
Some considerations to keep in mind when working with Flyte.
{{< /link-card >}}

{{< link-card target="flyte-cli" icon="terminal" title="Flyte CLI" >}}
Deploy and run workflows both programmatically and via CLI.
{{< /link-card >}}

{{< /grid >}}
