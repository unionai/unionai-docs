---
title: Roles & Policies
variants: -flyte -serverless +byoc +selfmanaged
weight: 1
---

# Roles & Policies

To operate Union, you need to have the following permissions in your AWS account. There are two sets of permissions that may be applicable depending on your deployment type:

| Deployment Type        | Union Admin        | Private Links      |
| ---------------------- | ------------------ | ------------------ |
| BYOC                   | {{< icon check >}} | {{< icon check >}} |
| Self-Managed           | {{< icon x >}}     | {{< icon x >}}     |
| Self-Managed + Support | {{< icon x >}}     | {{< icon check >}} |
| Airgapped              | {{< icon x >}}     | {{< icon x >}}     |
| Airgapped + Support    | {{< icon x >}}     | {{< icon check >}} |

## Permission Sets

### Union Admin

{{< download file="/_static/public/security/aws/UnionIAMPolicy.json" display=paragraph >}}

For the cases where Union is provisioning your infrastructure, we require a `union-admin` role so that we can create and manage the necessary resources in your account. This role is created automatically for you when you run the AWS Stack, avaiable as one-click deployment at [Data plane setup on AWS](../../deployment/data-plane-setup-on-aws/).

These permissions enable Union to provide a fully managed, secure, and scalable platform for running data and ML workloads while maintaining proper isolation and security boundaries.

This role will manage resources in your account, including:

- EKS (Elastic Kubernetes Service) Management
- EC2 (Compute & Networking) Infrastructure
- IAM (Identity & Access Management)
- Auto Scaling & Launch Management
- Storage & Data Services
- Monitoring & Logging
- Encryption & Security
- Event Management & Queuing
- Caching & Performance

For each of the above categories, we go in greater detail in the following sections.

> [!NOTE]
> If you are configuring the network yourself, the permissions to create and manage the VPC, subnets, routes, and other network resources are not required.

#### EKS (Elastic Kubernetes Service) Management

Union will manage all aspects of the EKS clusters, including:

- Cluster Operations : Create, delete, describe, update EKS clusters and their configurations
- Node Group Management : Create, update, delete, and manage EKS node groups
- Add-on Management : Install, update, and manage EKS add-ons like CNI, CoreDNS, and kube-proxy
- Access Control : Manage EKS access entries for RBAC integration
- Why needed : Union runs workloads on Kubernetes clusters and needs full control over EKS infrastructure

```json
[
  "eks:CreateNodegroup",
  "eks:DeleteCluster",
  "eks:DescribeCluster",
  "eks:DescribeNodegroup",
  "eks:DeleteNodegroup",
  "eks:CreateCluster",
  "eks:UpdateClusterVersion",
  "eks:UpdateClusterConfig",
  "eks:CreateAccessEntry",
  "eks:DescribeAccessEntry",
  "eks:UpdateAccessEntry",
  "eks:DeleteAccessEntry",
  "eks:UpdateNodegroupConfig",
  "eks:ListNodegroups",
  "eks:UpdateNodegroupVersion",
  "eks:TagResource",
  "eks:UntagResource",
  "eks:ListTagsForResource",
  "eks:DescribeUpdate",
  "eks:CreateAddon",
  "eks:UpdateAddon",
  "eks:DeleteAddon",
  "eks:DescribeAddonVersions",
  "eks:DescribeAddon",
  "eks:ListAddons"
]
```

Resource Scopes:

```json
[
  "arn:aws:eks:*:*:cluster/opta-*",
  "arn:aws:eks:*:*:cluster/union-*",
  "arn:aws:eks:*:*:nodegroup/opta-*",
  "arn:aws:eks:*:*:nodegroup/union-*",
  "arn:aws:eks:*:*:addon/opta-*",
  "arn:aws:eks:*:*:addon/union-*"
]
```

#### EC2 (Compute & Networking) Infrastructure

When Union manages your network fabric, it will create and manage the following resources:

- VPC Management : Create, modify, and delete VPCs, subnets, route tables, and internet gateways
- Security Groups : Manage firewall rules and network access controls
- NAT Gateways : Create and manage NAT gateways for private subnet internet access
- Elastic IPs : Allocate and manage static IP addresses
- Launch Templates : Create and manage EC2 launch configurations
- VPC Endpoints : Create private connections to AWS services

```json
[
  "ec2:AttachInternetGateway",
  "ec2:DetachInternetGateway",
  "ec2:CreateInternetGateway",
  "ec2:DeleteInternetGateway",
  "ec2:CreateRoute",
  "ec2:DeleteRoute",
  "ec2:CreateRouteTable",
  "ec2:DeleteRouteTable",
  "ec2:AssociateRouteTable",
  "ec2:DisassociateRouteTable",
  "ec2:RevokeSecurityGroupIngress",
  "ec2:AuthorizeSecurityGroupEgress",
  "ec2:AuthorizeSecurityGroupIngress",
  "ec2:CreateSecurityGroup",
  "ec2:RevokeSecurityGroupEgress",
  "ec2:DeleteSecurityGroup",
  "ec2:DeleteSubnet",
  "ec2:CreateNatGateway",
  "ec2:DeleteNatGateway",
  "ec2:CreateSubnet",
  "ec2:ModifySubnetAttribute",
  "ec2:DeleteFlowLogs",
  "ec2:CreateFlowLogs",
  "ec2:CreateVpc",
  "ec2:ModifyVpcAttribute",
  "ec2:DeleteVpc",
  "ec2:DescribeVpcAttribute",
  "ec2:AssociateVpcCidrBlock",
  "ec2:DisassociateVpcCidrBlock",
  "ec2:AllocateAddress",
  "ec2:AssociateAddress",
  "ec2:DisassociateAddress",
  "ec2:ReleaseAddress",
  "ec2:CreateVpcEndpoint",
  "ec2:ModifyVpcEndpoint",
  "ec2:DeleteVpcEndpoints",
  "ec2:RunInstances",
  "ec2:CreateLaunchTemplate",
  "ec2:CreateLaunchTemplateVersion",
  "ec2:DeleteLaunchTemplate",
  "ec2:DeleteLaunchTemplateVersions",
  "ec2:ModifyLaunchTemplate"
]
```

Resource Scopes:

```json
[
  "arn:aws:ec2:*:*:vpc/*",
  "arn:aws:ec2:*:*:subnet/*",
  "arn:aws:ec2:*:*:internet-gateway/*",
  "arn:aws:ec2:*:*:route-table/*",
  "arn:aws:ec2:*:*:security-group/*",
  "arn:aws:ec2:*:*:security-group-rule/*",
  "arn:aws:ec2:*:*:natgateway/*",
  "arn:aws:ec2:*:*:elastic-ip/*",
  "arn:aws:ec2:*:*:vpc-flow-log/*",
  "arn:aws:ec2:*:*:vpc-endpoint/*"
]
```

#### IAM (Identity & Access Management)

As part of the deployment and lockdown of the environment, Union will interact with IAM to create restricted roles to regulate user access:

- Role Management : Create, modify, and delete IAM roles for service accounts and workloads
- Policy Management : Create and manage custom IAM policies
- Instance Profiles : Manage EC2 instance profiles for workload authentication
- OIDC Providers : Manage OpenID Connect providers for Kubernetes service account integration

