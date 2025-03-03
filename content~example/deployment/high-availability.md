---
title: "High Availability Setup"
weight: 2
---

# High Availability Setup

Learn how to configure Union AI for high availability and fault tolerance.

## Architecture Overview

### Components

- Control Plane
- Worker Nodes
- Database Cluster
- Message Queue

## Cluster Configuration

### Control Plane HA

1. Configure multiple control plane nodes:
```yaml
controlPlane:
  replicas: 3
  nodes:
    - name: master-1
      zone: us-east-1a
    - name: master-2
      zone: us-east-1b
    - name: master-3
      zone: us-east-1c
```

### Database HA

1. Set up database replication:
```yaml
database:
  type: postgresql
  replicas: 3
  replicationMode: synchronous
```

## Load Balancing

### External Load Balancer

```yaml
loadBalancer:
  type: nlb
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
```

## Monitoring

### Health Checks

1. Configure health probes:
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
```

## Backup and Recovery

### Automated Backups

1. Enable backup schedule:
```yaml
backup:
  schedule: "0 2 * * *"
  retention: 7d
  storage:
    type: s3
    bucket: unionai-backups
```

## Disaster Recovery

### Multi-Region Setup

- Primary region configuration
- Failover region setup
- Data synchronization

## Next Steps

- Configure [Authentication](../authentication)
- Set up [Monitoring](../monitoring)
- Review [Scaling Strategies](../scaling)