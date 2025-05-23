---
title: Troubeshooting
weight: 5
variants: +flyte -serverless -byoc -selfmanaged
---

# Troubleshooting guide

The content in this section will help Flyte users isolate the most probable causes for some of the common issues that could arise while getting started with the project.

Before getting started, collect the following information from the underlying infrastructure:

- Capture the `Status` column from the output of:

```bash
kubectl describe pod <PodName> -n <namespace>
```

Where `<PodName>` will typically correspond to the node execution string that you can find in the UI.

- Pay close attention to the `Events` section in the output.
- Also, collect the logs from the Pod:

```bash
kubectl logs pods -n <namespace>
```

Where `<namespace>` will typically correspond to the Flyte `<project>-<domain>`, e.g., `flytesnacks-development`.

Depending on the contents of the logs or the `Events`, you can try different things:

## Debugging Common Execution Errors

### Error: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

This error will show if you are not running Docker with the native Docker engine in a Linux machine. Most probably you are running Docker via Docker Desktop.

- If you are using Docker Desktop in macOS, run:

```bash
sudo ln -s ~/Library/Containers/com.docker.docker/Data/docker.raw.sock /var/run/docker.sock
```

- If you are using Docker Desktop in Linux, run:

```bash
sudo ln -s ~$USER/.docker/desktop/docker.sock /var/run/docker.sock
```

- If you are using another tool to run Docker, you need to make sure that `/var/run/docker.sock` is linked to the correct socket file.

  For example, if you are using Rancher Desktop on Linux, run:

```bash
sudo ln -s ~$USER/.rd/docker.sock /var/run/docker.sock
```

### message: '0/1 nodes are available: 1 Insufficient cpu. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod.'

This issue is more common on macOS devices. Make sure that your Docker daemon has allocated a minimum of 4 CPU cores and 3GB of RAM.

### terminated with exit code (137). Reason [OOMKilled]

- For single binary environment deployed with Helm chart, make sure you are using [the most recent charts](https://github.com/flyteorg/flyte/tree/master/charts).

- For EKS deployments, you can adjust resource limits and requests in the `inline` section of the `eks-production.yaml` file. Example:

```yaml
inline:
  task_resources:
    defaults:
      cpu: 100m
      memory: 100Mi
      storage: 100Mi
    limits:
      memory: 1Gi
```

- Also, the default container resource limits can be overridden from the task itself:

```python
from flytekit import Resources, task

@task(limits=Resources(mem="256Mi"))
def your_task(...):
    ...
```

### Error: ImagePullBackOff

- If your environment requires the use of a network proxy, use the `--env` option when starting the sandbox and pass the proxy configuration:

```bash
flytectl demo start --env HTTP_PROXY=<your-proxy-IP>
```

- If you're building a custom Docker image, make sure to use a tag other than `latest`. Otherwise, the Kubernetes default pull policy will be changed from `IfNotPresent` to `Always`, forcing an image pull with every Pod deployment.

## Issues Running Workloads

### OPENSSL_internal:WRONG_VERSION_NUMBER

- For `flyte-binary`: make sure that the endpoint name you have set in your `config.yaml` file is included in the DNS names of the SSL certificate installed (be it self-signed or issued by a Certificate Authority).
- For `sandbox`: verify the `FLYTECTL_CONFIG` environment variable has the correct value by running:

```bash
export FLYTECTL_CONFIG=~/.flyte/config-sandbox.yaml
```

### ModuleNotFoundError

- If you're using a custom container image and using Docker, make sure your `Dockerfile` is located at the same level of the `flyte` directory and that there is an empty `__init__.py` file in your project's folder:

```plaintext
myflyteapp
├── Dockerfile
├── docker_build_and_tag.sh
├── flyte
│   ├── __init__.py
│   └── workflows
│       ├── __init__.py
│       └── example.py
└── requirements.txt
```

### An error occurred (AccessDenied) when calling the PutObject operation in an EKS deployment

- Make sure that the Kubernetes service account Flyte is using has the annotation that refers to the IAM Role connected to it:

```bash
kubectl describe sa <my-flyte-sa> -n <flyte-namespace>
```

Example output:

```plaintext
Name:                <my-flyte-sa>
Namespace:           flyte
Labels:              app.kubernetes.io/managed-by=eksctl
Annotations:         eks.amazonaws.com/role-arn: arn:aws:iam::<aws-account-id>:role/flyte-system-role
...
```

- Otherwise, obtain your IAM role's ARN and manually annotate the service account:

```bash
kubectl annotate serviceaccount -n <flyte-namespace> eks.amazonaws.com/role-arn=arn:aws:iam::xxxx:role/<flyte-iam-role>
```

- Refer to this community-maintained [guide](https://github.com/davidmirror-ops/flyte-the-hard-way/blob/main/docs/03-roles-service-accounts.md) for further information about Flyte deployment on EKS.

### FlyteScopedUserException: 'JavaPackage' object is not callable when running a Spark task

Please add `spark` to the list of `enabled-plugins` in the config YAML file. For example:

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - K8S-ARRAY
      - spark
    default-for-task-types:
      - container: container
      - container_array: K8S-ARRAY
```

### authentication handshake failed: x509: "Kubernetes Ingress Controller Fake Certificate" certificate is not trusted when deploying flyte-core to your own Kubernetes cluster

This issue is caused by TLS being disabled in your Kubernetes cluster. You can resolve the problem by following these steps:

- Enable `tls` in the `values.yaml` ingress configuration of flyte-core in order to expose gRPC service at port 443:

```yaml
ingress:
  host: example.com
  separateGrpcIngress: true
  separateGrpcIngressAnnotations:
    ingress.kubernetes.io/backend-protocol: "grpc"
  annotations:
    ingress.kubernetes.io/app-root: "/console"
    ingress.kubernetes.io/default-backend-redirect: "/console"
    kubernetes.io/ingress.class: haproxy
  tls:
    enabled: true
```

- Disable `insecure` in your `flytectl` client `config.yaml`:

```yaml
admin:
  endpoint: dns:///example.com
  authType: Pkce
  insecure: false
  insecureSkipVerify: true
```
