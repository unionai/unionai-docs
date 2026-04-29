---
title: Metrics Glossary
weight: 1
variants: -flyte +union
---

# Metrics Glossary

> [!NOTE] Release version
> This glossary is a point-in-time snapshot reflecting metrics available in helm-charts release **2026.4.9** (controlplane-2026.4.9 / dataplane-2026.4.9). Metrics may change between releases.

This page documents all metrics surfaced in the shipped Grafana dashboards and PrometheusRule definitions. It is organized by plane (controlplane / dataplane), then by dashboard section, followed by recording rules and alert rules.

## Naming conventions

Union services use **colon-separated** metric names (e.g., `flyte:admin:execution_manager:active_executions`). The first segment identifies the service, subsequent segments identify the subsystem.

Infrastructure metrics from kube-state-metrics and cAdvisor use the standard **underscore** convention (e.g., `kube_deployment_status_replicas_available`).

Recording rules are prefixed with `union:cp:` (controlplane) or `union:dp:` (dataplane).

**Metric types**: Counter (monotonically increasing), Gauge (point-in-time value), Histogram (bucketed distribution), Summary (quantile distribution).

---

## Controlplane metrics

### Health

| Metric | Type | Description |
|--------|------|-------------|
| `kube_deployment_status_replicas_available` | Gauge | Number of available replicas per deployment. Used with `kube_deployment_spec_replicas` to compute availability ratio. |
| `kube_deployment_spec_replicas` | Gauge | Desired replica count per deployment. |
| `kube_pod_container_status_restarts_total` | Counter | Cumulative container restart count. Non-zero increase indicates crashlooping or OOM kills. |
| `connect:server_requests_handled_total` | Counter | Total Connect RPC requests handled, labeled by `service` and `code`. Used to compute error rate (non-OK/Canceled/NotFound codes). |
| `authorizer:handler_panic` | Gauge | Handler panic count in the authorizer service. |
| `cluster:handler_panic` | Gauge | Handler panic count in the cluster service. |
| `dataproxy:handler_panic` | Gauge | Handler panic count in the data proxy service. |
| `executions:handler_panic` | Gauge | Handler panic count in the executions service. |
| `queue:handler_panic` | Gauge | Handler panic count in the queue service. |
| `usage:handler_panic` | Gauge | Handler panic count in the usage service. |

### Ingress (nginx)

| Metric | Type | Description |
|--------|------|-------------|
| `nginx_ingress_controller_request_duration_seconds_count` | Counter | Total ingress requests, labeled by `host`, `path`, `status`. Used for request rate and error rate calculations. |
| `nginx_ingress_controller_request_duration_seconds_bucket` | Histogram | Ingress request duration distribution. Used for latency percentile calculations (p50/p95/p99). Includes TLS + routing + upstream response time. |
| `nginx_ingress_controller_nginx_process_connections` | Gauge | Current number of active client connections to ingress-nginx. |

### Connect / gRPC

| Metric | Type | Description |
|--------|------|-------------|
| `connect:server_requests_handled_total` | Counter | Connect protocol request throughput, labeled by `service` (e.g., ExecutionService, ClusterService) and `code`. |
| `grpc_server_handled_total` | Counter | gRPC server request count, labeled by `grpc_service`, `grpc_method`, `grpc_code`. Used by CacheService (the only CP service using gRPC instead of Connect). |

### FlyteAdmin

