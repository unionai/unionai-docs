---
title: Data plane setup on AWS
weight: 5
variants: -flyte -serverless -byoc +selfmanaged
sidebar_expanded: true
---

# Data plane setup on AWS

To set up your {{< key product_name >}} data plane on Amazon Web Services (AWS), you must allow {{< key product_name >}} to provision and maintain compute resources under your AWS account.

There are two approaches to setting up your data plane:

- **CDK setup**: Use the {{< key product_name >}} [EKS Blueprints addon](https://www.npmjs.com/package/@unionai/union-eks-blueprints-addon) with [AWS CDK](https://aws.amazon.com/cdk/) to automate the provisioning of your data plane infrastructure, including the EKS cluster, IAM roles, and Helm chart deployment.
- **Manual setup**: Use AWS CloudFormation or the AWS console to create the required IAM roles and permissions, then share the role ARN with the {{< key product_name >}} team.

{{< grid >}}

{{< link-card target="./cdk" icon="zap" title="CDK setup" >}}
Automate data plane provisioning with AWS CDK and EKS Blueprints
{{< /link-card >}}

{{< link-card target="./manual" icon="settings" title="Manual setup" >}}
Set up your data plane using CloudFormation or the AWS console
{{< /link-card >}}

{{< /grid >}}
