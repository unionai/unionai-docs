---
title: Metrics reference
description: The Prometheus metrics the leaseworker exposes, what each one measures, and what to watch.
icon: speedometer
weight: 5
variants: -flyte +union
---

# Metrics reference

This page lists the metrics that the leaseworker, the component that executes your runs in your data
plane, exposes, what each one measures, and which readings mean something is wrong. Metric names and label
values are as of release 2026.11.2 and can change between releases.

| Component | Runs in | Metric prefix | Scraped by |
| --- | --- | --- | --- |
| Leaseworker | Data plane, one Deployment per cluster | `leaseworker:` | The data plane Prometheus, `union-services` job (see [Monitoring](./monitoring)) |

Metric names use `:` as the scope separator, as in `leaseworker:dispatcher:queue_main_depth`. Some
collectors rewrite `:` to `_` when they ingest Prometheus metrics, so the same metric can appear as
`leaseworker_dispatcher_queue_main_depth` in another system. Counters are cumulative: query them as
`rate()` or `increase()`. Histograms end in `_bucket`, `_sum`, and `_count`: query them with `histogram_quantile`.

## How work reaches the leaseworker

The control plane holds every action's **lease**. It schedules an action onto a connected leaseworker,
which runs it on your cluster, heartbeats the lease while the action runs, and reports the terminal
result. When an action finishes or is aborted, the control plane issues a **finalize** lease to the same
leaseworker for cleanup. Every stage of that exchange has a leaseworker metric:

| Symptom | Start with | Then |
| --- | --- | --- |
| Actions queue but never start | `leaseworker:leases_received` flat, `leaseworker:stream:reconnections` rising | `leaseworker:available_capacity` at 0, pod restarts and the `leaseworker quiesced` log line |
| Actions start late | `leaseworker:dispatcher:queue_wait_duration` p99, `leaseworker:dispatcher:queue_main_depth` | `leaseworker:dispatcher:in_flight` pinned at `dispatcherCount`, `leaseworker:dispatcher:round_duration` |
| Actions fail without a user error | `leaseworker:dispatcher:system_errors_exhausted` | `leaseworker:dispatcher:system_errors`, `leaseworker:evaluator:execute_errors`, `leaseworker:heartbeater:request_errors` |
| Results reach the control plane late | `leaseworker:finished_run_leases` growing | `leaseworker:heartbeater:request_errors`, `leaseworker:pool:*:async_backlog`, `leaseworker:pool:*:events_dropped` |
| Cleanup is stuck | `leaseworker:active_finalize_leases` growing | `leaseworker:evaluator:finalize_errors`, `leaseworker:dispatcher:queue_priority_depth` |
| A leaseworker looks unhealthy | `leaseworker:stream:reconnections`, `leaseworker:heartbeater:request_errors` | `leaseworker:stream:stream_duration` (short sessions), `leaseworker:heartbeater:nacks` |

## Dashboards

The charts ship Grafana dashboards that plot a subset of these metrics. They are installed as ConfigMaps
carrying the `grafana_dashboard: "1"` label (`monitoring.dashboards.enabled`, on by default; change the
label with `monitoring.dashboards.label` and `labelValue`), which a Grafana dashboard sidecar picks up.
Point each dashboard's `$datasource` variable at the Prometheus that scrapes the cluster.

| Dashboard | Row | Panels |
| --- | --- | --- |
| [Union Dataplane Overview](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/dashboards/union-dataplane-overview.json) | **V2 — leaseworker** | Active leases (run, finalize, and finished awaiting the leasor), Available capacity, Dispatcher queue depth (main and priority lanes), Dispatcher rounds: success vs errors, Actions terminated (by phase), System errors: transient vs exhausted, Control-plane link: heartbeat errors / stream reconnects, FastTask backlog vs limit, Task assignment (no capacity / no workers) |

Dataplane chart 2026.11.4 or later includes these panels. Earlier charts ship a Dispatcher queue depth
panel that reads a metric the leaseworker does not emit, and none of the Actions terminated, System
errors, or Control-plane link panels; if you alert on them, add panels for `actions_terminated`,
`system_errors`, `system_errors_exhausted`, `heartbeater:request_errors`, and `stream:reconnections`
from the tables below.

## Leaseworker

