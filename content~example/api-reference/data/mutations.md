---
title: "Mutations"
date: 2023-01-01
draft: false
---

# Mutations

This section covers how to modify data using our API mutation endpoints.

## Mutation Structure

All mutation endpoints follow a consistent structure:

```
POST/PATCH/DELETE /v1/{resource}
```

## Common Headers

| Header        | Value               | Description          |
| ------------- | ------------------- | -------------------- |
| Content-Type  | application/json    | Request body format  |
| Authorization | Bearer YOUR_API_KEY | Authentication token |

## Request Format

### Create Resource

```bash
curl -X POST https://api.example.com/v1/resources \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Resource",
    "description": "Resource description"
  }'
```

### Update Resource

```bash
curl -X PATCH https://api.example.com/v1/resources/{id} \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Name"
  }'
```

### Delete Resource

```bash
curl -X DELETE https://api.example.com/v1/resources/{id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Response Format

### Success Response

```json
{
  "data": {
    "id": "res_123",
    "type": "resource",
    "attributes": {
      "name": "New Resource",
      "description": "Resource description",
      "created_at": "2023-01-01T12:00:00Z"
    }
  }
}
```

### Error Response

```json
{
  "error": "validation_error",
  "message": "Invalid request parameters",
  "details": {
    "name": ["Name is required"]
  }
}
```

## Optimistic Updates

When implementing mutations in your client application:

1. Update local state immediately
2. Send mutation request
3. Handle success/error responses
4. Revert local state if error occurs

## Batch Operations

For bulk updates:

```bash
curl -X POST https://api.example.com/v1/resources/batch \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "operations": [
      {
        "op": "create",
        "data": { "name": "Resource 1" }
      },
      {
        "op": "update",
        "id": "res_123",
        "data": { "name": "Updated Resource" }
      }
    ]
  }'
```

## Best Practices

1. Validate data before sending
2. Use appropriate HTTP methods
3. Implement proper error handling
4. Consider using transactions for related mutations
5. Implement retry logic for failed requests

## Error Handling

### Common Error Codes

| Code | Description  | Action                 |
| ---- | ------------ | ---------------------- |
| 400  | Bad Request  | Check request format   |
| 401  | Unauthorized | Verify credentials     |
| 403  | Forbidden    | Check permissions      |
| 404  | Not Found    | Verify resource exists |
| 409  | Conflict     | Resolve data conflicts |

## Rate Limits

Mutation requests are subject to rate limits. See our [Rate Limits](/api-reference/rate-limits/overview/) documentation for details.

## See Also

- [Data Models](/api-reference/data/models/)
- [Queries](/api-reference/data/queries/)
- [Authentication](/api-reference/auth/getting-started/)
