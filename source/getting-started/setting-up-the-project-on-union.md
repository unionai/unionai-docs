# Setting up the project on Union

Union provides the Kubernetes cluster on which you will run your Flyte code.
As we mentioned earlier, the tasks that you defined in your Flyte code will each be run in their own pod in the cluster.
To enable this, Union needs to know how to set up those pods.
Since Kubernetes pods are essentially containers, Union needs to know which container image to use to instantiate the task pods.

When we ran your code on the local demo cluster, a predefined image was used, but, in general, you will want to define your own image to run your tasks.
The most important aspect of defining the image is ensuring that it contains all the Python dependencies that your task code requires.

In the `wine-classification` project that you created with `pyflyte init`, the task container is defined by the `Dockerfile`.
We will take a look at this below, but first, we need to set up a couple of things.

## Initialize configuration

The first step is to make sure that your local configuration information is correct.
The configuration information is stored in `~/.uctl/`.
Assuming that this was created using `uctl demo start`, it will contain configuration info pointing to your local demo cluster.

We want to start with a clean slate.
Delete the `~/.uctl/` directory:

```{code-block} shell
$ rm -rf ~/.uctl
```

Now we can initialize the `uctl` configuration to point to your Union instance:

```{code-block} shell
$ uctl config init --host https://<YourOrg>.hosted.unionai.cloud
```

For `<YourOrg>`, substitute the prefix specific to your organization.

This will recreate the `~/.uctl/` directory.
As before, do not forget to set the `FLYTECTL_CONFIG` environment variable in your shell:

```{code-block} shell
export FLYTECTL_CONFIG=~/.uctl/config.yaml
```

:::{admonition} `FLYTECTL_CONFIG` vs `--config`

Using the environment variable `FLYTECTL_CONFIG` usually the most convenient way of using `uctl`.
In this guide, we assume this method is being used.

Alternatively, you can specify the configuration file directly in the command line using the option `-c` or `--config`. For example:

`$ uctl --config ~/.uctl/config.yaml ...`

This method can be useful if you are interacting with multiple separate Union instances each requiring their own configuration (though for most users this is rarely the case).

:::

## Create a new project on Union

Next, we create the project on Union:

```{code-block} shell
$ uctl create project \
      --id "wine-classification" \
      --labels "my-label=wine-classification" \
      --description "Wine classification on Union" \
      --name "Wine classification"
```

This will create the project in Union.
You should see the project appear in your Union console at `https://<company>.<region>.unionai.cloud/console`.