| Metric | Type | Description |
|--------|------|-------------|
| `flyte:admin:execution_manager:active_executions` | Gauge | Current count of active workflow executions tracked by FlyteAdmin. |
| `flyte:admin:node_execution_manager:active_node_executions` | Gauge | Current count of active node executions. |
| `flyte:admin:task_execution_manager:active_executions` | Gauge | Current count of active task executions. |
| `flyte:admin:execution_manager:executions_created` | Counter | Total workflow executions created. |
| `flyte:admin:execution_manager:execution_events_created` | Counter | Total workflow execution events received from propeller. |
| `flyte:admin:node_execution_manager:node_execution_events_created` | Counter | Total node execution events received from propeller. |
| `flyte:admin:task_execution_manager:task_execution_events_created` | Counter | Total task execution events received from propeller. |
| `flyte:admin:execution_manager:propeller_failures` | Counter | Failures communicating with propeller. |
| `flyte:admin:execution_manager:transformer_error` | Counter | Model transformation errors during execution processing. |
| `flyte:admin:execution_manager:publish_error` | Counter | Notification publish failures. |
| `flyte:admin:execution_manager:execution_termination_failure` | Counter | Execution termination failures. |
| `flyte:admin:create_execution:duration_ms` | Summary | CreateExecution endpoint latency in milliseconds. |
| `flyte:admin:create_execution_event:duration_ms` | Summary | CreateExecutionEvent endpoint latency in milliseconds. |
| `flyte:admin:get_execution:duration_ms` | Summary | GetExecution endpoint latency in milliseconds. |
| `flyte:admin:list_execution:duration_ms` | Summary | ListExecution endpoint latency in milliseconds. |
| `flyte:middleware:authorization:authz_approved` | Counter | Requests approved by FlyteAdmin auth middleware. |
| `flyte:middleware:authorization:authz_denied` | Counter | Requests denied by FlyteAdmin auth middleware. High deny rate may indicate auth misconfiguration. |

### Executions service

| Metric | Type | Description |
|--------|------|-------------|
| `executions:executions:handle_create_op_count` | Counter | Execution create operations processed. |
| `executions:executions:handle_ack_op_count` | Counter | Execution acknowledgement operations processed (DP confirmed receipt). |
| `executions:executions:handle_create_op_bucket` | Histogram | Execution create operation latency distribution. |
| `executions:executions:handle_ack_op_bucket` | Histogram | Execution ack operation latency distribution. |
| `executions:workqueue:announce_cluster_assignment_bucket` | Histogram | Key SLI: end-to-end time from execution create to cluster assignment. Custom buckets from 10ms to 20min. |
| `executions:workqueue:send_operation_count` | Counter | Operations dispatched to the dataplane. |
| `executions:workqueue:claim_operations` | Counter | Operations claimed from the database queue. |
| `executions:workqueue:send_operation_failures` | Counter | Failed operation dispatches. |
| `executions:workqueue:claim_operation_failures` | Counter | Failed operation claims. |
| `executions:database:postgres:repositories:execution_ops:*_count` | Counter | Per-operation DB latency counters (create, ack, claim, unclaim, get, update). |
| `executions:database:postgres:errors:gorm_error` | Counter | GORM-level database errors. |
| `executions:database:postgres:errors:postgres_error` | Counter | Native PostgreSQL errors. |
| `executions:database:postgres:errors:not_found` | Counter | Database not-found errors. |
| `executions:executions:list_clusters:hits` | Counter | Cluster list cache hits. |
| `executions:executions:list_clusters:miss` | Counter | Cluster list cache misses. High miss rate indicates excessive DB queries. |
| `executions:executions:list_nodepools:hits` | Counter | Nodepool list cache hits. |
| `executions:executions:list_nodepools:miss` | Counter | Nodepool list cache misses. |
| `executions:app:leaser:pending_assignment_unlabeled` | Gauge | Apps waiting for cluster assignment. Growing backlog indicates a scheduling bottleneck. |
| `executions:app:service:first_ack_latency_unlabeled_bucket` | Histogram | Key V2 SLI: time to deliver an app to the dataplane. Measures end-to-end scheduling latency. |
| `executions:run:runs_sent` | Counter | V2 runs dispatched to dataplane. |
| `executions:run:actions_sent` | Counter | V2 actions dispatched to dataplane. |
| `executions:run:enqueue_action_failures` | Counter | V2 action enqueue failures. Indicates queue service issues. |
| `executions:run_notifier:notifications_sent` | Counter | V2 run notifications sent per second. |
| `executions:run_notifier:subscribers` | Gauge | Active V2 notification subscribers. |
| `executions:run:logs:tail_logs_bytes_read` | Counter | Log bytes streamed via V2 log tailing. |

