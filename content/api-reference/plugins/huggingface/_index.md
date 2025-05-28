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
