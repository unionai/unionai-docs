# User guide

{@@ if byok @@}

```{admonition} Prelimminary draft
This document is a preliminary draft of the BYOK user manual. Contents and procedures may change before the GA release.
```

## Deployment

In the BYOK model, the customer deploys the data plane themselves. Union data plane runs on a standard Kubernetes cluster.

Union data plane is distributed as standard Helm Charts, with overridable values.

```{admonition} Other distribution mechanisms
Although Helm Charts is a popular and well-established standard Kubernetes distribution mechanism,
our Engineering team is investigating other installation and distribution mechanisms, such as Terraform,
to more easily integrate with the customers’ deployment systems.
```

{@@ else @@}

{@@ if serverless @@}

```{admonition} Union Serverless
These docs are for [**Union Serverless**](./about-union.md#union-serverless).
Switch to another variant with the version selector above.
```

{@@ elif byoc or byok @@}

```{admonition} Union BYOC
These docs are for [**Union BYOC**](./about-union.md#union-byoc).
Switch to another variant with the version selector above.
```

{@@ elif byok @@}

```{admonition} Union BYOK
These docs are for [**Union BYOK**](./about-union.md#union-byok).
Switch to another variant with the version selector above.
```

```{admonition} Early Release Warning
Union BYOK is in Design Partner limited release. All documentation and procedures are subject to change as we drive towards General Availability.
```

{@@ endif @@}

The Union platform empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

- Run complex AI workloads with performance, scale, and efficiency.
- Achieve millisecond-level execution times with reusable containers.
- Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale or compliance.

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

{@@ if byoc or byok @@}
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

{@@ endif @@}
