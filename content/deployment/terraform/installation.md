---
title: Installation
weight: 1
variants: -flyte -serverless +byoc +selfmanaged
---

# Installing the Union Terraform Provider

Documentation for installing and configuring the Union Terraform provider is coming soon.

In the meantime, you can find the latest information about the provider in the [Terraform Registry](https://registry.terraform.io/providers/unionai/unionai/latest/docs).

## Quick Start

To use the Union Terraform provider, add it to your Terraform configuration:

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
  api_key = var.unionai_api_key
}
```

For detailed installation instructions, please refer to the [Terraform Registry documentation](https://registry.terraform.io/providers/unionai/unionai/latest/docs).
