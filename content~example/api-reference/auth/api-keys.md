---
title: "API Keys"
date: 2023-01-01
draft: false
---

# API Keys

API keys are the recommended authentication method for server-side applications. This guide explains how to create, manage, and use API keys securely.

## Creating API Keys

1. Log into your developer dashboard
2. Navigate to the API Keys section
3. Click "Create New API Key"
4. Name your key and select the appropriate permissions
5. Store the key securely - it won't be shown again

## Using API Keys

### HTTP Header Format

```bash
Authorization: Bearer YOUR_API_KEY
```

### Example Request

```python
import requests

headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

response = requests.get('https://api.example.com/v1/resources', headers=headers)
```

## Best Practices

1. **Never share your API keys**
2. **Rotate keys regularly**
3. **Use different keys for development and production**
4. **Set appropriate permissions**
5. **Monitor key usage**

## Key Management

### Rotating Keys

1. Create a new API key
2. Update your applications to use the new key
3. Monitor for any calls using the old key
4. Deactivate the old key

### Revoking Keys

If a key is compromised:
1. Immediately deactivate the key in the dashboard
2. Review security logs for unauthorized access
3. Create a new key with appropriate permissions

## Security Considerations

- Store keys in secure environment variables
- Never commit keys to version control
- Use key rotation schedules
- Implement IP whitelisting when possible

## Rate Limits

API key requests are subject to rate limits. See our [Rate Limits](/api-reference/rate-limits/overview/) documentation for details.

## Support

For issues with API keys, contact our support team or check the [FAQ](/user-guide/troubleshooting/faq/).