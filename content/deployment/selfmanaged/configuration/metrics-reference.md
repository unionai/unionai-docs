---
title: Metrics reference
description: The Prometheus metrics the leaseworker, the leasor, and the actions service expose, what each one measures, and what to watch.
icon: speedometer
weight: 5
variants: -flyte +union
---

# Metrics reference

This page lists the metrics that the components executing your runs expose, what each one measures,
and which readings mean something is wrong. It covers the **leaseworker**, which runs in your data plane,
and the **leasor** and **actions** services, which run in the control plane. Metric names and label
values are as of release 2026.11.2; they change between releases (for example the dispatcher queue
gauge was `queue_depth` before it split into `queue_main_depth` and `queue_priority_depth`).

| Component | Runs in | Metric prefix | Scraped by |
| --- | --- | --- | --- |
| Leaseworker | Data plane, one Deployment per cluster | `leaseworker:` | The data plane Prometheus, `union-services` job (see [Monitoring](./monitoring)) |
| Leasor | Control plane | `leasor:` | Your control plane Prometheus, on a self-hosted control plane only |
| Actions | Control plane | `actions:` | Your control plane Prometheus, on a self-hosted control plane only |

On a self-managed deployment with a Union-hosted control plane, only the leaseworker metrics are yours to scrape.

Metric names use `:` as the scope separator, as in `leaseworker:dispatcher:queue_main_depth`. Some
collectors rewrite `:` to `_` when they ingest Prometheus metrics, so the same metric can appear as
`leaseworker_dispatcher_queue_main_depth` in another system. Counters are cumulative: query them as
`rate()` or `increase()`. Histograms end in `_bucket`, `_sum`, and `_count`: query them with `histogram_quantile`.

## How work flows through the three components

The leasor holds every action's **lease**. It schedules an action onto a connected leaseworker, which
runs it on your cluster, heartbeats the lease while the action runs, and reports the terminal result.
The leasor then calls the actions service, which stores the result and notifies the run service. When an
action finishes or is aborted, the leasor issues a **finalize** lease to the same leaseworker for cleanup.

Reading the metrics in that order answers most questions:

| Symptom | Start with | Then |
| --- | --- | --- |
| Actions queue but never start | `leasor:leases_by_state{state="unassigned"}` growing, `leasor:workers_connected` | `leaseworker:available_capacity`, `leasor:schedule_skip_total` by `reason` |
| Actions start late | `leasor:enqueue_to_dispatch_seconds` p99 | `leasor:queue_wait_seconds` vs `leasor:dispatch_duration_seconds` |
| Actions run but results arrive late | `leasor:completion_duration_seconds` | `leasor:callback_duration_seconds`, `actions:complete_seconds` |
| Actions fail without a user error | `leaseworker:dispatcher:system_errors_exhausted` | `leasor:retries_total{cause="system"}`, `leasor:expirations_total` |
| A leaseworker looks unhealthy | `leaseworker:stream:reconnections`, `leaseworker:heartbeater:request_errors` | `leasor:stream_connections_total` for that org vs `leasor:workers_connected` |

## Dashboards

The charts ship Grafana dashboards that plot a subset of these metrics. They are installed as ConfigMaps
carrying the `grafana_dashboard: "1"` label (`monitoring.dashboards.enabled`, on by default; change the
label with `monitoring.dashboards.label` and `labelValue`), which a Grafana dashboard sidecar picks up.
Point each dashboard's `$datasource` variable at the Prometheus that scrapes the cluster.

| Dashboard | Chart | Row | Panels |
| --- | --- | --- | --- |
| [Union Dataplane Overview](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/dashboards/union-dataplane-overview.json) | `dataplane` | **V2 — leaseworker** | Active leases (run, finalize, and finished awaiting the leasor), Available capacity, Dispatcher queue depth (main and priority lanes), Dispatcher rounds: success vs errors, Actions terminated (by phase), System errors: transient vs exhausted, Control-plane link: heartbeat errors / stream reconnects, FastTask backlog vs limit, Task assignment (no capacity / no workers) |
| [Union Controlplane Overview](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/dashboards/union-controlplane-overview.json) | `controlplane` | **V2 — leasor (CP lease queue)** | Queue depth, Active runs / actions, Enqueue to dispatch latency (p99), Leaseworker fleet (capacity, active, available) |
| | | **V2 — actions (CP action store)** | Actions in memory, Active watchers, Archive queue depth and drain rate |

