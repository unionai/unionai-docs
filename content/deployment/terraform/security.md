---
title: Security Best Practices
weight: 3
variants: -flyte -serverless +byoc +selfmanaged
---

# Security Best Practices

**Never hardcode API keys directly in your Terraform configuration files.** API keys are sensitive credentials that should be stored securely and never committed to version control.

## Recommended Approaches

### 1. Use Cloud Secret Managers

Store your Union API key in a cloud-based secret manager and retrieve it dynamically:

#### AWS Secrets Manager

```hcl
data "aws_secretsmanager_secret" "unionai_api_key" {
  name = "unionai/terraform-api-key"
}

data "aws_secretsmanager_secret_version" "unionai_api_key" {
  secret_id = data.aws_secretsmanager_secret.unionai_api_key.id
}

provider "unionai" {
  api_key = data.aws_secretsmanager_secret_version.unionai_api_key.secret_string
}
```

#### Google Cloud Secret Manager

```hcl
data "google_secret_manager_secret_version" "unionai_api_key" {
  secret  = "unionai-terraform-api-key"
  project = "your-project-id"
}

provider "unionai" {
  api_key = data.google_secret_manager_secret_version.unionai_api_key.secret_data
}
```

#### Azure Key Vault

```hcl
data "azurerm_key_vault" "main" {
  name                = "your-keyvault-name"
  resource_group_name = "your-resource-group"
}

data "azurerm_key_vault_secret" "unionai_api_key" {
  name         = "unionai-api-key"
  key_vault_id = data.azurerm_key_vault.main.id
}

provider "unionai" {
  api_key = data.azurerm_key_vault_secret.unionai_api_key.value
}
```

### 2. Use HashiCorp Vault

For multi-cloud or on-premises deployments, HashiCorp Vault provides centralized secret management:

```hcl
data "vault_generic_secret" "unionai_api_key" {
  path = "secret/terraform/unionai"
}

provider "unionai" {
  api_key = data.vault_generic_secret.unionai_api_key.data["api_key"]
}
```

### 3. Use Environment Variables

For local development or CI/CD pipelines, use environment variables:

```bash
export UNIONAI_API_KEY="your-api-key-here"
```

The provider will automatically read from the `UNIONAI_API_KEY` environment variable:

```hcl
provider "unionai" {
  # api_key is read from UNIONAI_API_KEY environment variable
}
```

### 4. Use Terraform Variables with `.tfvars` Files

If using variable files, ensure they are excluded from version control:

```hcl
# variables.tf
variable "unionai_api_key" {
  description = "Union API key"
  type        = string
  sensitive   = true
}

# main.tf
provider "unionai" {
  api_key = var.unionai_api_key
}
```

Create a `terraform.tfvars` file (add to `.gitignore`):

```hcl
unionai_api_key = "your-api-key-here"
```

## Additional Security Measures

### Encrypt Terraform State

Always use encrypted remote state backends to protect sensitive data:

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "union/terraform.tfstate"
    region         = "us-west-2"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

### Use State Locking

Enable state locking to prevent concurrent modifications:

- **AWS S3**: Use DynamoDB for state locking
- **Google Cloud Storage**: Automatic state locking
- **Azure Blob Storage**: Automatic state locking

### Rotate API Keys Regularly

Implement a rotation schedule for your API keys:

1. Generate a new API key using the Flyte CLI
2. Update the key in your secret manager
3. Verify Terraform can authenticate with the new key
4. Delete the old API key

### Restrict Provider Permissions

Use the `allowed_orgs` parameter to limit which organizations the provider can access:

```hcl
provider "unionai" {
  api_key      = var.unionai_api_key
  allowed_orgs = ["production-org"]
}
```

This prevents accidental operations on the wrong organization.

### Use Separate API Keys per Environment

Create different API keys for each environment (development, staging, production):

```hcl
# Development
provider "unionai" {
  alias   = "dev"
  api_key = var.dev_api_key
}

# Production
provider "unionai" {
  alias   = "prod"
  api_key = var.prod_api_key
}
```

## Security Checklist

- ✅ Store API keys in a secret manager or secure vault
- ✅ Use environment variables for local development
- ✅ Mark variables containing secrets as `sensitive = true`
- ✅ Add `*.tfvars`, `*.tfstate`, and `*.tfstate.backup` to `.gitignore`
- ✅ Use remote state backends with encryption enabled
- ✅ Enable state locking to prevent concurrent modifications
- ✅ Rotate API keys regularly
- ✅ Use separate API keys per environment
- ✅ Restrict provider access with `allowed_orgs`
- ✅ Review Terraform plans before applying changes
- ❌ Never commit API keys to version control
- ❌ Never hardcode API keys in `.tf` files
- ❌ Never share API keys in plain text (chat, email, etc.)
- ❌ Never use production API keys in development environments

## CI/CD Pipeline Security

When using Terraform in CI/CD pipelines:

### GitHub Actions

```yaml
name: Terraform

on:
  push:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2

      - name: Terraform Init
        env:
          UNIONAI_API_KEY: ${{ secrets.UNIONAI_API_KEY }}
        run: terraform init

      - name: Terraform Apply
        env:
          UNIONAI_API_KEY: ${{ secrets.UNIONAI_API_KEY }}
        run: terraform apply -auto-approve
```

### GitLab CI

```yaml
terraform:
  image: hashicorp/terraform:latest
  variables:
    UNIONAI_API_KEY: $UNIONAI_API_KEY
  script:
    - terraform init
    - terraform apply -auto-approve
  only:
    - main
```

### Best Practices for CI/CD

- Store API keys as encrypted secrets in your CI/CD platform
- Use separate API keys for CI/CD (not personal keys)
- Implement approval gates for production deployments
- Enable audit logging for all Terraform operations
- Restrict who can view/modify CI/CD secrets

## Additional Resources

- [Terraform Security Best Practices](https://developer.hashicorp.com/terraform/tutorials/configuration-language/sensitive-variables)
- [HashiCorp Vault Documentation](https://developer.hashicorp.com/vault/docs)
- [Flyte CLI Documentation](../../api-reference/flyte-cli)
