---
title: "Queries"
date: 2023-01-01
draft: false
---

# Queries

This section covers how to retrieve data using our API query endpoints.

## Query Structure

All query endpoints follow a consistent structure:

```
GET /v1/{resource}?{parameters}
```

## Common Parameters

### Pagination

| Parameter | Type | Description | Default |
|-----------|------|-------------|----------|
| page | integer | Page number | 1 |
| per_page | integer | Items per page | 10 |

### Filtering

| Parameter | Type | Description | Example |
|-----------|------|-------------|----------|
| filter[field] | string | Field to filter on | filter[status]=active |
| sort | string | Field to sort by | sort=created_at |
| order | string | Sort order (asc/desc) | order=desc |

## Example Queries

### List Users

```bash
curl -X GET "https://api.example.com/v1/users?page=1&per_page=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Filter Projects

```bash
curl -X GET "https://api.example.com/v1/projects?filter[status]=active&sort=created_at&order=desc" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Response Format

```json
{
  "data": [
    {
      "id": "usr_123",
      "type": "user",
      "attributes": {
        "email": "user@example.com",
        "username": "johndoe"
      }
    }
  ],
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 10
  },
  "links": {
    "self": "https://api.example.com/v1/users?page=1",
    "next": "https://api.example.com/v1/users?page=2",
    "prev": null
  }
}
```

## Error Handling

### 400 Bad Request

```json
{
  "error": "invalid_parameter",
  "message": "Invalid filter parameter",
  "details": {
    "filter": ["Unknown field: status"]
  }
}
```

### 404 Not Found

```json
{
  "error": "not_found",
  "message": "Resource not found"
}
```

## Best Practices

1. Always use pagination for large datasets
2. Include only necessary fields in responses
3. Use appropriate filters to minimize data transfer
4. Handle rate limits appropriately

## Performance Considerations

- Use indexes for filtered fields
- Limit response size with pagination
- Cache frequently accessed data
- Monitor query performance

## See Also

- [Data Models](/api-reference/data/models/)
- [Mutations](/api-reference/data/mutations/)
- [Rate Limits](/api-reference/rate-limits/overview/)