```json
[
  "iam:DeleteOpenIDConnectProvider",
  "iam:GetOpenIDConnectProvider",
  "iam:CreateOpenIDConnectProvider",
  "iam:TagOpenIDConnectProvider",
  "iam:UntagOpenIDConnectProvider",
  "iam:ListOpenIDConnectProviderTags",
  "iam:UpdateOpenIDConnectProviderThumbprint",
  "iam:CreatePolicy",
  "iam:CreatePolicyVersion",
  "iam:DeletePolicyVersion",
  "iam:GetPolicyVersion",
  "iam:GetPolicy",
  "iam:ListPolicyVersions",
  "iam:DeletePolicy",
  "iam:ListPolicyTags",
  "iam:TagPolicy",
  "iam:UntagPolicy",
  "iam:GetRole",
  "iam:TagRole",
  "iam:UntagRole",
  "iam:ListRoleTags",
  "iam:CreateRole",
  "iam:DeleteRole",
  "iam:AttachRolePolicy",
  "iam:PutRolePolicy",
  "iam:ListInstanceProfilesForRole",
  "iam:PassRole",
  "iam:CreateServiceLinkedRole",
  "iam:DetachRolePolicy",
  "iam:ListAttachedRolePolicies",
  "iam:DeleteRolePolicy",
  "iam:ListRolePolicies",
  "iam:GetRolePolicy",
  "iam:CreateInstanceProfile",
  "iam:AddRoleToInstanceProfile",
  "iam:RemoveRoleFromInstanceProfile",
  "iam:DeleteInstanceProfile",
  "iam:TagInstanceProfile",
  "iam:UntagInstanceProfile",
  "iam:ListInstanceProfileTags",
  "iam:GetInstanceProfile",
  "iam:UpdateAssumeRolePolicy"
]
```

Resource Scopes:

```json
[
  "arn:aws:iam::*:oidc-provider/*",
  "arn:aws:iam::*:policy/*",
  "arn:aws:iam::*:role/*",
  "arn:aws:iam::*:instance-profile/*"
]
```

#### Auto Scaling & Launch Management

Union will deploy and manage the cluster auto-scaling to help the customer maintaining a lean infrastructure and reduce costs.

- Auto Scaling Groups : Create and manage ASGs for dynamic node scaling
- Launch Configurations : Define instance launch parameters
- Instance Management : Run, tag, and manage EC2 instances

```json
[
  "autoscaling:CreateAutoScalingGroup",
  "autoscaling:DeleteAutoScalingGroup",
  "autoscaling:DescribeAutoScalingGroups",
  "autoscaling:UpdateAutoScalingGroup",
  "autoscaling:CreateLaunchConfiguration",
  "autoscaling:SetInstanceProtection",
  "autoscaling:DescribeScalingActivities",
  "autoscaling:CreateOrUpdateTags",
  "autoscaling:DescribeTags",
  "autoscaling:DeleteTags",
  "ec2:CreateTags",
  "ec2:DescribeTags",
  "ec2:DeleteTags",
  "ec2:DescribeImages",
  "ec2:DescribeLaunchTemplates",
  "ec2:DescribeLaunchTemplateVersions"
]
```

#### Storage & Data Services

Union will manage storage for components required to its operations, including but not limited to: inputs, outputs, artifacts, caches, and logs.

- S3 Buckets : Full access to Union and Opta-prefixed S3 buckets for data storage
- DynamoDB : Complete access to Opta-prefixed tables for state management
- ECR Repositories : Manage container image repositories under the Union namespace

```json
[
  "s3:*",
  "dynamodb:*",
  "ecr:CreateRepository",
  "ecr:DeleteRepository",
  "ecr:TagResource",
  "ecr:UntagResource",
  "ecr:PutLifecyclePolicy",
  "ecr:DeleteLifecyclePolicy",
  "ecr:PutImageTagMutability",
  "ecr:PutImageScanningConfiguration",
  "ecr:BatchDeleteImage",
  "ecr:DeleteRepositoryPolicy",
  "ecr:SetRepositoryPolicy",
  "ecr:GetRepositoryPolicy",
  "ecr:PutReplicationConfiguration",
  "ecr:DescribeRepositories",
  "ecr:ListTagsForResource",
  "ecr:GetLifecyclePolicy",
  "ecr:DescribeImages",
  "ecr:GetAuthorizationToken"
]
```

Resource Scopes:

```json
[
  "arn:aws:s3:::opta-*",
  "arn:aws:s3:::opta-*/*",
  "arn:aws:s3:::union-*",
  "arn:aws:s3:::union-*/*",
  "arn:aws:dynamodb:*:*:table/opta-*",
  "arn:aws:ecr:*:*:repository/union/*"
]
```

#### Monitoring & Logging

Union provides comprehensive observability for workloads and infrastructure, and helps the customer to monitor and troubleshoot the system.