Every leaseworker metric carries the standard Kubernetes labels Prometheus adds at scrape time
(`namespace`, `pod`). The worker's own gauges are refreshed on every heartbeat round.

### Worker

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `leaseworker:active_run_leases` | gauge | Run leases this worker holds whose action is executing | Your running-action count. The chart records it as `union:dp:leaseworker:active_actions`. |
| `leaseworker:finished_run_leases` | gauge | Run leases whose action finished but whose report the leasor has not accepted yet. They hold no capacity | Growing steadily means the leasor is not accepting reports. Check `heartbeater:request_errors`. |
| `leaseworker:active_finalize_leases` | gauge | Finalize (cleanup) leases held | Growing without run leases finishing means cleanup is stuck. Check `evaluator:finalize_errors`. |
| `leaseworker:available_capacity` | gauge | `leaseworker.capacity` minus the run slots in use, floored at 0 | At 0 the worker accepts no new leases and the leasor skips it with `reason="no_capacity"`. The chart default capacity is 100000, so this gauge does not reach 0 from load. |
| `leaseworker:quiesced` | gauge | 1 after the worker shut itself down because its cluster was deleted on the control plane, else 0 | The worker sets it (and `available_capacity` to 0) right before it exits, so a scrape rarely sees either value. Detect quiescence from pod restarts plus the `leaseworker quiesced` warning in the pod log. On a cluster you expect to be live it means the cluster record is wrong. |
| `leaseworker:leases_received` | counter | Leases accepted from the control plane's lease stream | Your inflow. Flat while runs are being submitted means the stream is down; check `stream:reconnections`. |
| `leaseworker:leases_rejected` | counter | Leases refused at capacity or by the tracker | Any sustained rate while `available_capacity` is above 0 is a bug. |
| `leaseworker:leases_finalized` | counter | Finalize leases reported complete | Should track `active_finalize_leases` draining. |
| `leaseworker:plugin_panic` | counter | Panics recovered inside a plugin's Handle, Abort, or Finalize | Zero in a healthy worker. Alert on any increase. |

### Dispatcher

The dispatcher runs the per-action evaluation loop. Metrics live under `leaseworker:dispatcher:`.

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `queue_main_depth` | gauge | Attempt keys waiting in the main work queue | Grows when the `dispatcherCount` dispatchers cannot keep up. Compare with `round_duration`. |
| `queue_priority_depth` | gauge | Finalize leases waiting in the one-shot priority lane | Normally near 0. A standing depth means finalizes are not being picked up. |
| `queue_wait_duration` | histogram | Time an attempt key waits in the work queue before dispatch | p99 rising with `queue_main_depth` is dispatcher saturation. |
| `in_flight` | gauge | Attempt keys being processed right now | Capped by `leaseworker.dispatcherCount`. Pinned at the cap means the worker needs more dispatchers. |
| `round_duration` | histogram | Latency of one evaluation round for one action | p99 rising points at slow plugin calls or a slow Kubernetes API. |
| `round_success`, `round_errors`, `round_idle`, `round_pending` | counter | Rounds by outcome: progressed, failed, no state change, yielded for async state hydration | `round_errors` as a share of all rounds is the dispatcher error rate. The overview dashboard plots success vs errors. |
| `actions_terminated` | counter, `phase` | Actions this worker drove to a terminal phase, labeled by the phase name: `ACTION_PHASE_SUCCEEDED`, `ACTION_PHASE_FAILED`, `ACTION_PHASE_ABORTED`, `ACTION_PHASE_TIMED_OUT` | Your outflow. Compare succeeded against the other three. |
| `system_errors` | counter | Transient system errors while executing an action (not user code errors) | A rising rate means pods are failing to create, the API server is erroring, or storage is slow. |
| `system_errors_exhausted` | counter | Actions failed because consecutive system errors reached the leaseworker's `maxConsecutiveErrors` limit, default 3. Set it under the chart's free-form `leaseworker.config` block (`leaseworker.config.maxConsecutiveErrors`) | Each increment is an action that failed for a platform reason. Alert on any sustained rate. |
| `streak_length` | histogram | Evaluation rounds per streak before the dispatcher yields | Diagnostic only. |
| `finalize_first_arrival_wait_seconds` | histogram | Wait from a finalize lease's admission to its first dispatch | Rising means cleanup is being starved. |

