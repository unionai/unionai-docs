---
title: "Create User"
date: 2023-01-01
draft: false
---

# Create User

Create a new user account in the system.

## Endpoint

```
POST /v1/users
```

## Authentication

Requires an API key or OAuth 2.0 token with `write` scope.

## Request Body

```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123",
  "first_name": "John",
  "last_name": "Doe",
  "role": "user"
}
```

### Required Fields

- `email`: User's email address (string)
- `username`: Unique username (string)
- `password`: User's password (string, min 8 characters)

### Optional Fields

- `first_name`: User's first name (string)
- `last_name`: User's last name (string)
- `role`: User's role (string, default: "user")

## Response

### Success Response (201 Created)

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

### Error Responses

#### 400 Bad Request

```json
{
  "error": "validation_error",
  "message": "Invalid request parameters",
  "details": {
    "email": ["Invalid email format"],
    "password": ["Password must be at least 8 characters"]
  }
}
```

#### 409 Conflict

```json
{
  "error": "conflict",
  "message": "User with this email already exists"
}
```

## Example Request

### Using cURL

```bash
curl -X POST https://api.example.com/v1/users \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Using Python

```python
import requests

headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

data = {
    'email': 'user@example.com',
    'username': 'johndoe',
    'password': 'securepassword123',
    'first_name': 'John',
    'last_name': 'Doe'
}

response = requests.post(
    'https://api.example.com/v1/users',
    headers=headers,
    json=data
)
```

## Notes

- Passwords are automatically hashed before storage
- Email verification may be required depending on your configuration
- Rate limits apply to this endpoint

## See Also

- [Update User](/api-reference/users/update/)
- [Delete User](/api-reference/users/delete/)
- [Authentication](/api-reference/auth/getting-started/)
- [Rate Limits](/api-reference/rate-limits/overview/)
