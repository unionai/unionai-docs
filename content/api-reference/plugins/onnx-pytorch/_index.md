---
title: ONNX PyTorch
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: ONNX PyTorch
  title_expanded: Flytekit ONNX PyTorch Plugin
  name: flytekitplugins-onnxpytorch
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: ONNX PyTorch Plugin for Flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.onnxpytorch
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
  - torch>=1.11.0
  - onnx-pytorch
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
  folder: flytekit-onnx-pytorch
---


This plugin allows you to generate ONNX models from your PyTorch models.

To install the plugin, run the following command:

```
pip install flytekitplugins-onnxpytorch
```
