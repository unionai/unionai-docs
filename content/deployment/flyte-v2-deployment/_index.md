---
title: Flyte 2 deployment
variants: -flyte +union
weight: 14
llm_readable_bundle: true
---

# Flyte 2 deployment

{{< llm-bundle-note >}}

This section covers how to deploy **Flyte 2** to your own Kubernetes cluster using
the `flyte-binary` Helm chart.

Flyte 2 ships as a single unified binary (`flyte-binary-v2`) that bundles the runs
service, the task/actions controller, the data proxy, and the secret service, served
alongside the `flyteconsole-v2` web UI. You point it at three things you provision
yourself — a Kubernetes cluster, a PostgreSQL database, and an object store — and it
runs as one Deployment that you scale vertically.

Read these pages in order:

1. [Planning your deployment](./planning) — architecture, what changed from Flyte 1,
   and the external dependencies you need to provision.
2. [Installing Flyte 2](./installing) — a minimal `values.yaml`, the `helm install`
   command, object-storage access, ingress, and a worked AWS/EKS example.
3. [Authentication and SSO](./authentication) — securing the API and putting single
   sign-on in front of the console.
