---
title: flytekitplugins.spark.databricks_auth
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekitplugins.spark.databricks_auth

Authentication strategies for the Databricks connector.

PAT remains the default for backward compatibility. OAuth machine-to-machine
(M2M) authentication is opt-in through ``FLYTE_DATABRICKS_AUTH_TYPE`` or the
equivalent per-task setting.
## Directory

### Classes

| Class | Description |
|-|-|
| [`DatabricksAuth`](.././flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authdatabricksauth) | Interface for obtaining a bearer token for Databricks API calls. |
| [`OAuthM2MAuth`](.././flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authoauthm2mauth) | Authenticate a Databricks service principal with client credentials. |
| [`OIDCConnectorAuth`](.././flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authoidcconnectorauth) | Exchange the connector workload's projected JWT for a Databricks token. |
| [`OIDCNamespaceServiceAccountAuth`](.././flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authoidcnamespaceserviceaccountauth) | Federate as a ServiceAccount discovered in the workflow namespace. |
| [`PATAuth`](.././flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authpatauth) | Delegate to the connector's existing multi-tenant PAT lookup. |

### Errors

| Exception | Description |
|-|-|
| [`DatabricksAuthError`](.././flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authdatabricksautherror) | Raised when Databricks authentication cannot be obtained. |

### Methods

