---
title: "Data Models"
date: 2023-01-01
draft: false
---

# Data Models

This section describes the data models and schemas used across our API endpoints.

## User Model

```json
{
  "id": "usr_123abc456def",
  "email": "user@example.com",
  "username": "johndoe",
  "first_name": "John",
  "last_name": "Doe",
  "role": "user",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier for the user |
| email | string | User's email address |
| username | string | Unique username |
| first_name | string | User's first name |
| last_name | string | User's last name |
| role | string | User's role (user, admin) |
| created_at | string | ISO 8601 timestamp of creation |
| updated_at | string | ISO 8601 timestamp of last update |

## Project Model

```json
{
  "id": "prj_789xyz123abc",
  "name": "My Project",
  "description": "Project description",
  "owner_id": "usr_123abc456def",
  "status": "active",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier for the project |
| name | string | Project name |
| description | string | Project description |
| owner_id | string | ID of the project owner |
| status | string | Project status (active, archived) |
| created_at | string | ISO 8601 timestamp of creation |
| updated_at | string | ISO 8601 timestamp of last update |

## Error Model

```json
{
  "error": "error_code",
  "message": "Human readable error message",
  "details": {
    "field": ["Error details"]
  }
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| error | string | Error code identifier |
| message | string | Human-readable error message |
| details | object | Additional error details |

## Common Patterns

### Timestamps

All timestamps are returned in ISO 8601 format with UTC timezone:
```
YYYY-MM-DDThh:mm:ssZ
```

### IDs

Resource IDs follow the pattern:
```
{resource_type}_{unique_identifier}
```

### Pagination

List endpoints return paginated results in this format:
```json
{
  "data": [],
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 10
  }
}
```

## See Also

- [Queries](/api-reference/data/queries/)
- [Mutations](/api-reference/data/mutations/)
- [Rate Limits](/api-reference/rate-limits/overview/)