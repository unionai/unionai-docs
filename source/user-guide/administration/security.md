# Security

```{admonition} Prelimminary draft
This document is a preliminary draft of the BYOK user manual.
Contents and procedures may change before the GA release.
```

For details of the architecture, please see:

![Architecture{clickable}](/_static/images/user-guide/administration/security/architecture.png)

## Control plane

The control plane:

- Runs within the Union AWS account.
- Provides the user interface through which users can access authentication, authorization, observation, and management functions.
- Is responsible for placing executions onto data plane clusters and performing other cluster control and management functions.

The control plane holds data responsible for coordinating and executing workflows, as well as location of where the user data resides.

```{admonition} Customer data only resides on data plane.
The control plane does not store the customer data or task code.
Customer data lives exclusively in their data plane.
```

Examples of metadata stored in the control plane:

- Names of workflows, tasks, launch plans, and artifacts
- Input and output types for workflows and tasks
- Execution status, start time, end time, and duration of workflows and tasks
- Version information for workflows, tasks, launch plans, and artifacts
- Artifact definitions

## Data plane

All your workflow and task executions are performed in the data plane, which runs within your public, private, or hybrid clouds. The data plane’s clusters are provisioned and managed by the control plane through a resident Union operator with minimal required permissions.

All execution data resides exclusively in the data plane. _It is not transferred to the Control Plane._

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

### Literal data

The input output literal data/metadata is stored in a bucket in the users account. Only references are stored in the Control Plane.

Examples:

- Primitive execution inputs (int, string… etc.)
- JSON-serializable dataclasses

Only in limited situations literal data pass through the Control Plane, i.e., when the user views the details of the workflows or results from Union's UI. _Customer data is not retained._

## Security Principles

Union goes to great lengths to protect our customer data. The best way to avoid exposing their data is to not hold their data in the first place. Union keeps the minimum amount of metadata possible to make the systems work. No more, no less.

## SSO, AuthN & AuthZ

Union integrates with the customer’s single sign-on provider to leverage their SSO policies and enforcing their security practices.

## Certifications

Union is SOC-2 Type 2 certified.

Our security auditor, Vanta, provides an online report of their continuous monitor of our systems. You can access it online in our:

<div style="margin-left: 3rem;">

[<i class="fa-solid fa-shield-halved"></i> Trust Center](https://trust.union.ai)

</div>

A copy of the audit report is available upon request.
