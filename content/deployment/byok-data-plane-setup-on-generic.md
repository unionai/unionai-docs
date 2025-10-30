---
title: Data plane setup on generic Kubernetes
weight: 3
variants: -flyte -serverless -byoc +selfmanaged
---

# Data plane setup on generic Kubernetes

{{< key product_name >}}’s modular architecture allows for great flexibility and control. The customer can decide how many clusters to have, their shape, and who has access to what. All communication is encrypted.  The Union architecture is described on the [Architecture](../../architecture) page.

> [!NOTE] These instructions cover installing Union.ai in an on-premise Kubernetes cluster.
> If you are installing at a cloud provider, use the cloud provider specific instructions: [AWS](./install-unionai-on-AWS.md), GKE, Azure, OCI.

## Assumptions
* You have a {{< key product_name >}} organization and you know the Control Plane URL for your Organization. (e.g. https://your-org-name.us-east-2.unionai.cloud)
* You have a cluster name provided by or coordinated with Union
* You have a Kubernetes cluster, running one of the most recent three minor K8s versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* Object storage provided by a vendor or an S3 compatible platform (such as [Minio](https://min.io)).


## Prerequisites
* Install [Helm 3](https://helm.sh/docs/intro/install/)
* Install [union](../api-reference/union-cli) and [uctl](../api-reference/uctl-cli).

## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:
```shell
helm repo add unionai https://unionai.github.io/helm-charts/
helm repo update
```

2. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your Union control plane, provision authz permissions for the app to operate on the union cluster name you have selected, generate values file to install dataplane in your kubernetes cluster and provide followup instructions:
```shell
uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider metal
```
* The output will emit the ID, name, and a secret that will be used by the union services to communicate with your control plane and it also generate values file based on the passed in provider
```shell
  -------------- ------------------------------------ ---------------------------- ------------------------------------------------- ------------------------------------------------------------------ ---------- 
| ORGANIZATION | HOST                               | CLUSTER                    | CLUSTERAUTHCLIENTID                             | CLUSTERAUTHCLIENTSECRET                                          | PROVIDER |
 -------------- ------------------------------------ ---------------------------- ------------------------------------------------- ------------------------------------------------------------------ ---------- 
| xxxxxxxxxxx  | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | xxxxxxxxxxxxxxxxxxxxxxxxxx | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | xxxxx    |
 -------------- ------------------------------------ ---------------------------- ------------------------------------------------- ------------------------------------------------------------------ ---------- 
1 rows

✅ Generated <ORGNAME>-values.yaml
======================================================================
Installation Instructions
======================================================================

Step 1: Prepare your on-prem Kubernetes cluster.

Step 2: Clone and navigate to helm-charts repository
  git clone https://github.com/unionai/helm-charts && cd helm-charts

Step 3: Configure your S3-compatible storage endpoint & credentials in the values file

Step 4: Install the data plane CRDs
  helm upgrade --install unionai-dataplane-crds charts/dataplane-crds

Step 5: Install the data plane
  helm upgrade --install unionai-dataplane charts/dataplane \
    --namespace union \
    --values <ORGNAME>-values.yaml

Step 6: Verify installation
  kubectl get pods -n union

Step 7: Once you have your dataplane up and running, create API keys for your organization. If you have already just call the same command again to propogate the keys to new cluster:
  uctl create apikey --keyName EAGER_API_KEY --org <your-org-name>
Step 8: You can now trigger v2 executions on this dataplane.
```
* Save the secret that is displayed. Union does not store the credentials, rerunning the same command can be used to show same secret later which stream through the Oauth Apps provider.
* Note the creation of EAGER_API_KEY in Step 7. This is required for running v2 executions on this dataplane and the prerequisite for creating that api key is that the dataplane needs to up and runnning successfully.
* Note if you have already create EAGER_API_KEY for one of you connected clusters then also you would need to do this operation as it sync the api key to the new cluster.

3.  Update the values file correctly:
    eg  `<UNION_FLYTE_ROLE_ARN>` is the ARN of the new IAM role created in the [AWS Cluster Recommendations](./cluster-recommendations.md#iam)

4. Optionally configure the resource `limits` and `requests` for the different services.  By default these will be set minimally, will vary depending on usage, and follow the Kubernetes `ResourceRequirements` specification.
   * `clusterresourcesync.resources`
   * `flytepropeller.resources`
   * `flytepropellerwebhook.resources`
   * `operator.resources`
   * `proxy.resources`

5. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

```shell
uctl get cluster
 ----------- ------- --------------- -----------
| NAME      | ORG   | STATE         | HEALTH    |
 ----------- ------- --------------- -----------
| <cluster> | <org> | STATE_ENABLED | HEALTHY   |
 ----------- ------- --------------- -----------
1 rows
```

6. You can then register and run some example workflows through your cluster to ensure that it is working correctly.

```shell
uctl register examples --project=union-health-monitoring --domain=development
uctl validate snacks --project=union-health-monitoring --domain=development
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
| NAME                 | LAUNCH PLAN NAME                  | VERSION  | STARTED AT                     | ELAPSED TIME | RESULT    | ERROR MESSAGE |
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
| alskkhcd6wx5m6cqjlwm | basics.hello_world.hello_world_wf | v0.3.341 | 2025-05-09T18:30:02.968183352Z | 4.452440953s | SUCCEEDED |               |
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
1 rows
```