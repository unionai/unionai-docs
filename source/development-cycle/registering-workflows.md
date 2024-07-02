# Registering workflows

The numerous ways in which workflows can be deployed and run can be somewhat confusing. Here is a full overview.

## Local Python

```{code-block} shell
$ unionai run my_file.py my_workflow
```

* Task code runs in your local Python environment.
* Supports any Python dependencies you wish, since you have full control of your local environment.
* Does not support features that require running in a cluster (S3, plugins, etc.).
* Single workflow runs immediately.
* Useful for quick testing during the development cycle.

## Local cluster with default image

```{code-block} shell
$ unionai run --remote my_file.py my_workflow
```

_Where `unionai` is configured to point to the local cluster started with `uctl demo start`._

* Task code runs in the environment of the default image in your local cluster.
* Python code is dynamically overlaid into the container at runtime.
* Only supports Python code whose dependencies are installed in the default image (see here).
* Includes a local S3.
* Supports some plugins but not all.
* Single workflow runs immediately.
* Workflow is registered to a default project.
* Useful for demos.

## Local cluster with custom image

```{code-block} shell
$ unionai run --remote \
              --image my_cr.io/my_org/my_image:latest \
              my_file.py \
              my_workflow
```

_Where `unionai` is configured to point to the local cluster started with `uctl demo start`._

* Task code runs in the environment of your custom image (`my_cr.io/my_org/my_image:latest`) in your local cluster.
* Python code is dynamically overlaid into the container at runtime
* Supports any Python dependencies you wish, since you have full control of the image.
* Includes a local S3.
* Supports some plugins but not all.
* Single workflow runs immediately.
* Workflow is registered to a default project.
* Useful for advanced testing during the development cycle.

## Remote cluster with custom image

```{code-block} shell
$ unionai run --remote \
              --image my_cr.io/my_org/my_image:latest \
              my_file.py \
              my_workflow
```

_Where `unionai` is configured to point to your Union data plane._

* Task code runs in the environment of your custom image (`my_cr.io/my_org/my_image:latest`) in Union.
* Python code is dynamically overlaid into the container at runtime.
* Supports any Python dependencies you wish, since you have full control of the image.
* Full support for all features (S3, all plugins, etc.).
* Single workflow runs immediately on invocation of `unionai` command.
* Workflow is registered to a default project.
* Useful for advanced testing during the development cycle.

## Remote cluster using fast registration

```{code-block} shell
$ unionai register workflows \
       --project my_project \
       --image my_cr.io/my_org/my_image:latest
```

_Where `unionai` is configured to point to your Union data plane._

* Task code runs in the environment of your custom image (`my_cr.io/my_org/my_image:latest`) in Union.
* Python code is dynamically overlaid into the container at runtime.
* Supports any Python dependencies you wish, since you have full control of the image.
* Includes full support for all features (S3, all plugins, etc.).
* Multiple workflows are registered but do not run immediately.
* Workflows are registered to the specified project.
* Workflows are run from the Web interface.
* Useful for advanced testing during the development cycle (possible but not recommended for production deployment).

{@@ if byoc @@}

## Remote cluster using standard registration

First, package your workflows:

```{code-block} shell
$ unionai --pkgs workflows \
          package \
          --image my_cr.io/my_org/my_image:latest
```

Then, register them:

```{code-block} shell
$ uctl register files \
       --project onboarding \
       --domain development \
       --archive flyte-package.tgz \
       --version 1.0
```

_Where `unionai` and `uctl` are configured to point to your Union data plane._

* Task code runs in the environment of your custom image (`my_cr.io/my_org/my_image:latest`) in Union.
* Python code is built into the image and not dynamically overlaid into the container, thus preserving immutability.
* Supports any Python dependencies you wish, since you have full control of the image.
* Includes full support for all features (S3, all plugins, etc.).
* Multiple workflows are registered but do not run immediately.
* Workflows are registered to the specified project.
* Workflows are run from the Web interface.
* Recommended for production deployment.

{@@ endif @@}
