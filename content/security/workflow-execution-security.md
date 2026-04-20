---
title: Workflow execution security
weight: 9
variants: -flyte +byoc +selfmanaged
---

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
