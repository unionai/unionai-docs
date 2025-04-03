---
title: Monitoring
weight: 2 
variants: +flyte -serverless -byoc -byok
---

# Monitoring a Flyte deployment


> The Flyte core team publishes and maintains Grafana dashboards built using Prometheus data sources. You can import them to your Grafana instance from the [Grafana marketplace](https://grafana.com/orgs/flyteorg/dashboards).

Before configuring Flyte for observability, it's important to cover the metrics the system emits:

## Metrics for Executions

Whenever you run a workflow, Flyte automatically emits high-level metrics. These metrics follow a consistent schema and aim to provide visibility into aspects of the platform which might otherwise be opaque.
These metrics help users diagnose whether an issue is inherent to the platform or one's own task or workflow implementation.

At a high level, workflow execution goes through the following discrete steps:

![](/_static/images/deployment/flyte_wf_timeline.svg)


**Description of main events for workflow execution**

               Events                                                              Description
===================================  ==================================================================================================================================
Acceptance                           Measures the time consumed from receiving a service call to creating an Execution (Unknown) and moving to QUEUED.
Transition Latency                   Measures the latency between two consecutive node executions; the time spent in Flyte engine.
Queuing Latency                      Measures the latency between the node moving to QUEUED and the handler reporting the executable moving to RUNNING state.
Task Execution                       Actual time spent executing the user code.
Repeat steps 2-4 for every task
Transition Latency                   See #2
Completion Latency                   Measures the time consumed by a workflow moving from SUCCEEDING/FAILING state to TERMINAL state.
===================================  ==================================================================================================================================


==========================================================  ===========  ===============================================================================================================================================================
                    Flyte Stats Schema
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    Prefix                                     Type                                           Description
==========================================================  ===========  ===============================================================================================================================================================
``propeller.all.workflow.acceptance-latency-ms``            Timer (ms)   Measures the time consumed from receiving a service call to creating an Execution (Unknown) and moving to QUEUED.
``propeller.all.node.queueing-latency-ms``                  Timer (ms)   Measures the latency between the node moving to QUEUED and the handler reporting the executable moving to RUNNING state.
``propeller.all.node.transition-latency-ms``                Timer (ms)   Measures the latency between two consecutive node executions; the time spent in Flyte engine.
``propeller.all.workflow.completion-latency-ms``            Timer (ms)   Measures the time consumed by a workflow moving from SUCCEEDING/FAILING state to TERMINAL state.
``propeller.all.node.success-duration-ms``                  Timer (ms)   Actual time spent executing user code (when the node ends with SUCCESS state).
``propeller.all.node.success-duration-ms-count``            Counter      The number of times a node success has been reported.
``propeller.all.node.failure-duration-ms``                  Timer (ms)   Actual time spent executing user code (when the node ends with FAILURE state).
``propeller.all.node.failure-duration-ms-count``            Counter      The number of times a node failure has been reported.

==========================================================  ===========  ===============================================================================================================================================================

All the above stats are automatically tagged with the following fields for further scoping. This includes user-produced stats.
Users can also provide additional tags (or override tags) for custom stats.


===============  =================================================================================
                     Flyte Stats Tags
--------------------------------------------------------------------------------------------------
      Tag                                                 Description
===============  =================================================================================
wf               Name of the workflow that was executing when this metric was emitted.
                 ``{{project}}:{{domain}}:{{workflow_name}}``
===============  =================================================================================

## User Stats With Flyte


The workflow parameters object that the SDK injects into various tasks has a ``statsd`` handle that users should call to emit stats of their workflows not captured by the default metrics. The usual caveats around cardinality apply, of course.

Users are encouraged to avoid creating their own stats handlers.
If not done correctly, these can pollute the general namespace and accidentally interfere with the production stats of live services, causing pages and wreaking havoc.
If you're using any libraries that emit stats, it's best to turn them off if possible.


## Use Published Dashboards to Monitor Flyte Deployment


Flyte Backend is written in Golang and exposes stats using Prometheus. The stats are labeled with workflow, task, project & domain, wherever appropriate.

Both ``flyteadmin`` and ``flytepropeller`` are instrumented to expose metrics. To visualize these metrics, Flyte provides three Grafana dashboards, each with a different focus:

- **User-facing dashboard**: it can be used to investigate performance and characteristics of workflow and task executions. It's published under ID [22146](https://grafana.com/grafana/dashboards/22146-flyte-user-dashboard-via-prometheus/) in the Grafana marketplace.

- **System Dashboards**: Dashboards that are useful for the system maintainer to investigate the status and performance of their Flyte deployments. These are further divided into:
        - Data plane (``flytepropeller``) - [21719](https://grafana.com/grafana/dashboards/21719-flyte-propeller-dashboard-via-prometheus/): execution engine status and performance.
        - Control plane (``flyteadmin``) - [21720](https://grafana.com/grafana/dashboards/21720-flyteadmin-dashboard-via-prometheus/): API-level monitoring.

The corresponding JSON files for each dashboard are also located in the ``flyte`` repository at [deployment/stats/prometheus](https://github.com/flyteorg/flyte/tree/master/deployment/stats/prometheus).

> The dashboards are basic dashboards and do not include all the metrics exposed by Flyte. Feel free to use the scripts provided [here](https://github.com/flyteorg/flyte/tree/master/stats) to improve and contribute the improved dashboards.

## Setup instructions

The dashboards rely on a working Prometheus deployment with access to your Kubernetes cluster and Flyte pods.
Additionally, the user dashboard uses metrics that come from ``kube-state-metrics``. Both of these requirements can be fulfilled by installing the [kube-prometheus-stack](https://github.com/kubernetes/kube-state-metrics).

Once the prerequisites are in place, follow the instructions in this section to configure metrics scraping for the corresponding Helm chart:

{{< dropdown title="flyte-core" icon=arrow_forward >}}
{{< markdown >}}

Save the following in a ``flyte-monitoring-overrides.yaml`` file and run a ``helm upgrade`` operation pointing to that ``--values`` file:

```yaml

flyteadmin:
serviceMonitor:
    enabled: true
labels:
    release: kube-prometheus-stack #This is particular to the kube-prometheus-stacl
selectorLabels:
    - app.kubernetes.io/name: flyteadmin
flytepropeller:
serviceMonitor:
    enabled: true
    labels:
    release: kube-prometheus-stack
    selectorLabels:
    - app.kubernetes.io/name: flytepropeller
service:
    enabled: true
```

The above configuration enables the ``serviceMonitor`` that Prometheus can then use to automatically discover services and scrape metrics from them.

{{< /markdown >}}
{{< /dropdown >}}

{{< dropdown title="flyte-binary" icon=arrow_forward >}}
{{< markdown >}}

Save the following in a ``flyte-monitoring-overrides.yaml`` file and run a ``helm upgrade`` operation pointing to that ``--values`` file:

```yaml
configuration:
inline:
    propeller:
    prof-port: 10254
    metrics-prefix: "flyte:"
    scheduler:
    profilerPort: 10254
    metricsScope: "flyte:"
    flyteadmin:
    profilerPort: 10254
service:
extraPorts:
- name: http-metrics
    protocol: TCP
    port: 10254
```

The above configuration enables a ``serviceMonitor`` that Prometheus can use to automatically discover services and scrape metrics from them.
       
{{< /markdown >}}
{{< /dropdown >}}

> By default, the ``ServiceMonitor`` is configured with a ``scrapeTimeout`` of 30s and ``interval`` of 60s. You can customize these values if needed.


With the above configuration completed, you should be able to import the dashboards in your Grafana instance.