### Queue / Run-Scheduler

| Metric | Type | Description |
|--------|------|-------------|
| `queue:metadata_store:total_run_count` | Gauge | Total runs tracked by the queue metadata store. |
| `queue:metadata_store:total_action_count` | Gauge | Total actions tracked by the queue metadata store. |
| `queue:metadata_store:scheduled_run_count` | Gauge | Runs currently scheduled for execution. |
| `queue:metadata_store:scheduled_action_count` | Gauge | Actions currently scheduled for execution. |
| `queue:scheduler:enqueued_leases` | Counter | New leases enqueued by the scheduler. |
| `queue:runner:completed_leases` | Counter | Leases completed by the runner. |
| `queue:aborter:aborted_leases` | Counter | Leases aborted (cancelled). |
| `queue:scheduler:input_queue_length` | Gauge | Scheduler input queue depth. Growing values indicate backpressure. |
| `queue:runner:input_queue_length` | Gauge | Runner input queue depth. |
| `queue:aborter:input_queue_length` | Gauge | Aborter input queue depth. |
| `queue:dispatcher:chain_queue_length` | Gauge | Dispatcher chain queue depth. |
| `queue:db:queue_length` | Gauge | DB worker pool queue depth. |
| `queue:dispatcher:operation_duration_bucket` | Histogram | Dispatcher multi-step operation chain execution time, by operation type. |
| `queue:state:get_duration_bucket` | Histogram | State store get operation latency. |
| `queue:state:put_duration_bucket` | Histogram | State store put operation latency. |
| `queue:state:active_states` | Gauge | Number of active action states in the state store. |
| `queue:state:terminal_states` | Gauge | Number of terminal action states. |
| `queue:eventer:record_action_errors` | Counter | Eventer errors reporting action status to the executions service. |
| `queue:scheduler:worker_capacity` | Gauge | Remaining execution capacity per connected DP worker. Zero means worker is saturated. |
| `queue:dispatcher:operation_failures` | Counter | Failed dispatcher operations, by Go type. Indicates internal queue service errors. |
| `queue:db:free_threads` | Gauge | Idle worker goroutines in the DB pool. Zero means all threads busy. |
| `queue:queue_client:free_threads` | Gauge | Idle worker goroutines in the queue-client pool. |
| `queue:state_client:free_threads` | Gauge | Idle worker goroutines in the state-client pool. |

### Cluster service

| Metric | Type | Description |
|--------|------|-------------|
| `cluster:svc:update_status:updates_total` | Counter | DP cluster status updates received. |
| `cluster:svc:heartbeat:success_ms_count` | Counter | Successful heartbeats received from DP clusters. |
| `cluster:svc:update_status:success_ms` | Summary | UpdateStatus RPC latency in milliseconds. |
| `cluster:svc:heartbeat:success_ms` | Summary | Heartbeat RPC latency in milliseconds. |
| `cluster:svc:update_status:operator_restarts` | Gauge | DP-reported operator restart count. Set by DP on each UpdateStatus call. |
| `cluster:svc:update_status:propeller_restarts` | Gauge | DP-reported propeller restart count. |
| `cluster:database:postgres:errors:gorm_error` | Counter | GORM-level database errors in the cluster service. |
| `cluster:database:postgres:errors:postgres_error` | Counter | Native PostgreSQL errors in the cluster service. |
| `cluster:database:postgres:errors:not_found` | Counter | Database not-found errors in the cluster service. |
| `cluster:cluster_sync:health:unhealthy` | Gauge | Cluster health status: 1=unhealthy, 0=healthy. Emitted per cluster on every Prometheus scrape. |
| `cluster:cluster_sync:health:last_update_age` | Gauge | Seconds since a cluster last sent a heartbeat. High values indicate a stale or disconnected cluster. |
| `cluster:managed_cluster_client_cache:get:hits` | Counter | LRU cache hits for managed cluster lookups. |
| `cluster:managed_cluster_client_cache:get:miss` | Counter | LRU cache misses for managed cluster lookups. High miss rate indicates excessive DB queries. |

