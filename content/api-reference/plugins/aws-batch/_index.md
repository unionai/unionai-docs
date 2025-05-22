---
title: AWS Batch
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: AWS Batch
  title_expanded: Flytekit AWS Batch Plugin
  name: flytekitplugins-awsbatch
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the AWS Batch plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.awsbatch
  install_requires:
  - flytekit>=1.3.0b2
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
  folder: flytekit-aws-batch
---


Flyte backend can be connected with AWS batch. Once enabled, it allows you to run flyte task on AWS batch service

To install the plugin, run the following command:

```bash
pip install flytekitplugins-awsbatch
```
