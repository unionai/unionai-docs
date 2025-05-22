---
title: Comet ML
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Comet ML
  title_expanded: Flytekit Comet Plugin
  name: flytekitplugins-comet-ml
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package enables seamless use of Comet within Flyte
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.comet_ml
  install_requires:
  - flytekit>=1.12.3
  - comet-ml>=3.43.2
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
  folder: flytekit-comet-ml
---


Comet’s machine learning platform integrates with your existing infrastructure and tools so you can manage, visualize, and optimize models—from training runs to production monitoring. This plugin integrates Flyte with Comet.ml by configuring links between the two platforms.

To install the plugin, run:

```bash
pip install flytekitplugins-comet-ml
```

Comet requires an API key to authenticate with their platform. In the above example, a secret is created using
[Flyte's Secrets manager](https://docs.flyte.org/en/latest/user_guide/productionizing/secrets.html).

To enable linking from the Flyte side panel to Comet.ml, add the following to Flyte's configuration:

```yaml
plugins:
  logs:
    dynamic-log-links:
      - comet-ml-execution-id:
          displayName: Comet
          templateUris: "{{ .taskConfig.host }}/{{ .taskConfig.workspace }}/{{ .taskConfig.project_name }}/{{ .executionName }}{{ .nodeId }}{{ .taskRetryAttempt }}{{ .taskConfig.link_suffix }}"
      - comet-ml-custom-id:
          displayName: Comet
          templateUris: "{{ .taskConfig.host }}/{{ .taskConfig.workspace }}/{{ .taskConfig.project_name }}/{{ .taskConfig.experiment_key }}"
```
