---
title: Getting started
weight: 3
variants: +flyte +union
llm_readable_bundle: true
---

# Getting started

{{< llm-bundle-note >}}

This section gives you a quick introduction to writing and running {{< key product_name >}} workflows.


{{< variant union >}}
{{< markdown >}}

## Gather your credentials

After your administrator has onboarded you to {{< key product_name >}} (see [Deployment](../../deployment)), you should have the following at hand:

- Your {{< key product_name >}} credentials.
- The URL of your {{< key product_name >}} instance. We will refer to this as `<union-host-url>` below.

## Log into {{< key product_name >}}

Navigate to the UI at `<union-host-url>` and log in with your credentials.
Once you have logged in you should see the {{< key product_name >}} UI.

To get started, try selecting the default project, called `{{< key default_project >}}`, from the list of projects.
This will take you to `{{< key default_project >}}` project dashboard:

![{{< key product_name >}} UI](../../_static/images/quick-start/byoc-dashboard.png)

This dashboard gives you an overview of the workflows and tasks in your project.
Since you are just starting out, it will be empty.
To build and deploy your first workflow, the first step is to [set up your local environment](./local-setup).

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

## Try Flyte on your local machine

You can also install Flyte's SDK (called `flytekit`) and a local Flyte cluster to run workflows on your local machine.

To get started, follow the instructions on the next page, [Local setup](./local-setup).

{{< /markdown >}}
{{< /variant >}}
