---
title: "Update User"
date: 2023-01-01
draft: false
---

# Update User

Update an existing user's information in the system.

## Endpoint

```
PATCH /v1/users/{user_id}
```

## Authentication

Requires an API key or OAuth 2.0 token with `write` scope.

## Path Parameters

- `user_id`: The unique identifier of the user to update

## Request Body

```json
{
  "email": "newemail@example.com",
  "username": "newusername",
  "first_name": "Jane",
  "last_name": "Smith",
  "role": "admin"
}
```

### Optional Fields

All fields are optional. Only include the fields you want to update.

- `email`: New email address (string)
- `username`: New username (string)
- `first_name`: New first name (string)
- `last_name`: New last name (string)
- `role`: New role (string)

## Response

### Success Response (200 OK)

```json
{
  "id": "usr_123abc456def",
  "email": "newemail@example.com",
  "username": "newusername",
  "first_name": "Jane",
  "last_name": "Smith",
  "role": "admin",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T13:00:00Z"
}
```

### Error Responses

#### 400 Bad Request

```json
{
  "error": "validation_error",
  "message": "Invalid request parameters",
  "details": {
    "email": ["Invalid email format"]
  }
}
```

#### 404 Not Found

```json
{
  "error": "not_found",
  "message": "User not found"
}
```

#### 409 Conflict

```json
{
  "error": "conflict",
  "message": "Username already taken"
}
```

## Example Request

### Using cURL

```bash
curl -X PATCH https://api.example.com/v1/users/usr_123abc456def \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newemail@example.com",
    "first_name": "Jane",
    "last_name": "Smith"
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
    'email': 'newemail@example.com',
    'first_name': 'Jane',
    'last_name': 'Smith'
}

response = requests.patch(
    'https://api.example.com/v1/users/usr_123abc456def',
    headers=headers,
    json=data
)
```

## Notes

- Only include fields that need to be updated
- Password updates require a separate endpoint for security
- Email changes may require verification
- Rate limits apply to this endpoint

## See Also

- [Create User](/api-reference/users/create/)
- [Delete User](/api-reference/users/delete/)
- [Authentication](/api-reference/auth/getting-started/)
- [Rate Limits](/api-reference/rate-limits/overview/)