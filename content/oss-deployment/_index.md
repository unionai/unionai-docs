---
title: Platform deployment
variants: +flyte -union
weight: 5
top_menu: true
llm_readable_bundle: true
---

# Platform deployment

{{< llm-bundle-note >}}

This section covers how to deploy **Flyte** to your own Kubernetes cluster using the
`flyte-binary` Helm chart.

Flyte ships as a single unified binary that bundles the runs service, the
task/actions controller, the data proxy, and the app service, served alongside the
Flyte web console. You point it at three things you provision yourself — a Kubernetes
cluster, a PostgreSQL database, and an object store — and it runs as one Deployment
that you scale vertically.

Read these pages in order:

1. [Deployment overview](./overview) — architecture and the external
   dependencies you need to provision.
2. [Evaluation deployment with Kind](./kind-evaluation) — spin up the whole stack on
   a kind cluster (on your machine or a cloud VM) for evaluation, including an
   optional self-contained authentication setup with
   [Dex](./kind-evaluation/local-oidc) (or an
   [external OIDC provider](./kind-evaluation/external-oidc)).
3. [AWS deployment](./aws-deployment) — a minimal `values.yaml`, the `helm install`
   command, object-storage access, ingress, and a worked AWS/EKS example.
4. [Authentication and SSO](./authentication) — securing the API and putting single
   sign-on in front of the console.
5. [Enable app serving](./app-serving) — running long-running apps on Knative,
   including how to install the Knative Serving prerequisite.
