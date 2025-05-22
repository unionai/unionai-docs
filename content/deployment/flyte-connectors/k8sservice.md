---
title: K8s Data Service connector
weight: 12
variants: +flyte -serverless -byoc -selfmanaged
---

## Kubernetes (K8s) Data Service Connector

The Kubernetes (K8s) Data Service Connector enables machine learning (ML) users to efficiently handle non-training tasks—such as data loading, caching, and processing—concurrently with training jobs in Kubernetes clusters. This capability is particularly valuable in deep learning applications, such as those in Graph Neural Networks (GNNs).

This guide offers a comprehensive overview of setting up the K8s Data Service Connector within your Flyte deployment.

### Spin up a cluster

#### Flyte binary

You can spin up a demo cluster using the following command:

```bash
flytectl demo start
```

Or install Flyte using the [flyte-binary helm chart](deployment-deployment-cloud-simple).

#### Flyte core

If you've installed Flyte using the [flyte-core helm chart](https://github.com/flyteorg/flyte/tree/master/charts/flyte-core), please ensure:

- You have the correct kubeconfig and have selected the correct Kubernetes context.
- You have configured the correct flytectl settings in `~/.flyte/config.yaml`.

> [!NOTE]: Add the Flyte chart repo to Helm if you're installing via the Helm charts.
>
> ```bash
> helm repo add flyteorg https://flyteorg.github.io/flyte
> ```

### Specify connector configuration

Enable the K8s service connector by adding the following config to the relevant YAML file(s):

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - connector-service
    default-for-task-types:
      - dataservicetask: connector-service
```

```yaml
plugins:
  connector-service:
    connectors:
      k8sservice-connector:
        endpoint: <CONNECTOR_ENDPOINT>
        insecure: true
    connectorForTaskTypes:
    - dataservicetask: k8sservice-connector
    - sensor: k8sservice-connector
```

Substitute `<CONNECTOR_ENDPOINT>` with the endpoint of your MMCloud connector.

### Setup the RBAC

The K8s Data Service Connector will create a StatefulSet and expose the Service endpoint for the StatefulSet pods.
RBAC needs
to be set up to allow the K8s Data Service Connector to perform CRUD operations on the StatefulSet and Service.

#### Role: `flyte-flyteconnectorrole`

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: flyte-flyteconnector-role
  namespace: flyte
  labels:
    app.kubernetes.io/name: flyteconnector
    app.kubernetes.io/instance: flyte
rules:
- apiGroups:
    - apps
  resources:
    - statefulsets
    - statefulsets/status
    - statefulsets/scale
    - statefulsets/finalizers
  verbs:
    - get
    - list
    - watch
    - create
    - update
    - delete
    - patch
- apiGroups:
  - ""
  resources:
  - pods
  - configmaps
  - serviceaccounts
  - secrets
  - pods/exec
  - pods/log
  - pods/status
  - services
  verbs:
  - '*'
```

#### RoleBinding: `flyte-flyteconnector-rolebinding`

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: flyte-flyteconnector-rolebinding
  namespace: flyte
  labels:
    app.kubernetes.io/name: flyteconnector
    app.kubernetes.io/instance: flyte
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: flyte-flyteconnector-role
subjects:
- kind: ServiceAccount
  name: flyteconnector
  namespace: flyte
```

### Upgrade the deployment

#### Flyte binary

##### Demo cluster

```bash
kubectl rollout restart deployment flyte-sandbox -n flyte
```

##### Helm chart

```bash
helm upgrade <RELEASE_NAME> flyteorg/flyte-binary -n <YOUR_NAMESPACE> --values <YOUR_YAML_FILE>
```

Replace `<RELEASE_NAME>` with the name of your release (e.g., `flyte-backend`), `<YOUR_NAMESPACE>` with the name of your namespace (e.g., `flyte`), and `<YOUR_YAML_FILE>` with the name of your YAML file.

#### Flyte core

```bash
helm upgrade <RELEASE_NAME> flyte/flyte-core -n <YOUR_NAMESPACE> --values values-override.yaml
```

Replace `<RELEASE_NAME>` with the name of your release (e.g., `flyte`) and `<YOUR_NAMESPACE>` with the name of your namespace (e.g., `flyte`).

Wait for the upgrade to complete. You can check the status of the deployment pods by running the following command:

```bash
kubectl get pods -n flyte
```