- CloudWatch Logs : Create, manage, and access log groups for cluster and application logs
- Log Streams : Read log events for debugging and monitoring
- CloudWatch Metrics : Access metrics for monitoring and alerting

```json
[
  "logs:ListTagsLogGroup",
  "logs:TagLogGroup",
  "logs:UntagLogGroup",
  "logs:DescribeLogGroups",
  "logs:DeleteLogGroup",
  "logs:CreateLogGroup",
  "logs:PutRetentionPolicy",
  "logs:DescribeLogStreams",
  "logs:GetLogEvents",
  "logs:FilterLogEvents",
  "cloudwatch:GetMetricStatistics"
]
```

Resource Scopes:

```json
[
  "arn:aws:logs:*:*:log-group:opta-*",
  "arn:aws:logs:*:*:log-group::log-stream*",
  "arn:aws:logs:*:*:log-group:/aws/eks/opta-*:*",
  "arn:aws:logs:*:*:log-group:/aws/eks/opta-*:log-stream:kube-*",
  "arn:aws:logs:*:*:log-group:/union/cluster-*/dataplane:log-stream:*",
  "arn:aws:logs:*:*:log-group:/union/cluster-*/host:log-stream:*",
  "arn:aws:logs:*:*:log-group:/union/cluster-*/task:log-stream:*",
  "arn:aws:logs:*:*:log-group:/aws/containerinsights/opta-*/application:log-stream:fluentbit-kube.var.log.containers.union-operator-*",
  "arn:aws:logs:*:*:log-group:/aws/containerinsights/opta-*/application:log-stream:fluentbit-kube.var.log.containers.flytepropeller-*"
]
```

#### Encryption & Security

Union enforces encryption at rest and in transit for security compliance.

- KMS Keys : Create, manage, and use encryption keys for data protection
- Key Policies : Manage access to encryption keys
- EBS Encryption : Configure default encryption for storage volumes

```json
[
  "kms:CreateAlias",
  "kms:DeleteAlias",
  "kms:EnableKeyRotation",
  "kms:PutKeyPolicy",
  "kms:GetKeyPolicy",
  "kms:ListResourceTags",
  "kms:TagResource",
  "kms:UntagResource",
  "kms:GetKeyRotationStatus",
  "kms:ScheduleKeyDeletion",
  "kms:DescribeKey",
  "kms:CreateGrant",
  "kms:CreateKey",
  "kms:ListAliases",
  "ec2:EnableEbsEncryptionByDefault",
  "ec2:GetEbsEncryptionByDefault",
  "ec2:ResetEbsDefaultKmsKeyId",
  "ec2:GetEbsDefaultKmsKeyId",
  "ec2:ModifyEbsDefaultKmsKeyId",
  "ec2:DisableEbsEncryptionByDefault"
]
```

Resource Scopes:

```json
["arn:aws:kms:*:*:alias/*", "arn:aws:kms:*:*:key/*"]
```

#### Event Management & Queuing

Union uses event-driven architecture for efficient resource management.

- EventBridge Rules : Manage event rules for Karpenter auto-scaling
- SQS Queues : Create and manage queues for Karpenter node provisioning

```json
[
  "sqs:CreateQueue",
  "sqs:DeleteQueue",
  "sqs:SetQueueAttributes",
  "sqs:TagQueue",
  "sqs:UntagQueue",
  "sqs:GetQueueAttributes",
  "sqs:ListQueueTags",
  "events:DescribeRule",
  "events:DeleteRule",
  "events:ListTargetsByRule",
  "events:ListTagsForResource",
  "events:PutRule",
  "events:PutTargets",
  "events:RemoveTargets",
  "events:TagResource",
  "events:UntagResource"
]
```

Resource Scopes:

```json
["arn:aws:sqs:*:*:Karpenter*", "arn:aws:events:*:*:rule/Karpenter*"]
```

#### Caching & Performance

- ElastiCache : Manage cache subnet groups for Redis/Memcached clusters
- Why needed : Union may deploy caching layers for improved application performance

