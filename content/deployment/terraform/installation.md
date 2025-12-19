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

## Version

To choose the appropriate version of the provider (likely you should choose latest):

1. Visit the Provider Registry site and observe the latest version number
2. Use that version number in the provider declaration above

For detailed installation instructions, please refer to the [Terraform Registry documentation](https://registry.terraform.io/providers/unionai/unionai/latest/docs).
