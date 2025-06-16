---
title: Perian Job Platform
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Perian Job Platform
  title_expanded: Flytekit Perian Job Platform Plugin
  name: flytekitplugins-perian_job
  version: 0.0.0+develop
  author: Omar Tarabai
  author_email: otarabai@perian.io
  description: Flyte agent for Perian Job Platform (perian.io)
  long_description: "Flyte agent for Perian Job Platform (perian.io)"
  long_description_content_type: text/markdown
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.perian_job
  install_requires:
  - flytekit>=1.12.0,<2.0.0
  - perian==0.2.7
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
    - perian_job=flytekitplugins.perian_job
  folder: flytekit-perian
---


Flyte Agent plugin for executing Flyte tasks on Perian Job Platform (perian.io).

See the [official docs page](https://perian.io/docs/flyte-getting-started) for more details.
