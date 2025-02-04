{@@ if serverless @@}
# Union Serverless
{@@ elif byoc @@}
# Union BYOC
{@@ endif @@}

The Union platorm empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale or compliance.

::::{grid}

:::{grid-item-card} {octicon}`rocket` Getting started
:link: user-guide/getting-started/index
:link-type: doc
:columns: 12

Jump right into writing and running Union workflows.
:::

:::{grid-item-card} {octicon}`milestone` User guide
:link: user-guide/index
:link-type: doc
:columns: 4

Learn Union concepts and features.
:::

:::{grid-item-card} {octicon}`mortar-board` Tutorials
:link: tutorials/index
:link-type: doc
:columns: 4

Walk through example applications.
:::

:::{grid-item-card} {octicon}`book` API reference
:link: api-reference/index
:link-type: doc
:columns: 4

Explore the Union APIs, SDKs, and CLIs.
:::

:::{grid-item-card} {octicon}`cloud` Deployment options
:link: user-guide/about-union
:link-type: doc
:columns: 12

Union offers two deployment options: **Serverless** and **BYOC** (Bring Your Own Cloud).
:::

::::

{@@ if serverless @@}
You are currently in the **Union Serverless** docs.
[Switch to the Union BYOC docs](https://docs.union.ai/byoc).
{@@  elif byoc @@}
You are currently in the **Union BYOC** docs.
[Switch to the Union Serverless docs](https://docs.union.ai/serverless).
{@@ endif @@}
