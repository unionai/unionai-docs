---
title: Resource management
weight: 2
variants: -flyte +union
---

# Managing Union resources with Terraform

The Union Terraform provider enables you to manage Union resources using infrastructure-as-code principles. This page provides an overview of the provider's capabilities, including authentication, available resources, and data sources.

## Provider configuration

### Basic configuration

Configure the Union provider in your Terraform configuration:

```hcl
terraform {
  required_providers {
    unionai = {
      source  = "unionai/unionai"
      version = "~> 0.2"
    }
  }
}

provider "unionai" {
  api_key      = var.unionai_api_key
  allowed_orgs = ["your-org-name"]
}
```

### Configuration parameters

- **`api_key`** (Required): Your Union API key for authentication
- **`allowed_orgs`** (Optional): List of organization names to restrict operations to, preventing unintended operations across multiple organizations

## Authentication

The Union Terraform provider uses API key authentication. You can provide your API key in two ways:

### 1. Provider configuration

Specify the API key directly in the provider block (use variables to avoid hardcoding):

```hcl
provider "unionai" {
  api_key = var.unionai_api_key
}
```

### 2. Environment variable

Set the `UNIONAI_API_KEY` environment variable:

```bash
export UNIONAI_API_KEY="your-api-key"
```

### Generating an API key

Create an API key using the `flyte` CLI:

```bash
flyte create api-key --name "terraform-api-key"
```

