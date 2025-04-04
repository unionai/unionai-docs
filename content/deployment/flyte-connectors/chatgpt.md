---
title: ChatGPT connector
weight: 10
variants: +flyte -serverless -byoc -byok
---

# ChatGPT agent

This guide provides an overview of how to set up the ChatGPT agent in your Flyte deployment.  
Please note that you have to set up the OpenAI API key in the agent server to run ChatGPT tasks.

## Specify agent configuration

### flyte-binary

Add the following to your values file:

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - agent-service
    default-for-task-types:
      - container: container
      - chatgpt: agent-service

plugins:
  agent-service:
    # Configuring the timeout is optional.
    # Tasks like using ChatGPT with a large model might require a longer time, 
    # so we have the option to adjust the timeout setting here.
    defaultAgent:
      timeouts:
        ExecuteTaskSync: 10s
```

## flyte-core

Create a file named values-override.yaml and add the following configuration to it:

```yaml
configmap:
  enabled_plugins:
    # -- Tasks specific configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#GetConfig)
    tasks:
      # -- Plugins configuration, [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#TaskPluginConfig)
      task-plugins:
        # -- [Enabled Plugins](https://pkg.go.dev/github.com/flyteorg/flyteplugins/go/tasks/config#Config). Enable sagemaker*, athena if you install the backend
        enabled-plugins:
          - container
          - sidecar
          - agent-service
        default-for-task-types:
          container: container
          sidecar: sidecar
          chatgpt: agent-service
    plugins:
      agent-service:
        # Configuring the timeout is optional.
        # Tasks like using ChatGPT with a large model might require a longer time, 
        # so we have the option to adjust the timeout setting here.
        defaultAgent:
          timeouts:
            ExecuteTaskSync: 10s
```
## Add the OpenAI API token
1. Install the flyteagent pod using helm:
```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
helm install flyteagent flyteorg/flyteagent --namespace flyte
```

2. Set Your OpenAI API Token as a Secret (Base64 Encoded):
```bash
SECRET_VALUE=$(echo -n "<OPENAI_API_TOKEN>" | base64) && \
kubectl patch secret flyteagent -n flyte --patch "{\"data\":{\"flyte_openai_api_key\":\"$SECRET_VALUE\"}}"
```
3. Restart deployment:

```bash
kubectl rollout restart deployment flyteagent -n flyte
```
## Upgrade the Helm release


```bash
helm upgrade <RELEASE_NAME> flyteorg/<HELM_CHART> -n <YOUR_NAMESPACE> --values values-override.yaml

```

Replace ``<RELEASE_NAME>`` with the name of your release (e.g., ``flyte-backend``),
``<YOUR_NAMESPACE>`` with the name of your namespace (e.g., ``flyte``) and `<HELM_CHART>` with `flyte-binary`, `flyte-core ` or `flyte-sandbox`.


Wait for the upgrade to complete. You can check the status of the deployment pods by running the following command:

```bash
kubectl get pods -n flyte
```

Once all the components are up and running, go to the examples section to learn more about how to use Flyte connectors.



