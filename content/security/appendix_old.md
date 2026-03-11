---
title: Appendix
weight: 15
variants: -flyte +byoc +selfmanaged
---

# Appendix

## A. Data residency summary

| Data | Stored In | Accessed Via | Transits control plane? |
| --- | --- | --- | --- |
| Task definitions (spec metadata) | Control plane DB | ConnectRPC | Yes — metadata only |
| Run metadata (phase, timestamps) | Control plane DB | ConnectRPC | Yes |
| Action metadata (phase, attempts) | Control plane DB | ConnectRPC | Yes |
| Task inputs/outputs | Customer object store | Presigned URL | No — direct client ↔ object store |
| Code bundles | Customer object store | Presigned URL | No — direct client ↔ object store |
| Reports (HTML) | Customer object store | Presigned URL | No — direct client ↔ object store |
| Container images | Customer container registry | Pulled by K8s | No — stays in customer infra |
| Task logs | Customer log aggregator | Streamed via tunnel | Relayed in-memory (not stored) |
| Secrets | Customer secrets backend | Injected at runtime | Relayed during create (not stored) |
| Observability metrics | Customer ClickHouse | Proxied via DataProxy | Relayed in-memory (not stored) |
| User identity / RBAC | Control plane DB | ConnectRPC | Yes |
| Cluster state | Control plane DB | Internal | Yes |

## B. Presigned URL data types

| Data Type | Access Method | Direction |
| --- | --- | --- |
| Task inputs/outputs | Presign via ObjectStore service | Download (GET) |
| Code bundles (TGZ) | CreateDownloadLinkV2 | Download (GET) |
| Reports (HTML) | CreateDownloadLinkV2 | Download (GET) |
| Fast registration uploads | CreateUploadLocation | Upload (PUT) |

## C. Kubernetes RBAC - control plane

**All roles are `ClusterRole`**

| Role Name | Purpose | API Groups | Resources | Verbs |
| --- | --- | --- | --- | --- |
| `flyteadmin-clusterrole` | Full control over K8s resources for workflow orchestration, namespace provisioning, RBAC setup for workspaces | ""(core), flyte.lyft.com, rbac.authorization.k8s.io | configmaps, flyteworkflows, namespaces, pods, resourcequotas, roles, rolebindings, secrets, services, serviceaccounts, spark-role, limitranges | * (all) |
| `scyllacluster-edit` | Aggregated admin/edit role for ScyllaDB cluster management (control plane database) | scylla.scylladb.com | scyllaclusters, scylladbmonitorings, scylladbdatacenters, scylladbclusters, scylladbmanagerclusterregistrations, scylladbmanagertasks | create, patch, update, delete, deletecollection |
| `scylladb:controller:aggregate-to-operator` | ScyllaDB operator controller - manages ScyllaDB cluster lifecycle for the control plane database | ""(core), apps, policy, scylla.scylladb.com, networking.k8s.io, batch | events, nodes, endpoints, persistentvolumeclaims, pods, services, configmaps, secrets, statefulsets, deployments, daemonsets, jobs, poddisruptionbudgets, serviceaccounts, scyllaclusters, scyllaoperatorconfigs, nodeconfigs, ingresses | get, list, watch, create, update, delete, patch |
| `scylla-operator:webhook` | ScyllaDB webhook server for admission control of ScyllaDB resources | admissionregistration.k8s.io, scylla.scylladb.com | validatingwebhookconfigurations, mutatingwebhookconfigurations, scyllaclusters, nodeconfigs, scyllaoperatorconfigs, scylladbdatacenters, scylladbclusters, scylladbmanagertasks | get, list, watch, create, update, patch, delete |
| `console-clusterrole` | Read-only access for Union Console UI to display namespaces, workflows, and pod logs | ""(core), flyte.lyft.com | namespaces, flyteworkflows, pods, pods/log | get, list, watch |
| `authorizer-clusterrole` | Authorizer service reads namespaces for authorization decisions | ""(core) | namespaces | get, list, watch |
| `cluster-clusterrole` | Cluster management service monitors cluster state for health and capacity | ""(core), apps | namespaces, nodes, replicasets, deployments | get, list, watch |
| `dataproxy-clusterrole` | DataProxy service reads secrets for presigned URL generation and data relay configuration | ""(core) | secrets | get, list, watch |
| `executions-clusterrole` | Executions service reads workflow state for execution management and status tracking | ""(core), flyte.lyft.com | namespaces, configmaps, flyteworkflows | get, list, watch |
| `queue-clusterrole` | Queue service reads namespaces for task queue routing | ""(core) | namespaces | get, list, watch |
| `run-scheduler-clusterrole` | Run Scheduler reads namespaces to determine scheduling scope for workflows | ""(core) | namespaces | get, list, watch |
| `usage-clusterrole` | Usage tracking service reads namespaces for resource usage aggregation | ""(core) | namespaces | get, list, watch |

