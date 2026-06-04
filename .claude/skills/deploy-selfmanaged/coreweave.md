# CoreWeave path

Source of truth:
`content/deployment/selfmanaged/selfmanaged-coreweave/prepare-infra.md`
and `selfmanaged-coreweave/deploy-dataplane.md`. CoreWeave-specific
twist: object storage is **virtual-hosted-style only** — Union's default
config is path-style, so the values file needs explicit overrides.

## Cloud-specific prereqs

CoreWeave doesn't have a single official CLI. Cluster + bucket create
happen in the [CoreWeave Cloud Console](https://console.coreweave.com/).
The user needs:

- A CKS cluster created (the skill doesn't automate this — point them at
  https://docs.coreweave.com/products/cks/clusters/create).
- `kubectl` configured with that cluster's context.

Verify:

```bash
kubectl config current-context     # should reference the CKS cluster
kubectl get nodes
```

If kubectl isn't pointing at CKS, the user needs to download the
kubeconfig from the Cloud Console and merge it.

## Step-by-step deploy

### Phase A — Prepare infra (Cloud Console)

The user does these in the CoreWeave Cloud Console — the skill's job is
to **confirm each one is done** before continuing, not to drive the UI.

1. **CKS cluster** created and `kubectl` access verified above.
2. **CoreWeave AI Object Storage bucket** created.
3. **Access keys** generated. The user must copy:
   - Access Key ID
   - Secret Key
4. **Access policy** created — the JSON template lives in
   `prepare-infra.md` § "Create an access policy". Replace
   `<BUCKET_NAME>` with the actual bucket name; attach the policy to the
   access key.

Ask the user to confirm steps 1–4 are complete before generating values.

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
     --clusterName <CLUSTER_NAME> --provider generic
   ```
   (CoreWeave uses the `generic` provider — same as on-prem, with
   custom storage overrides.)

3. **Required overrides for CoreWeave** (full list in
   `deploy-dataplane.md`):
   - S3 endpoint URL → CoreWeave's regional endpoint
   - **`s3ForcePathStyle: false`** (path-style is unsupported)
   - Access Key ID + Secret Key — store as a Kubernetes secret, then
     reference it from the values file. Do not commit credentials.
   - Bucket name + region

   Show the user the values diff before saving.

4. Install:
   ```bash
   kubectl create secret generic union-s3-creds -n union \
     --from-literal=access-key-id=<ACCESS_KEY_ID> \
     --from-literal=secret-access-key=<SECRET_KEY>
   helm upgrade --install union unionai/dataplane \
     -n union --create-namespace \
     -f <org>-values.yaml \
     --wait
   ```

## Verify

Same as other manual paths.

## Teardown

```bash
helm uninstall union -n union
kubectl delete secret union-s3-creds -n union
```

Bucket deletion + access key revocation happen in the Cloud Console —
ask the user to do it manually and confirm.

The CKS cluster itself is usually long-lived; don't delete it unless the
user is explicit.

## CoreWeave-specific gotchas

- **Path-style vs virtual-hosted style** is the #1 thing to get right.
  If pods fail with S3 errors after install, this is almost always the
  cause. The override key is `s3ForcePathStyle: false` in the storage
  block.
- **Access keys are organization-scoped**, not bucket-scoped. The
  attached policy is what restricts them — don't skip the policy step.
- **No CLI for cluster + bucket create** — explicitly tell the user to
  do those in the Console rather than trying to find a `cw` binary.
