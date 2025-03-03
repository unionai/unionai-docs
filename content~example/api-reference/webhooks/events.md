---
title: "Webhook Events"
date: 2023-01-01
draft: false
---

# Webhook Events

This guide covers all available webhook events and their payload structures.

## Event Types

### User Events

#### user.created

Triggered when a new user is created.

```json
{
  "id": "evt_123abc",
  "type": "user.created",
  "created_at": "2023-01-01T12:00:00Z",
  "data": {
    "user_id": "usr_456def",
    "email": "user@example.com",
    "username": "johndoe"
  }
}
```

#### user.updated

Triggered when user information is modified.

```json
{
  "id": "evt_789xyz",
  "type": "user.updated",
  "created_at": "2023-01-01T12:00:00Z",
  "data": {
    "user_id": "usr_456def",
    "changes": {
      "email": {
        "old": "old@example.com",
        "new": "new@example.com"
      }
    }
  }
}
```

#### user.deleted

Triggered when a user account is deleted.

```json
{
  "id": "evt_abc123",
  "type": "user.deleted",
  "created_at": "2023-01-01T12:00:00Z",
  "data": {
    "user_id": "usr_456def"
  }
}
```

### Project Events

#### project.created

Triggered when a new project is created.

```json
{
  "id": "evt_def456",
  "type": "project.created",
  "created_at": "2023-01-01T12:00:00Z",
  "data": {
    "project_id": "prj_789xyz",
    "name": "New Project",
    "owner_id": "usr_456def"
  }
}
```

#### project.updated

Triggered when project details are modified.

```json
{
  "id": "evt_ghi789",
  "type": "project.updated",
  "created_at": "2023-01-01T12:00:00Z",
  "data": {
    "project_id": "prj_789xyz",
    "changes": {
      "name": {
        "old": "Old Name",
        "new": "New Name"
      }
    }
  }
}
```

## Event Structure

All webhook events follow this structure:

```json
{
  "id": "evt_unique_id",
  "type": "resource.action",
  "created_at": "ISO8601_TIMESTAMP",
  "data": {
    "resource_specific_data": "value"
  }
}
```

### Common Fields

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique event identifier |
| type | string | Event type identifier |
| created_at | string | ISO 8601 timestamp |
| data | object | Event-specific payload |

## Best Practices

1. **Event Processing**
   - Process events asynchronously
   - Implement idempotency checks
   - Store raw event data before processing

2. **Error Handling**
   - Implement retry logic
   - Log failed event processing
   - Set up monitoring for event processing

3. **Security**
   - Verify webhook signatures
   - Use HTTPS endpoints
   - Implement request timeouts

## Rate Limits

Webhook event delivery is subject to rate limits. See our [Rate Limits](/api-reference/rate-limits/overview/) documentation.

## See Also

- [Webhook Setup](/api-reference/webhooks/setup/)
- [Security Best Practices](/api-reference/webhooks/security/)
- [API Authentication](/api-reference/auth/getting-started/)