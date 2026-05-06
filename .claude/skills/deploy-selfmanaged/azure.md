# Azure path

Source of truth: `content/deployment/selfmanaged/selfmanaged-azure/prepare-infra.md`
and `selfmanaged-azure/deploy-dataplane.md`. The doc is authoritative —
follow it section by section. This file captures the verification gates,
the order, and the gotchas.

## Cloud-specific prereqs

```bash
az version              # Azure CLI 2.x
```

Install if missing:

```bash
brew install azure-cli
```

## Auth verification

```bash
az account show --query '{subscriptionId:id, tenantId:tenantId, name:name}'
```

Must return the subscription the user pinned at intent capture. If the
output is wrong or `az` reports "Please run 'az login'", run:

```bash
az login
az account set --subscription <SUBSCRIPTION_ID>
```

## Step-by-step deploy (mirrors `prepare-infra.md` then `deploy-dataplane.md`)

Walk these in order. **Confirm each cloud-mutating command with the
user before running it.** All variables come from the env-var block at
the top of `prepare-infra.md` — set those once at the start of the
session and reuse.

### Phase A — Prepare infra

1. **Set env vars** — read the block from `prepare-infra.md` § "Environment
   variables" and have the user fill in:
   - `RESOURCE_GROUP`, `LOCATION`, `CLUSTER_NAME`, `ORG_NAME`
   - `STORAGE_ACCOUNT`, `METADATA_CONTAINER`
   - `BACKEND_IDENTITY_NAME`, `WORKER_IDENTITY_NAME`
   - `DATAPLANE_NAMESPACE=union` (do not change)

2. **Resource group** (`prepare-infra.md` § 1) — `az group create`.

3. **AKS cluster** (`prepare-infra.md` § 2) — `az aks create` with the three
   required add-ons: `--enable-oidc-issuer`, `--enable-workload-identity`,
   `--enable-managed-identity`. Capture the OIDC issuer URL
   (`AKS_OIDC_ISSUER`) — you will need it for federated credentials.

4. **kubectl context** — `az aks get-credentials`. Verify with
   `kubectl get nodes`.

5. **Storage account + container** — follow `prepare-infra.md` § 3.

6. **Managed identities + Workload Identity federation** — follow
   `prepare-infra.md` § 4. Capture `BACKEND_CLIENT_ID` and
   `WORKER_CLIENT_ID` — both are required for the helm values.

7. **(Optional) Azure Key Vault** — if the user wants Union secrets
   backed by Key Vault, follow `prepare-infra.md` § 5.

### Phase B — Deploy

Source: `deploy-dataplane.md`.

1. Add helm repo:
   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Generate the values file via uctl:
   ```bash
   uctl config init --host=<CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources \
     --clusterName <CLUSTER_NAME> --provider azure
   ```
   This writes `<org>-values.yaml`. The user must save the printed
   client secret — Union does not store it; rerunning produces the same
   secret only if the same client is reused.

3. Edit the generated values file. Show the user the diff before saving.
   Required substitutions (from `deploy-dataplane.md` § 3):
   - `global.BACKEND_IAM_ROLE_ARN` → `${BACKEND_CLIENT_ID}`
   - `global.WORKER_IAM_ROLE_ARN` → `${WORKER_CLIENT_ID}`
   - `global.METADATA_BUCKET` → `${METADATA_CONTAINER}`
   - `storage.custom.stow.config.account` → `${STORAGE_ACCOUNT}`
   - `storage.region` → `${LOCATION}`
   - `commonServiceAccount.annotations."azure.workload.identity/client-id"` → `${BACKEND_CLIENT_ID}`
   - (If Key Vault) `AZURE_KEY_VAULT_URI` → `https://${KEY_VAULT_NAME}.vault.azure.net/`

4. Install:
   ```bash
   helm upgrade --install union unionai/dataplane \
     -n union --create-namespace \
     -f <org>-values.yaml \
     --wait
   ```

   In a second terminal, watch:
   ```bash
   kubectl get pods -n union -w
   ```

## Verify

```bash
kubectl get pods -n union
kubectl get events -n union --sort-by=.lastTimestamp | tail -20
```

All pods should be `Running`. For an end-to-end smoke against the new
cluster:

```bash
source scripts/.venv/bin/activate
cd scripts
python -m smoke_tests \
    --control_plane_url <CONTROL_PLANE_URL> \
    --cluster_name <CLUSTER_NAME>
```

(Requires the `scripts/.venv` from `aws.md` to be set up.)

## Teardown

Reverse order. **Ask before each delete.**

```bash
helm uninstall union -n union
az identity delete --name $WORKER_IDENTITY_NAME -g $RESOURCE_GROUP
az identity delete --name $BACKEND_IDENTITY_NAME -g $RESOURCE_GROUP
az storage container delete --name $METADATA_CONTAINER --account-name $STORAGE_ACCOUNT
az storage account delete --name $STORAGE_ACCOUNT -g $RESOURCE_GROUP --yes
az aks delete --name $CLUSTER_NAME -g $RESOURCE_GROUP --yes
# Only if the resource group was created exclusively for this dataplane:
az group delete --name $RESOURCE_GROUP --yes
```

Never delete the resource group if it predated this skill or hosts other
workloads.

## Azure-specific gotchas

- **OIDC issuer URL must be captured immediately after AKS create.** It
  is required for federated credentials and the `az aks show` command
  to retrieve it later is non-obvious.
- **`STORAGE_ACCOUNT` is globally unique** in Azure — if create fails,
  the name is taken; have the user pick another.
- **Workload Identity federation needs the AKS OIDC issuer plus the
  exact `union` namespace + service account name.** The provisioned
  values file uses these — don't rename the namespace.
