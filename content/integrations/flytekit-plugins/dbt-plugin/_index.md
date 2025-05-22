---
title: DBT
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
sidebar_expanded: false
---

# DBT

[dbt](https://www.getdbt.com/) is one of the widely-used data transformation
tools for working with data directly in a data warehouse. It's optimized for
analytics use cases and can be used for business intelligence, operational
analytics, and even machine learning.

The Flytekit `dbt` plugin is a Python module that provides an easy way to
invoke basic `dbt` CLI commands from within a Flyte task. The plugin supports
the commands [dbt run](https://docs.getdbt.com/reference/commands/run),
[dbt test](https://docs.getdbt.com/reference/commands/test), and
[dbt source freshness](https://docs.getdbt.com/reference/commands/source).

## Prerequisities

To use the `dbt` plugin you'll need to install the `flytekitplugins-dbt`
plugin.

> [!NOTE]
> See [the PyPi page here](https://pypi.org/project/flytekitplugins-dbt/).

```shell
$ pip install flytekitplugins-dbt
```

Then install dbt itself. You will have to install `dbt-core` as well as
the correct adapter for the database that you are accessing.

For example, if you are using a Postgres database you would do:



This will install `dbt-core` and `dbt-postgres`, but not any of the other
adapters, `dbt-redshift`, `dbt-snowflake`, or `dbt-bigquery`. See
[the official installation page](https://docs.getdbt.com/docs/get-started/pip-install)
for details.

## Running the Example

We use a Postgres database installed on the cluster and an example project from
dbt, called [jaffle-shop](https://github.com/dbt-labs/jaffle_shop).
To run the example on your local machine, do the following.

> [!IMPORTANT]
> The example below is not designed to run directly in your local
> python environment. It must be run in a Kubernetes cluster, either locally on
> your machine using the `flytectl demo start` command or on a cloud cluster.

Start up the demo cluster on your local machine:

```shell
$ flytectl demo start
```

Pull the pre-built image for this example:

```shell
$ docker pull ghcr.io/flyteorg/flytecookbook:dbt_example-latest
```

This image is built using the following `Dockerfile` and contains:

- The `flytekitplugins-dbt` and `dbt-postgres` Python dependencies.
- The `jaffle-shop` example.
- A postgres database.

This Dockerfile can be found in the ``flytesnacks/examples`` directory under
the filepath listed in the code block title below.

```dockerfile
FROM python:3.8-slim-buster

WORKDIR /root
ENV VENV /opt/venv
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONPATH /root

RUN apt-get update && apt-get install -y build-essential git postgresql-client libpq-dev

# Install the AWS cli separately to prevent issues with boto being written over
RUN pip3 install awscli

ENV VENV /opt/venv
# Virtual environment
RUN python3 -m venv ${VENV}
ENV PATH="${VENV}/bin:$PATH"

# Install Python dependencies
COPY requirements.in /root/
RUN pip install -r /root/requirements.in
# psycopg2-binary is a dependency of the dbt-postgres adapter, but that doesn't work on mac M1s.
# As per https://github.com/psycopg/psycopg2/issues/1360, we install psycopg to circumvent this.
RUN pip uninstall -y psycopg2-binary && pip install psycopg2

# Copy the actual code
COPY . /root/

# Copy dbt-specific files
COPY profiles.yml /root/dbt-profiles/
RUN git clone https://github.com/dbt-labs/jaffle_shop.git

# This tag is supplied by the build script and will be used to determine the version
# when registering tasks, workflows, and launch plans
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag

ENV FLYTE_SDK_LOGGING_LEVEL 10
```

To run this example, copy the code in the **dbt example** below into a file
called `dbt_example.py`, then run it on your local container using the
provided image:

```shell
$ pyflyte run --remote \
       --image ghcr.io/flyteorg/flytecookbook:dbt_example-latest \
       dbt_plugin/dbt_example.py wf
```

Alternatively, you can clone the `flytesnacks` repo and run the example directly:

```shell
$ git clone https://github.com/flyteorg/flytesnacks
$ cd flytesnacks/examples/dbt_example
$ pyflyte run --remote \
          --image ghcr.io/flyteorg/flytecookbook:dbt_example-latest \
          dbt_plugin/dbt_example.py wf
```