### Heartbeater

Metrics under `leaseworker:heartbeater:`. The heartbeater extends every active lease with the leasor on a fixed interval.

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `requests_sent` | counter | Heartbeat RPCs sent | |
| `request_errors` | counter | Heartbeat RPCs that failed | Sustained errors lead to lease expiry on the leasor and system retries of healthy actions. This is the first metric to check when actions restart for no reason. |
| `request_duration` | histogram | Heartbeat RPC latency | |
| `round_duration` | histogram | Wall time of a full heartbeat round across all chunks | A round longer than the heartbeat interval means leases can expire. |
| `chunks_per_round` | histogram | Chunk RPCs per round | Grows with the number of active leases. |
| `nacks` | counter | Leases the leasor refused to extend because it no longer knows them | Should be near 0. A spike after a leasor restart is expected. |

### Stream

Metrics under `leaseworker:stream:`. The stream is the long-lived connection on which the leasor delivers leases.

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `reconnections` | counter | Stream reconnects | A steady rate means the connection to the control plane is unstable or the leasor is rejecting the worker. |
| `stream_duration` | histogram | Lifetime of one stream session | Short sessions with many reconnects point at a load balancer idle timeout or an auth problem. |
| `stream_errors` | counter | Receive errors on the stream | |

### Evaluator

Metrics under `leaseworker:evaluator:`.

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `execute_duration` | histogram | Time to execute one action round | |
| `execute_errors` | counter | Errors during action execution | Feeds `dispatcher:system_errors`. |
| `finalize_duration` | histogram | Time to finalize one action | |
| `finalize_errors` | counter | Errors during finalization | Cleanup is failing. Pods or Kubernetes objects may be left behind. |

### Action store

Metrics under `leaseworker:action_store:`. The store caches each action's state and hydrates persisted
state from the control plane after a restart.

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `cache_hits`, `cache_misses` | counter | Lookups served from cache vs built fresh | A high miss rate after startup is expected; a high steady-state miss rate means the cache is being evicted. |
| `hydration_submitted`, `hydration_success`, `hydration_errors`, `hydration_pending` | counter | Async state hydration outcomes | `hydration_errors` rising means the control plane state service is failing. |
| `hydration_inflight` | gauge | Actions waiting on hydration | A standing value with `hydration_errors` means actions are stuck before their first round. |
| `finalize_cache_hits`, `finalize_fallback_reads`, `finalize_fallback_errors`, `finalize_fallback_duration` | counter, histogram | Finalize-path state reads and their blocking fallback | `finalize_fallback_errors` means cleanup could not load state. |

### Kubernetes informer

Metrics under `leaseworker:k8s_informer:`, labeled by watched `kind` (`Pod`, `RayJob`, and so on).

| Metric | Type | What to watch |
| --- | --- | --- |
| `events` | counter | Watch events that woke an action. Flat while pods are changing means the watch is stalled. |
| `enqueues` | counter | Actions re-enqueued from a watch event. |
| `events_dropped` | counter | Events with no usable labels. Should be 0. |
| `last_event_timestamp_seconds` | gauge | Unix time of the last event per kind. `time() - value` growing past a few minutes on a busy cluster means that kind's watch is stalled. |

### RPC pools

Each pool the worker uses for control plane calls exposes metrics under `leaseworker:pool:<name>:`.

| Metric | Type | What to watch |
| --- | --- | --- |
| `queue_depth`, `async_backlog` | gauge | Work waiting in the pool. Growing means the control plane is slow to answer. On the event pool, `queue_depth` is always 0: watch `async_backlog`. |
| `in_flight` | gauge | Calls executing. |
| `duration`, `queue_wait_duration` | histogram | Call latency and time spent waiting for a slot. |
| `errors`, `dropped` | counter | Internal pool errors and requests dropped because the channel was full. Both should be 0. |
| `events_accepted`, `events_rejected`, `events_flush_success`, `events_flush_errors`, `events_retried`, `events_dropped{reason}` | counter | Event pool only. `events_dropped` is the one that loses data: an action event never reached the control plane. |

### Reusable containers

The reusable-containers plugin reports under `leaseworker:core_plugins:fast_task:`. Gauges are per `queue_id`
(one reusable environment).

