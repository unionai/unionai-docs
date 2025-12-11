---
title: Installing Flyte
weight: 2
variants: +flyte -serverless -byoc -selfmanaged
---
# Installing Flyte

First, add the Flyte chart repo to Helm:

```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
```

Then download and update a values file:

```bash
curl -sL https://raw.githubusercontent.com/flyteorg/flyte/master/charts/flyte-binary/eks-starter.yaml
```
> Both the [flyte-binary](https://github.com/flyteorg/flyte/tree/master/charts/flyte-binary) and [flyte-core](https://github.com/flyteorg/flyte/tree/master/charts/flyte-core) charts include example YAML values files for different cloud environments.

You can provide your own values file overriding the base config. The minimum information required for each chart is detailed in the following table:

| Required config | `flyte-binary` key |`flyte-core` key | Notes |
|---|---|---|---|
| Database password  | `configuration.database.password`  | `userSettings.dbPassword`  | Default Postgres username: `postgres` |
| Database server  | `configuration.database.host`  |`userSettings.dbHost` (GCP and Azure), `userSettings.rdsHost`(EKS) | Default DB name: `flyteadmin`|
| S3 storage bucket  | `configuration.storage.metadataContainer` / `configuration.storage.userDataContainer`  |`userSettings.bucketName` / `userSettings.rawDataBucketName` | You can use the same bucket for both|

Once adjusted your values file, install the chart:

Example:
```bash
helm install flyte-backend flyteorg/flyte-binary \
    --dry-run --namespace flyte --values eks-starter.yaml
```
When ready to install, remove the `--dry-run` switch.

## Verify the Installation

The base values files provide only the simplest installation of Flyte. The core functionality and scalability of Flyte will be there but not Ingress, authentication or DNS/SSL is configured.

### Port Forward Flyte Service

To verify the installation you can to port forward the Kubernetes service:

Example:
```bash
kubectl -n flyte port-forward service/flyte-binary-http 8088:8088

kubectl -n flyte port-forward service/flyte-binary-grpc 8089:8089
 ```

You should be able to navigate to `http://localhost:8088/console`.

The Flyte server operates on two different ports, one for `HTTP` traffic and the other for `gRPC`, which is why we port forward both.

### Connect to your Flyte instance
- Generate a new configuration file (in case you don't have one already) using `flytectl config init`.

This will produce a file like the following:

```yaml
   admin:
     # For GRPC endpoints you might want to use dns:///flyte.myexample.com
     endpoint: dns:///localhost:8089 #the gRPC endpoint
     authType: Pkce
     insecure: true
   logger:
     show-source: true
     level: 0
```
- Test your connection using:

```bash
flytectl get projects
```
From this point on you can start running workflows!
