---
title: Knative Operator chart
description: Helm values for the Knative Operator chart.
icon: list-columns
variants: -flyte +union
chart_version: 2026.10.0
weight: 2
---

Deploys Knative Operator (consumed as a subchart of `dataplane`)

## Chart info

| | |
|---|---|
| **Chart version** | 2026.10.0 |
| **App version** | 1.16.0 |
| **Kubernetes version** | `>= 1.28.0-0` |

## Values

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| skipNamespaceCreation | bool | Skip creating the Namespace resource. Set to true when the namespace is managed by the parent chart (e.g. via --create-namespace or a separate template). | `false` |
