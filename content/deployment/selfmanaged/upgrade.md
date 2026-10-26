---
title: Upgrade the data plane
description: Keep a self-managed data plane current, including the chart, its CRDs, and your values file.
icon: arrow-up-circle
weight: 4
variants: -flyte +union
---

# Upgrade the data plane

In a self-managed deployment you own the data plane's version. This page covers what you keep
current, the supported way to do it, and how to automate it.

## What you maintain

A self-managed data plane has three pieces that move together:

| Piece | What it is | How it is updated |
|---|---|---|
| **The `dataplane` chart** | The Union components that run in your cluster (operator, leaseworker, proxy, image builder, app-serving gateway, monitoring). | `helm upgrade` to a new chart version. |
| **The CRDs** | Kubernetes schema definitions the chart's components require (`FlyteWorkflow`, Knative Serving, Prometheus Operator). | Applied by you, separately from the chart, from the same release tag. Helm does not update CRDs on `helm upgrade`. |
| **Your values file** | The configuration you pass to the chart. | Edited by you when a release renames, removes, or adds a key. Helm does not validate values against the chart, so keys the chart no longer reads are ignored. |

The chart and the CRDs are released together under one calendar version (for example
`2026.9.7`). Always pin both to the same version.

## The supported setup

- The chart is installed with `--skip-crds`.
- CRDs are applied with server-side apply from the `crds/` directory of the
  [`unionai/helm-charts`](https://github.com/unionai/helm-charts) repository, checked out at
  the git tag matching your chart version (`dataplane-<version>`):
  - `crds/dataplane/` — always required.
  - `crds/kube-prometheus-stack/` — required when you set `monitoring.enabled: true` (the
    default is `false`) and do not already manage the Prometheus Operator CRDs elsewhere.
- App serving uses the chart's built-in gateway: `gateway.enabled: true` and
  `knative-operator.enabled: false`.
- The cluster runs Kubernetes 1.28 or later, the chart's declared minimum (`kubeVersion`).

> [!NOTE] Older install mechanisms
> The `dataplane-crds` chart is deprecated. If you still install it, switch to applying
> `crds/dataplane/` as described above. Do **not** run `helm uninstall` or `terraform destroy`
> on `dataplane-crds`: because its `templates/flyteworkflow.yaml` rendered `FlyteWorkflow`
> as a standard template, Helm will delete the `FlyteWorkflow` CRD and every active workflow
> object across the cluster. In Terraform, detach the release with
> `terraform state rm helm_release.dataplane_crds`. In plain Helm, leave the existing release
> installed (it is dormant once CRDs are managed via server-side apply) or delete only the Helm
> release Secret directly.
>
> The `crds/` directory inside the `dataplane` chart package is a Helm convention that is only
> applied on the very first `helm install` and is never updated afterwards; it is not a substitute
> for the step above.
>
> If you installed by following [Deploy the data plane](./deploy/_index), Helm created your
> CRDs from that directory. The first server-side apply below (with `--force-conflicts`) takes
> over their ownership; use `--skip-crds` on every `helm upgrade` from then on.

## Before you upgrade

1. **Read the release notes** for every version between your current version and your
   target, oldest first. Each release is documented in
   [`charts/dataplane/RELEASE.md`](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/RELEASE.md),
   and larger changes have a dedicated entry in
   [`charts/MIGRATION.md`](https://github.com/unionai/helm-charts/blob/main/charts/MIGRATION.md).
   Look for three things: values keys that were renamed or removed, CRD version bumps, and
   any one-time migration step.
2. **Check for one-time migrations** before upgrading. If your cluster previously enabled
   `knative-operator`, complete the [Moving off the knative-operator path](#one-time-migrations)
   step before running `helm upgrade`.
3. **Save your current values and note the release revision.** The saved file includes
   everything you passed with `--set` at install time, such as your client ID and secret, so
   store it securely:

   ```bash
   NS=union                       # namespace of the dataplane release
   REL=union                      # release name; substitute yours if different

   helm get values "$REL" -n "$NS" -o yaml > values-backup-$(date +%Y%m%d-%H%M).yaml
   helm history "$REL" -n "$NS"
   ```

3. **Upgrade a non-production data plane first** if you have one.

## Upgrade

Set the target version once and use it for both the CRDs and the chart.

```bash
VERSION=2026.9.7
```

1. **Apply the CRDs at the target version.** From a clone of `unionai/helm-charts`:

   ```bash
   git fetch --tags
   git checkout "dataplane-${VERSION}"

   kubectl apply --server-side --force-conflicts -f crds/dataplane/
   kubectl apply --server-side --force-conflicts -f crds/kube-prometheus-stack/   # if monitoring.enabled
   ```

   `--force-conflicts` lets server-side apply take field ownership from a previous installer
   (Helm's first-install `crds/` directory, or the deprecated `dataplane-crds` chart). It is
   safe to include on every run.

2. **Prepare your upgrade values file.** Start from the file you saved in
   [Before you upgrade](#before-you-upgrade), not the original provider values file, so the
   settings you passed with `--set` at install time are carried over. Apply any changes the
   release notes call for.

3. **Upgrade the chart:**

   ```bash
   helm repo update
   helm upgrade "$REL" unionai/dataplane \
     --namespace "$NS" \
     --version "$VERSION" \
     --values <YOUR_UPGRADE_VALUES_FILE> \
     --skip-crds \
     --timeout 10m --wait
   ```

   Run the same command with `--dry-run=server` first to render the manifests against the
   cluster without applying them. For a diff against the live release, use the
   [`helm diff upgrade`](https://github.com/databus23/helm-diff) plugin.

4. **Verify:**

   ```bash
   kubectl get pods -n "$NS"
   kubectl logs -n "$NS" -l app.kubernetes.io/name=clusterresourcesync --tail=50
   ```

   All pods should be `Running` and `clusterresourcesync` should log a successful connection
   to the control plane. Run a test execution to verify end-to-end task scheduling:

   ```bash
   flyte run hello
   ```

   If you use app serving, open an app to confirm serving pods reach ready status.

## Roll back

```bash
helm history "$REL" -n "$NS"
helm rollback "$REL" <LAST_GOOD_REVISION> -n "$NS" --wait
```

## Automating upgrades

The chart is published to a standard Helm repository at
`https://unionai.github.io/helm-charts/`, so dependency bots such as Renovate or Dependabot
can open a pull request whenever a new version is released. Two things to build into that
automation:

- **Bump the CRDs with the chart.** The CRD apply should reference the same `dataplane-<version>`
  tag as the chart version in the same change.
- **Review the release notes as part of the pull request.** Check `RELEASE.md` for the versions
  the change spans and apply any values updates it calls for before merging.

## One-time migrations

Some releases include a step that runs once, outside the normal flow. These are called out in
`RELEASE.md` and `MIGRATION.md`:

- **Moving off the `knative-operator` path.** If app serving was ever enabled on the cluster
  with `knative-operator.enabled: true`, run the
  [`knative-migration`](https://github.com/unionai/helm-charts/tree/main/charts/knative-migration)
  chart before upgrading to a release that uses the built-in gateway. It removes the operator's
  `KnativeServing` resources and CRDs. Clusters that never enabled the operator can skip it; a
  quick check is that no `knativeservings` CRD exists:

  ```bash
  kubectl get crd knativeservings.operator.knative.dev
  ```

  Run the migration while the operator is still healthy
  (`kubectl get deploy -n "$NS" knative-operator`). Because you apply the `dataplane` chart with
  `helm upgrade`, install the migration chart with adoption enabled and the release name and
  namespace you use for the data plane:

  ```bash
  helm install unionai-knative-migration unionai/knative-migration \
    --namespace "$NS" \
    --set adoption.enabled=true \
    --set adoption.targetRelease="$REL" \
    --set adoption.targetNamespace="$NS" \
    --wait --wait-for-jobs --timeout 15m
  ```
