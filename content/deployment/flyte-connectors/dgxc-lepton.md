---
title: DGXC Lepton connector
weight: 19
variants: +flyte -serverless -byoc -selfmanaged
---

# DGXC Lepton Connector

This guide provides an overview of how to set up the DGXC Lepton connector in your Flyte deployment. The DGXC Lepton connector enables seamless deployment and management of AI inference endpoints on the Lepton AI platform directly from your Flyte workflows.

## Prerequisites

Before setting up the DGXC Lepton connector, ensure you have:

1. A Lepton AI account with appropriate access permissions
2. Lepton API tokens configured for your deployment environment
3. Access to a Kubernetes cluster with Flyte deployed

## Specify connector configuration

### flyte-binary

Edit the relevant YAML file to specify the connector.

```bash
kubectl edit configmap flyte-sandbox-config -n flyte
```

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - k8s-array
      - connector-service
    default-for-task-types:
      - container: container
      - container_array: k8s-array
      - lepton_endpoint_deployment_task: connector-service
      - lepton_endpoint_deletion_task: connector-service
```

### flyte-core

Create a file named `values-override.yaml` and add the following configuration to it:

```yaml
configmap:
  enabled_plugins:
    tasks:
      task-plugins:
        enabled-plugins:
          - container
          - sidecar
          - k8s-array
          - connector-service
        default-for-task-types:
          container: container
          sidecar: sidecar
          container_array: k8s-array
          lepton_endpoint_deployment_task: connector-service
          lepton_endpoint_deletion_task: connector-service
```

## Configure DGXC Lepton connector service

Create a connector configuration file to specify the DGXC Lepton connector settings:

```yaml
# dgxc-lepton-connector-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: dgxc-lepton-connector-config
  namespace: flyte
data:
  config.yaml: |
    connectors:
      lepton_endpoint_deployment_task:
        endpoint: http://dgxc-lepton-connector:8000
        insecure: true
        timeout: 1800s
      lepton_endpoint_deletion_task:
        endpoint: http://dgxc-lepton-connector:8000
        insecure: true
        timeout: 600s
```

Apply the configuration:

```bash
kubectl apply -f dgxc-lepton-connector-config.yaml
```

## Deploy DGXC Lepton connector service

Deploy the DGXC Lepton connector service to your Kubernetes cluster:

```yaml
# dgxc-lepton-connector-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dgxc-lepton-connector
  namespace: flyte
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dgxc-lepton-connector
  template:
    metadata:
      labels:
        app: dgxc-lepton-connector
    spec:
      containers:
      - name: dgxc-lepton-connector
        image: your-registry/dgxc-lepton-connector:latest
        ports:
        - containerPort: 8000
        env:
        - name: LEPTON_WORKSPACE_ID
          valueFrom:
            secretKeyRef:
              key: workspace_id
              name: lepton-secrets
        - name: LEPTON_TOKEN
          valueFrom:
            secretKeyRef:
              key: token
              name: lepton-secrets
        - name: LEPTON_WORKSPACE_ORIGIN_URL
          valueFrom:
            secretKeyRef:
              key: origin_url
              name: lepton-secrets
        - name: DEBUG_MODE
          value: "true"
        - name: ROOT_LOG_LEVEL
          value: "WARNING"
        resources:
          requests:
            memory: "256Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: dgxc-lepton-connector
  namespace: flyte
spec:
  selector:
    app: dgxc-lepton-connector
  ports:
  - port: 8000
    targetPort: 8000
  type: ClusterIP