```json
[
  "elasticache:CreateCacheSubnetGroup",
  "elasticache:AddTagsToResource",
  "elasticache:RemoveTagsFromResource",
  "elasticache:ListTagsForResource",
  "elasticache:DescribeCacheSubnetGroups",
  "elasticache:DeleteCacheSubnetGroup"
]
```

Resource Scopes:

```json
["arn:aws:elasticache:*:*:subnetgroup:opta-*"]
```

#### Global Read Permissions

Union needs visibility into existing resources and account limits for intelligent provisioning.

- Describe Operations : Read-only access to describe AWS resources across services
- Service Quotas : Check service limits to prevent provisioning failures

```json
[
  "ec2:DescribeAddresses",
  "ec2:DescribeFlowLogs",
  "ec2:DescribeInternetGateways",
  "ec2:DescribeNetworkInterfaces",
  "ec2:DescribeAvailabilityZones",
  "ec2:DescribeAccountAttributes",
  "ec2:DescribeNetworkAcls",
  "ec2:DescribeRouteTables",
  "ec2:DescribeVpcClassicLinkDnsSupport",
  "ec2:DescribeNatGateways",
  "ec2:DescribeSecurityGroups",
  "ec2:DescribeVpcClassicLink",
  "ec2:DescribeVpcs",
  "ec2:DescribeSubnets",
  "ec2:DescribeSecurityGroupRules",
  "ec2:DescribeAddressesAttribute",
  "ec2:DescribeInstanceTypeOfferings",
  "ec2:DescribeInstanceTypes",
  "ec2:DescribeVpcEndpoints",
  "ec2:DescribePrefixLists",
  "sts:GetCallerIdentity",
  "iam:ListRoles",
  "iam:ListPolicies",
  "servicequotas:GetServiceQuota"
]
```

#### FAQ

##### Q: Why some permissions have `*` instead of a more restricted scope?

Some permissions have star instead of a more restricted scope because either AWS does not provides means to restrict them or they are required to perform actions across multiple services or resources.

For example, a VPC object resource ID is a randomly generated identifier chosen at creation time, e.g., `vpc-01654a5601c67647f`. Due to the random nature of the resource unique identifier, one cannot create a policy like `arn:aws:ec2:*:*:vpc/???????`, because one cannot predict what goes in the `???????`.

In contrast, some APIs like EKS allows an identifier chosen by the customer, and therefore we can do `arn:aws:eks:*:*:cluster/union-*`, restricting to just Union clusters.

---

### Private Link

{{< download file="/_static/public/security/aws/UnionPrivateLinkPolicy.json" display=paragraph >}}

If you want Union to manage your EKS infrastructure (required for BYOC and optional for Self-Managed or Airgapped deployments), Union needs a mechanism to reach the customer EKS management endpoints without exposing it to the Internet.

On AWS, we achieve this goal using AWS Private Link (reference documentation at [AWS Private Link][aws-private-link].)

To set it up, Union will require access to the following AWS services:

- Private Link
- VPC Endpoint Services
- ELB (Elastic Load Balancing)
- ECS (Elastic Container Service)
- EKS (Elastic Kubernetes Service)

#### IAM Role Management

Union requires specific IAM roles for ECS task execution and management. These roles are essential for running containerized workloads and managing the execution environment securely.

**Permission Actions:**

```json
["iam:GetRole", "iam:PassRole"]
```

Resource Scopes:

```json
[
  "arn:aws:iam::*:role/unionai-access-*-ecs-execution-role",
  "arn:aws:iam::*:role/unionai-access-*-ecs-task-role"
]
```

#### Global Service Discovery and Monitoring

These permissions enable Union to discover, monitor, and manage AWS resources across multiple services. They provide read-only access for service discovery, health monitoring, and operational visibility.

**Permission Actions:**

