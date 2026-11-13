---
title: ProtectedResourceMetadata
description: "What an MCP server advertises about its own authorization, per RFC 9728."
icon: braces
version: 2.13.4
variants: +flyte +union
layout: py_api
---

# ProtectedResourceMetadata

**Package:** `flyte.ai.mcp`

What an MCP server advertises about its own authorization, per RFC 9728.

Pass one to `FlyteMCPAppEnvironment.protected_resource_metadata` to let MCP clients that
implement the [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
discover how to obtain a token instead of needing one pasted into their configuration.

The identity provider must support authorization-code flow with PKCE S256 and either
permit dynamic client registration, accept an administrator-approved client ID metadata
document, or provide a preregistered client supported by the MCP client. Register the
client's exact redirect URI, assign its users, and allow the requested scopes. Advertising
a registration endpoint or metadata-document support does not grant permission to use it.

MCP clients send this server's URL as the RFC 8707 `resource` parameter. The provider
must accept that resource and issue an access token whose audience Flyte accepts; this
metadata cannot change provider policy or Flyte's audience validation. Providers that
reject anonymous registration require administrator setup before a complete sign-in flow.

This feature retains token passthrough: Flyte validates tokens on remote tool calls,
while local search tools accept any nonempty bearer token. It does not implement local
audience validation or token exchange and does not establish full MCP OAuth security
conformance. Configure those separately rather than weakening downstream token checks.

Hostnames, configured or taken from the request's Host header, are limited to DNS labels
(or a dotted IPv4 address) or a bracketed IPv6 address with an optional numeric port. URLs
containing `,` (or `;` in the authority) are rejected because challenge parameters are
comma-separated and some clients, including the reference MCP client, also parse unquoted
values. That client also finds parameters anywhere in the header, so the resource URL and
`mcp_mount_path` must not contain `scope=`, `resource_metadata=`, `error=`,
`error_description=`, `error_uri=` or `realm=` in any letter case.

```python
from flyte.ai.mcp import FlyteMCPAppEnvironment, ProtectedResourceMetadata

env = FlyteMCPAppEnvironment(
    name="flyte-mcp",
    requires_auth=False,
    protected_resource_metadata=ProtectedResourceMetadata(
        authorization_servers=["https://auth.example.com/oauth2/default"],
    ),
)
```


## Parameters

```python
class ProtectedResourceMetadata(
    authorization_servers: list[str] | None = None,
    resource: str | None = None,
    scopes_supported: list[str] | None = None,
    resource_name: str | None = None,
    resource_documentation: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `authorization_servers` | `list[str] \| None` | Issuer URLs of the OAuth 2.0 authorization servers whose tokens this server accepts. `None` (the default) advertises the issuer that the Flyte endpoint the server is connected to advertises itself, fetched once when the metadata is first requested; the server forwards each caller's token to that endpoint, so that issuer is normally the right one. Issuers must use HTTPS without query, fragment or userinfo. Lists are copied at construction and revalidated before publication if changed in process. |
| `resource` | `str \| None` | The resource identifier, i.e. the full URL clients use to reach the MCP endpoint (for example `https://mcp.example.com/flyte-mcp/mcp`). Clients reject metadata whose `resource` does not match the URL they connected to. `None` (the default) uses the request's ASGI scheme and Host, plus the MCP endpoint path. INTERNAL_APP_ENDPOINT_PATTERN is a private service URL and is not used. Set resource explicitly when a proxy rewrites the public host or path. For TLS termination, configure Uvicorn's proxy_headers and forwarded_allow_ips (or FORWARDED_ALLOW_IPS) to trust only the proxy that supplies X-Forwarded-Proto. Raw Forwarded and X-Forwarded-Host headers are never used for discovery. Explicit resource paths must not contain ?, #, { or } after one percent-decoding: the current auth middleware and Starlette routing cannot serve their metadata paths. This limitation applies to the path, not a URL query. |
| `scopes_supported` | `list[str] \| None` | OAuth scopes a client should request. Also sent as the `scope` parameter of the `401` challenge. |
| `resource_name` | `str \| None` | Human-readable name for the server, shown by some clients on their consent screen. |
| `resource_documentation` | `str \| None` | URL of documentation for developers using the server. |

