---
title: Installation
weight: 1
variants: -flyte +union
---

# Installing the Union Terraform provider

The Union Terraform provider is distributed through the [Terraform Registry](https://registry.terraform.io/providers/unionai/unionai/latest/docs). Terraform installs it automatically when you declare it in your configuration and run `terraform init`, so there is no separate download step. Add the provider block below, then run `terraform init` to fetch it.

## Quick start

To use the Union Terraform provider, add it to your Terraform configuration:

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
  api_key = var.unionai_api_key
}
```

> **Security note:** Never hardcode API keys in your Terraform files. See [Security best practices](./security) for recommended approaches to securely manage your API keys.

## Versioning

To choose the appropriate version of the provider (likely you should choose latest):

1. Visit the Provider Registry site and observe the latest version number
2. Use that version number in the provider declaration above

For detailed installation instructions, please refer to the [Terraform Registry documentation](https://registry.terraform.io/providers/unionai/unionai/latest/docs).