The links point at the charts' `main` branch. Released dataplane charts through 2026.11.3 ship the
previous version of the dashboard: its Dispatcher queue depth panel reads a metric the leaseworker does
not emit and shows "No data", and it has none of the Actions terminated, System errors, or Control-plane
link panels. Those arrive with the next dataplane chart release; until then, add panels for
`actions_terminated`, `system_errors`, `system_errors_exhausted`, `heartbeater:request_errors`, and
`stream:reconnections` from the tables below if you alert on them. The controlplane dashboard applies to
a self-hosted control plane only.

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
| `leaseworker:leases_received` | counter | Leases accepted from the leasor stream | Your inflow. Flat while `leasor:leases_by_state{state="unassigned"}` grows means the stream is down. |
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
| `system_errors_exhausted` | counter | Actions failed because consecutive system errors reached `maxConsecutiveErrors` | Each increment is an action that failed for a platform reason. Alert on any sustained rate. |
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
| `queue_depth`, `async_backlog` | gauge | Work waiting in the pool. Growing means the control plane is slow to answer. |
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

### Recording rule

The data plane chart's monitoring rules record `union:dp:leaseworker:active_actions` from
`leaseworker:active_run_leases`, next to the propeller and operator rules, so a dashboard can use one
name for running work regardless of execution path.

## Leasor

The leasor runs in the control plane. These metrics are available when you run the control plane chart.
All names carry the `leasor:` prefix. The labels `org` and `queue` appear on most series.

### Lease state and workers

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `leases_by_state{state,type}` | gauge | Leases in each state: `unassigned`, `sent`, `pending_completion`, `pending_finalize`, `pending_retry`, `pending_abort_cascade`, `pending_abort_completion`, split by `run_action` and `finalize` | The single most useful gauge. `unassigned` growing is a scheduling bottleneck. `sent` growing with no completions means workers are stuck. `pending_completion` growing means the actions service callback is failing. |
| `workers_connected` | gauge | Leaseworkers with an open lease stream | 0 means nothing can run. A sudden drop is a worker crash, redeploy, or network partition. |
| `leaseworker_capacity`, `leaseworker_active`, `leaseworker_available{org,worker_cluster,worker}` | gauge | The leasor's view of each worker's slots | Utilization is `leaseworker_active / leaseworker_capacity`. `leaseworker_available` at 0 for a worker means its actions wait with `reason="no_capacity"`. |
| `work_queue_depth` | gauge | Items in the leasor's internal work channel | When the channel is full, new state-advancement work is left for the anti-entropy sweep rather than rejected. Watch `sweep_recoveries_total` and `work_queue_wait_seconds` alongside it. |
| `active_actions{org}`, `active_runs{org}` | gauge | Actions and runs the leasor holds per organization | Which org drives the load. |

### Queues

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `queue_depth{org,queue}` | gauge | Run leases admitted to the queue, waiting plus in progress | A queue at its `max_depth` rejects new work with `RESOURCE_EXHAUSTED`. |
| `queue_active_actions`, `queue_active_runs` | gauge | Work holding the queue's action and run concurrency | Compare with `queue_max_action_concurrency` and `queue_max_run_concurrency`. |
| `queue_max_depth`, `queue_max_action_concurrency`, `queue_max_run_concurrency` | gauge | The queue's configured limits. 0 is unlimited | |
| `queue_finalizes` | gauge | Outstanding cleanup leases for the queue | A draining queue is only drained once this reaches 0. |
| `queue_status{status}` | gauge | 1 for the queue's current status: `active`, `draining`, `drained`, `unknown` | |
| `queue_in_flight_resources{resource}`, `queue_max_resources{resource}` | gauge | Resources held by the queue's dispatched actions (cpu in millicores, memory and ephemeral storage in bytes) against its cap | In-flight approaching max means the queue is about to hold work. An absent max series means no cap on that resource. |
| `queue_in_flight_accelerators{accelerator}`, `queue_max_accelerators{accelerator}` | gauge | GPU devices charged against each accelerator cap | Same reading as the resources pair, per GPU type. |
| `queue_head_blocked` | gauge | 1 while a strict-FIFO queue's head action is held | Stuck at 1 while `queue_in_flight_resources` is flat means the queue's running work is not completing. |
| `queue_unknown_demand` | gauge | Active leases whose resource demand could not be projected | They count as zero against the cap, so a high value means the cap bounds less than it appears to. |
| `queue_enqueue_reject_total{reason}` | counter | Enqueues refused per queue: `queue_depth_exceeded`, `queue_not_active`, `unknown_queue`, `cross_cluster_pool` | `unknown_queue` means a client names a queue that does not exist. |

### Flow counters

Query these as rates.

