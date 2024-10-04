{@@ if serverless @@}
# Union Serverless
{@@ elif byoc @@}
# Union BYOC
{@@ endif @@}

The Union orchestrator empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with unparalleled performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale or compliance.

:::{admonition} Deployment options
Union offers two deployment options: [**Serverless** and **BYOC**](guide/union-overview).

{@@ if serverless @@}
You are currently in the **Union Serverless** docs.
[Switch to the Union BYOC docs](https://docs.union.ai/byoc).
{@@  elif byoc @@}
You are currently in the **Union BYOC** docs.
[Switch to the Union Serverless docs](https://docs.union.ai/serverless).
{@@ endif @@}
:::

::::{grid}

:::{grid-item-card} {octicon}`rocket` Quick start
:link: quick-start.html
:link-type: url
:columns: 6 6 6 12

Jump right into writing and running Union workflows.
:::

:::{grid-item-card} {octicon}`milestone` Guide
:link: guide/index.html
:link-type: url
:columns: 6 6 6 12

Learn Union concepts and features.
:::

:::{grid-item-card} {octicon}`mortar-board` Tutorials
:link: tutorials/index.html
:link-type: url
:columns: 6 6 6 12

Walk through example applications.
:::

:::{grid-item-card} {octicon}`book` API
:link: api/index.html
:link-type: url
:columns: 6 6 6 12

Explore the Union APIs, SDKs, and CLIs.
:::

::::
