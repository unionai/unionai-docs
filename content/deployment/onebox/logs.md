---
title: Task logs
description: Keep the logs of finished tasks available in the UI by shipping container logs to onebox's bucket with fluent-bit.
icon: journal-text
weight: 7
variants: -flyte +union
---

# Task logs

The Logs tab streams a task's logs from its pod while the pod exists. Onebox deletes task pods when they finish, so to keep logs available afterwards, ship container logs to onebox's bucket with a log shipper. Onebox reads them back from there once the pod is gone. This page uses [fluent-bit](https://fluentbit.io), installed separately; onebox doesn't depend on it to start.

## Where onebox reads logs

For a container that no longer exists, onebox reads every object under this prefix in its bucket, in key order:

```text
persisted-logs/namespace-<namespace>.pod-<pod>.cont-<container>/
```

Each object holds JSON lines with `time` (RFC 3339), `stream`, and `log`, which is what fluent-bit's tail input produces for container logs. Name objects so their keys sort by time.

## Install fluent-bit

Save this as `fluent-bit-values.yaml`, replacing the namespace, bucket, region, and endpoint. Leave out `endpoint` for Amazon S3.

```yaml
tolerations:
  - operator: Exists
# Credentials for the bucket. With IRSA, annotate the service account instead:
# serviceAccount: {annotations: {eks.amazonaws.com/role-arn: <role>}}
envFrom:
  - secretRef:
      name: onebox-s3          # AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY
config:
  inputs: |
    [INPUT]
        Name                tail
        Tag                 namespace-<namespace_name>.pod-<pod_name>.cont-<container_name>
        Tag_Regex           (?<pod_name>[a-z0-9](?:[-a-z0-9]*[a-z0-9])?(?:\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*)_(?<namespace_name>[^_]+)_(?<container_name>.+)-
        Path                /var/log/containers/*_union_*.log
        DB                  /var/log/flb_onebox.db
        multiline.parser    docker, cri
        Mem_Buf_Limit       5MB
        Skip_Long_Lines     On
        Refresh_Interval    10
  filters: ""
  outputs: |
    [OUTPUT]
        Name             s3
        Match            *
        upload_timeout   1m
        s3_key_format    /persisted-logs/$TAG/%Y%m%d%H%M%S-$UUID
        json_date_key    false
        region           <region>
        bucket           <bucket>
        endpoint         <https://store endpoint>
```

`Path` limits the shipper to onebox's namespace (`union` here). Install it in the same namespace, so it can read the credentials Secret:

```shell
helm install fluent-bit fluent-bit --repo https://fluent.github.io/helm-charts \
  --version 0.48.9 -n union -f fluent-bit-values.yaml
```

fluent-bit uploads at most once a minute, so the last minute of a finished task appears in the Logs tab up to a minute after the task ends.

## Gotchas

| Symptom | Cause and fix |
|---|---|
| The fluent-bit pods stay in `ContainerCreating` with `hostPath type check failed: /etc/machine-id` | The chart mounts `/etc/machine-id`, which some nodes (k3d, kind) don't have. Mount only `/var/log`: set `daemonSetVolumes` and `daemonSetVolumeMounts` to a single `hostPath` volume for `/var/log`. |
| Only the last minute of a long task's logs is shown | `s3_key_format` writes the same key on every upload (for example `static_file_path true` without a timestamp), so each upload overwrites the previous one. Use a per-upload key as above. |
| Logs of finished tasks fail with `LIMIT_EXCEEDED` | A single object is larger than `storage.limits.maxDownloadMBs` in onebox's configuration (default `1024`). |
