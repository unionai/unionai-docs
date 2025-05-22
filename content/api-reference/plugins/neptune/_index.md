---
title: Neptune
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Neptune
  title_expanded: Flytekit Neptune Plugin
  name: flytekitplugins-neptune
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package enables seamless use of Neptune within Flyte
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.neptune
  install_requires:
  - flytekit>=1.13.3
  - neptune>=1.10.4
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
  folder: flytekit-neptune
---


Neptune is the MLOps stack component for experiment tracking. It offers a single place to log, compare, store, and collaborate on experiments and models. This plugin integrates Flyte with Neptune by configuring links between the two platforms.

To install the plugin, run:

```bash
pip install flytekitplugins-neptune
```

Neptune requires an API key to authenticate with their platform. This Flyte plugin requires a `flytekit` `Secret` to be configured using [Flyte's Secrets manager](https://docs.flyte.org/en/latest/user_guide/productionizing/secrets.html).

```python
from flytekit import Secret, current_context

neptune_api_token = Secret(key="neptune_api_token", group="neptune_group")

@task
@neptune_init_run(project="flytekit/project", secret=neptune_api_token)
def neptune_task() -> bool:
    ctx = current_context()
    run = ctx.neptune_run
    run["algorithm"] = "my_algorithm"
    ...
```

To enable linking from the Flyte side panel to Neptune, add the following to Flyte's configuration:

```yaml
plugins:
  logs:
    dynamic-log-links:
      - neptune-run-id:
          displayName: Neptune
          templateUris: "{{ .taskConfig.host }}/{{ .taskConfig.project }}?query=(%60flyte%2Fexecution_id%60%3Astring%20%3D%20%22{{ .executionName }}-{{ .nodeId }}-{{ .taskRetryAttempt }}%22)&lbViewUnpacked=true"
```