| Method | Description |
|-|-|
| [`build_auth()`](#build_auth) | Rebuild an auth strategy from persisted connector metadata. |
| [`select_auth()`](#select_auth) | Select an explicitly configured strategy, defaulting to PAT. |
| [`validate_connector_config()`](#validate_connector_config) | Validate an explicitly configured connector-wide auth type. |


### Variables

| Property | Type | Description |
|-|-|-|
| `ANNOTATION_DATABRICKS_AUDIENCE` | `str` |  |
| `ANNOTATION_DATABRICKS_CLIENT_ID` | `str` |  |
| `AWS_WEB_IDENTITY_TOKEN_FILE_ENV` | `str` |  |
| `DATABRICKS_CLIENT_ID_ENV` | `str` |  |
| `DATABRICKS_CLIENT_SECRET_ENV` | `str` |  |
| `DATABRICKS_ENABLED_LABEL_SELECTOR` | `str` |  |
| `DEFAULT_OAUTH_SECRET_NAME` | `str` |  |
| `DEFAULT_OIDC_AUDIENCE` | `str` |  |
| `DEFAULT_PROJECTED_SA_TOKEN_PATH` | `str` |  |
| `FLYTE_DATABRICKS_AUTH_TYPE_ENV` | `str` |  |
| `FLYTE_DATABRICKS_OAUTH_SECRET_NAME_ENV` | `str` |  |
| `FLYTE_DATABRICKS_OIDC_AUDIENCE_ENV` | `str` |  |
| `FLYTE_DATABRICKS_OIDC_TOKEN_FILE_ENV` | `str` |  |
| `LABEL_DATABRICKS_ENABLED` | `str` |  |
| `NAMESPACE_DISCOVERY_CACHE_TTL_SECONDS` | `int` |  |
| `TOKEN_ENDPOINT_BACKOFF_BASE_SECONDS` | `float` |  |
| `TOKEN_ENDPOINT_MAX_RETRIES` | `int` |  |
| `TOKEN_REFRESH_BUFFER_SECONDS` | `int` |  |
| `VALID_AUTH_TYPES` | `set` |  |

## Methods

#### build_auth()

```python
def build_auth(
    workspace_url: str,
    auth_type: str,
    namespace: typing.Optional[str] = None,
    client_id: typing.Optional[str] = None,
    oauth_secret_name: typing.Optional[str] = None,
    oidc_token_file: typing.Optional[str] = None,
    oidc_audience: typing.Optional[str] = None,
    oidc_service_account: typing.Optional[str] = None,
) -> flytekitplugins.spark.databricks_auth.DatabricksAuth
```
Rebuild an auth strategy from persisted connector metadata.


| Parameter | Type | Description |
|-|-|-|
| `workspace_url` | `str` | |
| `auth_type` | `str` | |
| `namespace` | `typing.Optional[str]` | |
| `client_id` | `typing.Optional[str]` | |
| `oauth_secret_name` | `typing.Optional[str]` | |
| `oidc_token_file` | `typing.Optional[str]` | |
| `oidc_audience` | `typing.Optional[str]` | |
| `oidc_service_account` | `typing.Optional[str]` | |

#### select_auth()

```python
def select_auth(
    task_template: typing.Optional[flytekit.models.task.TaskTemplate],
    workspace_url: str,
    namespace: typing.Optional[str],
) -> flytekitplugins.spark.databricks_auth.DatabricksAuth
```
Select an explicitly configured strategy, defaulting to PAT.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `typing.Optional[flytekit.models.task.TaskTemplate]` | |
| `workspace_url` | `str` | |
| `namespace` | `typing.Optional[str]` | |

#### validate_connector_config()

```python
def validate_connector_config()
```
Validate an explicitly configured connector-wide auth type.


## flytekitplugins.spark.databricks_auth.DatabricksAuth

Interface for obtaining a bearer token for Databricks API calls.


### Parameters

```python
class DatabricksAuth(
    workspace_url: str,
    settings: flytekitplugins.spark.databricks_auth._Settings,
)
```
| Parameter | Type | Description |
|-|-|-|
| `workspace_url` | `str` | |
| `settings` | `flytekitplugins.spark.databricks_auth._Settings` | |

### Methods

| Method | Description |
|-|-|
| [`describe()`](#describe) | Return a description that is safe to write to connector logs. |
| [`get_bearer_token()`](#get_bearer_token) | Return a bearer token for a Databricks API request. |
| [`invalidate_cache()`](#invalidate_cache) | Invalidate cached authentication state, if any. |


#### describe()

```python
def describe()
```
Return a description that is safe to write to connector logs.


#### get_bearer_token()

```python
def get_bearer_token(
    session: aiohttp.ClientSession,
) -> str
```
Return a bearer token for a Databricks API request.


| Parameter | Type | Description |
|-|-|-|
| `session` | `aiohttp.ClientSession` | |

#### invalidate_cache()

```python
def invalidate_cache()
```
Invalidate cached authentication state, if any.


## flytekitplugins.spark.databricks_auth.DatabricksAuthError

Raised when Databricks authentication cannot be obtained.


## flytekitplugins.spark.databricks_auth.OAuthM2MAuth

Authenticate a Databricks service principal with client credentials.


### Parameters

```python
class OAuthM2MAuth(
    workspace_url: str,
    settings: flytekitplugins.spark.databricks_auth._Settings,
)
```
| Parameter | Type | Description |
|-|-|-|
| `workspace_url` | `str` | |
| `settings` | `flytekitplugins.spark.databricks_auth._Settings` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cache_key` | `typing.Tuple[str, str, str]` |  |

### Methods

| Method | Description |
|-|-|
| [`describe()`](#describe) | Return a description that is safe to write to connector logs. |
| [`get_bearer_token()`](#get_bearer_token) | Return a bearer token for a Databricks API request. |
| [`invalidate_cache()`](#invalidate_cache) | Invalidate cached authentication state, if any. |


#### describe()

```python
def describe()
```
Return a description that is safe to write to connector logs.


#### get_bearer_token()

```python
def get_bearer_token(
    session: aiohttp.ClientSession,
) -> str
```
Return a bearer token for a Databricks API request.


| Parameter | Type | Description |
|-|-|-|
| `session` | `aiohttp.ClientSession` | |

#### invalidate_cache()

```python
def invalidate_cache()
```
Invalidate cached authentication state, if any.


## flytekitplugins.spark.databricks_auth.OIDCConnectorAuth

Exchange the connector workload's projected JWT for a Databricks token.


### Parameters

```python
class OIDCConnectorAuth(
    workspace_url: str,
    settings: flytekitplugins.spark.databricks_auth._Settings,
)
```
| Parameter | Type | Description |
|-|-|-|
| `workspace_url` | `str` | |
| `settings` | `flytekitplugins.spark.databricks_auth._Settings` | |

### Methods

| Method | Description |
|-|-|
| [`describe()`](#describe) | Return a description that is safe to write to connector logs. |
| [`get_bearer_token()`](#get_bearer_token) | Return a bearer token for a Databricks API request. |
| [`invalidate_cache()`](#invalidate_cache) | Invalidate cached authentication state, if any. |


#### describe()

```python
def describe()
```
Return a description that is safe to write to connector logs.


#### get_bearer_token()

```python
def get_bearer_token(
    session: aiohttp.ClientSession,
) -> str
```
Return a bearer token for a Databricks API request.


| Parameter | Type | Description |
|-|-|-|
| `session` | `aiohttp.ClientSession` | |

#### invalidate_cache()

```python
def invalidate_cache()
```
Invalidate cached authentication state, if any.


## flytekitplugins.spark.databricks_auth.OIDCNamespaceServiceAccountAuth

Federate as a ServiceAccount discovered in the workflow namespace.


### Parameters

```python
class OIDCNamespaceServiceAccountAuth(
    workspace_url: str,
    settings: flytekitplugins.spark.databricks_auth._Settings,
    discovered: flytekitplugins.spark.databricks_auth._DiscoveredOIDCConfig,
)
```
| Parameter | Type | Description |
|-|-|-|
| `workspace_url` | `str` | |
| `settings` | `flytekitplugins.spark.databricks_auth._Settings` | |
| `discovered` | `flytekitplugins.spark.databricks_auth._DiscoveredOIDCConfig` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cache_key` | `typing.Tuple[str, str, str]` |  |

### Methods

| Method | Description |
|-|-|
| [`describe()`](#describe) | Return a description that is safe to write to connector logs. |
| [`get_bearer_token()`](#get_bearer_token) | Return a bearer token for a Databricks API request. |
| [`invalidate_cache()`](#invalidate_cache) | Invalidate cached authentication state, if any. |


#### describe()

```python
def describe()
```
Return a description that is safe to write to connector logs.


#### get_bearer_token()

```python
def get_bearer_token(
    session: aiohttp.ClientSession,
) -> str
```
Return a bearer token for a Databricks API request.


| Parameter | Type | Description |
|-|-|-|
| `session` | `aiohttp.ClientSession` | |

#### invalidate_cache()

```python
def invalidate_cache()
```
Invalidate cached authentication state, if any.


## flytekitplugins.spark.databricks_auth.PATAuth

Delegate to the connector's existing multi-tenant PAT lookup.


### Parameters

```python
class PATAuth(
    workspace_url: str,
    settings: flytekitplugins.spark.databricks_auth._Settings,
)
```
| Parameter | Type | Description |
|-|-|-|
| `workspace_url` | `str` | |
| `settings` | `flytekitplugins.spark.databricks_auth._Settings` | |

### Methods

| Method | Description |
|-|-|
| [`describe()`](#describe) | Return a description that is safe to write to connector logs. |
| [`get_bearer_token()`](#get_bearer_token) | Return a bearer token for a Databricks API request. |
| [`invalidate_cache()`](#invalidate_cache) | Invalidate cached authentication state, if any. |


#### describe()

```python
def describe()
```
Return a description that is safe to write to connector logs.


#### get_bearer_token()

```python
def get_bearer_token(
    session: aiohttp.ClientSession,
) -> str
```
Return a bearer token for a Databricks API request.


| Parameter | Type | Description |
|-|-|-|
| `session` | `aiohttp.ClientSession` | |

#### invalidate_cache()

```python
def invalidate_cache()
```
Invalidate cached authentication state, if any.