### CacheService

| Metric | Type | Description |
|--------|------|-------------|
| `flyte:cacheservice:cache:cache_hit_unlabeled` | Counter | Cache hits — cached task output reused. |
| `flyte:cacheservice:cache:not_found_unlabeled` | Counter | Cache misses — task must execute. |
| `flyte:cacheservice:cache:get_failure_unlabeled` | Counter | Cache get failures — storage errors. |
| `flyte:cacheservice:cache:reservation_contention_unlabeled` | Counter | Cache reservation contention — workers blocked waiting for another worker's cache computation. |
| `flyte:cacheservice:cache:get_reservation_success_unlabeled` | Counter | Cache reservations successfully acquired. |
| `flyte:cacheservice:cache:release_reservation_success_unlabeled` | Counter | Cache reservations successfully released. |

### Authorizer

| Metric | Type | Description |
|--------|------|-------------|
| `authorizer:authorizer:cloudauthorizer:connect:authz_type_info` | Gauge | Info metric indicating the active authorization mode (labeled by `type`). |
| `authorizer:authorizer:cloudauthorizer:connect:authz_allowed` | Counter | Requests allowed by the authorizer, labeled by `identity_type` and `action`. |
| `authorizer:authorizer:cloudauthorizer:connect:authz_denied` | Counter | Requests denied by the authorizer, labeled by `identity_type` and `action`. |
| `authorizer:authorizer:cloudauthorizer:connect:authorize_duration_ms` | Summary | End-to-end authorization decision latency in milliseconds. |
| `authorizer:authorizer:cloudauthorizer:connect:backend_authorize_duration_ms_bucket` | Histogram | Backend authorization call latency distribution (external authz server or policy engine). |
| `authorizer:authorizer:cloudauthorizer:connect:backend_authorize_errors` | Counter | Backend authorization errors, labeled by `error_type`. |
| `authorizer:authorizer:cloudauthorizer:connect:authorize_errors_total` | Counter | Total authorization errors, labeled by `error_source`. |
| `authorizer:authorizer:cloudauthorizer:connect:external:fail_open_activated` | Counter | Fail-open mode activations — authorization bypass due to unreachable external backend. |
| `authorizer:authorizer:cloudauthorizer:connect:external:errors` | Counter | External authorization backend errors. Used in recording rules to compute error rate. |
| `authorizer:authorizer:cloudauthorizer:connect:external:authorize_duration_count` | Counter | External authorization call count. Used as denominator for error rate calculation. |

### Data Proxy

| Metric | Type | Description |
|--------|------|-------------|
| `dataproxy:domains:hits` | Counter | Domain resolution cache hits. |
| `dataproxy:domains:miss` | Counter | Domain resolution cache misses. |
| `dataproxy:clusterpoolcache:hits` | Counter | Cluster pool routing cache hits. |
| `dataproxy:clusterpoolcache:miss` | Counter | Cluster pool routing cache misses. |
| `dataproxy:images:read:success_ms_count` | Counter | Successful image metadata reads from dataplane. |
| `dataproxy:images:read:failure_ms_count` | Counter | Failed image metadata reads from dataplane. |
| `dataproxy:secrets_service:cluster_errors` | Counter | Per-cluster secret proxy errors during fan-out operations, labeled by `cluster` and `operation`. |

### Usage service

| Metric | Type | Description |
|--------|------|-------------|
| `usage:svc:report_billable_usage` | Counter | Billable usage reports submitted. |
| `usage:messages:messages_received` | Counter | Usage messages received. |
| `usage:messages:messages_sent` | Counter | Usage messages sent. |
| `usage:messages:messages_dropped` | Counter | Usage messages dropped. |
| `usage:messages:messages_failed` | Counter | Usage message processing failures. |
| `usage:messages:messages_processed` | Counter | Usage messages successfully processed. |
| `usage:messages:processing_time_ms` | Summary | Usage message processing latency in milliseconds. |

### Infrastructure

