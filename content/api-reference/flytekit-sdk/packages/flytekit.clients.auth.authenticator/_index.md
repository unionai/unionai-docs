---
title: flytekit.clients.auth.authenticator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.auth.authenticator

## Directory

### Classes

| Class | Description |
|-|-|
| [`Authenticator`](../flytekit.clients.auth.authenticator/authenticator) | Base authenticator for all authentication flows. |
| [`ClientConfig`](../flytekit.clients.auth.authenticator/clientconfig) | Client Configuration that is needed by the authenticator. |
| [`ClientConfigStore`](../flytekit.clients.auth.authenticator/clientconfigstore) | Client Config store retrieve client config. |
| [`ClientCredentialsAuthenticator`](../flytekit.clients.auth.authenticator/clientcredentialsauthenticator) | This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`CommandAuthenticator`](../flytekit.clients.auth.authenticator/commandauthenticator) | This Authenticator retrieves access_token using the provided command. |
| [`DeviceCodeAuthenticator`](../flytekit.clients.auth.authenticator/devicecodeauthenticator) | This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`PKCEAuthenticator`](../flytekit.clients.auth.authenticator/pkceauthenticator) | This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`StaticClientConfigStore`](../flytekit.clients.auth.authenticator/staticclientconfigstore) | Client Config store retrieve client config. |

