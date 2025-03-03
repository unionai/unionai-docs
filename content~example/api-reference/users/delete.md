---
title: "Delete User"
date: 2023-01-01
draft: false
---

# Delete User

Permanently remove a user account from the system.

## Endpoint

```
DELETE /v1/users/{user_id}
```

## Authentication

Requires an API key or OAuth 2.0 token with `write` scope.

## Path Parameters

- `user_id`: The unique identifier of the user to delete

## Response

### Success Response (204 No Content)

A successful deletion returns no content.

### Error Responses

#### 404 Not Found

```json
{
  "error": "not_found",
  "message": "User not found"
}
```

#### 403 Forbidden

```json
{
  "error": "forbidden",
  "message": "Insufficient permissions to delete user"
}
```

## Example Request

### Using cURL

```bash
curl -X DELETE https://api.example.com/v1/users/usr_123abc456def \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Using Python

```python
import requests

headers = {
    'Authorization': 'Bearer YOUR_API_KEY'
}

response = requests.delete(
    'https://api.example.com/v1/users/usr_123abc456def',
    headers=headers
)
```

## Notes

- This action cannot be undone
- Associated data may also be deleted
- Consider implementing soft delete for recoverable deletion
- Rate limits apply to this endpoint

## See Also

- [Create User](/api-reference/users/create/)
- [Update User](/api-reference/users/update/)
- [Authentication](/api-reference/auth/getting-started/)
- [Rate Limits](/api-reference/rate-limits/overview/)