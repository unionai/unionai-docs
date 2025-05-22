---
title: AWS Athena
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: AWS Athena
  title_expanded: Flytekit AWS Athena Plugin
  name: flytekitplugins-athena
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the Athena plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.athena
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
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
  folder: flytekit-aws-athena
---


Flyte backend can be connected with Athena. Once enabled, it allows you to query AWS Athena service (Presto + ANSI SQL Support) and retrieve typed schema (optionally).

To install the plugin, run the following command:

```bash
pip install flytekitplugins-athena
```

An [example](https://docs.flyte.org/en/latest/flytesnacks/examples/athena_plugin/index.html) can be found in the documentation.
