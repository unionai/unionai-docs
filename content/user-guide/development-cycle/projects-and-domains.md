---
title: Projects and domains
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Projects and domains

Projects and domains are the principle organizational categories into which you group your workflows in {{< key product_name >}}.

Projects define groups of task, workflows, launch plans and other entities that share a functional purpose.
Domains represent distinct steps through which the entities in a project transition as they proceed through the development cycle.

{{< variant serverless >}}
{{< markdown >}}

{{< key product_name >}} provides three domains: `development`, `staging`, and `production`.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

By default, {{< key product_name >}} provides three domains: `development`, `staging`, and `production`.
During onboarding, you can configure your {{< key product_name >}} instance to have different domains.
Speak to the {{< key product_name >}} team for more information.

{{< /markdown >}}
{{< /variant >}}

Projects and domains are orthogonal to each other, meaning that a project has
multiple domains and a domain has multiple projects.

Here is an example arrangement:

|           | Development       | Staging           | Production        |
|-----------|-------------------|-------------------|-------------------|
| Project 1 | workflow_1 (v2.0) | workflow_1 (v1.0) | workflow_1 (v1.0) |
| Project 2 | workflow_2 (v2.0) | workflow_2 (v1.0) | workflow_2 (v1.0) |

## Projects

Projects represent independent workflows related to specific teams, business
areas, or applications.  Each project is isolated from others, but workflows can
reference entities (workflows or tasks) from other projects to reuse
generalizable resources.

## Domains

Domains represent distinct environments orthogonal to the set of projects in
your org within {{< key product_name >}}, such as development, staging, and production.  These
enable dedicated configurations, permissions, secrets, cached execution history,
and resource allocations for each environment, preventing unintended impact on
other projects and/or domains.

Using domains allows for a clear separation between environments, helping ensure
that development and testing don't interfere with production workflows.

A production domain ensures a “clean slate” so that cached development
executions do not result in unexpected behavior.  Additionally, secrets may be
configured for external production data sources.

## When to use different {{< key product_name >}} projects?

Projects help group independent workflows related to specific teams, business
areas, or applications.  Generally speaking, each independent team or ML product
should have its own {{< key product_name >}} project.  Even though these are isolated from one
another, teams may reference entities (workflows or tasks) from other {{< key product_name >}}
projects to reuse generalizable resources.  For example, one team may create a
generalizable task to train common model types.  However, this requires advanced
collaboration and common coding standards.

When setting up workflows in {{< key product_name >}}, effective use of **projects** and
**domains** is key to managing environments, permissions, and resource
allocation.  Below are best practices to consider when organizing workflows in
{{< key product_name >}}.

## Projects and Domains: The Power of the Project-Domain Pair

{{< key product_name >}} uses a project-domain pair to create isolated configurations for
workflows. This pairing allows for:

* **Dedicated Permissions**: Through Role-Based Access Control (RBAC), users can be assigned roles with tailored permissions—such as contributor or admin—specific to individual project-domain pairs. This allows fine-grained control over who can manage or execute workflows within each pair, ensuring that permissions are both targeted and secure. More details [here](../administration/user-management#custom-roles-and-policies).

* **Resource and Execution Monitoring**: Track and monitor resource utilization, executions, and performance metrics on a dashboard unique to each project-domain pair. This helps maintain visibility over workflow execution and ensures optimal performance. More details [here](../administration/resources).

* **Resource Allocations and Quotas**: By setting quotas for each project-domain pair, {{< key product_name >}} can ensure that workflows do not exceed designated limits, preventing any project or domain from unintentionally impacting resources available to others. Additionally, you can configure unique resource defaults—such as memory, CPU, and storage allocations—for each project-domain pair. This allows each pair to meet the specific requirements of its workflows, which is particularly valuable given the unique needs across different projects. More details [here](../core-concepts/tasks/task-hardware-environment/customizing-task-resources#execution-defaults-and-resource-quotas) and [here](../administration/resources).

* **Configuring Secrets**: {{< key product_name >}} allows you to configure secrets at the project-domain level, ensuring sensitive information, such as API keys and tokens, is accessible only within the specific workflows that need them. This enhances security by isolating secrets according to the project and domain, reducing the risk of unauthorized access across environments. More details [here](managing-secrets).

## Domains: Clear Environment Separation

Domains represent distinct environments within {{< key product_name >}}, allowing clear separation between development, staging, and production. This structure helps prevent cross-environment interference, ensuring that changes made in development or testing do not affect production workflows. Using domains for this separation ensures that workflows can evolve in a controlled manner across different stages, from initial development through to production deployment.

## Projects: Organizing Workflows by Teams, Business Areas, or Applications

Projects in {{< key product_name >}} are designed to group independent workflows around specific teams, business functions, or applications. By aligning projects to organizational structure, you can simplify access control and permissions while encouraging a clean separation of workflows across different teams or use cases. Although workflows can reference each other across projects, it's generally cleaner to maintain independent workflows within each project to avoid complexity.

{{< key product_name >}}’s CLI tools and SDKs provide options to specify projects and domains easily:

* **CLI Commands**: In most commands within the `{{< key cli >}}` and `uctl` CLIs, you can specify the project and domain by using the `--project` and `--domain` flags, enabling precise control over which project-domain pair a command applies to. More details [here](../../api-reference/union-cli) and [here](../../api-reference/uctl-cli).

* **Python SDK**: When working with the `{{< key kit >}}` SDK, you can leverage `{{< key kit_remote >}}` to define the project and domain for workflow interactions programmatically, ensuring that all actions occur in the intended environment. More details [here](union-remote).
