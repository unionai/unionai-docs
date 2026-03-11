# Security

Union.ai provides a production-grade workflow orchestration platform built on Flyte, designed for AI/ML and data-intensive workloads.
Security is foundational to Union.ai’s architecture, not an afterthought.
This document provides a comprehensive overview of Union.ai’s security practices, architecture, and compliance posture for enterprise security professionals evaluating the platform.

Union.ai’s security model is built on several core principles:

* **Data residency:** Customer data is stored and computed only within the customer's compute plane. The Union.ai control plane stores only orchestration metadata—no task inputs, outputs, code, logs, secrets, or container images.
* **Architectural isolation:** A strict separation between the Union-hosted control plane and the customer-hosted compute plane ensures that the blast radius of any control plane compromise does not extend to customer data.
* **Outbound only connectivity:** The Cloudflare Tunnel connecting the control plane to the compute plane is outbound-only from the customer’s network, requiring no inbound firewall rules. All communication uses mutual TLS (mTLS) and is authenticated using the customer's Auth / SSO.
* **Compliance:** Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity, with practices aligned to ISO 27001 and GDPR standards. Union is certified HIPAA-compliant and maintains CIS 1.4 AWS and CIS 3.0 certifications. The Union.ai trust portal can be found at [https://trust.union.ai/](https://trust.union.ai)
* **Defense in depth:** Multiple layers of encryption, authentication, authorization, and network segmentation protect data throughout its lifecycle.
* **Human / operational isolation:** Your data is protected by least privileged access, comprehensive auditing, and detailed logging. Union AI personnel cannot view it without customer authorization.

> [!NOTE]
> In Union.ai’s BYOC architecture, all customer data—including task inputs/outputs, code bundles, container images, logs, secrets, and observability metrics—resides exclusively in the customer’s own cloud infrastructure.

# Company overview

Union.ai was founded to enable enterprises to build, deploy, and govern reliable AI/ML workflows at scale.
The platform is built on Flyte, a widely-adopted open-source workflow orchestration system originally developed at Lyft and now trusted by organizations including Spotify, LinkedIn, Freenome, and Lyft.

## Platform capabilities

* **Workflow orchestration:** Strongly-typed, reproducible workflows for ML training, data processing, and model deployment pipelines
* **Enterprise governance:** Role-based access control, audit trails, and compliance-ready deployment models
* **Kubernetes native:** Union AI's architecture integrates natively with Kubernetes, the industry-standard container orchestration system.
* **Multi-cloud support:** Deploy compute planes on AWS, GCP, or Azure with consistent security guarantees
* **Observability:** Built-in metrics, logging, and cost tracking for full pipeline visibility
* **Agentic workflows:** Support for complex, multistep automated workflows and applications with guardrails

## Deployment models

Union.ai offers multiple deployment models to meet varying enterprise requirements:

| Deployment Model | Control Plane | Compute Plane | Best For |
| --- | --- | --- | --- |
| BYOC (Bring Your Own Cloud) | Union.ai hosted & managed | Customer cloud account hosted, Union.ai managed | Managed operation for enterprises that require complete data sovereignty and a lower support overhead. |
| Self-Managed (Hybrid) | Union.ai hosted & managed | Customer cloud account hosted and managed | Organizations requiring full infrastructure control or those with specific compliance or unique infrastructure needs. |

# Security architecture

Union.ai’s security architecture is founded on the principle of strict separation between orchestration (control plane) and execution (compute plane).
This architectural decision ensures that customer data remains within the customer’s own cloud infrastructure at all times.

## Control plane / compute plane separation

The control plane and compute plane serve fundamentally different purposes and handle different types of data:

### Control plane (Union.ai hosted)

The control plane is responsible for workflow orchestration, user management, and providing the web interface.
It runs within Union.ai’s AWS account and stores only orchestration metadata in a managed PostgreSQL database.
This metadata includes task definitions (image references, resource requirements, typed interfaces), run and action metadata (identifiers, phase, timestamps, error information), user identity and RBAC records, cluster configuration and health records, and trigger/schedule definitions.
The control plane never stores customer data payloads.
It stores only references (URIs) to data in the customer’s object store, no data.
When data must be surfaced to a client, the control plane either proxies a signing request to generate a presigned URL or relays a data stream from the compute plane without persisting it.

**See comprehensive list of control plane roles and permissions in [Appendix C](#c-kubernetes-rbac---control-plane).**

### Compute plane (customer hosted)

The compute plane runs inside the customer’s own cloud account on their own Kubernetes cluster.
All customer data resides here, including:

| Data Type | Storage Technology | Access Pattern |
| --- | --- | --- |
| Task inputs/outputs | Object Store | Read/write by task pods via IAM roles |
| Code bundles (TGZ) | Object Store (fast-registration bucket) | Write via presigned URL; read by task pods and presigned URL by the browser |
| Container images | Container Registry | Built on-cluster; pulled by K8s |
| Task logs | Cloud Log Aggregator + live K8s API | Streamed via tunnel (never stored in CP) |
| Secrets | K8s Secrets, Vault, or Cloud Secrets Manager | Injected into pods at runtime |
| Observability metrics | Prometheus (in-cluster / customer managed) | Proxied queries via DataProxy |
| Reports (HTML) | Object Store (S3/GCS/Azure Blob) | Accessed by the browser via presigned URL |
| Cluster events | K8s API (ephemeral) | Live from K8s API |

**See comprehensive list of compute plane roles and permissions in [Appendix D](#d-kubernetes-rbac---compute-plane).**

## Network architecture

Network security is enforced through multiple layers:

### Cloudflare tunnel (outbound-only)

The compute plane connects to the control plane via a Cloudflare Tunnel—an outbound-only encrypted connection initiated from the customer’s cluster.
This architecture provides several critical security benefits:

* No inbound firewall rules are required on the customer’s network
* All traffic through the tunnel uses mutual TLS (mTLS) encryption
* The Tunnel Service performs periodic health checks and state reconciliation
* Connection is initiated outward to Cloudflare’s edge network, from the compute plane, which then connects to the control plane

### Control plane tunnel (outbound only)

The compute plane reaches out to the control plane to establish a bidirectional, encrypted and authenticated, outbound-only tunnel.
Union.ai operates regional control plane endpoints:

| Area | Region | Endpoint |
| --- | --- | --- |
| US | us-east-2 | hosted.unionai.cloud |
| US | us-west-2 | us-west-2.unionai.cloud |
| Europe | eu-west-1 | eu-west-1.unionai.cloud |
| Europe | eu-west-2 | eu-west-2.unionai.cloud |
| Europe | eu-central-1 | eu-central-1.unionai.cloud |

In locked-down environments, networking teams can limit egress access to published Cloudflare CIDR blocks, and further restrict to specific regions in coordination with the Union networking team.

### Communication paths

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Client → Control Plane | ConnectRPC (gRPC-Web) over HTTPS | TLS 1.2+ |
| Control Plane ↔ Compute Plane | Cloudflare Tunnel (outbound-initiated) | mTLS |
| Client → Object Store (presigned URL) | HTTPS | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit → Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods → Object Store | Cloud provider SDK | TLS (cloud-native) |

## Data flow architecture

Union.ai implements two primary data access patterns, both designed to keep customer data out of the control plane:

### Presigned URL pattern

For task inputs, outputs, code bundles, and reports, the control plane generates time-limited presigned URLs.
The client fetches data directly from the customer’s object store—the data never transits the control plane.
Presigned URLs are single-object scope, operation-specific (GET or PUT), time-limited (default 1 hour maximum), and transport-encrypted at every hop.

### Streaming relay pattern

For logs and observability metrics, the control plane acts as a stateless relay—streaming data from the compute plane through the Cloudflare tunnel to the client in real time.
The data passes through the control plane’s memory as a TLS encrypted stream with a termination point in the cloud.
It is never written to disk, cached, or stored.

![alt_text](images/image2.png "image_tooltip")

### Data in the UI:

* TODO: Need a table that clarifies how data shows up in UI

### Data in the API / CLI:

* TODO: Need a table that clarifies how data shows up

# Data protection

## Data classification

Union.ai maintains a rigorous data classification framework.
Every data type handled by the platform is classified by residency and access pattern:

| Data Type | Classification | Residency | Transits Control Plane? |
| --- | --- | --- | --- |
| Task inputs/outputs | Customer Data | Customer object store | Relayed in-memory (not stored) |
| Code bundles | Customer Data | Customer object store | No — direct via presigned URL |
| Container images | Customer Data | Customer registry | No — stays in customer infra |
| Reports (HTML) | Customer Data | Customer object store | No — direct via presigned URL |
| Task logs | Customer Data | Customer log aggregator | Relayed in-memory (not stored) |
| Secrets | Customer Data | Customer secrets backend | Relayed during create (not stored) |
| Observability metrics | Customer Data | Customer ClickHouse | Relayed in-memory (not stored) |
| Task definitions | Orchestration Metadata | Control plane DB | Yes — metadata only |
| Run/action metadata | Orchestration Metadata | Control plane DB | Yes |
| User identity/RBAC | Platform Metadata | Control plane DB | Yes |
| Cluster records | Platform Metadata | Control plane DB | Yes |

## Encryption at rest

All data at rest is encrypted using cloud-provider native encryption:

| Storage | Encryption Standard | Key Management |
| --- | --- | --- |
| Object Store (S3/GCS/Azure Blob) | Cloud-provider default (SSE-S3, Google-managed, Azure SSE) | Cloud provider managed; CMK supported |
| Container Registry | Cloud-provider encryption | Cloud provider managed |
| Secrets Backend (cloud) | Cloud-provider encryption | Cloud secrets manager |
| Secrets Backend (K8s) | `etcd` encryption | K8s cluster-level encryption |
| ClickHouse | Encrypted EBS/persistent disk | Cloud provider managed |
| Control Plane PostgreSQL | AWS RDS encryption | AES-256; AWS KMS managed |

## Encryption in transit

Union.ai enforces encryption for all data in transit.
No unencrypted communication paths exist in the platform architecture.
All client-to-control-plane communication uses TLS 1.2 or higher.
All control-plane-to-data-plane communication uses mutual TLS via Cloudflare Tunnel.
All client-to-object-store communication (via presigned URLs) uses HTTPS, enforced by cloud providers.
All internal compute plane communication uses cloud-native TLS.

## Data residency and sovereignty

Union.ai’s architecture provides strong data residency guarantees:

### Compute plane

* All customer data resides in the customer’s own cloud account and region
* Customers choose the region for their compute plane deployment

### Control plane

* Union.ai hosts your control plane in these supported regions: US West, US East, EU West-1 (London), EU West-2 (Ireland), EU Central, with more being added
* No customer data is replicated to or cached in Union.ai infrastructure. See [Data classification](#data-classification) for more detail on data classification and handling.

For organizations operating under GDPR or other data residency regulations, Union.ai’s EU-region compute planes ensure all customer data remains within the European Union.

# Identity and access management

## Authentication

Union.ai supports three authentication methods to accommodate different usage patterns:

| Method | Identity Type | Credentials | Use Case |
| --- | --- | --- | --- |
| OIDC (Okta) | Human user | Browser SSO | UI access, initial CLI login |
| API Keys | Human user (delegated) | Static bearer token | CI/CD scripts, simple automation |
| Service Accounts | Application identity | OAuth2 client_id + client_secret → short-lived token | Production pipelines, multi-service systems |

API keys are issued per user and inherit the user’s RBAC permissions.
They can be created and revoked via the UI or CLI.
Service accounts are provisioned through the Identity Service, creating OAuth2 applications with distinct, auditable identities independent of any human user.

## Authorization (RBAC)

Union.ai implements a policy-based Role-Based Access Control (RBAC) system with three built-in role types.

| Role | Capabilities | Typical Assignment |
| --- | --- | --- |
| Admin | Full access: manage users, clusters, secrets, projects, and all runs | Platform administrators, security team leads |
| Contributor | Create/abort runs, register tasks, manage secrets within assigned projects | ML engineers, data scientists, DevOps |
| Viewer | Read-only access to runs, actions, logs, reports | Stakeholders, auditors, read-only consumers |
| Custom Policies | Custom policies bind roles (built-in or custom) to resources scoped at org-wide, domain, or project+domain level using composable YAML bindings via `uctl` | Giving contributor access to a specific project's development and staging domains, but only viewer access in production |

RBAC policies are enforced at the service layer.
Every API request is authenticated and authorized against the user’s role assignments before any data access occurs.
Users have the ability to create custom policies to further refine access control.

## Organization isolation

Every record in the control plane database is scoped by organization (org).
The identity context, extracted from the authenticated token, gates all database queries.
The actions table uses org as part of its unique index, and the tasks table uses org as part of its primary key.
Cross-organization access is explicitly denied at the service layer, providing strong multi-tenant isolation.

## Least privilege principle

Union.ai enforces the principle of least privilege across all system components:

* IAM roles on the compute plane are scoped to minimum required permissions
* Two IAM roles per compute plane: admin role (for platform services) and user role (for task pods)
* IAM roles are bound to Kubernetes service accounts via cloud-native workload identity federation
* Presigned URLs grant single-object, operation-specific, time-limited access
* Service accounts receive only the permissions needed for their specific function

# Secrets management

Union.ai provides enterprise-grade secrets management with a security-first design that ensures secret values never leave the customer’s infrastructure during normal operations.

## Secrets architecture

The compute plane supports four configurable secrets backends:

| Backend | Storage Location | Default? |
| --- | --- | --- |
| Kubernetes Secrets | K8s `etcd` on the customer cluster | Yes (default for self-managed) |
| AWS Secrets Manager | AWS-managed service | Optional |
| GCP Secret Manager | GCP-managed service | Optional |
| Azure Key Vault | Azure-managed service | Optional |

In all cases, secrets are stored within the customer’s infrastructure.
The choice of backend is a deployment configuration on the compute plane operator.

## Secret lifecycle

### Creation

When a user creates a secret via the UI or CLI, the request is relayed through the Cloudflare tunnel to the compute plane’s secrets backend.
The secret value transits the control plane in-memory during this relay but is never written to disk or database on the control plane.

### Consumption

When a task pod is created, the Executor configures it to mount the requested secrets from the secrets backend (as environment variables or files).
The secret value is read by the compute plane’s secrets backend and injected into the pod—it never leaves the customer’s infrastructure during this process.

### Write-only API

> [!NOTE]
> Security by Design: There is no API to read back secret values. The GetSecret RPC returns only the secret’s metadata (name, scope, creation time, cluster presence status)—never the value itself. Secret values can only be consumed by task pods at runtime. This eliminates an entire class of secret exfiltration attacks.

## Secret scoping

Secrets can be scoped at multiple levels (organization, project, domain) to provide granular access control.
Only task pods running within the appropriate scope can access the corresponding secrets.

# Infrastructure security

## Kubernetes security

The compute plane runs on customer-managed Kubernetes clusters with the following security measures:

* Workload identity federation for pod-level IAM role binding (no static credentials)
* Kubernetes RBAC for service account permissions within the cluster
* Network policies for pod-to-pod communication isolation
* Resource quotas and limit ranges to prevent resource abuse
* Pod security contexts enforcing non-root execution where applicable

A complete list of compute plane permissions appears in **[Appendix D](#d-kubernetes-rbac---compute-plane)**

## Container security

Union.ai’s container security model ensures that code execution is isolated and controlled:

* Image Builder runs on the customer’s cluster using Buildkit, ensuring source code and built images never leave customer infrastructure
* Base images are pulled from customer-approved registries (public or private)
* Built images are pushed to the customer’s container registry (ECR/GCR/ACR)
* Task pods mount code bundles via presigned URLs with limited TTL
* Container images follow customer-defined tagging and scanning policies

## IAM and workload identity

Two IAM roles are provisioned per compute plane, each with narrowly scoped permissions:

| Role | Permissions | Assumed By | Mechanism |
| --- | --- | --- | --- |
| Admin Role (`adminflyterole`) | R/W to object store buckets, secrets manager access, persisted logs read | Platform services: Executor, Object Store Service, DataProxy | Workload identity federation |
| User Role (`userflyterole`) | R/W to object store buckets | Task pods (user workloads) | Workload identity via K8s service account annotation |

These roles use cloud-native workload identity federation (IAM Roles for Service Accounts on AWS, Workload Identity on GCP, Azure Workload Identity on Azure), eliminating the need for static credential storage.

## Control plane infrastructure

The Union.ai control plane is hosted on AWS with enterprise-grade infrastructure security:

* Managed PostgreSQL (AWS RDS) with AES-256 encryption at rest
* Network isolation via VPC with restricted security groups
* TLS termination at the edge for all incoming connections
* Automated backups and disaster recovery procedures
* Infrastructure-as-code deployment with version-controlled configurations
* Automated patch management and security updates

# Logging, monitoring, and audit

## Task logging

Logs are collected by Fluent Bit (deployed as a DaemonSet on the compute plane) and shipped to the customer’s cloud-native log service:

| Cloud Provider | Log Service | Integration |
| --- | --- | --- |
| AWS | CloudWatch Logs | Fluent Bit → CloudWatch |
| GCP | Cloud Logging (Stackdriver) | Fluent Bit → Cloud Logging |
| Azure | Azure Monitor / Log Analytics | Fluent Bit → Azure Monitor |

The compute plane log provider serves logs from two sources: live logs streamed directly from the Kubernetes API while a task is running, and persisted logs read from the cloud log aggregator after a pod terminates.
Log data is never stored in the control plane—it is streamed from the customer’s compute plane through the Cloudflare tunnel and relayed to the client as a stateless pass-through.

## Observability metrics

A per-cluster instance (Prometheus and/or ClickHouse) stores time-series observability metrics including resource utilization and cost data.
Queries are proxied through the DataProxy service to the customer’s instance.
Metrics data never leaves the customer’s infrastructure.

## Audit trail

Union.ai maintains comprehensive audit capabilities:

* Every API request is authenticated, and the identity context is captured
* Run and action lifecycle events are recorded with timestamps, phases, and responsible identities
* RBAC changes and user management operations are logged
* Secret creation and management operations are tracked (values are never logged)
* Cluster state changes and tunnel health events are recorded
* Error information is preserved per attempt, enabling forensic analysis of failures

## Incident response

Union.ai maintains documented incident response procedures aligned with SOC 2 Type II requirements.
These include defined escalation paths, communication protocols, containment procedures, and post-incident review processes.
The control plane’s stateless handling of customer data limits the potential impact of any control plane incident.

# Compliance and certifications

## Certifications overview

Union.ai maintains a rigorous certification program validated by independent third-party auditors.
Full details at the [Union.ai Trust Center](https://trust.union.ai/).

| Standard | Certification | Verifier | Status |
| --- | --- | --- | --- |
| SOC 2 Type II | Security, Availability, Integrity | Vanta / Sansiba San Filippo LLP | Certified |
| SOC 2 Type I | Security, Availability, Integrity | Vanta | Certified |
| HIPAA | Health data privacy and security | Vanta | Certified |
| CIS 1.4 AWS | Restricted access benchmark | AWS | Certified |
| CIS 3.0 | Security benchmark | In progress | In progress |

The SOC 2 Type II audit was conducted over a 12-week period and is available upon request.
Key areas covered include protection against unauthorized access (Security), system availability commitments and disaster recovery (Availability), and complete, valid, accurate, and timely processing (Processing Integrity).
Union.ai uses Vanta for continuous compliance monitoring and automated control assessments.

## Standards compliance

In addition to certifications, Union.ai complies with the following standard control frameworks through its private compute plane architecture:

| Framework | Control | Description |
| --- | --- | --- |
| ISO 27001 A.5.15 | Access control | Restricts access to network services and management interfaces; management endpoints not exposed to public Internet |
| ISO 27001 A.8.20 | Network security | Segregation and protection of networks; management interfaces on dedicated, private channels |
| ISO 27001 A.8.28 | Secure configuration | Minimizes public exposure of management plane by default |
| ISO 27001 A.8.21 | Cryptography | TLS encryption with minimized exposure of sensitive channels |
| ISO 27001 A.5.23 | Cloud service security | Cloud services configured securely with mitigated public exposure risks |
| CIS v8 4.4 | Administrative access | Administrative interfaces not exposed to Internet; VPN/bastion required |
| CIS v8 12.11 | Segment admin interfaces | Separation of administrative interfaces from public access |
| CIS v8 13.2 | Boundary protections | Management plane endpoints behind strong network segmentation |

## HIPAA compliance

Union.ai is HIPAA certified, enabling healthcare and life sciences organizations to process protected health information (PHI) within their BYOC compute planes.
Because all customer data—including any PHI—remains exclusively in the customer’s own cloud infrastructure, Union.ai’s architecture inherently supports HIPAA’s data protection requirements.
The control plane stores only orchestration metadata and never persists PHI.

## GDPR alignment

Union.ai’s architecture inherently supports GDPR through its data residency model.
For EU-region compute planes, all customer data remains within the European Union.
The control plane stores only orchestration metadata, and where error messages may contain user-generated content, this is documented and scoped.

## Trust Center

Union.ai maintains a public Trust Center at trust.union.ai (powered by Vanta), providing real-time transparency into the company’s security controls, compliance status, and security practices.
The Trust Center provides up-to-date information on certifications, downloadable resources (SOC 2 reports upon request), and over 70 verified security controls organized across five categories:

| Control Category | Controls | Key Controls Include |
| --- | --- | --- |
| Infrastructure Security | 17 controls | Encryption key access restricted, unique account authentication enforced, production application/database/OS/network access restricted, intrusion detection, log management, network segmentation, firewalls reviewed and utilized, network hardening standards |
| Organizational Security | 13 controls | Asset disposal procedures, production inventory, portable media encryption, anti-malware, code of conduct, confidentiality agreements, password policy, MDM, security awareness training |
| Product Security | 5 controls | Data encryption at rest, control self-assessments, penetration testing, data transmission encryption, vulnerability/system monitoring |
| Internal Security Procedures | 35 controls | BC/DR plans established and tested, cybersecurity insurance, change management, SDLC, incident response tested, risk assessments, vendor management, board oversight, whistleblower policy |
| Data and Privacy | 3 controls | Data retention procedures, customer data deleted upon leaving, data classification policy |

## Shared responsibility model

Union.ai operates under a shared responsibility model:

| Responsibility Area | Union.ai | Customer |
| --- | --- | --- |
| Control plane security | Full ownership | N/A |
| Compute plane infrastructure | Guidance and tooling | Provisioning and maintenance |
| Data encryption at rest | Default cloud encryption | Optional CMK configuration |
| Network security (tunnel) | Tunnel management | Firewall and VPC configuration |
| IAM roles and policies | Role templates and documentation | Role creation and binding |
| Secrets management | API and relay infrastructure | Backend selection and secret values |
| Application-level access control | RBAC framework | Role assignment and policy |
| Compliance documentation | SOC 2 report, Trust Center | Customer-specific attestations |

# Workflow execution security

This section traces the security controls applied at each stage of a workflow’s lifecycle, from registration through execution and result retrieval.

## Task registration

* SDK serializes the task specification (container image reference, resource requirements, typed interface) into a protobuf message
* Code bundle is uploaded directly to the customer’s object store via presigned PUT URL—the code never touches the control plane
* Only the specification metadata (including the object store URI) is stored in the control plane database

## Run creation and execution

* Input data is serialized and uploaded to the customer’s object store; only the input URI is stored in the control plane
* The control plane enqueues the action to the compute plane via the Cloudflare tunnel
* The Executor (a Kubernetes controller on the compute plane) creates a pod that reads inputs from the customer’s object store and writes outputs back to it
* Secrets are injected into pods from the customer’s secrets backend—they never traverse the control plane during runtime

## Result retrieval

* Outputs, reports, and code bundles are accessed via presigned URLs—the data flows directly from the customer’s object store to the client
* Logs are streamed from the compute plane through the Cloudflare tunnel as a stateless relay
* Metadata (run status, phase, errors) is served from the control plane database

## Data flow summary

> [!NOTE]
> At every stage of the workflow lifecycle, customer data (code, inputs, outputs, images, secrets) stays within the customer’s infrastructure or travels directly between the client and the customer’s object store. Logs are relayed through the tunnel but never stored. The control plane handles only orchestration metadata.

# Multi-cloud and region support

Union.ai supports compute plane deployments across multiple cloud providers and regions, ensuring that organizations can meet their specific infrastructure and regulatory requirements.

## Supported cloud providers

| Cloud Provider | Object Store | Secrets Backend | Log Aggregator | Container Registry |
| --- | --- | --- | --- | --- |
| AWS | S3 | K8s Secrets / AWS Secrets Manager | CloudWatch Logs | ECR |
| GCP | GCS | K8s Secrets / GCP Secret Manager | Cloud Logging | GCR / Artifact Registry |
| Azure | Azure Blob Storage | K8s Secrets / Azure Key Vault | Azure Monitor | ACR |

Union Implementation Services supports additional cloud providers and on-premises deployments through a case-by-case engagement.

## Supported regions

Union.ai currently operates control planes in the following regions, with additional regions being added: **US West, US East, EU West, and EU Central**.
Customers choose the region for their compute plane deployment, ensuring that all customer data remains within the selected geographic region.

## Consistent security across clouds

Regardless of the cloud provider selected, Union.ai enforces consistent security guarantees through its architecture: the same control plane/compute plane separation, the same presigned URL model, the same tunnel-based connectivity, the same RBAC framework, and the same encryption standards.
Cloud-specific implementations (IAM roles, encryption services, log aggregators) are abstracted by the platform while maintaining native integration with each provider’s security services.

# Organizational & physical security practices

Union.ai maintains organizational security controls to protect people, facilities, and endpoint devices.
These controls are independently verified through SOC 2 Type II audits and continuously monitored via the Vanta Trust Center (trust.union.ai).

## Employee security lifecycle

**Verified controls** (source: Trust Center, SOC 2 Type II audit)

| Control | Description | Verification |
| --- | --- | --- |
| Background checks | All employees with access to production systems undergo background checks prior to onboarding | SOC 2 Type II |
| Security awareness training | Required within 30 days of hire and annually thereafter for all employees | Trust Center (passing) |
| Confidentiality agreements | Signed by all employees and contractors during onboarding | Trust Center (passing) |
| Code of conduct | Acknowledged by all employees and contractors; violations subject to disciplinary action | Trust Center (passing) |
| Access provisioning | Documented procedures for granting, modifying, and revoking user access | Trust Center (passing) |
| Termination checklists | Access revoked for terminated employees via formal checklist process | Trust Center (passing) |
| Performance evaluations | Managers complete evaluations for direct reports at least annually | Trust Center (passing) |
| Least-privilege access | Internal systems follow least-privilege; regular access reviews conducted | SOC 2 Type II |

## Governance & organizational controls

| Control | Description | Verification |
| --- | --- | --- |
| Defined security roles | Formal roles and responsibilities for design, implementation, and monitoring of security controls | Trust Center (passing) |
| Organizational structure | Documented org chart with reporting relationships | Trust Center (passing) |
| Board-level oversight | Board or relevant subcommittee briefed by senior management on security and risk at least annually | Trust Center (passing) |
| Information security policies | Policies and procedures documented and reviewed at least annually | Trust Center (passing) |
| Whistleblower policy | Formalized policy with anonymous communication channel for reporting violations | Trust Center (passing) |
| Vendor management | Third-party vendors and sub-processors evaluated and monitored; sub-processor list available via Trust Center | SOC 2 Type II |
| Business continuity | BC/DR plans aligned with SOC 2 | SOC 2 Type II |

## Security development lifecycle

* **Secure coding:** Guidelines enforced through mandatory code review processes
* **Automated security testing:** Integrated into CI/CD pipelines
* **Dependency scanning:** Vulnerability scanning and management for all software dependencies
* **Infrastructure-as-code:** Version-controlled security configurations
* **Penetration testing:** Regular third-party security assessments
* **Incident response:** Documented procedures aligned with SOC 2 Type II, including defined escalation paths and post-incident review

> [!NOTE]
> All controls marked as “passing” are continuously monitored via Vanta and verified through the Union.ai Trust Center at trust.union.ai. The SOC 2 Type II audit report is available upon request.

# Compute plane components reference

This section provides a detailed reference for each security-relevant component running on the customer’s compute plane.
Understanding these components is essential for enterprise security teams conducting architecture reviews.

## Executor

The Executor is a Kubernetes controller that runs on the customer’s compute plane.
It is the core component responsible for translating orchestration instructions into actual workload execution.
The Executor watches for TaskAction custom resources created by the Queue Service, reconciles each TaskAction through its lifecycle (Queued, Initializing, Running, Succeeded/Failed), reports state transitions back to the control plane’s State Service via ConnectRPC through the Cloudflare tunnel, and creates and manages Kubernetes pods for task execution.

The Executor runs entirely within the customer’s cluster.
It accesses the customer’s object store and secrets using IAM roles bound to its Kubernetes service account via workload identity federation.
At no point does the Executor communicate directly with external services outside the customer’s cloud account (except through the Cloudflare tunnel to the control plane).

## Apps and serving

Apps and Serving enables customers to deploy long-running web applications — Streamlit dashboards, FastAPI services, notebooks, and inference endpoints — directly on the customer's compute plane.
Apps run as Knative Services within tenant-scoped Kubernetes namespaces, with the Union Operator managing the full lifecycle including autoscaling and scale-to-zero.
No application code, data, or serving traffic passes through the Union.ai control plane.
Inbound traffic routes through Cloudflare for DDoS protection to a Kourier gateway (Union's Envoy fork) running on the customer's cluster, which enforces authentication against the control plane before forwarding to the app container.
Browser access uses SSO; programmatic access requires a Union API key.
All endpoints require authentication by default, with optional per-app anonymous access.
Union's RBAC controls which users can deploy and access apps per project, and resource quotas constrain consumption.
The load balancer, serving infrastructure, and app containers all run within the customer's cluster, maintaining the same data residency guarantees as workflow execution.

## Object store service

The Object Store Service runs on the compute plane and provides the signing capabilities that enable the presigned URL security model.
Its key operations include CreateSignedURL (generates presigned URLs using the customer’s IAM credentials via the admin role), CreateUploadLocation (generates presigned PUT URLs for fast registration with Content-MD5 integrity verification), Presign (generic presigning for arbitrary object store keys), and Get/Put (direct object store read/write used internally by platform services).

Two object store buckets are provisioned per compute plane cluster: a metadata bucket for task inputs, outputs, reports, and intermediate data, and a fast-registration bucket for code bundles uploaded during task registration.
Object layout follows a hierarchical pattern: org/project/domain/run-name/action-name, providing natural namespace isolation.

## Log provider

The Log Provider runs on the compute plane and serves task logs from two sources.
For live tasks, logs are streamed directly from the Kubernetes API (pod stdout/stderr) in real time.
For completed tasks, logs are read from the cloud log aggregator (CloudWatch, Cloud Logging, or Azure Monitor) after pod termination.
Log lines include structured metadata: timestamp, message content, and originator classification (user vs. system).
This structured approach enables security teams to distinguish between application-generated logs and platform-generated logs for audit purposes.

## Image builder

When enabled, the Image Builder runs on the compute plane and uses Buildkit to construct container images without exposing source code or built artifacts outside the customer’s infrastructure.
The build process pulls the base image from a customer-approved registry (public or private), accesses user code via a presigned URL with a limited time-to-live, builds the container image with specified layers (pip packages, apt packages, custom commands, UV/Poetry projects), and pushes the built image to the customer’s container registry (ECR, GCR, or ACR).
Source code and built images never leave the customer’s infrastructure during the build process.

## Tunnel service

The Tunnel Service maintains the Cloudflare Tunnel connection between the compute plane and control plane.
It is responsible for initiating and maintaining the outbound-only encrypted connection, performing periodic health checks and heartbeats, and reconnecting automatically in case of network disruption.
The Cluster Service on the control plane performs periodic reconciliation to ensure tunnel health and DNS records are current.

# Vulnerability and risk management

## Vulnerability assessment

Union.ai maintains a comprehensive vulnerability management program that includes dependency analysis and automated alerts for known CVEs in software dependencies, container image scanning for both platform and customer-facing components, and periodic third-party penetration testing to identify potential attack vectors.

## Patch management

Union.ai follows a risk-based approach to patch management.
Critical vulnerabilities (CVSS 9.0+) are prioritized for immediate remediation, while high-severity vulnerabilities are addressed within defined SLA windows.
The control plane is updated independently of customer compute planes, ensuring that security patches can be applied rapidly without requiring customer-side changes.

## Threat modeling

Union.ai’s architecture has been designed with the following threat model considerations:

### Control plane compromise

In the event of a control plane compromise, an attacker would gain access to orchestration metadata only.
They would not obtain customer data payloads, secret values, code bundles, container images, or log content.
The attacker could not initiate connections to customer compute planes (outbound-only tunnel).
Presigned URLs are generated on the compute plane, so the attacker could not generate data access URLs.

### Tunnel interception

The Cloudflare Tunnel uses mTLS, making man-in-the-middle attacks infeasible.
Even if an attacker could intercept tunnel traffic, customer data flowing through the tunnel (logs, secret creation requests) is encrypted in transit and is not cached or stored at any intermediate point.

### Presigned URL leakage

If a presigned URL were leaked, the exposure is limited to a single object for a maximum of one hour (default configuration).
URLs grant only the specific operation requested (GET or PUT) and cannot be used to enumerate or access other objects.
Organizations can configure shorter expiration times to further reduce this risk window.

## Security architecture benefits

Union.ai’s architectural decisions provide inherent security benefits that reduce overall risk exposure:

| Architectural Decision | Security Benefit | Risk Mitigated |
| --- | --- | --- |
| Control plane stores no customer data | Minimizes blast radius of CP compromise | Data breach from CP attack |
| Outbound-only tunnel | No inbound attack surface on customer network | Network intrusion via open ports |
| Presigned URLs for data access | No persistent data access credentials | Credential theft / lateral movement |
| Write-only secrets API | Cannot exfiltrate secrets via API | Secret leakage via API abuse |
| Workload identity federation | No static credentials on compute plane | Static credential compromise |
| Per-org database scoping | Enforces tenant isolation at data layer | Cross-tenant data access |
| Cloud-native encryption | Leverages provider-managed encryption | Data at rest exposure |

# Security FAQ for enterprise evaluators

### Does Union.ai store any of my data?

No. Union.ai’s control plane stores only orchestration metadata (task definitions, run status, user records).
All customer data—including task inputs/outputs, code, logs, secrets, container images, and reports—resides exclusively in your own cloud infrastructure.

### Can Union.ai access my data?

Union.ai does not have persistent access to your data.
The control plane does not possess your cloud IAM credentials.
Data access is mediated through presigned URLs (generated on your compute plane using your IAM credentials) or through the Cloudflare tunnel as a stateless relay.

### What happens if the Union.ai control plane is compromised?

Because the control plane stores only orchestration metadata and never persists customer data, a control plane compromise would not expose your task inputs, outputs, code, secrets, or logs.
The attacker would gain access only to workflow metadata (task names, run status, scheduling configuration).

### Do I need to open inbound firewall rules?

No.
The Cloudflare Tunnel is outbound-only from your compute plane.
Your network requires no inbound firewall rules, reducing your attack surface.

### Can I use my own encryption keys?

Yes.
Because your data resides in your own cloud infrastructure, you can configure customer-managed keys (CMK) on your object stores, databases, and secrets managers according to your organization’s key management policies.

### Is there an API to read secret values?

No.
The Secrets API is write-only for values.
The GetSecret RPC returns only metadata (name, scope, creation time).
Secret values are consumable only by task pods at runtime, eliminating API-based secret exfiltration.

### How does Union.ai handle multi-tenancy?

Every database record is scoped by organization.
Cross-organization access is denied at the service layer.
Each customer’s compute plane is completely isolated in their own cloud account.
Within an organization, RBAC controls access at the project and role level.

### What compliance certifications does Union.ai hold?

Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity.
The audit was conducted by Sansiba San Filippo LLP.
The SOC 2 report is available upon request.
Union.ai’s architecture also supports GDPR compliance through EU-region compute plane deployment.

# Appendix

## A: Data residency summary

| Data | Stored In | Accessed Via | Transits Control Plane? |
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

## B: Presigned URL data types

| Data Type | Access Method | Direction |
| --- | --- | --- |
| Task inputs/outputs | Presign via ObjectStore service | Download (GET) |
| Code bundles (TGZ) | CreateDownloadLinkV2 | Download (GET) |
| Reports (HTML) | CreateDownloadLinkV2 | Download (GET) |
| Fast registration uploads | CreateUploadLocation | Upload (PUT) |

## C: Kubernetes RBAC - control plane

**All roles are ClusterRole**

| Role Name | Purpose | API Groups | Resources | Verbs |
| --- | --- | --- | --- | --- |
| [TODO] | Full control over K8s resources for workflow orchestration, namespace provisioning, RBAC setup for workspaces | ""(core) `flyte.lyft.com rbac.authorization.k8s.io` | `configmaps flyteworkflows namespaces pods resourcequotas roles rolebindings secrets services serviceaccounts spark-role limitranges` | *(all) |
| `scyllacluster-edit` | Aggregated admin/edit role for ScyllaDB cluster management (control plane database) | `scylla.scylladb.com` | `scyllaclusters scylladbmonitorings scylladbdatacenters scylladbclusters scylladbmanagerclusterregistrations scylladbmanagertasks` | `create patch update delete deletecollection` |
| `scylladb:controller:aggregate-to-operator` | ScyllaDB operator controller - manages ScyllaDB cluster lifecycle for the control plane database | ""(core) `apps policy scylla.scylladb.com networking.k8s.io batch` | `events nodes endpoints persistentvolumeclaims pods services configmaps secrets statefulsets deployments daemonsets jobs poddisruptionbudgets serviceaccounts scyllaclusters scyllaoperatorconfigs nodeconfigs ingresses` | `get list watch create update delete patch` |
| `scylla-operator:webhook` | ScyllaDB webhook server for admission control of ScyllaDB resources | `admissionregistration.k8s.io scylla.scylladb.com` | `validatingwebhookconfigurations mutatingwebhookconfigurations scyllaclusters nodeconfigs scyllaoperatorconfigs scylladbdatacenters scylladbclusters scylladbmanagertasks` | `get list watch create update patch delete` |
| `console-clusterrole` | Read-only access for Union Console UI to display namespaces, workflows, and pod logs | ""(core) `flyte.lyft.com` | `namespaces flyteworkflows pods pods/log` | `get list watch` |
| `authorizer-clusterrole` | Authorizer service reads namespaces for authorization decisions | ""(core) | `namespaces` | `get list watch` |
| `cluster-clusterrole` | Cluster management service monitors cluster state for health and capacity | ""(core) `apps` | `namespaces nodes replicasets deployments` | `get list watch` |
| `dataproxy-clusterrole` | DataProxy service reads secrets for presigned URL generation and data relay configuration | ""(core) | `secrets` | `get list watch` |
| `executions-clusterrole` | Executions service reads workflow state for execution management and status tracking | ""(core) `flyte.lyft.com` | `namespaces configmaps flyteworkflows` | `get list watch` |
| `queue-clusterrole` | Queue service reads namespaces for task queue routing | ""(core) | `namespaces` | `get list watch` |
| `run-scheduler-clusterrole` | Run Scheduler reads namespaces to determine scheduling scope for workflows | ""(core) | `namespaces` | `get list watch` |
| `usage-clusterrole` | Usage tracking service reads namespaces for resource usage aggregation | ""(core) | `namespaces` | `get list watch` |

## D: Kubernetes RBAC - compute plane

### Union core services (compute plane)

| Role Name | Purpose | Kind | API Groups | Scope | Resources | Verbs |
| --- | --- | --- | --- | --- | --- | --- |
| `clustersync-resource` | Synchronizes K8s resources across namespaces: creates per-workspace namespaces, RBAC bindings, service accounts, and resource quotas | ClusterRole | ""(core) `rbac.authorization.k8s.io` | Cluster-wide | `configmaps namespaces pods resourcequotas roles rolebindings secrets services serviceaccounts clusterrolebindings` | *(all) |
| `union-executor` | Node Executor: creates/manages task pods, handles FlyteWorkflow and TaskAction CRDs, manages all plugin resource types (Spark, Ray, etc.) | ClusterRole | ""(core) *(all) `apiextensions.k8s.io flyte.lyft.com` | Cluster-wide | `pods (RO) events *(all plugin objects) customresourcedefinitions flyteworkflows/* taskactions/*` | `get list watch create update delete patch` |
| `proxy-system` | Read-only monitoring: streams workflow events, pod logs, and resource utilization data back to control plane via tunnel | ClusterRole | "*" | Cluster-wide | `events flyteworkflows pods/log pods rayjobs resourcequotas` | `get list watch` |
| `operator-system` | Union Operator: manages FlyteWorkflow lifecycle, cluster-level configuration, health monitoring, node management | ClusterRole | `flyte.lyft.com` *(all) | Cluster-wide | `flyteworkflows flyteworkflows/finalizers resourcequotas pods configmaps podtemplates secrets namespaces nodes` | `get list watch create update delete patch post deletecollection` |
| `flytepropeller-role` | FlytePropeller workflow engine: creates task pods, manages FlyteWorkflow CRDs, handles all plugin resource types, enforces resource limits | ClusterRole | ""(core) *(all) `apiextensions.k8s.io flyte.lyft.com` | Cluster-wide | `pods (RO) events *(all plugin objects) customresourcedefinitions flyteworkflows/* limitranges` | `get list watch create update delete patch` |
| `flytepropeller-webhook-role` | Admission webhook: intercepts pod creation to inject secrets from the secrets backend into task containers | ClusterRole | "*" | Cluster-wide | `mutatingwebhookconfigurations secrets pods replicasets/finalizers` | `get create update patch` |
| `proxy-system-secret` | Manages proxy service secrets within the union namespace for tunnel authentication and configuration | Role | "*" | union namespace | `secrets` | `get list create update delete` |
| `operator-system` (ns) | Operator manages its own secrets and deployments within the union namespace | Role | "*" | union namespace | `secrets deployments` | `get list watch create update` |
| `union-operator-admission` | Webhook admission controller reads/creates TLS secrets for webhook serving certificates | Role | ""(core) | union namespace | `secrets` | `get create` |

### Observability and monitoring

| Role Name | Purpose | Kind | API Groups | Scope | Resources | Verbs |
| --- | --- | --- | --- | --- | --- | --- |
| `release-name-fluentbit` | Fluent Bit log collector: reads pod metadata to tag and route container logs to CloudWatch/Cloud Logging | ClusterRole | ""(core) | Cluster-wide | `namespaces pods` | `get list watch` |
| `opencost` | OpenCost: read-only access to all cluster resources for cost attribution and resource usage tracking | ClusterRole | ""(core) `extensions apps batch autoscaling storage.k8s.io` | Cluster-wide | `configmaps deployments nodes pods services resourcequotas replicationcontrollers limitranges PVCs PVs namespaces endpoints daemonsets replicasets statefulsets jobs storageclasses` | `get list watch` |
| `release-name-kube-state-metrics` | KSM: exports K8s object metrics for Prometheus monitoring dashboards | ClusterRole | ""(core) `extensions apps batch autoscaling policy networking.k8s.io certificates.k8s.io discovery.k8s.io storage.k8s.io admissionregistration.k8s.io` | Cluster-wide | `certificatesigningrequests configmaps cronjobs daemonsets deployments endpoints HPAs ingresses jobs leases limitranges namespaces networkpolicies nodes PVCs PVs pods replicasets replicationcontrollers resourcequotas secrets services statefulsets storageclasses validatingwebhookconfigurations volumeattachments endpointslices` | `list watch` |
| `release-name-grafana-clusterrole` | Grafana: reads `configmaps`/`secrets` for dashboard definitions and data source configuration | ClusterRole | ""(core) | Cluster-wide | `configmaps secrets` | `get watch list` |
| `union-operator-prometheus` | Prometheus: scrapes metrics from all cluster services and nodes for monitoring | ClusterRole | ""(core) `discovery.k8s.io networking.k8s.io` | Cluster-wide | `nodes nodes/metrics services endpoints pods endpointslices ingresses`; `nonResourceURLs`: `/metrics /metrics/cadvisor` | `get list watch` |
| `prometheus-operator` | Prometheus Operator: manages the full Prometheus monitoring stack lifecycle, CRDs, and configurations | ClusterRole | `monitoring.coreos.com apps extensions` (core) `networking.k8s.io policy admissionregistration.k8s.io storage.k8s.io` | Cluster-wide | `alertmanagers prometheuses thanosrulers servicemonitors podmonitors prometheusrules probes scrapeconfigs prometheusagents statefulsets daemonsets deployments configmaps secrets pods services endpoints namespaces ingresses PDBs webhookconfigs storageclasses` | *(all) |
| `release-name-dcgm-exporter` | DCGM Exporter: reads node/pod metadata for GPU metrics labeling (optional, for GPU workloads) | ClusterRole | ""(core) | Cluster-wide | `nodes pods` | `get list watch` |

## E: AWS IAM roles

| Plane | Service Account | Purpose | K8s Namespace | IAM Role ARN Pattern | Bound To | S3 Access |
| --- | --- | --- | --- | --- | --- | --- |
| Control Plane | `flyteadmin` | Orchestration metadata management, namespace provisioning, presigned URL generation for code upload/download | union | `arn:aws:iam::<account-id>:role/adminflyterole` | FlyteAdmin (workflow admin service) | Generates presigned URLs for customer S3 buckets (does not directly read/write data) |
| Compute Plane | `clustersync-system` | Synchronizes K8s namespaces, RBAC roles, service accounts, resource quotas, and config across the cluster | union | `adminflyterole` (compute plane admin) | ClusterResourceSync controller | No direct S3 access |
| Compute Plane | `executor` | Receives task assignments via tunnel, creates task pods, manages pod lifecycle, reports status back to control plane | union | `adminflyterole` (compute plane admin) | Node Executor (TaskAction controller) | R/W to metadata bucket and fast-registration bucket for staging task inputs/outputs |
| Compute Plane | `proxy-system` | Monitors events, Flyte workflows, pod logs; streams data back to control plane via tunnel | union | `adminflyterole` (compute plane admin) | Proxy Service | Read-only access to metadata bucket for proxying presigned URL requests |
| Compute Plane | `operator-system` | Cluster operations, health monitoring, config management, image builder orchestration, tunnel management | union | `adminflyterole` (compute plane admin) | Union Operator | R/W to metadata bucket for operator state and config |
| Compute Plane | `flytepropeller-system` | K8s operator managing FlyteWorkflow CRDs, pod creation, workflow lifecycle execution | union | `adminflyterole` (compute plane admin) | FlytePropeller (workflow engine) | R/W to metadata bucket for workflow data (inputs, outputs, offloaded data) |
| Compute Plane | `flytepropeller-webhook-system` | Mutating admission webhook that injects secrets into task pods at creation time | union | `adminflyterole` (compute plane admin) | FlytePropeller Webhook | No direct S3 access (handles secrets injection only) |
| Compute Plane | `clusterresource-template` (per-namespace) | Executes user workflow tasks; reads inputs, writes outputs to S3 | Per-workspace namespace | `userflyterole` (compute plane user) | Task Pods (user workloads) | R/W to metadata bucket for task inputs/outputs, code bundles, artifacts |

## F: Deployment concerns for Union-managed Bring Your Own Cloud (BYOC) deployments

### Private cluster management

Union strongly recommends against exposing Kubernetes clusters to the public Internet.
To manage customer EKS/GKE clusters without public endpoint exposure, Union leverages cloud-native private connectivity technologies:

| Cloud Provider | Technology | Purpose |
| --- | --- | --- |
| AWS | AWS PrivateLink | Private, secure connection to EKS management nodes without Internet exposure |
| GCP | GCP Private Service Connect | Private, secure connection to GKE management nodes without Internet exposure |
| Azure | Azure Private Link | Private, secure connection to AKS management nodes without Internet exposure |

This approach ensures that the Kubernetes management plane is never exposed to the public Internet, preventing unauthorized access, data breaches, and DDoS attacks while satisfying ISO 27001 A.5.15 (access control), CIS v8 4.4 (restrict administrative access), and CIS v8 12.11 (segment administration interfaces) requirements.

## Contact and resources

Trust Center: trust.union.ai

Website: union.ai

Documentation: docs.union.ai

SOC 2 Type II Report: Available upon request

Security Inquiries: Contact your Union.ai account representative or visit trust.union.ai
