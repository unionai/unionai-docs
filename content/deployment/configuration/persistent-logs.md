---
title: Persistent logs
weight: 4
variants: -flyte -serverless -byoc +selfmanaged
---

# Persistent logs

Persisted logging is enabled by default and uses an object store to store task logs. By default persisted logs (also called Task Logs) will be stored in the `persisted-logs/*` path on the Storage  endpoint configured for your data plane.

