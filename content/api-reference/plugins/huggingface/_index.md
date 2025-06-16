---
title: Hugging Face
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Hugging Face
  title_expanded: Flytekit Hugging Face Plugin
  name: flytekitplugins-huggingface
  version: 0.0.0+develop
  author: Evan Sadler
  description: Hugging Face plugin for flytekit
  url: https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-huggingface
  long_description: "Hugging Face plugin for flytekit"
  long_description_content_type: text/markdown
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.huggingface
  install_requires:
  - flytekit>=1.3.0b2
  - datasets>=2.4.0
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
    - huggingface=flytekitplugins.huggingface
  folder: flytekit-huggingface
---

[Hugging Face](https://github.com/huggingface) is a community and data science platform that provides: Tools that enable users to build, train and deploy ML models based on open source (OS) code and technologies

This plugin supports `datasets.Dataset` as a data type with [StructuredDataset](https://docs.flyte.org/en/latest/user_guide/data_types_and_io/structureddataset.html).

To install the plugin, run the following command:

```bash
pip install flytekitplugins-huggingface
```
