---
title: Resource Management
weight: 2
variants: -flyte -serverless -byoc +selfmanaged
---

# Managing Union Resources with Terraform

The Union Terraform provider enables you to manage Union resources using infrastructure-as-code principles. This page provides an overview of the provider's capabilities, including authentication, available resources, and data sources.

## Provider Configuration

### Basic Configuration

Configure the Union provider in your Terraform configuration:

```hcl
terraform {
  required_providers {
    unionai = {
      source  = "unionai/unionai"
      version = "~> 1.0"
    }
  }
}

provider "unionai" {
  api_key      = var.unionai_api_key
  allowed_orgs = ["your-org-name"]
}
```

### Configuration Parameters

- **`api_key`** (Required): Your Union API key for authentication
- **`allowed_orgs`** (Optional): List of organization names to restrict operations to, preventing unintended operations across multiple organizations

## Authentication

The Union Terraform provider uses API key authentication. You can provide your API key in two ways:

### 1. Provider Configuration

Specify the API key directly in the provider block (use variables to avoid hardcoding):

```hcl
provider "unionai" {
  api_key = var.unionai_api_key
}
```

### 2. Environment Variable

Set the `UNIONAI_API_KEY` environment variable:

```bash
export UNIONAI_API_KEY="your-api-key"
```

### Generating an API Key

Create an API key using the Flyte CLI:

```bash
union create api-key admin --name "terraform-api-key"
```

For more information on creating API keys, see the [Flyte CLI documentation](../../api-reference/flyte-cli#flyte-create-api-key).

Save the generated key securely, as it will be used to authenticate all Terraform operations against your Union deployment.

## Available Resources

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
}
```

### Policies

Create access policies that define permissions:

```hcl
resource "unionai_policy" "example" {
  name        = "project-access-policy"
  description = "Policy for project access"
  # Policy configuration details
}
```

### API Keys

Generate and manage API keys programmatically:

```hcl
resource "unionai_api_key" "example" {
  name        = "automation-key"
  description = "API key for CI/CD automation"
}
```

### OAuth Applications

Configure OAuth applications for external integrations:

```hcl
resource "unionai_oauth_application" "example" {
  name         = "external-app"
  redirect_uri = "https://example.com/callback"
}
```

### Access Assignments

Assign users and applications to resources with specific roles:

```hcl
resource "unionai_user_access" "example" {
  user_id    = unionai_user.example.id
  project_id = unionai_project.example.id
  role_id    = unionai_role.example.id
}

resource "unionai_application_access" "example" {
  application_id = unionai_oauth_application.example.id
  project_id     = unionai_project.example.id
  role_id        = unionai_role.example.id
}
```

## Available Data Sources

Data sources allow you to query existing Union resources for use in your Terraform configuration.

### Projects

Query existing projects:

```hcl
data "unionai_project" "existing" {
  name = "existing-project"
}
```

### Users

Look up user information:

```hcl
data "unionai_user" "existing" {
  email = "user@example.com"
}
```

### Roles

Reference existing roles:

```hcl
data "unionai_role" "admin" {
  name = "admin"
}
```

### Policies

Query existing policies:

```hcl
data "unionai_policy" "existing" {
  name = "default-policy"
}
```

### API Keys

Reference existing API keys:

```hcl
data "unionai_api_key" "existing" {
  name = "existing-key"
}
```

### Applications

Look up OAuth applications:

```hcl
data "unionai_application" "existing" {
  name = "existing-app"
}
```

### Data Plane Information

Query information about the data plane:

```hcl
data "unionai_dataplane" "current" {
  id = "dataplane-id"
}
```

### Control Plane Information

Access control plane details:

```hcl
data "unionai_controlplane" "current" {
  # Control plane data source
}
```

### Data Plane Listings

List all available data planes:

```hcl
data "unionai_dataplanes" "all" {
  # Returns list of all data planes
}
```

## Best Practices

### Use Variables for Sensitive Data

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

### Organize Resources with Modules

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

### Use Organization Restrictions

Prevent accidental operations across multiple organizations:

```hcl
provider "unionai" {
  api_key      = var.unionai_api_key
  allowed_orgs = ["production-org"]
}
```

### Version Control Your Configuration

Store your Terraform configuration in version control to track changes over time, but ensure sensitive files are excluded:

```gitignore
# .gitignore
*.tfvars
*.tfstate
*.tfstate.backup
.terraform/
```

### Use Remote State

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

## Example: Complete Setup

Here's a complete example that creates a project with access control:

```hcl
terraform {
  required_providers {
    unionai = {
      source  = "unionai/unionai"
      version = "~> 1.0"
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
}

# Create a user
resource "unionai_user" "data_scientist" {
  email      = "data.scientist@example.com"
  first_name = "Jane"
  last_name  = "Smith"
}

# Assign user to project with role
resource "unionai_user_access" "scientist_access" {
  user_id    = unionai_user.data_scientist.id
  project_id = unionai_project.ml_pipeline.id
  role_id    = unionai_role.ml_engineer.id
}

# Create API key for automation
resource "unionai_api_key" "ci_cd" {
  name        = "ci-cd-pipeline"
  description = "API key for CI/CD automation"
}
```

## Additional Resources

- [Union Terraform Provider Documentation](https://registry.terraform.io/providers/unionai/unionai/latest/docs)
- [Terraform Documentation](https://www.terraform.io/docs)
- [Flyte CLI Documentation](../../api-reference/flyte-cli)

## Requirements

- **Terraform**: >= 1.0
- **Union API Key**: Generated via Flyte CLI
- **Go**: >= 1.24 (for development only)

## Support and Contributions

The Union Terraform provider is open source and licensed under the Mozilla Public License 2.0. For the complete provider documentation, visit the [Terraform Registry](https://registry.terraform.io/providers/unionai/unionai/latest/docs).
