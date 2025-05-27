---
title: Memory Machine Cloud
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Memory Machine Cloud
  title_expanded: Flytekit Memory Machine Cloud Plugin
  name: flytekitplugins-mmcloud
  version: 0.0.0+develop
  author: Edwin Yu, Helen Zhang
  author_email: helen.zhang@memverge.com
  description: MemVerge Flyte plugin
  long_description: "# Union.ai Docs Builder\n\n**[union.ai/docs](https://union.ai/docs)**\n\
    \nThis repository builds and publishes all Union.ai documentation.\n\nThe site is\
    \ _automatically published_ when the PR targeting `main` branch is merged.\n\nWhat\
    \ do you want to do today?\n\n- [**Developer & Local environment**](DEVELOPER.md).\n\
    \  How to setup your computer.\n\n- [**Authoring Content**](AUTHOR.md).\n  101 of\
    \ how to create and view content\n\n- [**Advanced Content Creation**](SHORTCODES.md).\n\
    \  Advanced techniques and features to generate content, e.g., audio player.\n\n\
    - [**Building API content**](APIS.md).\n  How to automatically generate content\
    \ for APIs, e.g., Python packages.\n\n- [**Redirecting URLS**](REDIRECTS.md).\n\
    \  How to send users to a new page when the content changed its location."
  long_description_content_type: text/markdown
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.mmcloud
  install_requires:
  - flytekit>=1.9.1,<2.0.0
  - kubernetes
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  entry_points:
    flytekit.plugins:
    - mmcloud=flytekitplugins.mmcloud
  folder: flytekit-mmcloud
---


Flyte Agent plugin to allow executing Flyte tasks using MemVerge Memory Machine Cloud.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-mmcloud
```

To get started with MMCloud, refer to the [MMCloud User Guide](https://docs.memverge.com/mmce/current/userguide/olh/index.html).

## Getting Started

This plugin allows executing `PythonFunctionTask` using MMCloud without changing any function code.

[Resource](https://docs.flyte.org/en/latest/user_guide/productionizing/customizing_task_resources.html) (cpu and mem) requests and limits, [container](https://docs.flyte.org/en/latest/user_guide/customizing_dependencies/multiple_images_in_a_workflow.html) images, and [environment](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.task.html) variable specifications are supported.

[ImageSpec](https://docs.flyte.org/en/latest/user_guide/customizing_dependencies/imagespec.html) may be used to define images to run tasks.

### Credentials

The following [secrets](https://docs.flyte.org/en/latest/user_guide/productionizing/secrets.html) are required to be defined for the agent server:
* `mmc_address`: MMCloud OpCenter address
* `mmc_username`: MMCloud OpCenter username
* `mmc_password`: MMCloud OpCenter password

### Defaults

Compute resources:
* If only requests are specified, there are no limits.
* If only limits are specified, the requests are equal to the limits.
* If neither resource requests nor limits are specified, the default requests used for job submission are `cpu="1"` and `mem="1Gi"`, and there are no limits.

### Example

`example.py` workflow example:
```python
import pandas as pd
from flytekit import ImageSpec, Resources, task, workflow
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

from flytekitplugins.mmcloud import MMCloudConfig

image_spec = ImageSpec(packages=["scikit-learn"], registry="docker.io/memverge")


@task
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    return load_wine(as_frame=True).frame


@task(task_config=MMCloudConfig(), container_image=image_spec)  # Task will be submitted as MMCloud job
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Simplify the task from a 3-class to a binary classification problem."""
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))


@task(
    task_config=MMCloudConfig(submit_extra="--migratePolicy [enable=true]"),
    requests=Resources(cpu="1", mem="1Gi"),
    limits=Resources(cpu="2", mem="4Gi"),
    container_image=image_spec,
    environment={"KEY": "value"},
)
def train_model(data: pd.DataFrame, hyperparameters: dict) -> LogisticRegression:
    """Train a model on the wine dataset."""
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(max_iter=3000, **hyperparameters).fit(features, target)


@workflow
def training_workflow(hyperparameters: dict) -> LogisticRegression:
    """Put all of the steps together into a single workflow."""
    data = get_data()
    processed_data = process_data(data=data)
    return train_model(
        data=processed_data,
        hyperparameters=hyperparameters,
    )
```

### Agent Image

Install `flytekitplugins-mmcloud` in the agent image.

A `float` binary (obtainable via the OpCenter) is required. Copy it to the agent image `PATH`.

Sample `Dockerfile` for building an agent image:
```dockerfile
FROM python:3.11-slim-bookworm

WORKDIR /root
ENV PYTHONPATH /root

# flytekit will autoload the agent if package is installed.
RUN pip install flytekitplugins-mmcloud
COPY float /usr/local/bin/float

CMD pyflyte serve agent --port 8000
```