| Metric | Type | Description |
|--------|------|-------------|
| `container_cpu_usage_seconds_total` | Counter | Cumulative CPU time consumed per container, in cores. |
| `container_memory_working_set_bytes` | Gauge | Working set memory per container in bytes. Watch for values approaching resource limits. |

---

## Dataplane metrics

### Health

| Metric | Type | Description |
|--------|------|-------------|
| `kube_deployment_status_replicas_available` | Gauge | Available replicas per DP deployment. |
| `kube_deployment_spec_replicas` | Gauge | Desired replica count per DP deployment. |
| `kube_pod_container_status_restarts_total` | Counter | Cumulative container restart count in the DP namespace. |
| `flyte:propeller:all:execstats:active_workflow_executions` | Gauge | Current active FlyteWorkflow CRD count managed by propeller. |
| `executor:handler_panic` | Gauge | Handler panic count in DP executor. |

### Union Operator

| Metric | Type | Description |
|--------|------|-------------|
| `union_operator:work_queue:operations_processed` | Counter | Execution operations successfully processed. |
| `union_operator:work_queue:operations_failed` | Counter | Execution operations that failed processing. |
| `union_operator:heartbeat_updater:runs` | Counter | Heartbeat update cycle runs. |
| `union_operator:heartbeat_updater:run_errors` | Counter | Heartbeat update cycle errors. |
| `union_operator:status_updater:runs` | Counter | Status update cycle runs. |
| `union_operator:status_updater:run_errors` | Counter | Status update cycle errors. |
| `union_operator:prometheus_health_checker:run_errors` | Counter | Prometheus health check errors. |
| `union_operator:heartbeat:compute_capabilities_ms` | Summary | Time to compute cluster capabilities during heartbeat (milliseconds). |
| `union_operator:heartbeat:compute_usages_ms` | Summary | Time to compute resource usages during heartbeat (milliseconds). |
| `union_operator:heartbeat:list_workflows_ms` | Summary | Time to list workflows during heartbeat (milliseconds). |
| `union_operator:config_syncer:runs` | Counter | Config sync cycle runs. |
| `union_operator:config_syncer:run_errors` | Counter | Config sync cycle errors. |
| `union_operator:config_syncer:propeller_configmap_updated` | Counter | Propeller ConfigMap updates triggered by config syncer. |
| `union_operator:billable_usage_collector:runs` | Counter | Billing collection cycle runs. |
| `union_operator:billable_usage_collector:run_errors` | Counter | Billing collection cycle errors. Failures mean billing data may be delayed. |
| `union_operator:work_queue:paused` | Gauge | 1 when operator paused due to resource limits (FlyteWorkflow count or storage exceeded). |

### Executor (V2)

| Metric | Type | Description |
|--------|------|-------------|
| `executor:active_actions_count` | Gauge | Current active V2 actions. |
| `executor:available_capacity` | Gauge | Available executor capacity. Zero means executor is saturated. |
| `executor:discovery_miss_count` | Counter | V2 cache discovery misses for task output caching. |
| `executor:discovery_put_success_count` | Counter | V2 cache discovery successful puts. |
| `executor:actions_terminated` | Counter | Task completion count, labeled by `phase` (Succeeded, Failed, Aborted). Key V2 SLI for task health. |
| `executor:evaluator:evaluate_duration` | Summary | Time spent in RecursiveNodeHandler (pod creation). Dominant component of V2 task latency. |
| `executor:system_failures` | Counter | System failures (retryable). |
| `executor:system_failures_exhausted` | Counter | System failures with retries exhausted — task permanently failed. |
| `executor:invalid_leases` | Counter | Invalid leases received from queue service (malformed). |
| `executor:evaluator:evaluate_errors` | Counter | Evaluator errors during task processing. |

### Flyte Propeller (V1)

