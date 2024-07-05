# Running your code

Union let's you iterate on your workflow code easily and naturally with commands suitable for deploying and running code at different stages of the development cycle:

{@# TODO: Link to the unionai commands below to the unionai CLI reference section #@}

1. `unionai run`: For deploying and running a single script immediately in your local Python environment.
2. `unionai run --remote`: For deploying and running a single script immediately in the cloud on Union.
3. `unionai register`: For deploying multiple scripts to Union and running them from the Web interface.
{@@ if byoc @@}
4. `unionai package` and `uctl register`: For deploying workflows to production and for scripting within a CI/CD pipeline.

```{note}
In some cases you may wish to to have the option of testing your code in a local cluster before deploying it to Union.
Setting up a cluster in your local machine is supported by Union.
This step would correspond to using the commands 2, 3, or 4 but targeting your local cluster instead of Union.
For more details on this option see [Running in a local cluster](running-in-a-local-cluster).
```
{@@ endif @@}

## Running a script in local Python with `unionai run`

During the development cycle you will want to run a specific workflow or task in your local Python environment to test it.
To quickly try out the code locally use `unionai run`:

```{code-block} shell
$ unionai run workflows/example.py wf --name 'Albert'
```

Here you are invoking `unionai run` and passing the name of the Python file and the name of the workflow within that file that you want to run.
In addition, you are passing the named parameter `name` and its value.

You should see the following output:

```{code-block} shell
Hello, Albert!
```

## Running a script on Union with `unionai run --remote`

[DONE TO HERE]()

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

## Deploying your code to Union with `unionai register`

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

## Deploying your code to production with `unionai package` and `uctl register`

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
