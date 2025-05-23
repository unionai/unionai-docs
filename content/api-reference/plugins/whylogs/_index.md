---
title: whylogs
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: whylogs
  title_expanded: Flytekit whylogs Plugin
  name: flytekitplugins-whylogs
  version: 0.0.0+develop
  author: whylabs
  author_email: support@whylabs.ai
  description: Enable the use of whylogs profiles to be used in flyte tasks to get aggregate
    statistics about data.
  url: https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-whylogs
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
  - flytekitplugins.whylogs
  install_requires:
  - flytekit>=1.3.0b2
  - whylogs[viz]>=1.1.16
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  entry_points:
    flytekit.plugins:
    - whylogs=flytekitplugins.whylogs
  folder: flytekit-whylogs
---


whylogs is an open source library for logging any kind of data. With whylogs,
you are able to generate summaries of datasets (called whylogs profiles) which
can be used to:

- Create data constraints to know whether your data looks the way it should
- Quickly visualize key summary statistics about a dataset
- Track changes in a dataset over time

```bash
pip install flytekitplugins-whylogs
```

To generate profiles, you can add a task like the following:

```python
import whylogs as why
from whylogs.core import DatasetProfileView

import pandas as pd

from flytekit import task

@task
def profile(df: pd.DataFrame) -> DatasetProfileView:
    result = why.log(df) # Various overloads for different common data types exist
    profile_view = result.view()
    return profile
```

>**NOTE:** You'll be passing around `DatasetProfileView` from tasks, not `DatasetProfile`.

## Validating Data

A common step in data pipelines is data validation. This can be done in
`whylogs` through the constraint feature. You'll be able to create failure tasks
if the data in the workflow doesn't conform to some configured constraints, like
min/max values on features, data types on features, etc.

```python
from whylogs.core.constraints.factories import greater_than_number, mean_between_range

@task
def validate_data(profile_view: DatasetProfileView):
    builder = ConstraintsBuilder(dataset_profile_view=profile_view)
    builder.add_constraint(greater_than_number(column_name="my_column", number=0.14))
    builder.add_constraint(mean_between_range(column_name="my_other_column", lower=2, upper=3))
    constraint = builder.build()
    valid = constraint.validate()

    if valid is False:
        print(constraint.report())
        raise Exception("Invalid data found")
```

If you want to learn more about whylogs, check out our [example notebooks](https://github.com/whylabs/whylogs/tree/mainline/python/examples).