| Metric | Type | What to watch |
| --- | --- | --- |
| `workers`, `healthy_workers`, `initializing_workers`, `orphaned_workers` | gauge | Replica counts per environment. `orphaned_workers` above 0 means replicas lost their environment. |
| `executions`, `executions_limit`, `active_tasks` | gauge | Tasks running against the environment's limit. |
| `backlog`, `backlog_limit` | gauge | Tasks waiting for a replica against the limit. The overview dashboard plots the two together. Backlog pinned at its limit means the environment needs more replicas or a higher limit. |
| `available_execution_slots`, `available_total_slots` | gauge | Healthy slots remaining after pending reservations. |
| `task_assigned` | counter | Tasks handed to a replica. |
| `task_no_workers_available`, `task_no_capacity_available`, `task_no_capacity_by_reason{reason}` | counter | Assignment attempts that found no replica or no slot. A sustained rate means the environment is undersized or its replicas are not becoming healthy. |
| `worker_connection_errors{error_type}` | counter | Errors talking to replicas. |
| `env_builder:fast_task:*` | counter, gauge | Environment lifecycle, under the longer prefix `leaseworker:core_plugins:env_builder:fast_task:`: `env_created`, `env_gced`, `pods_created_total`, `pod_creation_errors_total`, `scale_up_buffer_size`, `scale_down_buffer_size`. `pod_creation_errors_total` rising means replicas cannot be scheduled. |

### Generated artifacts

Metrics under `leaseworker:generated_artifacts:`. The worker extracts artifacts from a task's outputs and attaches them to the terminal report.

| Metric | Type | What to watch |
| --- | --- | --- |
| `extracted` | counter | Artifacts attached to terminal reports. |
| `dropped_budget` | counter | Artifacts left off a report because the terminal payload budget was exceeded. Any increase means artifacts are missing from the console for those actions. |
| `skipped_oversize` | counter | Extractions skipped because the outputs file exceeded the download size limit. |
| `errors` | counter | Extraction errors. Best effort and never fatal to the action. |

### Recording rule

The data plane chart's monitoring rules record `union:dp:leaseworker:active_actions` from
`leaseworker:active_run_leases`, next to the propeller and operator rules, so a dashboard can use one
name for running work regardless of execution path.

## Metrics replaced by the leaseworker

Data plane charts earlier than 2026.8.0 ran the queue executor, which exposed its metrics under the
`executor::v2:` prefix. The leaseworker replaces it. The table maps each executor metric to its leaseworker
equivalent.

| Executor metric (charts before 2026.8.0) | Leaseworker metric | Difference |
| --- | --- | --- |
| `executor::v2:active_actions_count` | `leaseworker:active_run_leases` | Same meaning: actions executing on this worker. Finished-but-unreported actions are now separate, in `leaseworker:finished_run_leases`. |
| `executor::v2:available_capacity` | `leaseworker:available_capacity` | Same meaning. The capacity it is measured against is `leaseworker.capacity` in the chart. |
| `executor::v2:queue_depth` | `leaseworker:dispatcher:queue_main_depth` | The work queue now has two lanes; `leaseworker:dispatcher:queue_priority_depth` is the finalize lane. |
| `executor::v2:actions_terminated{phase}` | `leaseworker:dispatcher:actions_terminated{phase}` | Same meaning and label. |
| `executor::v2:system_failures` | `leaseworker:dispatcher:system_errors` | Same meaning. |
| `executor::v2:system_failures_exhausted` | `leaseworker:dispatcher:system_errors_exhausted` | Same meaning; the limit is `maxConsecutiveErrors` (default 3, under `leaseworker.config`). |
| `executor::v2:leases_received_count`, `executor::v2:leases_finalized_count` | `leaseworker:leases_received`, `leaseworker:leases_finalized` | Same meaning. |
| `executor:handler_panic` | `leaseworker:plugin_panic` | Different. `handler_panic` counted panics recovered in RPC handlers; `plugin_panic` counts panics in a plugin's Handle, Abort, or Finalize. It is the closest signal, not an equivalent. |
| `union:dp:executor:active_actions` (recording rule) | `union:dp:leaseworker:active_actions` | Rewritten to read `leaseworker:active_run_leases`. |

## See also

- [Monitoring](./monitoring): the data plane Prometheus, its scrape jobs, and the optional cluster monitoring stack.
