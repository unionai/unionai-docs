---
title: Secure namespaces
description: Run projects in Kubernetes namespaces closed by network policy, and see what their workloads reach.
icon: shield-lock
weight: 10
variants: -flyte +union
---

# Secure namespaces

A secure namespace is a Kubernetes namespace closed by [Cilium](https://cilium.io/) network
policy that projects run in. Runs and apps of a project placed in one can reach Union's own
services and the destinations its rules allow, and nothing else. The console's **Security** tab
shows each destination they called and whether it was allowed or blocked.

Turning it on takes three steps:

1. Install Cilium (with Hubble Relay) in each data plane cluster.
2. Enable secure namespaces in the `dataplane` chart.
3. Enable them in the control plane, then create a namespace and attach projects.

## Requirements

- **Cilium 1.20 or later in the data plane cluster**, either as the network plugin or chained
  after the one the cluster has (for EKS, [chained after the AWS VPC CNI](https://docs.cilium.io/en/stable/installation/cni-chaining-aws-cni/)).
  Without Cilium, namespaces are created but nothing enforces their policies.
- **Hubble and Hubble Relay**, for the traffic view. The operator reads flows from
  `hubble-relay.kube-system.svc.cluster.local:80` unless you set another address.
- **Secure namespaces enabled on the control plane.** On a Union-hosted control plane, ask Union
  to enable them for your organization.

## Install Cilium

On EKS, chain Cilium after the VPC CNI, which keeps pod networking, and add Hubble Relay:

```yaml
# values for the cilium chart (https://helm.cilium.io)
cni:
  chainingMode: aws-cni
  exclusive: false
enableIPv4Masquerade: false
routingMode: native
endpointRoutes:
  enabled: true
hubble:
  enabled: true
  relay:
    enabled: true
```

Cilium only enforces policy for pods created after its agent runs on the node. Two things follow:

- **Restart Union's pods after the install**, at least the leaseworker, the apps gateway and
  Knative's activator and autoscaler. A pod older than Cilium has no Cilium identity, so a secure
  namespace's policy treats it as outside the cluster and blocks it. If apps in a secure
  namespace time out when called through the gateway, restart the gateway and activator.
- **Give new nodes the `node.cilium.io/agent-not-ready` startup taint** (`NoSchedule`), which the
  Cilium agent removes once it runs, so no pod starts on a node before policy is enforced there.
  With Karpenter, add it to each node pool's startup taints.

## Enable secure namespaces in the data plane

Set `config.operator.secureNamespaces` in the `dataplane` chart's values:

```yaml
config:
  operator:
    secureNamespaces:
      enabled: true
      # Union's services that workloads in a secure namespace may call: the leaseworker (fast
      # tasks), and for apps the gateway and Knative's activator.
      systemEgress:
        - namespace: union
          labels: {app: leaseworker}
          ports: [15605]
        - namespace: union
          labels: {app: gateway}
        - namespace: union
          labels: {app: activator}
      # Pods that may call into a secure namespace (the operator proxy, the gateway, Knative).
      systemIngress:
        - namespace: union
      # DNS names always reachable: the control plane, and the object store and identity
      # endpoints the tasks use.
      systemDomains:
        - <your-org>.<control-plane-host>
        - sts.amazonaws.com
        - s3.amazonaws.com
        - "*.s3.amazonaws.com"
      # Annotations on each secure namespace's default service account, for example the IAM
      # role its pods use.
      serviceAccountAnnotations:
        eks.amazonaws.com/role-arn: <task role ARN>
```

Replace `union` with the namespace the `dataplane` chart is installed in. The chart then grants the
operator a ClusterRole for namespaces, service accounts, secrets and Cilium policies, and routes
the traffic report to the operator.

Other settings, with their defaults:

| Setting | Default | |
|---|---|---|
| `dns` | `kube-dns` pods in `kube-system` | Set `entities: [host]` when node-local DNS answers on the node. |
| `hubbleRelayAddress` | `hubble-relay.kube-system.svc.cluster.local:80` | Empty records no traffic. |
| `systemCIDRs` | none | Address ranges always reachable. |
| `trafficRetention` | `24h` | How long a destination nobody called again stays in the report. |

> [!NOTE]
> `systemDomains` entries are always reachable from every secure namespace, and are not shown in
> the traffic view. A wildcard such as `*.s3.amazonaws.com` allows every bucket, not only yours.

## Enable secure namespaces in the control plane

On a self-hosted control plane, set `secureNamespaces.enabled: true` in the `controlplane` chart.
The cluster service then serves the secure namespaces API, the gateway routes it, and the console
shows **Settings > Secure namespaces** and each project's **Security** tab.

## Create a namespace and attach projects

In the console, open **Settings > Secure namespaces** and create one. A new namespace blocks all
traffic out of the cluster; switch it to an allowlist of domains, `*.` wildcards, CIDRs and ports,
or to monitor mode, which records traffic without blocking it.

Attach projects in the same form. A project is in a secure namespace when its
`security.kubernetes_namespace` setting names it (`secure-<name>`), so you can also set it for a
whole domain or the organization, and override it on a project. Changing the setting needs project
administration (account administration for the organization), and it applies to runs and apps
started afterwards: running ones keep their namespace.

Secure namespaces are applied on every data plane with them enabled. A run placed in one fails
with `SecureNamespaceUnavailable` on a cluster that does not have it, so route those projects to a
queue on a cluster that does.

## Turn it off

1. Clear the `security.kubernetes_namespace` settings, so new runs and apps are no longer placed.
2. Delete the namespaces in **Settings > Secure namespaces**. Deleting one stops everything still
   running in it.
3. Set `config.operator.secureNamespaces.enabled: false` in the `dataplane` chart.

To remove Cilium, drop the startup taint from your node pools, upgrade the Cilium release with
`cni.uninstall=true` and let its agents roll, then uninstall it.
