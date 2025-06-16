---
title: Snowflake
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Snowflake
  title_expanded: Flytekit Snowflake Plugin
  name: flytekitplugins-snowflake
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the Snowflake plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.snowflake
  install_requires:
  - flytekit>1.13.1
  - snowflake-connector-python>=3.11.0
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
    - snowflake=flytekitplugins.snowflake
  folder: flytekit-snowflake
---


Snowflake enables us to build data-intensive applications without operational burden. Flyte backend can be connected with the Snowflake service. Once enabled, it can allow you to query a Snowflake service.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-snowflake
```

To configure Snowflake in the Flyte deployment's backend, follow the [configuration guide](https://docs.flyte.org/en/latest/deployment/plugins/webapi/snowflake.html#deployment-plugin-setup-webapi-snowflake).

An [example](https://docs.flyte.org/en/latest/flytesnacks/examples/snowflake_plugin/index.html) showcasing Snowflake service can be found in the documentation.
