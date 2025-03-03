---
title: "OAuth 2.0"
date: 2023-01-01
draft: false
---

# OAuth 2.0 Integration

This guide explains how to implement OAuth 2.0 authentication for your applications. OAuth 2.0 is recommended for user-facing applications that need to access API resources on behalf of users.

{{< if-variant "serverless byoc" >}}

SERVERLESS OR BYOC

{{< /if-variant >}}

{{< if-variant "serverless" >}}

SERVERLESS

{{< /if-variant >}}

{{< if-variant "byoc" >}}

BYOC

Everything is taken care by our team. Nothing to worry.

{{< /if-variant >}}

## Prerequisites

Before implementing OAuth 2.0:

1. Register your application in the developer dashboard
2. Obtain your client ID and client secret
3. Configure your redirect URIs

## OAuth 2.0 Flow

### 1. Authorization Request

```
GET https://api.example.com/oauth/authorize
?client_id=YOUR_CLIENT_ID
&redirect_uri=YOUR_REDIRECT_URI
&response_type=code
&scope=read write
&state=random_state_string
```

### 2. User Consent

Users will be prompted to authorize your application's access to their data.

### 3. Authorization Code Exchange

```bash
curl -X POST https://api.example.com/oauth/token \
  -d client_id=YOUR_CLIENT_ID \
  -d client_secret=YOUR_CLIENT_SECRET \
  -d grant_type=authorization_code \
  -d code=AUTHORIZATION_CODE \
  -d redirect_uri=YOUR_REDIRECT_URI
```

### 4. Access Token Usage

{{< if-variant "serverless" >}}

```java
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/v1/user"))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .header("Content-Type", "application/json")
    .GET()
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

{{< /if-variant >}}

{{< if-variant "cpp" >}}

```cpp
#include <cpr/cpr.h>

auto response = cpr::Get(
    cpr::Url{"https://api.example.com/v1/user"},
    cpr::Header{{
        {"Authorization", "Bearer YOUR_ACCESS_TOKEN"},
        {"Content-Type", "application/json"}
    }}
);
```

{{< /if-variant >}}

{{< if-variant "go" >}}

```go
package main

import (
    "net/http"
)

func main() {
    client := &http.Client{}
    req, _ := http.NewRequest("GET", "https://api.example.com/v1/user", nil)
    req.Header.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    req.Header.Add("Content-Type", "application/json")

    resp, _ := client.Do(req)
}
```

{{< /if-variant >}}

## Scopes

- `read`: Read access to user data
- `write`: Write access to user data
- `admin`: Administrative access (requires special approval)

## Token Management

### Refresh Tokens

```bash
curl -X POST https://api.example.com/oauth/token \
  -d client_id=YOUR_CLIENT_ID \
  -d client_secret=YOUR_CLIENT_SECRET \
  -d grant_type=refresh_token \
  -d refresh_token=YOUR_REFRESH_TOKEN
```

### Token Expiration

- Access tokens expire after 1 hour
- Refresh tokens expire after 30 days
- Always handle token expiration gracefully in your application

## Security Best Practices

1. **Always use HTTPS**
2. **Validate state parameter**
3. **Store tokens securely**
4. **Implement PKCE for mobile apps**
5. **Regular token rotation**

## Error Handling

Common OAuth errors and how to handle them:

```json
{
  "error": "invalid_grant",
  "error_description": "Authorization code expired"
}
```

## Rate Limits

OAuth requests are subject to rate limits. See our [Rate Limits](/api-reference/rate-limits/overview/) documentation for details.

## Additional Resources

- [OAuth 2.0 Specification](https://oauth.net/2/)
- [Security Best Practices](/api-reference/webhooks/security/)
- [API Keys Alternative](/api-reference/auth/api-keys/)

## Support

For OAuth-related issues, contact our support team or check the [FAQ](/user-guide/troubleshooting/faq/).
