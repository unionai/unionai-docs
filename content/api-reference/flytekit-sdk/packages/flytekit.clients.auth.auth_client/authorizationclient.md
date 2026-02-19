---
title: AuthorizationClient
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AuthorizationClient

**Package:** `flytekit.clients.auth.auth_client`

Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the
credentials. NOTE: This will open an web browser to retrieve the credentials.



```python
class AuthorizationClient(
    endpoint: str,
    auth_endpoint: str,
    token_endpoint: str,
    audience: typing.Optional[str],
    scopes: typing.Optional[typing.List[str]],
    client_id: typing.Optional[str],
    redirect_uri: typing.Optional[str],
    endpoint_metadata: typing.Optional[EndpointMetadata],
    verify: typing.Optional[typing.Union[bool, str]],
    session: typing.Optional[requests.Session],
    request_auth_code_params: typing.Optional[typing.Dict[str, str]],
    request_access_token_params: typing.Optional[typing.Dict[str, str]],
    refresh_access_token_params: typing.Optional[typing.Dict[str, str]],
    add_request_auth_code_params_to_request_access_token_params: typing.Optional[bool],
)
```
Create new AuthorizationClient



| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | str endpoint to connect to |
| `auth_endpoint` | `str` | str endpoint where auth metadata can be found |
| `token_endpoint` | `str` | str endpoint to retrieve token from |
| `audience` | `typing.Optional[str]` | Audience parameter for Auth0 |
| `scopes` | `typing.Optional[typing.List[str]]` | list[str] oauth2 scopes |
| `client_id` | `typing.Optional[str]` | oauth2 client id |
| `redirect_uri` | `typing.Optional[str]` | oauth2 redirect uri |
| `endpoint_metadata` | `typing.Optional[EndpointMetadata]` | EndpointMetadata object to control the rendering of the page on login successful or failure |
| `verify` | `typing.Optional[typing.Union[bool, str]]` | Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to ``True``. When set to ``False``, requests will accept any TLS certificate presented by the server, and will ignore hostname mismatches and/or expired certificates, which will make your application vulnerable to man-in-the-middle (MitM) attacks. Setting verify to ``False`` may be useful during local development or testing. |
| `session` | `typing.Optional[requests.Session]` | A custom requests.Session object to use for making HTTP requests. If not provided, a new Session object will be created. |
| `request_auth_code_params` | `typing.Optional[typing.Dict[str, str]]` | dict of parameters to add to login uri opened in the browser |
| `request_access_token_params` | `typing.Optional[typing.Dict[str, str]]` | dict of parameters to add when exchanging the auth code for the access token |
| `refresh_access_token_params` | `typing.Optional[typing.Dict[str, str]]` | dict of parameters to add when refreshing the access token |
| `add_request_auth_code_params_to_request_access_token_params` | `typing.Optional[bool]` | Whether to add the `request_auth_code_params` to the parameters sent when exchanging the auth code for the access token. Defaults to False. Required e.g. for the PKCE flow with flyteadmin. Not required for e.g. the standard OAuth2 flow on GCP. |

## Methods

| Method | Description |
|-|-|
| [`get_creds_from_remote()`](#get_creds_from_remote) | This is the entrypoint method. |
| [`refresh_access_token()`](#refresh_access_token) |  |


### get_creds_from_remote()

```python
def get_creds_from_remote()
```
This is the entrypoint method. It will kickoff the full authentication
flow and trigger a web-browser to retrieve credentials. Because this
needs to open a port on localhost and may be called from a
multithreaded context (e.g. pyflyte register), this call may block
multiple threads and return a cached result for up to 60 seconds.


### refresh_access_token()

```python
def refresh_access_token(
    credentials: Credentials,
) -> Credentials
```
| Parameter | Type | Description |
|-|-|-|
| `credentials` | `Credentials` | |