| Metric | Type | Description |
|--------|------|-------------|
| `flyte:propeller:all:round:round_time_unlabeled_ms` | Summary | Propeller reconciliation round time in milliseconds. One round = one FlyteWorkflow CRD processed. |
| `flyte:propeller:all:round:success_count` | Counter | Successful propeller rounds. |
| `flyte:propeller:all:round:error_count` | Counter | Failed propeller rounds. |
| `flyte:propeller:all:round:panic_unlabeled` | Counter | Panics during propeller rounds. |
| `flyte:propeller:all:free_workers_count` | Gauge | Idle propeller worker goroutines. Zero means all workers busy processing workflows. |
| `flyte:propeller:all:main_depth` | Gauge | Main workqueue depth. |
| `flyte:propeller:all:sub_depth` | Gauge | Sub workqueue depth. |
| `flyte:propeller:all:main_adds` | Counter | Items enqueued to propeller's main workqueue. |
| `flyte:propeller:all:sub_adds` | Counter | Items enqueued to propeller's sub workqueue. |
| `flyte:propeller:all:main_retries` | Counter | Main workqueue retries. |
| `flyte:propeller:all:wf_updated` | Counter | Successful FlyteWorkflow etcd writes. |
| `flyte:propeller:all:wf_update_failed` | Counter | Failed FlyteWorkflow etcd writes. |
| `flyte:propeller:all:wf_too_large` | Counter | FlyteWorkflow objects exceeding 1.5MB etcd size limit. |
| `flyte:propeller:all:wf_update_conflict` | Counter | Optimistic concurrency conflicts on FlyteWorkflow writes. |
| `flyte:propeller:all:wf_update_latency_ms` | Summary | etcd write latency for FlyteWorkflow status updates (milliseconds). |
| `flyte:propeller:all:node:queueing_latency_unlabeled_ms` | Summary | Node queueing latency: time from queued to running (milliseconds). |
| `flyte:propeller:all:node:node_exec_latency_unlabeled_us` | Summary | Node execution latency: time spent in handler (microseconds). |
| `flyte:propeller:all:metastore:cache_hit` | Counter | In-memory cache hits for object store (S3/GCS) reads. |
| `flyte:propeller:all:metastore:cache_miss` | Counter | In-memory cache misses for object store reads. Low hit rate indicates excessive storage calls. |
| `flyte:propeller:all:execstats:active_workflow_executions` | Gauge | Active workflow execution count. |
| `flyte:propeller:all:execstats:active_node_executions` | Gauge | Active node execution count. |
| `flyte:propeller:all:execstats:active_task_executions` | Gauge | Active task execution count. |
| `flyte:propeller:all:task:event_recording:success_duration_ms_count` | Counter | Successful task event recordings to FlyteAdmin. |
| `flyte:propeller:all:node:event_recording:success_duration_ms_count` | Counter | Successful node event recordings to FlyteAdmin. |
| `flyte:propeller:all:task:event_recording:failure_duration_ms_count` | Counter | Failed task event recordings. Indicates CP connectivity issues. |
| `flyte:propeller:all:node:event_recording:failure_duration_ms_count` | Counter | Failed node event recordings. |
| `flyte:propeller:all:discovery_hit_count` | Counter | Task output cache discovery hits. |
| `flyte:propeller:all:discovery_miss_count` | Counter | Task output cache discovery misses. |
| `flyte:propeller:all:discovery_skip_count` | Counter | Task output cache discovery skips. |
| `flyte:propeller:all:discovery_get_failure_count` | Counter | Task output cache discovery get failures. |

### K8s API client

| Metric | Type | Description |
|--------|------|-------------|
| `k8s_client_request_total_unlabeled` | Counter | Propeller's total K8s API requests. High rates may indicate excessive pod watches or creates. |
| `k8s_client_request_latency_unlabeled_bucket` | Histogram | K8s API request latency distribution. |
| `k8s_client_rate_limiter_latency_unlabeled_bucket` | Histogram | Client-side rate limiter wait time distribution. Non-zero indicates the K8s API client is being throttled. |

### gRPC client (DP to CP)

| Metric | Type | Description |
|--------|------|-------------|
| `grpc_client_handled_total` | Counter | DP-to-CP gRPC client request count, labeled by `grpc_service`, `grpc_method`, `grpc_code`. |
| `grpc_client_handling_seconds_bucket` | Histogram | DP-to-CP gRPC call latency distribution. High latency indicates slow control plane or network issues. |

