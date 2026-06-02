---
title: Separate-cluster install
weight: 8
variants: -flyte +union
sidebar_expanded: true
---

# Separate-cluster install

This guide walks you through installing a {{< key product_name >}} self-hosted deployment in the **separate-cluster topology** — control plane and data plane in distinct Kubernetes clusters, communicating over the control plane's ingress. This is the default and recommended topology described in [Self-hosted deployment → Topologies](./_index#topologies); it isolates blast radius between the planes, allows them to evolve independently, and supports multi-region / multi-environment fan-out from a single control plane.

If you instead want both planes on a single cluster, see [Getting started](./getting-started) (intra-cluster walkthrough).

It assumes both clusters' cloud substrate is already provisioned. For what to provision per plane and how to size it, see [Infrastructure requirements](./infrastructure-requirements) — especially the [Networking](./infrastructure-requirements#networking) and [Kubernetes cluster](./infrastructure-requirements#kubernetes-cluster) sections, which break out CP vs DP requirements.

> [!NOTE]
> Separate-cluster topology is officially supported on **AWS**. **GCP** support is in preview; additional cloud providers are coming. The walkthrough below uses tabs to switch between cloud-specific details where they differ.

## Prerequisites

In addition to everything listed in the [Getting started → Prerequisites](./getting-started#prerequisites) section, separate-cluster topology requires:

1. **Two Kubernetes clusters**, each meeting [Infrastructure requirements](./infrastructure-requirements) for its respective plane (the CP cluster is sized for steady-state; the DP cluster is sized for peak workload).
2. **Network reachability from the DP cluster to the CP's ingress endpoint**. Two common options:
   - **Public**: DP nodes reach the CP via the internet using the CP's public DNS name. Simplest to operate; no peering required. DP→CP traffic exits the DP VPC, hits the CP's public load balancer, and terminates TLS at the CP's ingress.
   - **Private**: DP nodes reach the CP via a private hostname over VPC peering (AWS Transit Gateway / VPC peering, GCP VPC Network Peering, Azure VNet peering). Lower latency and avoids egress charges, at the cost of running an internal load balancer on the CP and reconciling DNS records into a private zone shared by both VPCs.
3. **DNS hostnames for both ingress endpoints**:
   - `controlplane.<domain>` (public, or internal if private routing) — clients and DP agents reach the CP here.
   - `<dp-name>.<domain>` (typically internal) — CP reaches the DP here for execution status reconciliation and log streaming.
4. **TLS certificates** for each hostname (public CA via cert-manager / ACM, or internal CA if private routing is used end-to-end).
5. **Per-cluster identity bindings** — each cluster's workloads need IRSA (AWS) / Workload Identity Federation (GCP) configured against its own OIDC provider. The CP and DP do not share IAM roles; each plane's IAM bindings are scoped to its own cluster's OIDC provider.

## Deployment overview

1. Confirm cross-cluster networking and DNS resolution.
2. Install the control plane on the CP cluster (Helm release, ingress, DNS record, TLS).
3. Register the data plane with the control plane (workload-identity binding so the DP can authenticate to the CP).
4. Install the data plane on the DP cluster (Helm release pointing at the CP).
5. Verify the installation end-to-end.

The chart-side steps (Helm repository setup, CRD install, namespace + image-pull-secret creation, TLS certificate generation, database password secret) are identical to the intra-cluster walkthrough — see [Getting started → Steps 1–4](./getting-started#step-1-helm-repositories-and-control-plane-crds) and apply them to each cluster as appropriate (CP-side steps on the CP cluster, DP-side steps on the DP cluster). The sections below cover only what differs in separate-cluster topology.

## Step 1: Confirm cross-cluster networking and DNS

Before installing, verify that:

- From a pod in the DP cluster, the CP's ingress hostname resolves and the TCP/443 connection succeeds. A quick check:
  ```shell
  kubectl --context <dp-cluster> run -it --rm netcheck --image=nicolaka/netshoot --restart=Never -- \
    curl -sv -o /dev/null https://controlplane.<domain>/healthz
  ```
  Expect HTTP 200. A DNS resolution failure indicates Cloud DNS / Route53 peering isn't wired up; a TCP timeout indicates VPC peering or security-group rules block egress.
- The CP cluster can resolve the DP's ingress hostname. The CP only needs to reach the DP after a data plane is registered (Step 3); it's worth confirming preemptively.

If you're using **public** routing (DP→CP over the internet via the CP's public DNS), DNS resolution works out of the box — there's nothing additional to wire up. Skip to Step 2.

If you're using **private** routing, the following needs to be in place:

- VPC peering (or Transit Gateway attachment / cross-region peering) between the CP VPC and each DP VPC. Routes installed on both sides.
- Security-group / firewall rules allowing TCP/443 from DP nodes to the CP's internal load balancer (and vice-versa for CP→DP, if applicable).
- A private DNS zone (Route53 private zone / Cloud DNS private zone / Azure Private DNS zone) reachable from both VPCs. Both clusters' `external-dns` instances must be able to write to it.

## Step 2: Install the control plane (CP cluster)

Apply Steps 1–6 from [Getting started](./getting-started#step-1-helm-repositories-and-control-plane-crds) on the CP cluster. The control plane's `values-overrides.yaml` differs from the intra-cluster case in only two places:

1. **CP `union.ingress.host`** is the public (or private, if you chose private routing) hostname clients and DP agents will use to reach the CP:
   ```yaml
   union:
     ingress:
       host: controlplane.<domain>
   ```
2. **`dataplane` block is absent at install time.** In intra-cluster topology, the chart's selfhosted overrides preconfigure a single in-cluster DP. In separate-cluster topology, you register data planes after installation (Step 3); the CP starts with zero registered DPs and accepts registrations as DP clusters come online.

Everything else — database connection string, OIDC provider, object storage buckets, Helm release name and namespace — follows the intra-cluster walkthrough.

After the control plane install completes and reports `Ready` for the `unionai-controlplane` Helm release, confirm:

```shell
kubectl --context <cp-cluster> -n <controlplane-namespace> get pods
```

All pods `Running` / `Ready`. The ingress controller should have an external IP (public LB) or internal IP (internal LB) assigned. DNS for `controlplane.<domain>` should resolve to that IP — `external-dns` writes the A record automatically once the Service / Ingress has its address.

## Step 3: Register the data plane

The DP authenticates to the CP using a workload identity bound to the CP's OIDC provider. The CP needs to know:

- **The DP's name** — a stable identifier (`dp-1`, `us-west-2-prod`, etc.) used in routing decisions.
- **The DP's ingress host** — where the CP can reach the DP for execution status reconciliation and log streaming.
- **The DP's OIDC issuer URL and the client identity** the DP will present.

Register the DP by adding an entry to the CP's `values-overrides.yaml` and applying a `helm upgrade`:

```yaml
union:
  registered_dataplanes:
    - name: dp-1
      ingress_host: dp-1.<domain>
      oidc:
        issuer: https://<dp-cluster-oidc-issuer-url>
        client_id: union-dataplane-dp-1
```

```shell
helm upgrade unionai-controlplane unionai/controlplane \
  --namespace <controlplane-namespace> \
  --values values-overrides.yaml \
  --skip-crds
```

The CP creates an OAuth client representing the DP and authorizes its OIDC subject claim (the DP's workload identity) to invoke CP APIs scoped to that DP's name.

## Step 4: Install the data plane (DP cluster)

Apply Steps 7–8 from [Getting started](./getting-started#step-7-install-data-plane-crds) on the DP cluster, with two differences in the data plane's `values-overrides.yaml`:

1. **`controlplane.host` points at the CP's ingress hostname** — the DP discovers all CP API endpoints from this single hostname:
   ```yaml
   controlplane:
     host: controlplane.<domain>
   ```
2. **`union.ingress.host` is the DP's own internal hostname** — the address the CP will use to reach this DP:
   ```yaml
   union:
     ingress:
       host: dp-1.<domain>
   ```

The DP's `controlplane.host` value must match the CP's `union.ingress.host` exactly (including any internal subdomain if you're using private routing). The DP operator authenticates to the CP using its workload identity bound to the OIDC client you registered in Step 3.

After the data plane install completes:

```shell
kubectl --context <dp-cluster> -n <dataplane-namespace> get pods
```

All pods `Running` / `Ready`. The operator's logs should show successful registration with the CP and periodic heartbeat traffic:

```shell
kubectl --context <dp-cluster> -n <dataplane-namespace> logs -l app=union-operator --tail=50
```

Expect lines reporting a successful connection to `controlplane.<domain>` and no auth errors. If the DP fails to authenticate, the OIDC client registration in Step 3 or the workload identity binding on the DP cluster is misconfigured — see [Authentication](./authentication).

## Step 5: Verify end-to-end

From a workstation with `unionctl` configured against the CP:

```shell
unionctl get projects
unionctl get cluster-pools
```

The DP should appear in `get cluster-pools` (registered and healthy). Submit a hello-world workflow to confirm CP→DP routing works:

```shell
unionctl run --remote examples/basics/hello_world.py hello_world_wf
```

The action should land on the registered DP, execute, and report back. If the DP shows registered but actions time out, the most common causes are:

- **DNS resolution failures** between the planes (Step 1's network check).
- **Mismatched `controlplane.host` value** on the DP versus `union.ingress.host` on the CP.
- **OIDC subject claim mismatch** — the DP's workload identity doesn't match the subject the CP authorized in Step 3.

[Troubleshooting → Cross-cluster connectivity](./operations/troubleshooting) covers each of these in detail.

## Adding additional data planes

Repeat Steps 3 and 4 for each additional data plane, choosing a distinct name (`dp-2`, `us-east-1-prod`, etc.) and a distinct ingress hostname per DP. Each DP can be in a different VPC, region, or cloud provider; the CP doesn't care about substrate as long as the network path and OIDC trust are in place.

## Differences from intra-cluster topology

| Aspect | Intra-cluster | Separate-cluster |
|---|---|---|
| Clusters | 1 | 1 CP + N DPs |
| VPC peering | Not applicable | Required for private routing; optional otherwise |
| `controlplane.host` (DP-side) | In-cluster DNS (`controlplane-nginx-controller.controlplane.svc.cluster.local`) | CP's ingress hostname |
| `union.ingress.host` (CP-side) | Optional (clients hit in-cluster service) | Required (clients hit ingress) |
| `dataplane` block on CP install | Preconfigured by chart | Registered post-install (Step 3) |
| `external-dns` instances | One per cluster | One per cluster — both planes write to a shared zone if private routing |
| TLS certificate scope | Single CP hostname | One per CP + one per DP |
| DP→CP auth | In-cluster service account, in-cluster IdP | OIDC workload identity against the CP cluster's IdP |
| Failure isolation | Plane outage = full-cluster outage | DP cluster outage doesn't affect CP availability or other DPs |

## Next steps

- [Authentication](./authentication) — wiring your OIDC provider for the CP.
- [Authorization](./authorization) — granting users access to projects and DPs.
- [Operations → Monitoring](./operations/monitoring) — health metrics for both planes (deploy the chart's monitoring stack on each cluster independently).
- [Operations → Troubleshooting](./operations/troubleshooting) — common failure modes and recovery procedures.
