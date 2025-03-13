---
title: Running in a local cluster
weight: 16
variants: +flyte +serverless +byoc +byok
---

# Running in a local cluster

## Running in a local Kubernetes cluster

Ultimately you will be running your workflows in a Kubernetes cluster in Union. But it can be handy to try out a workflow in a cluster on your local machine. Flyte enables this.

First, ensure that you have [Docker](https://www.docker.com/products/docker-desktop/) (or a similar OCI-compliant container engine) installed locally and that _the daemon is running_.

Then start the demo cluster using `uctl`:

```shell
$ uctl demo start
```

### Configuration

When `uctl` starts the cluster in your local container engine it also writes configuration information to the directory `~/.uctl/`.

Most importantly, it creates the file `~/.uctl/config-sandbox.yaml`. This file holds (among other things) the location of the Kubernetes cluster to which we will be deploying the workflow:

```yaml
admin:
  endpoint: localhost:30080
  authType: Pkce
  insecure: true
console:
  endpoint: http://localhost:30080
logger:
  show-source: true
  level: 0
```

Right now this file indicates that the target cluster is your local Docker instance (`localhost:30080`), but later we will change it to point to your Union cluster.

Later invocations of `uctl` or `union` will need to know the location of the target cluster. This can be provided in two ways:

1. Explicitly passing the location of the config file on the command line
   * `uctl --config ~/.uctl/config-sandbox.yaml <command>`
   * `union --config ~/.uctl/config-sandbox.yaml <command>`
2. Setting the environment variable `FLYTECTL_CONFIG`to the location of the config file:
   * `export FLYTECTL_CONFIG=~/.uctl/config-sandbox.yaml`

{{< note >}}
In this guide, we assume that you have set the`FLYTECTL_CONFIG` environment variable in your shell to the location of the configuration file.
{{< /note >}}

### Start the workflow

Now you can run your workflow in the local cluster simply by adding the `--remote` flag to your `union` command:

```shell
[~/wine-classification]:wine-classification
$ union run --remote \
          workflows/example.py \
          training_workflow \
          --hyperparameters '{"C": 0.1}'
```

The output supplies a URL to your workflow execution in the Flyte console. It should look something like this:

```shell
Go to http://localhost:30080/console/projects/flytesnacks/domains/development/executions/f6ac3844ff43b4be69a9 to see execution in the console.
```

### Inspect the results

Navigate to the URL produced by `union run` to see your workflow in the Union UI.

## Local cluster with default image

```shell
$ union run --remote my_file.py my_workflow
```

_Where `union` is configured to point to the local cluster started with `uctl demo start`._

* Task code runs in the environment of the default image in your local cluster.
* Python code is dynamically overlaid into the container at runtime.
* Only supports Python code whose dependencies are installed in the default image (see here).
* Includes a local S3.
* Supports some plugins but not all.
* Single workflow runs immediately.
* Workflow is registered to a default project.
* Useful for demos.

## Local cluster with custom image

```shell
$ union run --remote \
              --image my_cr.io/my_org/my_image:latest \
              my_file.py \
              my_workflow
```

_Where `union` is configured to point to the local cluster started with `uctl demo start`._

* Task code runs in the environment of your custom image (`my_cr.io/my_org/my_image:latest`) in your local cluster.
* Python code is dynamically overlaid into the container at runtime
* Supports any Python dependencies you wish, since you have full control of the image.
* Includes a local S3.
* Supports some plugins but not all.
* Single workflow runs immediately.
* Workflow is registered to a default project.
* Useful for advanced testing during the development cycle.