### Infrastructure

| Metric | Type | Description |
|--------|------|-------------|
| `container_cpu_usage_seconds_total` | Counter | Cumulative CPU time consumed per DP container. |
| `container_memory_working_set_bytes` | Gauge | Working set memory per DP container. Watch for values approaching resource limits. |

---

## Recording rules

Recording rules are pre-computed by Prometheus and used in dashboard panels and alert conditions. They are defined in the PrometheusRule CRDs shipped with the Helm charts.

### Controlplane recording rules (always active)

These rules are always enabled when `monitoring.prometheusRules.enabled: true` (default). Evaluation interval: 30s.

| Rule | What it computes | Source metrics |
|------|-----------------|----------------|
| `union:cp:service_availability` | Min availability ratio across all CP deployments | `kube_deployment_status_replicas_available` / `kube_deployment_spec_replicas` |
| `union:cp:pod_restart_rate_1h` | Pod restart count over the last hour | `kube_pod_container_status_restarts_total` |
| `union:cp:connect_request_rate:by_service` | Connect request rate per service (5m window) | `connect:server_requests_handled_total` |
| `union:cp:connect_error_rate:by_service` | Connect error rate per service (non-OK codes, 5m window) | `connect:server_requests_handled_total` |
| `union:cp:ingress_request_rate` | Total ingress request rate (5m window) | `nginx_ingress_controller_request_duration_seconds_count` |
| `union:cp:ingress_error_rate_5xx` | Ingress 5xx error rate (5m window) | `nginx_ingress_controller_request_duration_seconds_count` |
| `union:cp:authz:external_error_rate` | External authorizer error rate as a fraction | `authorizer:...:external:errors` / `authorizer:...:external:authorize_duration_count` |

### Controlplane SLO recording rules (opt-in)

Enabled when `monitoring.slos.enabled: true`. Evaluation interval: 30s.

| Rule | What it computes | Source metrics |
|------|-----------------|----------------|
| `union:cp:slo:availability:ratio` | Average deployment availability across all CP services | `kube_deployment_status_replicas_available` / `kube_deployment_spec_replicas` |
| `union:cp:slo:connect_success_rate` | Fraction of Connect requests with OK/Canceled/NotFound codes | `connect:server_requests_handled_total` |
| `union:cp:slo:ingress_success_rate` | Fraction of ingress requests with non-5xx status | `nginx_ingress_controller_request_duration_seconds_count` |
| `union:cp:slo:ingress_latency_p99` | Ingress p99 latency in seconds | `nginx_ingress_controller_request_duration_seconds_bucket` |
| `union:cp:slo:error_budget_remaining` | Fraction of error budget remaining (< 0 = exhausted) | Derived from `union:cp:slo:connect_success_rate` and configured availability target |

### Dataplane recording rules (always active)

These rules are always enabled when `monitoring.prometheusRules.enabled: true` (default). Evaluation interval: 30s.

| Rule | What it computes | Source metrics |
|------|-----------------|----------------|
| `union:dp:service_availability` | Min availability ratio across all DP deployments | `kube_deployment_status_replicas_available` / `kube_deployment_spec_replicas` |
| `union:dp:propeller:round_latency_p99` | Propeller round time at p99 | `flyte:propeller:all:round:round_time_unlabeled_ms` |
| `union:dp:propeller:active_workflows` | Total active workflow executions | `flyte:propeller:all:execstats:active_workflow_executions` |
| `union:dp:propeller:queue_depth` | Total propeller main workqueue depth | `flyte:propeller:all:main_depth` |
| `union:dp:operator:work_queue_failed_rate` | Operator work queue failure rate (5m window) | `union_operator:work_queue:operations_failed` |
| `union:dp:executor:active_actions` | Current executor active action count | `executor:active_actions_count` |

### Dataplane SLO recording rules (opt-in)

Enabled when `monitoring.slos.enabled: true`. Evaluation interval: 30s.

