---
title: Terraform
weight: 2
variants: -flyte -serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Managing Union with Terraform

Union provides a Terraform provider that enables infrastructure-as-code management of your Union deployment. With the Union Terraform provider, you can define, deploy, and manage Union resources using declarative configuration files.

## Overview

The Union Terraform provider allows you to manage Union resources programmatically, including:

- **Projects**: Create and manage Union projects
- **Access Control**: Configure users, roles, and policies
- **API Keys**: Generate and manage API keys for automation
- **OAuth Applications**: Set up OAuth applications for external integrations
- **Access Assignments**: Assign users and applications to resources

## Why use Terraform?

Using Terraform to manage Union provides several benefits:

- **Version Control**: Track changes to your Union configuration over time
- **Reproducibility**: Easily replicate configurations across environments
- **Automation**: Integrate Union management into your CI/CD pipelines
- **Consistency**: Ensure consistent configuration across your organization
- **Documentation**: Your Terraform files serve as living documentation

## Getting Started

To get started with the Union Terraform provider:

1. **Installation**: Set up the Terraform provider in your environment
2. **Management**: Learn about the available resources and data sources for managing Union

{{< grid >}}

{{< link-card target="./installation" icon="download" title="Installation" >}}
Install and configure the Union Terraform provider
{{< /link-card >}}

{{< link-card target="./management" icon="settings" title="Resource Management" >}}
Learn about available resources and data sources
{{< /link-card >}}

{{< link-card target="./security" icon="lock" title="Security Best Practices" >}}
Securely manage API keys and credentials
{{< /link-card >}}

{{< /grid >}}

## Requirements

- Terraform >= 1.0
- Union API key (generated using the [Flyte CLI](../../api-reference/flyte-cli#flyte-create-config))
- Access to a Union deployment
