# Project
project = 'union-docs'
copyright = '2024, Union'
author = 'Union'
release = '1.0'

# Sphinx basic
master_doc = 'index'
html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = ['custom.css']
exclude_patterns = []
extensions = ['myst_parser', 'sphinx_design', 'sphinx_reredirects']
html_theme = 'sphinx_book_theme'

# Myst
myst_enable_extensions = ['colon_fence']
myst_heading_anchors = 6

# Sphinx book theme
html_logo = '_static/public/logo.svg'

html_sidebars = {
    "**": ['navbar-logo.html', 'variant-selector.html', 'search-button-field.html', 'sbt-sidebar-nav.html']
}

# Redirects
redirects = {
    'building-workflows': 'core-concepts/index.html',
    'building-workflows/artifacts': '../core-concepts/artifacts/index.html',
    'building-workflows/artifacts/connecting-workflows-with-artifact-event-triggers': '../../core-concepts/artifacts/connecting-workflows-with-artifact-event-triggers.html',
    'building-workflows/artifacts/consuming-artifacts-in-workflows': '../../core-concepts/artifacts/consuming-artifacts-in-workflows.html',
    'building-workflows/artifacts/declaring-artifacts': '../../core-concepts/artifacts/declaring-artifacts.html',
    'building-workflows/artifacts/materializing-artifacts': '../../core-concepts/artifacts/materializing-artifacts.html',
    'building-workflows/launch-plans': '../core-concepts/launch-plans/index.html',
    'building-workflows/launch-plans/reactive-workflows': '../../core-concepts/launch-plans/reactive-workflows.html',
    'building-workflows/launch-plans/running-launch-plans': '../../core-concepts/launch-plans/running-launch-plans.html',
    'building-workflows/launch-plans/triggers': '../../core-concepts/launch-plans/reactive-workflows.html',
    'building-workflows/tasks': '../core-concepts/tasks/index.html',
    'building-workflows/tasks/task-caching': '../../core-concepts/tasks/task-caching.html',
    'building-workflows/tasks/task-hardware-environment': '../../core-concepts/tasks/task-hardware-environment/index.html',
    'building-workflows/tasks/task-hardware-environment/accelerators': '../../../core-concepts/tasks/task-hardware-environment/accelerators.html',
    'building-workflows/tasks/task-hardware-environment/customizing-task-resources': '../../../core-concepts/tasks/task-hardware-environment/customizing-task-resources.html',
    'building-workflows/tasks/task-hardware-environment/interruptible-instances': '../../../core-concepts/tasks/task-hardware-environment/interruptible-instances.html',
    'building-workflows/tasks/task-parameters': '../../core-concepts/tasks/task-parameters.html',
    'building-workflows/tasks/task-software-environment': '../../core-concepts/tasks/task-software-environment/index.html',
    'building-workflows/tasks/task-software-environment/environment-variables': '../../../core-concepts/tasks/task-software-environment/environment-variables.html',
    'building-workflows/tasks/task-software-environment/imagespec-with-ecr': '../../../core-concepts/tasks/task-software-environment/imagespec-with-ecr.html',
    'building-workflows/tasks/task-software-environment/imagespec-with-gar': '../../../core-concepts/tasks/task-software-environment/imagespec-with-gar.html',
    'building-workflows/tasks/task-software-environment/imagespec': '../../../core-concepts/tasks/task-software-environment/imagespec.html',
    'building-workflows/tasks/task-software-environment/secrets': '../../../core-concepts/tasks/task-software-environment/secrets.html',
    'building-workflows/tasks/task-types': '../../core-concepts/tasks/task-types.html',
    'building-workflows/workflows': '../core-concepts/workflows/index.html',
    'building-workflows/workflows/dynamic-workflows': '../../core-concepts/workflows/dynamic-workflows.html',
    'building-workflows/workflows/eager-workflows': '../../core-concepts/workflows/eager-workflows.html',
    'building-workflows/workflows/standard-workflows': '../../core-concepts/workflows/standard-workflows.html',
    'building-workflows/workflows/subworkflows': '../../core-concepts/workflows/subworkflows.html',
    'concepts': 'core-concepts/index.html',
    'developing-workflows': 'core-concepts/index.html',
    'developing-workflows/accelerated-datasets': '../data-input-output/accelerated-datasets.html',
    'developing-workflows/artifacts': '../core-concepts/artifacts/index.html',
    'developing-workflows/artifacts/connecting-workflows-with-artifact-event-triggers': '../../core-concepts/artifacts/connecting-workflows-with-artifact-event-triggers.html',
    'developing-workflows/artifacts/connecting-workflows-with-triggers-via-artifact-events': '../../core-concepts/artifacts/connecting-workflows-with-artifact-event-triggers.html',
    'developing-workflows/artifacts/consuming-artifacts-in-workflows': '../../core-concepts/artifacts/consuming-artifacts-in-workflows.html',
    'developing-workflows/artifacts/declaring-artifacts': '../../core-concepts/artifacts/declaring-artifacts.html',
    'developing-workflows/artifacts/materializing-artifacts': '../../core-concepts/artifacts/materializing-artifacts.html',
    'developing-workflows/caching': '../core-concepts/tasks/task-caching.html',
    'developing-workflows/customizing-task-resources': '../core-concepts/tasks/task-hardware-environment/customizing-task-resources.html',
    'developing-workflows/flytefile': '../data-input-output/flytefile.html',
    'developing-workflows/heterogeneous-tasks': '../core-concepts/tasks/index.html',
    'developing-workflows/imagespec': '../core-concepts/tasks/task-software-environment/imagespec.html',
    'developing-workflows/imagespec/imagespec-with-ecr': '../../core-concepts/tasks/task-software-environment/imagespec-with-ecr.html',
    'developing-workflows/imagespec/imagespec-with-gar': '../../core-concepts/tasks/task-software-environment/imagespec-with-gar.html',
    'developing-workflows/interactive-tasks': '../development-cycle/interactive-tasks.html',
    'developing-workflows/interruptible-instances': '../core-concepts/tasks/task-hardware-environment/interruptible-instances.html',
    'developing-workflows/registering-workflows': '../development-cycle/registering-workflows.html',
    'developing-workflows/setting-up-ci-cd-deployment': '../development-cycle/setting-up-ci-cd-deployment.html',
    'developing-workflows/spot-instances': '../core-concepts/tasks/task-hardware-environment/interruptible-instances.html',
    'developing-workflows/task-execution-context': '../core-concepts/tasks/task-software-environment/imagespec.html',
    'developing-workflows/triggers': '../core-concepts/launch-plans/reactive-workflows.html',
    'developing-workflows/unionremote': '../development-cycle/unionremote.html',
    'flyte-fundamentals': 'core-concepts/index.html',
    'flyte-fundamentals/caching': '../core-concepts/tasks/task-caching.html',
    'flyte-fundamentals/customizing-task-resources': '../core-concepts/tasks/task-hardware-environment/customizing-task-resources.html',
    'flyte-fundamentals/flytefile': '../data-input-output/flytefile.html',
    'flyte-fundamentals/task-execution-context': '../core-concepts/tasks/task-software-environment/imagespec.html',
    'getting-started/deploying-the-project-on-union-cloud': '../getting-started/deploying-the-project-on-union.html',
    'getting-started/registering-workflows': '../development-cycle/registering-workflows.html',
    'getting-started/setting-up-ci-cd-deployment': '../development-cycle/setting-up-ci-cd-deployment.html',
    'getting-started/setting-up-the-project-on-union-cloud': '../getting-started/setting-up-the-project-on-union.html',
    'integrations/additional-integrations': '../integrations/agents/index.html',
    'integrations/additional-integrations/airflow-agent': '../../integrations/agents/airflow-agent/index.html',
    'integrations/additional-integrations/airflow-agent/airflow-agent-example': '../../../integrations/agents/airflow-agent/airflow-agent-example.html',
    'integrations/additional-integrations/bigquery-agent': '../../integrations/agents/bigquery-agent/index.html',
    'integrations/additional-integrations/bigquery-agent/bigquery-agent-example': '../../../integrations/agents/bigquery-agent/bigquery-agent-example.html',
    'integrations/additional-integrations/chatgpt-agent': '../../integrations/agents/chatgpt-agent/index.html',
    'integrations/additional-integrations/chatgpt-agent/chatgpt-agent-example': '../../../integrations/agents/chatgpt-agent/chatgpt-agent-example.html',
    'integrations/additional-integrations/databricks-agent': '../../integrations/agents/databricks-agent/index.html',
    'integrations/additional-integrations/databricks-agent/databricks-agent-example': '../../../integrations/agents/databricks-agent/databricks-agent-example.html',
    'integrations/additional-integrations/file-sensor-agent': '../../integrations/agents/file-sensor-agent/index.html',
    'integrations/additional-integrations/file-sensor-agent/file-sensor-agent-example': '../../../integrations/agents/file-sensor-agent/file-sensor-agent-example.html',
    'integrations/additional-integrations/mmcloud-agent': '../../integrations/agents/mmcloud-agent/index.html',
    'integrations/additional-integrations/mmcloud-agent/mmcloud-agent-example': '../../../integrations/agents/mmcloud-agent/mmcloud-agent-example.html',
    'integrations/additional-integrations/snowflake-agent': '../../integrations/agents/snowflake-agent/index.html',
    'integrations/additional-integrations/snowflake-agent/snowflake-agent-example': '../../../integrations/agents/snowflake-agent/snowflake-agent-example.html',
    'release-notes': 'index.html',
    'running-workflows': 'web-console/index.html',
    'running-workflows/execution-view': '../web-console/execution-view.html',
    'running-workflows/launching-workflows-and-tasks': '../web-console/launching-workflows-and-tasks.html',
    'running-workflows/logging': '../web-console/logging.html',
    'running-workflows/project-view': '../web-console/execution-list.html',
    'running-workflows/registering-workflows': '../development-cycle/registering-workflows.html',
    'running-workflows/resource-monitoring': '../web-console/usage.html',
    'running-workflows/task-level-monitoring': '../web-console/task-level-monitoring.html',
    'running-workflows/web-console': '../web-console/index.html',
    'union-cloud-and-flyte': 'union-and-flyte.html',
    'web-console/usage-view': '../web-console/usage.html',
    'core-concepts/launch-plans/activating-and-deactivating-launch-plans': '../../core-concepts/launch-plans/activating-and-deactivating.html',
    'core-concepts/workflows/subworkflows': '../../core-concepts/workflows/subworkflows-and-sub-launch-plans.html',
    'web-console/index': '../getting-started/index.html',
    'web-console/artifact-list': '../core-concepts/artifacts/viewing-artifacts.html',
    'web-console/artifact-view': '../core-concepts/artifacts/viewing-artifacts.html',
    'web-console/execution-list': '../core-concepts/workflows/viewing-workflow-executions.html',
    'web-console/execution-view': '../core-concepts/workflows/viewing-workflow-executions.html',
    'web-console/launch-plan-list': '../core-concepts/launch-plans/inspecting-launch-plans.html',
    'web-console/launch-plan-view': '../core-concepts/launch-plans/inspecting-launch-plans.html',
    'web-console/logging': '../core-concepts/tasks/viewing-cloudwatch-logs-for-a-task.html',
    'web-console/task-level-monitoring': '../core-concepts/tasks/task-hardware-environment/task-level-monitoring.html',
    'web-console/task-list': '../core-concepts/tasks/viewing-tasks.html',
    'web-console/task-view': '../core-concepts/tasks/viewing-tasks.html',
    'web-console/launching-workflows-and-tasks': '../core-concepts/workflows/launching-workflows.html',
    'core-concepts/launch-plans/inspecting-launch-plans': '../../core-concepts/viewing-launch-plans.html',
    'core-concepts/tasks/viewing-cloudwatch-logs-for-a-task': '../../core-concepts/tasks/viewing-logs.html',
}