## D: Kubernetes RBAC - data plane

| Role Name | Purpose | Kind | API Groups | Scope | Resources | Verbs |
| --- | --- | --- | --- | --- | --- | --- |
| **Union Core Services (data plane)** | | | | | | |
| `clustersync-resource` | Synchronizes K8s resources across namespaces: creates per-workspace namespaces, RBAC bindings, service accounts, and resource quotas | ClusterRole | ""(core), rbac.authorization.k8s.io | Cluster-wide | configmaps, namespaces, pods, resourcequotas, roles, rolebindings, secrets, services, serviceaccounts, clusterrolebindings | * (all) |
| `union-executor` | Node Executor: creates/manages task pods, handles FlyteWorkflow and TaskAction CRDs, manages all plugin resource types (Spark, Ray, etc.) | ClusterRole | ""(core), *(all), apiextensions.k8s.io, flyte.lyft.com | Cluster-wide | pods (RO), events, *(all plugin objects), customresourcedefinitions, flyteworkflows/*, taskactions/* | get, list, watch, create, update, delete, patch |
| `proxy-system` | Read-only monitoring: streams workflow events, pod logs, and resource utilization data back to control plane via tunnel | ClusterRole | "*" | Cluster-wide | events, flyteworkflows, pods/log, pods, rayjobs, resourcequotas | get, list, watch |
| `operator-system` | Union Operator: manages FlyteWorkflow lifecycle, cluster-level configuration, health monitoring, node management | ClusterRole | flyte.lyft.com, *(all) | Cluster-wide | flyteworkflows, flyteworkflows/finalizers, resourcequotas, pods, configmaps, podtemplates, secrets, namespaces, nodes | get, list, watch, create, update, delete, patch, post, deletecollection |
| `flytepropeller-role` | FlytePropeller workflow engine: creates task pods, manages FlyteWorkflow CRDs, handles all plugin resource types, enforces resource limits | ClusterRole | ""(core), *(all), apiextensions.k8s.io, flyte.lyft.com | Cluster-wide | pods (RO), events, *(all plugin objects), customresourcedefinitions, flyteworkflows/*, limitranges | get, list, watch, create, update, delete, patch |
| `flytepropeller-webhook-role` | Admission webhook: intercepts pod creation to inject secrets from the secrets backend into task containers | ClusterRole | "*" | Cluster-wide | mutatingwebhookconfigurations, secrets, pods, replicasets/finalizers | get, create, update, patch |
| `proxy-system-secret` | Manages proxy service secrets within the union namespace for tunnel authentication and configuration | Role | "*" | union namespace | secrets | get, list, create, update, delete |
| `operator-system (ns)` | Operator manages its own secrets and deployments within the union namespace | Role | "*" | union namespace | secrets, deployments | get, list, watch, create, update |
| `union-operator-admission` | Webhook admission controller reads/creates TLS secrets for webhook serving certificates | Role | ""(core) | union namespace | secrets | get, create |
| **Observability and Monitoring** | | | | | | |
| `release-name-fluentbit` | FluentBit log collector: reads pod metadata to tag and route container logs to CloudWatch/Cloud Logging | ClusterRole | ""(core) | Cluster-wide | namespaces, pods | get, list, watch |
| `opencost` | OpenCost: read-only access to all cluster resources for cost attribution and resource usage tracking | ClusterRole | ""(core), extensions, apps, batch, autoscaling, storage.k8s.io | Cluster-wide | configmaps, deployments, nodes, pods, services, resourcequotas, replicationcontrollers, limitranges, PVCs, PVs, namespaces, endpoints, daemonsets, replicasets, statefulsets, jobs, storageclasses | get, list, watch |
| `release-name-kube-state-metrics` | KSM: exports K8s object metrics for Prometheus monitoring dashboards | ClusterRole | ""(core), extensions, apps, batch, autoscaling, policy, networking.k8s.io, certificates.k8s.io, discovery.k8s.io, storage.k8s.io, admissionregistration.k8s.io | Cluster-wide | All standard K8s resource types (certificatesigningrequests, configmaps, cronjobs, daemonsets, deployments, endpoints, HPAs, ingresses, jobs, leases, limitranges, namespaces, networkpolicies, nodes, PVCs, PVs, pods, replicasets, replicationcontrollers, resourcequotas, secrets, services, statefulsets, storageclasses, validatingwebhookconfigurations, volumeattachments, endpointslices) | list, watch |
| `release-name-grafana-clusterrole` | Grafana: reads configmaps/secrets for dashboard definitions and data source configuration | ClusterRole | ""(core) | Cluster-wide | configmaps, secrets | get, watch, list |
| `union-operator-prometheus` | Prometheus: scrapes metrics from all cluster services and nodes for monitoring | ClusterRole | ""(core), discovery.k8s.io, networking.k8s.io | Cluster-wide | nodes, nodes/metrics, services, endpoints, pods, endpointslices, ingresses; nonResourceURLs: /metrics, /metrics/cadvisor | get, list, watch |
| `prometheus-operator` | Prometheus Operator: manages the full Prometheus monitoring stack lifecycle, CRDs, and configurations | ClusterRole | monitoring.coreos.com, apps, extensions, (core), networking.k8s.io, policy, admissionregistration.k8s.io, storage.k8s.io | Cluster-wide | alertmanagers, prometheuses, thanosrulers, servicemonitors, podmonitors, prometheusrules, probes, scrapeconfigs, prometheusagents, statefulsets, daemonsets, deployments, configmaps, secrets, pods, services, endpoints, namespaces, ingresses, PDBs, webhookconfigs, storageclasses | * (all) |
| `release-name-dcgm-exporter` | DCGM Exporter: reads node/pod metadata for GPU metrics labeling (optional, for GPU workloads) | ClusterRole | ""(core) | Cluster-wide | nodes, pods | get, list, watch |

**E: AWS IAM Roles:**

| Plane | Service Account | Purpose | K8s Namespace | IAM Role ARN Pattern | Bound To | S3 Access |
| --- | --- | --- | --- | --- | --- | --- |
| **Control plane** | `flyteadmin` | Orchestration metadata management, namespace provisioning, presigned URL generation for code upload/download | `union` | `arn:aws:iam::<account-id>:role/adminflyterole` | FlyteAdmin (workflow admin service) | Generates presigned URLs for customer S3 buckets (does not directly read/write data) |
| **Data plane** | `clustersync-system` | Synchronizes K8s namespaces, RBAC roles, service accounts, resource quotas, and config across the cluster | `union` | `adminflyterole` (data plane admin) | ClusterResourceSync controller | No direct S3 access |
| **Data plane** | `executor` | Receives task assignments via tunnel, creates task pods, manages pod lifecycle, reports status back to control plane | `union` | `adminflyterole` (data plane admin) | Node Executor (TaskAction controller) | R/W to metadata bucket and fast-registration bucket for staging task inputs/outputs |
| **Data plane** | `proxy-system` | Monitors events, FlyteWorkflows, pod logs; streams data back to control plane via tunnel | `union` | `adminflyterole` (data plane admin) | Proxy Service | Read-only access to metadata bucket for proxying presigned URL requests |
| **Data plane** | `operator-system` | Cluster operations, health monitoring, config management, image builder orchestration, tunnel management | `union` | `adminflyterole` (data plane admin) | Union Operator | R/W to metadata bucket for operator state and config |
| **Data plane** | `flytepropeller-system` | K8s operator managing FlyteWorkflow CRDs, pod creation, workflow lifecycle execution | `union` | `adminflyterole` (data plane admin) | FlytePropeller (workflow engine) | R/W to metadata bucket for workflow data (inputs, outputs, offloaded data) |
| **Data plane** | `flytepropeller-webhook-system` | Mutating admission webhook that injects secrets into task pods at creation time | `union` | `adminflyterole` (data plane admin) | FlytePropeller Webhook | No direct S3 access (handles secrets injection only) |
| **Data plane** | `clusterresource-template` (per-namespace) | Executes user workflow tasks; reads inputs, writes outputs to S3 | Per-workspace namespace | `userflyterole` (data plane user) | Task Pods (user workloads) | R/W to metadata bucket for task inputs/outputs, code bundles, artifacts |

## F: Deployment concerns for Union-managed "bring your own cloud" (BYOC) deployments

### Private cluster management

Union strongly recommends against exposing Kubernetes clusters to the public Internet.
To manage customer EKS/GKE clusters without public endpoint exposure, Union leverages cloud-native private connectivity technologies:

| Cloud Provider | Technology | Purpose |
| --- | --- | --- |
| AWS | AWS PrivateLink | Private, secure connection to EKS management nodes without Internet exposure |
| GCP | GCP Private Service Connect | Private, secure connection to GKE management nodes without Internet exposure |
| Azure | Azure Private Link | Private, secure connection to AKS management nodes without Internet exposure |

This approach ensures that the Kubernetes management plane is never exposed to the public Internet, preventing unauthorized access, data breaches, and DDoS attacks while satisfying ISO 27001 A.5.15 (access control), CIS v8 4.4 (restrict administrative access), and CIS v8 12.11 (segment administration interfaces) requirements.

## G. AWS Union Admin IAM policy

For BYOC deployments where Union provisions your infrastructure, a `union-admin` IAM role is required so that Union can create and manage the necessary resources in your account.

These permissions enable Union to provide a fully managed, secure, and scalable platform for running data and ML workloads while maintaining proper isolation and security boundaries.

> [!NOTE]
> If you are configuring the network yourself, the permissions to create and manage the VPC, subnets, routes, and other network resources are not required.

### EKS (Elastic Kubernetes Service) management

Union manages all aspects of EKS clusters, including cluster operations, node group management, add-on management, and access control.

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

### EC2 (Compute and Networking) infrastructure

When Union manages your network fabric, it creates and manages VPCs, subnets, route tables, internet gateways, security groups, NAT gateways, elastic IPs, launch templates, and VPC endpoints.

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

### IAM (Identity and Access Management)

Union interacts with IAM to create restricted roles for user access, including role management, policy management, instance profiles, and OIDC providers.

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

### Auto scaling and launch management

Union deploys and manages cluster auto-scaling to maintain lean infrastructure and reduce costs.

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

### Storage and data services

Union manages storage for inputs, outputs, artifacts, caches, and logs.

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

### Monitoring and logging

Union provides comprehensive observability for workloads and infrastructure, including CloudWatch Logs and Metrics.

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

### Encryption and security

Union enforces encryption at rest and in transit, including KMS key management and EBS encryption.

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

### Event management and queuing

Union uses event-driven architecture for efficient resource management, including EventBridge rules and SQS queues for Karpenter auto-scaling.

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

### Caching and performance

Union may deploy caching layers (ElastiCache) for improved application performance.

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

### Global read permissions

Union needs visibility into existing resources and account limits for intelligent provisioning.

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

## H. AWS Private Link IAM policy

If Union manages your EKS infrastructure (required for BYOC, optional for Self-Managed or Air-gapped deployments), Union needs a mechanism to reach customer EKS management endpoints without Internet exposure.
On AWS, this is achieved using AWS Private Link.

### IAM role management

Union requires specific IAM roles for ECS task execution and management.

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

### Global service discovery and monitoring

Read-only permissions for service discovery, health monitoring, and operational visibility across multiple services.

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

Resource Scopes: `["*"]`

### VPC endpoint service management

Permissions to create and manage VPC endpoint services for establishing Private Link connections.

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

### Security group management

Permissions to create and manage security groups for Private Link network isolation.

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

### EKS cluster access

Permissions to interact with EKS clusters through the Kubernetes API and manage node groups.

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

### SSL certificate management

Union manages SSL certificates through ACM for secure HTTPS communication for Private Link endpoints.

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

### CloudWatch logs management

Union creates and manages CloudWatch log groups for monitoring Private Link proxy services and ECS container insights.

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

### Load balancer management

Union creates and manages Network Load Balancers (NLB) for Private Link connections.

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

### ECS container management

Union uses Amazon ECS to run proxy containers that facilitate Private Link communication.

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

## I. Required AWS VPC endpoints

Ensure your VPC includes these endpoints so the Union stack connects to the corresponding AWS services without leaving the AWS network.
Replace `<REGION>` with your AWS region (e.g., `us-east-2`).

| Endpoint | Purpose |
| --- | --- |
| `com.amazonaws.<REGION>.autoscaling` | Manage autoscaling groups in the VPC |
| `com.amazonaws.<REGION>.xray` | Collect and store X-Ray traces |
| `com.amazonaws.<REGION>.s3` | Store and retrieve data from S3 |
| `com.amazonaws.<REGION>.sts` | Assume IAM roles |
| `com.amazonaws.<REGION>.ecr.api` | Interact with the ECR API |
| `com.amazonaws.<REGION>.ssm` | Interact with Systems Manager |
| `com.amazonaws.<REGION>.ec2messages` | EC2 messages |
| `com.amazonaws.<REGION>.ec2` | Interact with EC2 |
| `com.amazonaws.<REGION>.ssmmessages` | SSM messages |
| `com.amazonaws.<REGION>.ecr.dkr` | Interact with ECR (Docker) |
| `com.amazonaws.<REGION>.logs` | Interact with CloudWatch Logs |
| `com.amazonaws.<REGION>.eks-auth` | EKS authentication |
| `com.amazonaws.<REGION>.eks` | Interact with EKS |
| `com.amazonaws.<REGION>.elasticloadbalancing` | Interact with Elastic Load Balancing |

## Contact

For security-related inquiries you can contact your Union.ai account representative, visit [trust.union.ai](https://trust.union.ai), or email `security@unionai.ai`.
