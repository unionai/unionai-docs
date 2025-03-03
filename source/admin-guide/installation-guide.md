# Installation guide

In the BYOK model, the customer deploys the data plane themselves. Union data plane runs on a standard Kubernetes cluster.

Union data plane is distributed as standard Helm Charts, with overridable values.

```{admonition} Other distribution mechanisms
Although Helm Chart is a popular and well-established standard Kubernetes distribution mechanism,
our Engineering team is investigating other installation and distribution mechanisms, such as Terraform,
to more easily integrate with the customers’ deployment systems.
```

## BYOK data plane

### Assumptions

- You have a union organization that has already been created.
- You have a running Kubernetes cluster and object storage provided by a vendor or an S3 compatible platform (such as [Minio](https://min.io).
- You have reviewed the [Cluster recommendations](./cluster-recommendations.md).

### Installation via Helm

- [Install Helm 3](https://helm.sh/docs/intro/install/)
- Install the [union](https://docs.union.ai/byoc/api-reference/union-cli) and [uctl](https://docs.union.ai/byoc/api-reference/uctl-cli/) command line tools.
- Install the Union helm charts.
```
helm repo add unionai https://unionai.github.io/helm-charts/
helm repo update
```

- Generate a new client and client secret to communicate with your Union control plane by creating a new `AppSpec` configuration and using the `create app` command from `uctl`.
```shell
cat > dataplane-operator.yaml << EOF
clientId: dataplane-operator
clientName: dataplane-operator
grantTypes:
- AUTHORIZATION_CODE
- CLIENT_CREDENTIALS
redirectUris:
- http://localhost:8080/authorization-code/callback
responseTypes:
- CODE
tokenEndpointAuthMethod: CLIENT_SECRET_BASIC
EOF
uctl config init --host=<cloud.host>
uctl create app --appSpecFile dataplane-operator.yaml
```
- The output will emit the ID, name, and a secret that will be used by the union services to communicate with your control plane.

```shell
Initializing app config from file dataplane-operator.yaml
 -------------------- -------------------- ------------------------------------------------------------------ ---------
| CLIENT ID          | CLIENT NAME        | SECRET                                                           | CREATED |
 -------------------- -------------------- ------------------------------------------------------------------ ---------
| dataplane-operator | dataplane-operator | secretxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx |         |
 -------------------- -------------------- ------------------------------------------------------------------ ---------
1 rows
```
- Save the secret that is displayed.  Union does not store the credentials and it cannot be retrieved later.
- Optionally configure any values that are relevant to your installation.  A full list of values can be found here: [charts/dataplane/README.md](charts/dataplane/README.md).  At a minimum you will need to provide the following values in a file or as an argument on the command line:
  - `host`: The admin host used to communicate with your Union.ai organization's control plane.  You will have been provided this value when union has created your control plane.
  - `clusterName`: An arbitrary and unique identifier for your cluster.
  - `orgName`: The name of your Union.ai organization.
  - `provider`: The cloud provider your cluster is running in.  Acceptable values include `aws`, `gcp`, `azure`, `oci`, and `metal` (for self-managed or on-prem clusters).
  - `storage`: Several storage parameters exist for configuration.  By default the `authType` of `accesskey` is used and requires `storage.accessKey` and `storage.secretKey` to be set.  A full list of storage parameters can be found here: [charts/dataplane/README.md](charts/dataplane/README.md)
  - `secrets`: You have the option of creating the admin client secrets by setting `secrets.admin.create` to `true` and providing both the `clientId` and the `clientSecret` either in the values file or as command line arguments.
  - Optionally configure the resource `limits` and `requests` for the different services.  By default these will be set minimally, will vary depending on usage, and follow the kubernetes `ResourceRequirements` specification.
    - `clusterresourcesync.resources`
    - `flytepropeller.resources`
    - `flytepropellerwebhook.resources`
    - `operator.resources`
    - `proxy.resources`
- Create a values file.
```yaml
# union-dataplane.yaml
host: <host>
clusterName: <cluster_name>
orgName: <org>
provider: <provider>

secrets:
  admin:
    create: true
    clientId: <client_id>
    clientSecret: "<client_secret>"
storage:
  endpoint: <endpoint>
  bucketName: union-dp-bucket
  fastRegistrationBucketName: union-dp-bucket
  accessKey: "<access_key>"
  secretKey: "<secret_key>"
  region: "<region>" 

config:
  logger:
    level: 4
```
- Install the data plane CRDS and data plane.
```shell
helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds
helm upgrade --install unionai-dataplane unionai/dataplane \
    --create-namespace \
    --namespace union \
    --values union-dataplane.yaml
```

Once deployed you can check to see if the cluster has been successfully registered to the control plane by running the `get cluster` command in `uctl`

```shell
uctl get cluster
 ----------- ------- --------------- -----------
| NAME      | ORG   | STATE         | HEALTH    |
 ----------- ------- --------------- -----------
| <cluster> | <org> | STATE_ENABLED | HEALTHY   |
 ----------- ------- --------------- -----------
1 rows
```