```

Apply the deployment:

```bash
kubectl apply -f dgxc-lepton-connector-deployment.yaml
```

## Configure DGXC Lepton API credentials

The DGXC Lepton connector requires specific credentials to authenticate with the Lepton AI platform. These credentials must be configured as Kubernetes secrets.

### Required secrets

The connector requires the following secrets to be configured:

- `origin_url`: The base URL for the DGXC Lepton gateway (Base64 encoded)
- `token`: Your DGXC Lepton API token (Base64 encoded)  
- `workspace_id`: Your DGXC Lepton workspace identifier (Base64 encoded)

### Setup instructions

1. Create the DGXC Lepton secrets:

    ```bash
    # Create the lepton-secrets with all required credentials
    kubectl create secret generic lepton-secrets -n flyte \
      --from-literal=origin_url="https://gateway.dgxc-lepton.nvidia.com" \
      --from-literal=token="<YOUR_LEPTON_API_TOKEN>" \
      --from-literal=workspace_id="<YOUR_WORKSPACE_ID>"
    ```

    > [!NOTE]
    > Replace `<YOUR_LEPTON_API_TOKEN>` with your actual DGXC Lepton API token and `<YOUR_WORKSPACE_ID>` with your workspace identifier.

    Alternatively, you can create the secret from a YAML file:

    ```yaml
    # lepton-secrets.yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: lepton-secrets
      namespace: flyte
    type: Opaque
    data:
      origin_url: aHR0cHM6Ly9nYXRld2F5LmRneGMtbGVwdG9uLm52aWRpYS5jb20=  # Base64 encoded URL
      token: <BASE64_ENCODED_TOKEN>  # Your Base64 encoded API token
      workspace_id: <BASE64_ENCODED_WORKSPACE_ID>  # Your Base64 encoded workspace ID
    ```

    ```bash
    kubectl apply -f lepton-secrets.yaml
    ```

2. Install `flyteconnector` pod using Helm (if not already installed):

    ```bash
    helm repo add flyteorg https://flyteorg.github.io/flyte
    helm install flyteconnector flyteorg/flyteconnector --namespace flyte
    ```

3. Restart the deployment:

    ```bash
    kubectl rollout restart deployment flyteconnector -n flyte
    kubectl rollout restart deployment dgxc-lepton-connector -n flyte
    ```

## Upgrade the Flyte Helm release

### flyte-binary

```bash
helm upgrade <RELEASE_NAME> flyteorg/flyte-binary -n <YOUR_NAMESPACE> --values <YOUR_YAML_FILE>
```

Replace `<RELEASE_NAME>` with the name of your release (e.g., `flyte-backend`),
`<YOUR_NAMESPACE>` with the name of your namespace (e.g., `flyte`),
and `<YOUR_YAML_FILE>` with the name of your YAML file.

### flyte-core

```bash
helm upgrade <RELEASE_NAME> flyte/flyte-core -n <YOUR_NAMESPACE> --values values-override.yaml
```

Replace `<RELEASE_NAME>` with the name of your release (e.g., `flyte`)
and `<YOUR_NAMESPACE>` with the name of your namespace (e.g., `flyte`).

## Verify the setup

After completing the setup, verify that the DGXC Lepton connector is working correctly:

1. Check that the connector pods are running:

    ```bash
    kubectl get pods -n flyte | grep dgxc-lepton-connector
    ```

2. Check the connector logs for any errors:

    ```bash
    kubectl logs -n flyte deployment/dgxc-lepton-connector
    ```

3. Test the connector by running a simple DGXC Lepton workflow in your Flyte cluster.

## Supported task types

The DGXC Lepton connector supports the following task types:

- `lepton_endpoint_deployment_task`: Deploy AI inference endpoints to the Lepton platform
- `lepton_endpoint_deletion_task`: Delete existing endpoints from the Lepton platform

## Configuration options

The DGXC Lepton connector supports various configuration options including:

- **Resource shapes**: Specify CPU, GPU, and memory requirements
- **Scaling policies**: Configure auto-scaling based on traffic, GPU utilization, or queries per minute
- **Environment variables**: Set custom environment variables and secrets
- **Mount configurations**: Configure shared storage mounts for model caches and datasets
- **Engine configurations**: Support for VLLM, SGLang, NIM, and custom container deployments

For detailed usage examples and API reference, refer to the DGXC Lepton plugin documentation in your Flyte deployment.
