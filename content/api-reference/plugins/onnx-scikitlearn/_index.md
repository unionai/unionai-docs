---
title: ONNX ScikitLearn
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: ONNX ScikitLearn
  title_expanded: Flytekit ONNX ScikitLearn Plugin
  name: flytekitplugins-onnxscikitlearn
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: ONNX ScikitLearn Plugin for Flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.onnxscikitlearn
  install_requires:
  - flytekit
  - skl2onnx>=1.10.3
  - networkx<3.2; python_version<'3.9'
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
  folder: flytekit-onnx-scikitlearn
---


This plugin allows you to generate ONNX models from your ScikitLearn models.

To install the plugin, run the following command:

```
pip install flytekitplugins-onnxscikitlearn
```
