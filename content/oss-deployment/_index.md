---
title: Platform deployment
description: Deploy Flyte to your own Kubernetes cluster with the flyte-binary Helm chart.
icon: server
variants: +flyte -union
weight: 5
top_menu: true
---

# Platform deployment

This section covers how to deploy **Flyte** to your own Kubernetes cluster using the
`flyte-binary` Helm chart.

Flyte ships as a single unified binary that bundles the runs service, the
task/actions controller, the data proxy, and the app service, served alongside the
Flyte web console. You point it at three things you provision yourself (a Kubernetes
cluster, a PostgreSQL database, and an object store) and it runs as one Deployment
that you scale vertically.

> [!INFO] Try Flyte Devbox in your browser
>
> You can deploy Flyte Devbox, a light-weight Flyte cluster, locally using the [Flyte Devbox](../user-guide/get-started/run-modes/running-devbox).
>
> If you want to try it without installing anything on your local machine or cloud environment, create a Flyte Devbox in Github Codespaces.
>
> [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/flyteorg/flyte-devbox-codespace?quickstart=1)

Walk through these pages in order:

1. [Deployment overview](./overview): architecture and the external
   dependencies you need to provision.
2. [Kind deployment](./kind-deployment/_index): spin up the whole stack on a kind cluster
   (on your machine or a DigitalOcean cloud VM) for evaluation,
   including an optional self-contained authentication setup with
   [Dex](./kind-deployment/local-oidc) (or an
   [external OIDC provider](./kind-deployment/external-oidc)).
3. [AWS deployment](./aws-deployment): a minimal `values.yaml`, the `helm install`
   command, object-storage access, ingress, and a worked AWS/EKS example.
4. [Authentication and SSO](./authentication): securing the API and putting single
   sign-on in front of the console.
5. [Enable app serving](./app-serving): running long-running apps on Knative,
   including how to install the Knative Serving prerequisite.
6. [Plugin setup](./plugin-setup/_index): cluster-side configuration some plugins need,
   including [copilot's access](./plugin-setup/copilot-storage) to your object store.

{{< subpage-cards >}}