For more information on creating API keys, see the [Flyte CLI documentation](../../api-reference/flyte-cli#flyte-create-api-key).

Save the generated key securely, as it will be used to authenticate all Terraform operations against your Union deployment.

## Available resources

The Union Terraform provider supports the following resources for managing your Union deployment:

### Projects

Create and manage Union projects:

```hcl
resource "unionai_project" "example" {
  name        = "my-project"
  description = "Example project managed by Terraform"
}
```

Projects are the primary organizational unit in Union, containing workflows, tasks, and executions.

### Users

Manage user accounts:

```hcl
resource "unionai_user" "example" {
  email      = "user@example.com"
  first_name = "John"
  last_name  = "Doe"
}
```

### Roles

Define custom roles for access control:

```hcl
resource "unionai_role" "example" {
  name        = "custom-role"
  description = "Custom role with specific permissions"
  actions = [
    "create_flyte_executions",
    "view_flyte_inventory",
  ]
}
```

The `actions` argument is required: it is the set of actions the role grants (for example, `create_flyte_executions`, `register_flyte_inventory`, `administer_project`).

### Policies

Create access policies that define permissions:

```hcl
resource "unionai_policy" "example" {
  name        = "project-access-policy"
  description = "Policy for project access"

  project {
    id      = unionai_project.example.id
    role_id = unionai_role.example.id
    domains = ["development", "staging"]
  }
}
```

A policy binds a role to a subject at a given scope. Use an `organization`, `project`, or `domain` block (each takes an `id` and a `role_id`); the `project` block also accepts an optional `domains` set.

### API keys

Generate and manage API keys programmatically:

```hcl
resource "unionai_api_key" "example" {
  id = "automation-key"
}
```

The `id` is the only argument; it must be unique within your organization. The generated `secret` is a read-only, sensitive attribute stored in state, available only at creation time.

### OAuth applications

Configure OAuth applications for external integrations:

```hcl
resource "unionai_application" "example" {
  client_id   = "external-app"
  client_name = "External Application"

  grant_types   = ["AUTHORIZATION_CODE"]
  redirect_uris = ["https://example.com/callback"]
}
```

The required arguments are `client_id` and `client_name`. `redirect_uris` is a set of strings (not a single value). The client `secret` is a read-only, sensitive attribute available only at creation time.

### Access assignments

Access is policy-based: a policy carries the role-to-scope binding, and an access resource assigns that policy to a user or an application. Each access resource takes just two arguments.

```hcl
# Assign a policy to a user
resource "unionai_user_access" "example" {
  user_id   = unionai_user.example.id
  policy_id = unionai_policy.example.id
}

# Assign a policy to an application
resource "unionai_application_access" "example" {
  app_id    = unionai_application.example.id
  policy_id = unionai_policy.example.id
}
```

## Available data sources

Data sources allow you to query existing Union resources for use in your Terraform configuration. Each is looked up by its `id`; attributes such as `name` and `email` are read-only outputs, not lookup keys.

### Projects

Query an existing project:

```hcl
data "unionai_project" "existing" {
  id = "my-project-id"
}
```

### Users

Look up user information:

```hcl
data "unionai_user" "existing" {
  id = "user-id"
}
```

### Roles

Reference an existing role:

```hcl
data "unionai_role" "admin" {
  id = "admin-role-id"
}
```

### Policies

Query an existing policy:

```hcl
data "unionai_policy" "existing" {
  id = "policy-id"
}
```

### API keys

Reference an existing API key:

```hcl
data "unionai_api_key" "existing" {
  id = "api-key-id"
}
```

### Applications

Look up an OAuth application:

```hcl
data "unionai_application" "existing" {
  id = "app-client-id"
}
```

### Data plane information

Query information about the data plane:

```hcl
data "unionai_dataplane" "current" {
  id = "dataplane-id"
}
```

### Control plane information

Access control plane details:

```hcl
data "unionai_controlplane" "current" {
  # Control plane data source
}
```

### Data plane listings

List all available data planes:

```hcl
data "unionai_dataplanes" "all" {
  # Returns list of all data planes
}
```

## Best practices

### Use variables for sensitive data

Never hardcode sensitive information like API keys in your Terraform files:

```hcl
variable "unionai_api_key" {
  description = "Union API key"
  type        = string
  sensitive   = true
}

provider "unionai" {
  api_key = var.unionai_api_key
}
```

### Organize resources with modules

Structure your Terraform code using modules for reusability:

```
terraform/
├── modules/
│   ├── project/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── access-control/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
└── main.tf
```

### Use organization restrictions

Prevent accidental operations across multiple organizations:

```hcl
provider "unionai" {
  api_key      = var.unionai_api_key
  allowed_orgs = ["production-org"]
}
```

### Version control your configuration

Store your Terraform configuration in version control to track changes over time, but ensure sensitive files are excluded:

```gitignore
# .gitignore
*.tfvars
*.tfstate
*.tfstate.backup
.terraform/
```

### Use remote state

For team environments, use remote state storage:

```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "union/terraform.tfstate"
    region = "us-west-2"
  }
}
```

## Example: complete setup

Here's a complete example that creates a project with access control:

```hcl
terraform {
  required_providers {
    unionai = {
      source  = "unionai/unionai"
      version = "~> 0.2"
    }
  }
}

provider "unionai" {
  api_key      = var.unionai_api_key
  allowed_orgs = ["my-organization"]
}

# Create a project
resource "unionai_project" "ml_pipeline" {
  name        = "ml-pipeline"
  description = "Machine learning pipeline project"
}

# Create a custom role
resource "unionai_role" "ml_engineer" {
  name        = "ml-engineer"
  description = "Role for ML engineers"
  actions = [
    "create_flyte_executions",
    "view_flyte_inventory",
  ]
}

# Create a user
resource "unionai_user" "data_scientist" {
  first_name = "Jane"
  last_name  = "Smith"
  email      = "data.scientist@example.com"
}

# Bind the role to the project with a policy
resource "unionai_policy" "ml_pipeline_access" {
  name        = "ml-pipeline-access"
  description = "Grant the ML engineer role on the ML pipeline project"

  project {
    id      = unionai_project.ml_pipeline.id
    role_id = unionai_role.ml_engineer.id
  }
}

# Assign the policy to the user
resource "unionai_user_access" "scientist_access" {
  user_id   = unionai_user.data_scientist.id
  policy_id = unionai_policy.ml_pipeline_access.id
}

# Create an API key for automation
resource "unionai_api_key" "ci_cd" {
  id = "ci-cd-pipeline-key"
}
```

## Additional resources

- [Union Terraform Provider Documentation](https://registry.terraform.io/providers/unionai/unionai/latest/docs)
- [Terraform Documentation](https://www.terraform.io/docs)
- [Flyte CLI Documentation](../../api-reference/flyte-cli)

## Requirements

- **Terraform**: >= 1.0
- **Union API key**: Generated via the `flyte` CLI
- **Go**: >= 1.24 (for development only)

## Support and contributions

The Union Terraform provider is open source and licensed under the Mozilla Public License 2.0. For the complete provider documentation, visit the [Terraform Registry](https://registry.terraform.io/providers/unionai/unionai/latest/docs).
