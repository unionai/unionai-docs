---
title: Bigquery
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Bigquery
  title_expanded: Flytekit BigQuery Plugin
  name: flytekitplugins-bigquery
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the Bigquery plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.bigquery
  install_requires:
  - flytekit>1.10.7
  - google-cloud-bigquery>=3.21.0
  - google-cloud-bigquery-storage>=2.25.0
  - flyteidl>1.10.7
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
    - bigquery=flytekitplugins.bigquery
  folder: flytekit-bigquery
---


BigQuery enables us to build data-intensive applications without operational burden. Flyte backend can be connected with the BigQuery service. Once enabled, it can allow you to query a BigQuery table.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-bigquery
```

To configure BigQuery in the Flyte deployment's backend, follow the [configuration guide](https://docs.flyte.org/en/latest/deployment/plugin_setup/gcp/bigquery.html#deployment-plugin-setup-gcp-bigquery).
