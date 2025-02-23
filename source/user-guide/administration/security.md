# Security

``` {admonition} Prelimminary draft
This document is a preliminary draft of the BYOK user manual.
Contents and procedures may change before the GA release.
```

# Introduction

Union BYOK (Bring Your Own Kubernetes) is a mode of deployment where the customer providesmanages the data plane while Union staff managed the Control Plane.

## BYOC vs. BYOK

The main difference between BYOC and BYOK is who manages the data plane.

In the BYOC case, in contrast, Union staff manages all aspects of the clusters for the customer.

# Architecture

Union’s modular architecture allows for great flexibility and control. The customer can decide how many clusters to have, their shape, and who has access to what. All communication is encrypted.

![Architecture](/_static/images/user-guide/administration/security/architecture.png)

## Control plane

The control plane:

- Runs within the Union AWS account.
- Provides the user interface through which users can access authentication, authorization, observation, and management functions.
- Is responsible for placing executions onto data plane clusters and performing other cluster control and management functions.

## Data plane

All your workflow and task executions are performed in the data plane, which runs within your public, private, or hybrid clouds. The data plane’s clusters are provisioned and managed by the control plane through a resident Union operator with minimal required permissions.

### Worker nodes

Worker nodes are responsible for executing your workloads. You have full control over the configuration of your worker nodes.

When worker nodes are not in use, they automatically scale down to the configured minimum. (we scale to zero.)

# Deployment

In the BYOK model, the customer deploys the data plane themselves. Union data plane runs on a standard Kubernetes cluster.

Union data plane is distributed as standard Helm Charts, with overridable values.

``` {admonition} Other distribution mechanisms
Although Helm Charts is a popular and well-established standard Kubernetes distribution mechanism,
our Engineering team is investigating other installation and distribution mechanisms, such as Terraform,
to more easily integrate with the customers’ deployment systems.
```

# Security

Union goes to great lengths to protect our customer data. The best way to avoid exposing their data is to not hold their data in the first place. Union keeps the minimum amount of metadata possible to make the systems work. No more, no less.

## SSO / Authentication / Authorization

Union integrates with the customer’s single sign-on provider to leverage their SSO policies and enforcing their security practices.

## Control plane data

The control plane holds data responsible for coordinating and executing workflows, as well as location of where the user data resides.

``` {admonition} Customer data only on data plane
The control plane does not store the customer data or task code.
Customer data lives exclusively in their data plane.
```

Examples of metadata stored in the control plane:

- Names of workflows, tasks, launch plans, and artifacts
- Input and output types for workflows and tasks
- Execution status, start time, end time, and duration of workflows and tasks
- Version information for workflows, tasks, launch plans, and artifacts
- Artifact definitions

### Literal data

These are passed by value, not by reference, and may be stored in the Union control plane.

Examples:

- Primitive execution inputs (int, string… etc.)
- JSON-serializable dataclasses

``` {admonition} Privacy concerns
If you are concerned with maintaining strict data privacy,
be sure not to pass private information in literal form between tasks.
```

## Data plane data

As discussed previously, the data plane is responsible for the execution of the workflows and tasks. All execution data resides exclusively in the data plane. *It is not transferred to the Control Plane.*

Examples of execution data:

- Event data
- Workflow inputs
- Workflow outputs
- Data passed between tasks (task inputs and outputs)

### Raw data

These are passed by reference between tasks and are always stored in an object store in your data plane. This type of data is read by (and may be temporarily cached) by the control plane as needed, but is never stored there.

Examples:

- Files and directories
- Dataframes
- Models
- Python-pickled types

## Certifications

Union is SOC-2 Type 2 certified.

Our security auditor, Vanta, provides an online report of their continuous monitor of our systems. You can access it online in the [Trust Center](https://trust.union.ai).

A copy of the audit report is available upon request.