```json
[
  "application-autoscaling:DescribeScalableTargets",
  "application-autoscaling:DescribeScalingActivities",
  "application-autoscaling:DescribeScalingPolicies",
  "cloudwatch:GetMetricData",
  "cloudwatch:GetMetricStatistics",
  "cloudwatch:ListMetrics",
  "ec2:DescribeNetworkInterfaces",
  "ec2:DescribeSecurityGroups",
  "ec2:DescribeSubnets",
  "ec2:DescribeVpcAttribute",
  "ec2:DescribeVpcEndpoints",
  "ec2:DescribeVpcEndpointConnections",
  "ec2:DescribeVpcEndpointServiceConfigurations",
  "ec2:DescribeVpcs",
  "ec2:DescribeInstances",
  "ec2:DescribeInstanceStatus",
  "ec2:GetConsoleOutput",
  "ecs:DeregisterTaskDefinition",
  "ecs:DescribeContainerInstances",
  "ecs:DescribeServiceDeployments",
  "ecs:DescribeServices",
  "ecs:DescribeTaskDefinition",
  "ecs:DescribeTasks",
  "ecs:GetTaskProtection",
  "ecs:ListClusters",
  "ecs:ListServices",
  "ecs:ListTaskDefinitionFamilies",
  "ecs:ListTaskDefinitions",
  "ecs:ListTasks",
  "eks:DescribeClusterVersions",
  "elasticloadbalancing:DescribeListeners",
  "elasticloadbalancing:DescribeLoadBalancerAttributes",
  "elasticloadbalancing:DescribeLoadBalancers",
  "elasticloadbalancing:DescribeTags",
  "elasticloadbalancing:DescribeTargetGroupAttributes",
  "elasticloadbalancing:DescribeTargetGroups",
  "elasticloadbalancing:DescribeTargetHealth",
  "logs:DescribeLogGroups",
  "servicediscovery:ListNamespaces",
  "iam:SimulatePrincipalPolicy",
  "ssm:StartSession"
]
```

Resource Scopes:

```json
["*"]
```

#### VPC Endpoint Service Management

These permissions allow Union to create and manage VPC endpoint services, which are essential for establishing Private Link connections. This enables secure, private communication between Union's infrastructure and your AWS resources.

**Permission Actions:**

```json
[
  "ec2:AcceptVpcEndpointConnections",
  "ec2:CreateTags",
  "ec2:CreateVpcEndpointServiceConfiguration",
  "ec2:DeleteVpcEndpointServiceConfigurations",
  "ec2:DescribeVpcEndpointServicePermissions",
  "ec2:ModifyVpcEndpointServiceConfiguration",
  "ec2:ModifyVpcEndpointServicePermissions",
  "ec2:RejectVpcEndpointConnections",
  "ec2:StartVpcEndpointServicePrivateDnsVerification",
  "vpce:AllowMultiRegion"
]
```

Resource Scopes:

```json
["arn:aws:ec2:*:*:vpc-endpoint-service/*"]
```

#### Security Group Management

Union needs to create and manage security groups to control network access for Private Link connections. These permissions ensure proper network isolation and security for the communication channels.

**Permission Actions:**

```json
[
  "ec2:AuthorizeSecurityGroupEgress",
  "ec2:AuthorizeSecurityGroupIngress",
  "ec2:CreateSecurityGroup",
  "ec2:CreateTags",
  "ec2:DeleteSecurityGroup",
  "ec2:RevokeSecurityGroupEgress"
]
```

Resource Scopes:

```json
["arn:aws:ec2:*:*:security-group/*", "arn:aws:ec2:*:*:vpc/*"]
```

#### EKS Cluster Access

These permissions enable Union to interact with your EKS clusters through the Kubernetes API and manage node groups as needed for workload execution.

**Permission Actions:**

```json
[
  "eks:AccessKubernetesApi",
  "eks:DeleteNodegroup",
  "eks:DescribeCluster",
  "eks:DescribeNodegroup"
]
```

Resource Scopes:

```json
["arn:aws:eks:*:*:cluster/*"]
```

#### SSL Certificate Management

Union manages SSL certificates through AWS Certificate Manager (ACM) to ensure secure HTTPS communication for Private Link endpoints.

**Permission Actions:**

```json
[
  "acm:AddTagsToCertificate",
  "acm:DeleteCertificate",
  "acm:DescribeCertificate",
  "acm:ListTagsForCertificate",
  "acm:RequestCertificate"
]
```

