---
title: Sensor
weight: 1
variants: +flyte -serverless -byoc -byok
sidebar_expanded: true
---

# Sensor

## Usage

For an example of detecting a file with the `FileSensor`, see the [File sensor example](./file_sensor_example).

### Run the file senseor example on a Flyte cluster

To run the provided example on a Flyte cluster, use the following command:

```shell
$ pyflyte run --remote \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/sensor/sensor/file_sensor_example.py wf
```

## Deployment configuration

> [!NOTE]
> If you are using a managed deployment of Flyte, you will need to contact your deployment administrator to configure agents in your deployment.

To enable the sensor agent in your Flyte deployment, see the [Sensor agent deployment guide](https://docs-legacy.flyte.org/en/latest/deployment/agents/sensor.html#deployment-agent-setup-sensor).