| Metric | Type | What it measures | What to watch |
| --- | --- | --- | --- |
| `enqueue_total{result,org}` | counter | Actions accepted (`ok`), refused by a limit (`backpressure`: the global active-action limit, the per-org action and run limits, or a queue's `max_depth`), or failed to store (`error`) | Inflow. `error` means the database write failed. |
| `enqueue_reject_total{reason,org}` | counter | Enqueues refused before storage for a queue-routing reason: `missing_queue`, `not_synced`, `unknown_queue`, `queue_not_active`, `cross_cluster_pool`, `missing_run_spec`, `missing_root_queue` | Any `unknown_queue` or `missing_queue` rate is a configuration problem. `not_synced` means the queue reconciler is behind. `queue_not_active` is expected during an intentional drain. |
| `terminal_total{phase,org}` | counter | Actions reaching a terminal phase: `succeeded`, `failed`, `aborted`, `timed_out`, `recovered` | Outflow. Compare `succeeded` against the rest. |
| `retries_total{cause,org}` | counter | Retries by cause: `system` (lease expired or platform error) or `user` (task code failed) | Sustained `system` means pods or workers are dying. |
| `expirations_total{type}` | counter | Leases that expired because the worker stopped heartbeating | A burst during a deploy is normal. A sustained rate is a worker outage. |
| `timeouts_total{cause,org}` | counter | Actions reaped for `deadline` (the absolute budget; fires whether the lease is still queued or already sent to a worker) or `queued_timeout` (the per-attempt budget before dispatch; fires only while queued) | Sustained `queued_timeout` for one org means its workers are saturated. |
| `dispatch_total{result}` | counter | Lease assignments: `ok`, `worker_gone`, `persist_failed`, `rollback`, `rollback_failed` | `persist_failed` is a database problem. `rollback_failed` should never be sustained. |
| `heartbeat_total{result}` | counter | Heartbeats accepted or `rejected` because the lease is unknown | A high reject rate means workers and leasor disagree about live leases. |
| `heartbeat_persist_failures_total` | counter | Individual lease extensions that failed to persist | Only matters across a leasor restart, when stale expiries cause false expirations. |
| `callback_total{result}` | counter | Completion callbacks to the actions service | `error` rising is the actions service being unhealthy; `pending_completion` leases pile up. |
| `sweep_recoveries_total` | counter | Leases recovered by the anti-entropy sweep | Near 0 when healthy. |
| `stream_connections_total{org}` | counter | Lease streams opened | A high rate while `workers_connected` stays flat means workers are crash-looping. |
| `db_calls_total{operation,result}` | counter | ScyllaDB calls by operation and result | Any `error` rate is a database health issue. |
| `schedule_skip_total{reason,org,queue}` | counter | Actions the scheduler evaluated but could not place, by reason | `no_capacity` is worker saturation. `no_workers` is an outage. `no_matching_worker` means a worker kind is missing from the data plane. `queue_resource_cap` and `cluster_resource_cap` are expected backpressure under resource caps. |
| `infeasible_total{reason,org,queue}` | counter | Actions failed because they can never be placed: `queue_cap`, `node_shape`, `cluster_capacity`, `no_accelerator` | Expected to be 0. Any rate means a cap is smaller than the work, or work is routed to clusters that cannot run it. |
| `queue_sync:tick_total{result}`, `cluster_sync:tick_total{result}` | counter | Reconciler ticks that read queues and clusters from the control plane | No `ok` tick in 10 minutes on a shard means the leasor has stale routing. Alert on the counter over a window, not on `time() - last_success_timestamp_seconds`. |

### Latency histograms

Read p99. Every second an action spends inside the leasor, outside worker execution, is covered by these.

| Metric | What it measures | What to watch |
| --- | --- | --- |
| `enqueue_to_dispatch_seconds` | Enqueue to delivery on a worker stream. Equals `queue_wait_seconds` plus `dispatch_duration_seconds` | The bottleneck metric. If p99 spikes, check `workers_connected`, then `leases_by_state{state="unassigned"}`, then the two components. |
| `queue_wait_seconds{org}` | Time in `unassigned` before dispatch begins | High with normal dispatch duration is worker saturation. Confirm with `schedule_skip_total{reason="no_capacity"}`. |
| `dispatch_duration_seconds` | Persist the assignment and deliver the lease | High means the database write or the worker channel is slow. See `db_call_duration_seconds{operation="update"}` and `send_lease_seconds`. |
| `send_lease_seconds{org}` | Time blocked delivering to one worker's stream | High for one org means that org's worker is slow to consume and is blocking others. |
| `schedule_duration_seconds` | One scheduler cycle | Normally microseconds. Alert on the mean or on the share of cycles over the 10 ms bucket, not p99. |
| `completion_duration_seconds` | Worker reported done to callback accepted | High with normal `callback_duration_seconds` means the work queue is backed up. |
| `callback_duration_seconds` | The completion callback RPC to the actions service | High means the actions service is slow. |
| `db_call_duration_seconds{operation}` | ScyllaDB round trip per operation | p99 spikes precede error spikes. `batch_extend` is the heartbeat persist. |
| `work_queue_wait_seconds` | Time any work item waits in the leasor's work channel | High means the orchestrator worker pool is saturated. |

## Actions service

The actions service stores action state and relays results to the run service. These metrics are
available when you run the control plane chart. All names carry the `actions:` prefix.

### Gauges

| Metric | What it measures | What to watch |
| --- | --- | --- |
| `actions_in_memory{org}` | Actions held in memory per organization | The primary capacity signal. |
| `active_watchers{org}` | Open `WatchForUpdates` streams per organization | 0 means the run service is disconnected from this shard. |
| `replication_queue_depth{pipeline}` | Items waiting in each replication pipeline | Growing means the pipeline cannot keep up. |
| `leasor_backoff_level{org}` | Backoff level of replication to the leasor | Non-zero means the leasor is returning transient errors. |
| `circuit_breaker_state{org,queue}` | Leasor-backpressure breaker: 0 closed, 1 open, 2 half-open | 1 means enqueues for that queue are being rejected. |
| `paused_conditions{org}` | Actions paused and waiting for a signal | |
| `run_spec_cache_size` | Cached run specs | Pinned at the cap with rising `run_spec_cache_misses_total` means the cap is too small. |
| `archive_queue_depth` | Actions waiting to be archived | Growing means archiving is behind. The overview dashboard plots it with the drain rate. |

### Counters

| Metric | What it measures | What to watch |
| --- | --- | --- |
| `enqueue_total{result,org}` | Enqueue RPC results: `ok`, `error`, `already_exists`, `circuit_open` | `circuit_open` means the leasor is overloaded for that queue. |
| `complete_total{phase,org}` | Terminal completions by phase | Outflow counterpart to enqueue. |
| `update_total{result,org}`, `abort_total{result,org}`, `signal_total{result,reason,org}` | Update, abort, and signal RPC results | `error` rates mean database or validation failures. |
| `watcher_events_total{result,org}` | Notifications to watchers | `dropped` means the run service is too slow to consume. |
| `leasor_replication_total{result,org,queue}` | Enqueue replication to the leasor | `error` means actions are not reaching the scheduler. |
| `circuit_breaker_rejects_total{org,queue,mode}`, `circuit_breaker_transitions_total{org,queue,to,cause}` | Breaker rejects and state changes | A breaker opening is the leasor telling this service to slow down. |
| `record_replication_total`, `update_replication_total`, `notification_replication_total`, `artifact_replication_total{result}` | Replication to the run service, the notifications stream, and the artifact service | Any `error` rate means results are not reaching the console or artifacts. |
| `archive_drained_total`, `archive_drain_errors_total{step}` | Actions archived, and actions dropped at an archive step | `archive_drain_errors_total` is the primary archive alert: each increment is a lost archive. |
| `gc_runs_completed_total`, `gc_errors_total{type}` | Garbage collection of finished runs | |
| `db:calls_total{operation,result}` | ScyllaDB calls | Any `error` rate is a database issue. |

### Latency histograms

| Metric | What it measures | What to watch |
| --- | --- | --- |
| `enqueue_seconds` | Full Enqueue RPC | |
| `complete_seconds` | Full terminal-report RPC | The bottleneck metric for this service. It includes `watcher_notify_seconds`. |
| `update_seconds`, `abort_seconds`, `signal_seconds` | Other RPCs | |
| `watcher_notify_seconds` | Time notifying watchers inside a completion | High means the run service is slow to accept notifications. |
| `replication_queue_wait_seconds{pipeline}` | Time in a replication queue before processing | |
| `archive_tombstone_to_drained_seconds` | Time from an action's tombstone to its archive commit | The archive lag. |
| `db:call_duration_seconds{operation}` | ScyllaDB round trip | |

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
| `executor::v2:system_failures_exhausted` | `leaseworker:dispatcher:system_errors_exhausted` | Same meaning; the limit is `maxConsecutiveErrors`. |
| `executor::v2:leases_received_count`, `executor::v2:leases_finalized_count` | `leaseworker:leases_received`, `leaseworker:leases_finalized` | Same meaning. |
| `executor:handler_panic` | `leaseworker:plugin_panic` | Different. `handler_panic` counted panics recovered in RPC handlers; `plugin_panic` counts panics in a plugin's Handle, Abort, or Finalize. It is the closest signal, not an equivalent. |
| `union:dp:executor:active_actions` (recording rule) | `union:dp:leaseworker:active_actions` | Rewritten to read `leaseworker:active_run_leases`. |

## See also

- [Monitoring](./monitoring): the data plane Prometheus, its scrape jobs, and the optional cluster monitoring stack.
- [Resource caps and scheduling](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling): what the queue cap metrics enforce.