| Rule | What it computes | Source metrics |
|------|-----------------|----------------|
| `union:dp:slo:availability:ratio` | Average deployment availability across all DP services | `kube_deployment_status_replicas_available` / `kube_deployment_spec_replicas` |
| `union:dp:slo:propeller_success_rate` | Fraction of propeller rounds that succeed | `flyte:propeller:all:round:success_count` / (`success_count` + `error_count`) |
| `union:dp:slo:propeller_round_latency_p99` | Propeller round p99 latency in seconds | `flyte:propeller:all:round:round_time_unlabeled_ms` / 1000 |
| `union:dp:slo:executor_success_rate` | Fraction of V2 actions that succeed | `executor:actions_terminated{phase="Succeeded"}` / total terminated |
| `union:dp:slo:execution_success_rate` | Combined V1+V2 execution success rate (average of propeller + executor) | Derived from `propeller_success_rate` and `executor_success_rate` |
| `union:dp:slo:error_budget_remaining` | Fraction of error budget remaining (< 0 = exhausted) | Derived from `union:dp:slo:execution_success_rate` and configured availability target |

---

## Alert rules

Alert rules fire when conditions are met for the specified duration. They are opt-in and require explicit Helm configuration to enable.

### Controlplane operational alerts

Enabled when `monitoring.alerting.enabled: true`.

| Alert | Severity | Condition | For | Description |
|-------|----------|-----------|-----|-------------|
| `UnionCPServiceDown` | critical | `replicas_available == 0` | 5m | A CP deployment has zero available replicas. |
| `UnionCPHighRestartRate` | warning | `restarts > 5 in 1h` | 5m | A pod is restarting frequently (crash loop). |
| `UnionCPHandlerPanic` | critical | `panic count > 0 in 1h` | 0m | Unrecovered panic in any CP service handler. |
| `UnionCPAuthorizerExternalErrors` | warning | `error rate > 0.1/s` | 5m | External authorization backend returning errors. |
| `UnionCPAuthorizerFailOpenActive` | critical | `fail_open rate > 0` | 1m | Authorization bypass due to unreachable external backend. |
| `UnionCPAuthorizerHighDenyRate` | warning | `deny rate > 50%` | 10m | Possible authorization policy misconfiguration. |

### Controlplane SLO alerts

Enabled when both `monitoring.slos.enabled: true` and `monitoring.slos.alerting.enabled: true`.

| Alert | Severity | Condition | For | Description |
|-------|----------|-----------|-----|-------------|
| `UnionCPHighErrorBudgetBurn` | warning | `error_budget_remaining < 50%` | 15m | More than half the error budget has been consumed. |
| `UnionCPErrorBudgetExhausted` | critical | `error_budget_remaining < 0` | 5m | Error budget fully exhausted. |
| `UnionCPIngressLatencySLOBreach` | warning | `p99 > target` | 10m | Ingress p99 latency exceeding the configured SLO target. |

### Dataplane operational alerts

Enabled when `monitoring.alerting.enabled: true`.

| Alert | Severity | Condition | For | Description |
|-------|----------|-----------|-----|-------------|
| `UnionDPServiceDown` | critical | `replicas_available == 0` | 5m | A DP deployment has zero available replicas. |
| `UnionDPHighRestartRate` | warning | `restarts > 5 in 1h` | 5m | A pod is restarting frequently (crash loop). |
| `UnionDPHandlerPanic` | critical | `executor panic > 0 in 1h` | 0m | Handler panic detected in DP executor. |

### Dataplane SLO alerts

Enabled when both `monitoring.slos.enabled: true` and `monitoring.slos.alerting.enabled: true`.

| Alert | Severity | Condition | For | Description |
|-------|----------|-----------|-----|-------------|
| `UnionDPHighErrorBudgetBurn` | warning | `error_budget_remaining < 50%` | 15m | More than half the error budget has been consumed. |
| `UnionDPErrorBudgetExhausted` | critical | `error_budget_remaining < 0` | 5m | Error budget fully exhausted. |
| `UnionDPPropellerLatencySLOBreach` | warning | `p99 > target` | 10m | Propeller p99 latency exceeding the configured SLO target. |
