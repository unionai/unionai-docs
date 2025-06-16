---
title: DBT
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: DBT
  title_expanded: Flytekit dbt plugin
  name: flytekitplugins-dbt
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: DBT Plugin for Flytekit
  url: https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-dbt
  long_description: "DBT Plugin for Flytekit"
  long_description_content_type: text/markdown
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.dbt
  install_requires:
  - flytekit>=1.3.0b2
  - dbt-core>=1.6.0,<1.8.0
  - networkx>=2.5
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Programming Language :: Python :: 3.12'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  folder: flytekit-dbt
---


Flytekit plugin for performing DBT tasks. Currently it supports  `dbt run` , `dbt test`, `dbt source freshness` tasks.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-dbt
```

_Example coming soon!_

## Contributors

- [Gojek](https://www.gojek.io/)