Resource Scopes:

```json
["arn:aws:acm:*:*:certificate/*"]
```

#### CloudWatch Logs Management

Union creates and manages CloudWatch log groups for monitoring and debugging Private Link proxy services and ECS container insights.

**Permission Actions:**

```json
[
  "logs:CreateLogGroup",
  "logs:DeleteLogGroup",
  "logs:DescribeLogGroups",
  "logs:FilterLogEvents",
  "logs:GetLogEvents",
  "logs:ListTagsForResource",
  "logs:PutRetentionPolicy",
  "logs:TagResource",
  "logs:UntagResource",
  "logs:DescribeLogStreams",
  "logs:GetQueryResults",
  "logs:StartQuery",
  "logs:StopQuery"
]
```

Resource Scopes:

```json
[
  "arn:aws:logs:*:*:log-group:/ecs/unionai/proxy-*",
  "arn:aws:logs:*:*:log-group::log-stream",
  "arn:aws:logs:*:*:log-group:/aws/ecs/containerinsights/unionai-access-*/*"
]
```

#### Load Balancer Management

Union creates and manages Network Load Balancers (NLB) to provide highly available and scalable entry points for Private Link connections.

**Permission Actions:**

```json
[
  "elasticloadbalancing:AddTags",
  "elasticloadbalancing:CreateListener",
  "elasticloadbalancing:CreateLoadBalancer",
  "elasticloadbalancing:CreateTargetGroup",
  "elasticloadbalancing:DescribeListeners",
  "elasticloadbalancing:DescribeLoadBalancerAttributes",
  "elasticloadbalancing:DescribeLoadBalancers",
  "elasticloadbalancing:DescribeTargetGroups",
  "elasticloadbalancing:DescribeTargetGroupAttributes",
  "elasticloadbalancing:DescribeTags",
  "elasticloadbalancing:DeleteListener",
  "elasticloadbalancing:DeleteLoadBalancer",
  "elasticloadbalancing:DeleteTargetGroup",
  "elasticloadbalancing:ModifyLoadBalancerAttributes",
  "elasticloadbalancing:ModifyTargetGroup",
  "elasticloadbalancing:ModifyTargetGroupAttributes"
]
```

Resource Scopes:

```json
[
  "arn:aws:elasticloadbalancing:*:*:loadbalancer/net/unionai-access-*/*",
  "arn:aws:elasticloadbalancing:*:*:targetgroup/unionai-access-*/*",
  "arn:aws:elasticloadbalancing:*:*:listener/net/unionai-access-*/*"
]
```

#### ECS Container Management

Union uses Amazon ECS to run proxy containers that facilitate Private Link communication. These permissions enable full lifecycle management of ECS clusters, services, and tasks.

**Permission Actions:**

```json
[
  "ecs:CreateCluster",
  "ecs:CreateService",
  "ecs:DeleteCluster",
  "ecs:DeleteService",
  "ecs:DescribeClusters",
  "ecs:DescribeContainerInstances",
  "ecs:DescribeServices",
  "ecs:DescribeServiceDeployments",
  "ecs:DescribeServiceRevisions",
  "ecs:DescribeTaskDefinition",
  "ecs:ExecuteCommand",
  "ecs:ListClusters",
  "ecs:ListTagsForResource",
  "ecs:ListTaskDefinitions",
  "ecs:ListServices",
  "ecs:RegisterTaskDefinition",
  "ecs:TagResource",
  "ecs:UntagResource",
  "ecs:UpdateService",
  "ecs:StartTask",
  "ecs:StopTask"
]
```

Resource Scopes:

```json
[
  "arn:aws:ecs:*:*:cluster/unionai-access-*",
  "arn:aws:ecs:*:*:service/unionai-access-*/*",
  "arn:aws:ecs:*:*:task/unionai-access-*/*",
  "arn:aws:ecs:*:*:task-definition/unionai-access-*:*"
]
```

[aws-private-link]: https://aws.amazon.com/privatelink/
