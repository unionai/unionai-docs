---
title: ONNX TensorFlow
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: ONNX TensorFlow
  title_expanded: Flytekit ONNX TensorFlow Plugin
  name: flytekitplugins-onnxtensorflow
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: ONNX TensorFlow Plugin for Flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.onnxtensorflow
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
  - tf2onnx>=1.9.3
  - tensorflow>=2.7.0
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
  folder: flytekit-onnx-tensorflow
---


This plugin allows you to generate ONNX models from your TensorFlow Keras models.

To install the plugin, run the following command:

```
pip install flytekitplugins-onnxtensorflow
```
