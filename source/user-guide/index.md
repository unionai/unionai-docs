# User guide

{@@ if flyte @@}

```{admonition} Flyte
These docs are for [**Flyte**](./about-union.md#flyte).
Switch to another variant with the version selector above.
```
{@@ elif serverless @@}

```{admonition} Union Serverless
These docs are for [**Union Serverless**](./about-union.md#union-serverless).
Switch to another variant with the version selector above.
```
{@@ elif byoc @@}

```{admonition} Union BYOC
These docs are for [**Union BYOC**](./about-union.md#union-byoc).
Switch to another variant with the version selector above.
```
{@@ elif byok @@}

```{admonition} Union BYOK
These docs are for [**Union BYOK**](./about-union.md#union-byok).
Switch to another variant with the version selector above.
```
{@@ endif @@}

The Union platform empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale or compliance.


::::{grid} 2

:::{grid-item-card} {octicon}`telescope` About Union
:link: about-union
:link-type: doc

Union builds on the leading OSS orchestrator, Flyte, to provide a powerful, scalable, and flexible platform for AI workflows.
:::

:::{grid-item-card} {octicon}`file-binary` Getting started
:link: getting-started/index
:link-type: doc

Build your first Union workflow, exploring the major features of the platform along the way.
:::

:::{grid-item-card} {octicon}`mortar-board` Core concepts
:link: core-concepts/index
:link-type: doc

Understand the core concepts of the Union platform.
:::

:::{grid-item-card} {octicon}`iterations` Development cycle
:link: development-cycle/index
:link-type: doc

Explore the Union development cycle from experimentation to production.
:::

:::{grid-item-card} {octicon}`arrow-switch` Data input/output
:link: data-input-output/index
:link-type: doc

Manage the input and output of data in your Union workflow.
:::

{@@ if byoc or byok or flyte @@}
:::{grid-item-card} {octicon}`person-add` Administration
:link: administration/index
:link-type: doc

Union BYOC administrators can manage users, projects, and resources.
:::

:::{grid-item-card} {octicon}`tools` Integrations
:link: integrations/index
:link-type: doc

Union BYOC integrates with your cloud resources and external services.
:::

:::{grid-item-card} {octicon}`question` FAQ
:link: faq
:link-type: doc

Frequently asked questions.
:::
{@@ endif @@}

::::
