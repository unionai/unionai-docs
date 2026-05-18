# OCI path

Source of truth: `content/deployment/selfmanaged/selfmanaged-oci/prepare-infra.md`
and `selfmanaged-oci/deploy-dataplane.md`. Follow the doc — this file
captures gates and order.

## Cloud-specific prereqs

```bash
oci --version
```

Install if missing:

```bash
brew install oci-cli
```

## Auth verification

```bash
oci iam region list >/dev/null && echo OK
```

If this fails, run `oci setup config` (interactive — the user supplies
their tenancy OCID, user OCID, region, and an API key).

Confirm the active tenancy and region match what the user pinned:

```bash
oci iam compartment get --compartment-id <COMPARTMENT_OCID>
```

## Step-by-step deploy

### Phase A — Prepare infra (`prepare-infra.md`)

1. **Set env vars**: `COMPARTMENT_ID`, `REGION`, `VCN_ID`, `SUBNET_ID`,
   `BUCKET_PREFIX`. The user must pre-create a VCN + subnet — the doc
   links to OCI's networking guide. Don't try to provision networking
   from inside this skill.

2. **OKE cluster** — `oci ce cluster create`. Confirm before running.

3. **kubectl context** — follow `prepare-infra.md` for the
   `oci ce cluster create-kubeconfig` invocation. Verify with
   `kubectl get nodes`.

4. **Object Storage buckets** — metadata + fast-registration buckets via
   `oci os bucket create`.

5. **OCI Identity** — set up the Instance Principal or Workload Identity
   binding the doc describes. Capture the OCIDs needed for the values
   file.

### Phase B — Deploy (`deploy-dataplane.md`)

1. Helm repo:
   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Generate values:
   ```bash
   uctl config init --host=<CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources \
     --clusterName <CLUSTER_NAME> --provider oci
   ```

3. Edit values per `deploy-dataplane.md` (bucket names, region,
   identity OCIDs). Show the user the diff before saving.

4. Install:
   ```bash
   helm upgrade --install union unionai/dataplane \
     -n union --create-namespace \
     -f <org>-values.yaml \
     --wait
   ```

## Verify

Same as other manual paths — `kubectl get pods -n union`, then optionally
the smoke suite from `scripts/`.

## Teardown

Reverse order. **Confirm each delete.**

```bash
helm uninstall union -n union
oci os bucket delete --bucket-name <FAST_REG_BUCKET> --force
oci os bucket delete --bucket-name <METADATA_BUCKET> --force
oci ce cluster delete --cluster-id <CLUSTER_OCID> --force
```

Do not touch the VCN, subnet, or compartment unless the user explicitly
asks — those usually predate the dataplane.

## OCI-specific gotchas

- **VCN + subnet must exist** before cluster create. The skill should
  refuse to create them — direct the user to the OCI networking docs.
- **Instance Principals vs Workload Identity** — OKE supports both.
  Read the prepare-infra doc carefully and confirm with the user which
  the cluster is using before generating values.
- **Bucket namespace**: OCI Object Storage buckets are scoped to a
  tenancy namespace. The values file needs both bucket name *and*
  namespace.
