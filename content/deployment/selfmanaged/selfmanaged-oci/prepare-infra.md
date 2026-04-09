---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through creating the OCI resources needed for a Union data plane. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-oci/deploy-dataplane).

## OKE Cluster

You need an OKE cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

If you don't already have a cluster, create one via the [OCI Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm) or the OCI CLI:

```bash
export COMPARTMENT_ID=<YOUR_COMPARTMENT_OCID>
export REGION=<YOUR_OCI_REGION>              # e.g. us-ashburn-1
export VCN_ID=<YOUR_VCN_OCID>
export SUBNET_ID=<YOUR_KUBERNETES_API_SUBNET_OCID>

oci ce cluster create \
  --compartment-id ${COMPARTMENT_ID} \
  --name union-dataplane \
  --kubernetes-version v1.31.1 \
  --vcn-id ${VCN_ID} \
  --endpoint-subnet-id ${SUBNET_ID} \
  --region ${REGION}
```

> [!NOTE] The OKE cluster creation requires a pre-existing VCN and subnet. See the [OCI networking documentation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm) for details on setting up the required network resources.

Union supports Autoscaling and the use of preemptible instances.

## Object Storage

Each data plane uses OCI Object Storage buckets to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `flyte deploy` or `flyte run --copy-style all`.

You can also choose to use a single bucket.

Create the buckets:

```bash
export BUCKET_PREFIX=union-dataplane   # choose a unique prefix within your tenancy

oci os bucket create \
  --compartment-id ${COMPARTMENT_ID} \
  --name ${BUCKET_PREFIX}-metadata \
  --region ${REGION}

oci os bucket create \
  --compartment-id ${COMPARTMENT_ID} \
  --name ${BUCKET_PREFIX}-fast-reg \
  --region ${REGION}
```

### CORS Configuration

To enable the [Code Viewer](../configuration/code-viewer) in the Union UI, configure a CORS policy on your bucket(s). This allows the UI to securely fetch code bundles directly from storage.

OCI Object Storage CORS is configured via bucket settings. See the [OCI CORS documentation](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-CORS.htm) for details. Apply the following rule:

- **Allowed Origins:** `https://*.unionai.cloud`
- **Allowed Methods:** `GET`, `HEAD`
- **Allowed Headers:** `*`
- **Expose Headers:** `ETag`
- **Max Age Seconds:** `3600`

### Data Retention

Union recommends using lifecycle policies on these buckets to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

## Container Registry

Create an [OCI Container Registry (OCIR)](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm) repository for Image Builder to push and pull container images:

```bash
oci artifacts container-repository create \
  --compartment-id ${COMPARTMENT_ID} \
  --display-name union-dataplane/imagebuilder \
  --is-public false
```

Note the repository path (e.g. `${REGION}.ocir.io/<TENANCY_NAMESPACE>/union-dataplane/imagebuilder`) — you will reference it when configuring access below.

## Identity & Access

Union services and workflow task pods need access to your Object Storage buckets and Container Registry. OCI supports two authentication models:

### Option A: Instance Principals (recommended)

Use [Instance Principals](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm) so that pods running on OKE nodes inherit permissions automatically.

#### 1. Create a Dynamic Group

Create a [Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm) matching your OKE worker nodes:

```bash
oci iam dynamic-group create \
  --compartment-id ${COMPARTMENT_ID} \
  --name union-dataplane-nodes \
  --description "OKE worker nodes for Union data plane" \
  --matching-rule "ALL {instance.compartment.id = '${COMPARTMENT_ID}'}"
```

#### 2. Create IAM policies

Grant the dynamic group access to Object Storage and OCIR:

```bash
oci iam policy create \
  --compartment-id ${COMPARTMENT_ID} \
  --name union-dataplane-policy \
  --description "Allow Union data plane access to Object Storage and OCIR" \
  --statements \
  '["Allow dynamic-group union-dataplane-nodes to manage objects in compartment id '"${COMPARTMENT_ID}"' where target.bucket.name='"'"''"${BUCKET_PREFIX}"'-metadata'"'"'",
    "Allow dynamic-group union-dataplane-nodes to manage objects in compartment id '"${COMPARTMENT_ID}"' where target.bucket.name='"'"''"${BUCKET_PREFIX}"'-fast-reg'"'"'",
    "Allow dynamic-group union-dataplane-nodes to manage repos in compartment id '"${COMPARTMENT_ID}"'"]'
```

### Option B: Static Credentials

If Instance Principals are not available, you can use S3-compatible access keys:

#### 1. Generate a Customer Secret Key

Create a [Customer Secret Key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#s3) for S3 Compatibility API access:

```bash
export USER_OCID=<YOUR_USER_OCID>

oci iam customer-secret-key create \
  --user-id ${USER_OCID} \
  --display-name union-dataplane-s3-compat
```

> [!NOTE] The command output contains the secret key value. Save it immediately — it cannot be retrieved again.

You will configure these credentials in the generated values file during deployment (see step 3 in [Deploy the dataplane](../selfmanaged-oci/deploy-dataplane)).
