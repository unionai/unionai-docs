---
title: "Kubernetes RBAC: Control plane"
weight: 1
variants: -flyte +union
---

# Kubernetes RBAC: Control plane

**All roles are ClusterRole**

| Role Name | Purpose | API Groups | Resources | Verbs |
| --- | --- | --- | --- | --- |
| `flyteadmin` | Full control over K8s resources for workflow orchestration, namespace provisioning, RBAC setup for workspaces | ""(core) `flyte.lyft.com rbac.authorization.k8s.io` | `configmaps flyteworkflows namespaces pods resourcequotas roles rolebindings secrets services serviceaccounts spark-role limitranges` | *(all) |
| `scyllacluster-edit` | Aggregated admin/edit role for ScyllaDB cluster management (control plane database) | `scylla.scylladb.com` | `scyllaclusters scylladbmonitorings scylladbdatacenters scylladbclusters scylladbmanagerclusterregistrations scylladbmanagertasks` | `create patch update delete deletecollection` |
| `scylladb:controller:aggregate-to-operator` | ScyllaDB operator controller - manages ScyllaDB cluster lifecycle for the control plane database | ""(core) `apps policy scylla.scylladb.com networking.k8s.io batch` | `events nodes endpoints persistentvolumeclaims pods services configmaps secrets statefulsets deployments daemonsets jobs poddisruptionbudgets serviceaccounts scyllaclusters scyllaoperatorconfigs nodeconfigs ingresses` | `get list watch create update delete patch` |
| `scylla-operator:webhook` | ScyllaDB webhook server for admission control of ScyllaDB resources | `admissionregistration.k8s.io scylla.scylladb.com` | `validatingwebhookconfigurations mutatingwebhookconfigurations scyllaclusters nodeconfigs scyllaoperatorconfigs scylladbdatacenters scylladbclusters scylladbmanagertasks` | `get list watch create update patch delete` |
| `console-clusterrole` | Read-only access for Union Console UI to display namespaces, workflows, and pod logs | ""(core) `flyte.lyft.com` | `namespaces flyteworkflows pods pods/log` | `get list watch` |
| `authorizer-clusterrole` | Authorizer service reads namespaces for authorization decisions | ""(core) | `namespaces` | `get list watch` |
| `cluster-clusterrole` | Cluster management service monitors cluster state for health and capacity | ""(core) `apps` | `namespaces nodes replicasets deployments` | `get list watch` |
| `dataproxy-clusterrole` | DataProxy service reads secrets for presigned URL generation and data relay configuration | ""(core) | `secrets` | `get list watch` |
| `executions-clusterrole` | Executions service reads workflow state for execution management and status tracking | ""(core) `flyte.lyft.com` | `namespaces configmaps flyteworkflows` | `get list watch` |
| `queue-clusterrole` | Queue service reads namespaces for task queue routing | ""(core) | `namespaces` | `get list watch` |
| `run-scheduler-clusterrole` | Run Scheduler reads namespaces to determine scheduling scope for workflows | ""(core) | `namespaces` | `get list watch` |
| `usage-clusterrole` | Usage tracking service reads namespaces for resource usage aggregation | ""(core) | `namespaces` | `get list watch` |
