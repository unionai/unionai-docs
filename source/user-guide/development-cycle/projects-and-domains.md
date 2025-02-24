# Projects and domains

Projects and domains are the principle organizational categories into which you group your workflows in Union.

Projects define groups of task, workflows, launch plans and other entities that share a functional purpose.
Domains represent distinct steps through which the entities in a project transition as they proceed through the development cycle.

{@@ if serverless @@}
Union provides three domains: `development`, `staging`, and `production`.
{@@ elif byoc or byok or flyte @@}
By default, Union provides three domains: `development`, `staging`, and `production`.
During onboarding, you can configure your Union instance to have different domains.
Speak to the Union team for more information.
{@@ endif @@}

Projects and domains are orthogonal to each other, meaning that a project has multiple domains and a domain has multiple projects.
Here is an example arrangement:

:::{list-table} Projects and domains
:widths: auto
:header-rows: 1
:stub-columns: 1
*   -
    - Development
    - Staging
    - Production
*   - Project_1
    - workflow_1 (v=2.0)
    - workflow_1 (v=1.0)
    - workflow_1 (v=1.0)
*   - Project_2
    - workflow_2 (v=2.0)
    - workflow_2 (v=1.0)
    - workflow_2 (v=1.0)
:::

## Projects

Projects represent independent workflows related to specific teams, business areas, or applications.
Each project is isolated from others, but workflows can reference entities (workflows or tasks) from other projects to reuse generalizable resources.


## Domains

Domains represent distinct environments orthogonal to the set of projects in your org within Union, such as development, staging, and production.
These enable dedicated configurations, permissions, secrets, cached execution history, and resource allocations for each environment, preventing unintended impact on other projects and/or domains.

Using domains allows for a clear separation between environments, helping ensure that development and testing don't interfere with production workflows.

A production domain ensures a “clean slate” so that cached development executions do not result in unexpected behavior.
Additionally, secrets may be configured for external production data sources.


## When to use different Union projects?

Projects help group independent workflows related to specific teams, business areas, or applications.
Generally speaking, each independent team or ML product should have its own Union project.
Even though these are isolated from one another, teams may reference entities (workflows or tasks) from other Union projects to reuse generalizable resources.
For example, one team may create a generalizable task to train common model types.
However, this requires advanced collaboration and common coding standards.

When setting up workflows in Union, effective use of **projects** and **domains** is key to managing environments, permissions, and resource allocation.
Below are best practices to consider when organizing workflows in Union.


## Projects and Domains: The Power of the Project-Domain Pair

Union uses a project-domain pair to create isolated configurations for workflows. This pairing allows for:

* **Dedicated Permissions**: Through Role-Based Access Control (RBAC), users can be assigned roles with tailored permissions—such as contributor or admin—specific to individual project-domain pairs. This allows fine-grained control over who can manage or execute workflows within each pair, ensuring that permissions are both targeted and secure. More details [here](https://docs.union.ai/byoc/user-guide/administration/user-management#custom-roles-and-policies).

* **Resource and Execution Monitoring**: Track and monitor resource utilization, executions, and performance metrics on a dashboard unique to each project-domain pair. This helps maintain visibility over workflow execution and ensures optimal performance. More details [here](https://docs.union.ai/byoc/user-guide/administration/usage#usage).

* **Resource Allocations and Quotas**: By setting quotas for each project-domain pair, Union can ensure that workflows do not exceed designated limits, preventing any project or domain from unintentionally impacting resources available to others. Additionally, you can configure unique resource defaults—such as memory, CPU, and storage allocations—for each project-domain pair. This allows each pair to meet the specific requirements of its workflows, which is particularly valuable given the unique needs across different projects. More details [here](https://docs.union.ai/byoc/user-guide/core-concepts/tasks/task-hardware-environment/customizing-task-resources#execution-defaults-and-resource-quotas) and [here](https://docs.union.ai/byoc/user-guide/administration/usage#resource-quotas).

* **Configuring Secrets**: Union allows you to configure secrets at the project-domain level, ensuring sensitive information, such as API keys and tokens, is accessible only within the specific workflows that need them. This enhances security by isolating secrets according to the project and domain, reducing the risk of unauthorized access across environments. More details [here](https://docs.union.ai/byoc/user-guide/development-cycle/managing-secrets#managing-secrets).

## Domains: Clear Environment Separation

Domains represent distinct environments within Union, allowing clear separation between development, staging, and production. This structure helps prevent cross-environment interference, ensuring that changes made in development or testing do not affect production workflows. Using domains for this separation ensures that workflows can evolve in a controlled manner across different stages, from initial development through to production deployment.

## Projects: Organizing Workflows by Teams, Business Areas, or Applications

Projects in Union are designed to group independent workflows around specific teams, business functions, or applications. By aligning projects to organizational structure, you can simplify access control and permissions while encouraging a clean separation of workflows across different teams or use cases. Although workflows can reference each other across projects, it's generally cleaner to maintain independent workflows within each project to avoid complexity.

Union’s CLI tools and SDKs provide options to specify projects and domains easily:

* **CLI Commands**: In most commands within the `union` and `uctl` CLIs, you can specify the project and domain by using the `--project` and `--domain` flags, enabling precise control over which project-domain pair a command applies to. More details [here](https://docs.union.ai/byoc/api-reference/union-cli) and [here](https://docs.union.ai/byoc/api-reference/uctl-cli/).

* **Python SDK**: When working with the `flytekit` and `union` Python SDKs, you can leverage `FlyteRemote` and `UnionRemote` to define the project and domain for workflow interactions programmatically, ensuring that all actions occur in the intended environment. More details [here](https://docs.union.ai/byoc/user-guide/development-cycle/union-remote#unionremote) and [here](https://docs.flyte.org/en/latest/api/flytekit/design/control_plane.html).


