---
title: flytekitplugins.identity_aware_proxy.cli
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.identity_aware_proxy.cli

## Directory

### Classes

| Class | Description |
|-|-|
| [`GCPIdentityAwareProxyAuthenticator`](.././flytekitplugins.identity_aware_proxy.cli#flytekitpluginsidentity_aware_proxycligcpidentityawareproxyauthenticator) | This Authenticator encapsulates the entire OAauth 2. |

### Methods

| Method | Description |
|-|-|
| [`get_gcp_secret_manager_secret()`](#get_gcp_secret_manager_secret) | Retrieve secret from GCP secret manager. |
| [`get_service_account_id_token()`](#get_service_account_id_token) | Fetch an ID Token for the service account used by the current environment. |


### Variables

| Property | Type | Description |
|-|-|-|
| `WEBAPP_CLIENT_ID_HELP` | `str` |  |

## Methods

#### get_gcp_secret_manager_secret()

```python
def get_gcp_secret_manager_secret(
    project_id: str,
    secret_id: str,
    version: typing.Optional[str],
)
```
Retrieve secret from GCP secret manager.


| Parameter | Type |
|-|-|
| `project_id` | `str` |
| `secret_id` | `str` |
| `version` | `typing.Optional[str]` |

#### get_service_account_id_token()

```python
def get_service_account_id_token(
    audience: str,
    service_account_email: str,
) -> str
```
Fetch an ID Token for the service account used by the current environment.

Uses flytekit's KeyringStore to cache the ID token.

This function acquires ID token from the environment in the following order.
See https://google.aip.dev/auth/4110.

1. If the environment variable ``GOOGLE_APPLICATION_CREDENTIALS`` is set
   to the path of a valid service account JSON file, then ID token is
   acquired using this service account credentials.
2. If the application is running in Compute Engine, App Engine or Cloud Run,
   then the ID token are obtained from the metadata server.



| Parameter | Type |
|-|-|
| `audience` | `str` |
| `service_account_email` | `str` |

## flytekitplugins.identity_aware_proxy.cli.GCPIdentityAwareProxyAuthenticator

This Authenticator encapsulates the entire OAauth 2.0 flow with GCP Identity Aware Proxy.

The auth flow is described in https://cloud.google.com/iap/docs/authentication-howto#signing_in_to_the_application

Automatically opens a browser window for login.


```python
class GCPIdentityAwareProxyAuthenticator(
    audience: str,
    client_id: str,
    client_secret: str,
    verify: typing.Union[bool, str, NoneType],
)
```
Initialize with default creds from KeyStore using the audience name.


| Parameter | Type |
|-|-|
| `audience` | `str` |
| `client_id` | `str` |
| `client_secret` | `str` |
| `verify` | `typing.Union[bool, str, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) | Refresh the IAP credentials. |


#### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
#### get_credentials()

```python
def get_credentials()
```
#### refresh_credentials()

```python
def refresh_credentials()
```
Refresh the IAP credentials. If no credentials are found, it will kick off a full OAuth 2.0 authorization flow.


