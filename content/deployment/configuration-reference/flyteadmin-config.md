---
title: FlyteAdmin configuration
weight: 2
variants: +flyte -serverless -byoc -selfmanaged
---

# Flyte Admin Configuration

- [admin](#section-admin)
- [auth](#section-auth)
- [catalog-cache](#section-catalog-cache)
- [cloudevents](#section-cloudevents)
- [cluster_resources](#section-cluster_resources)
- [clusterpools](#section-clusterpools)
- [clusters](#section-clusters)
- [database](#section-database)
- [domains](#section-domains)
- [event](#section-event)
- [externalevents](#section-externalevents)
- [flyteadmin](#section-flyteadmin)
- [logger](#section-logger)
- [namespace_mapping](#section-namespace_mapping)
- [notifications](#section-notifications)
- [otel](#section-otel)
- [plugins](#section-plugins)
- [propeller](#section-propeller)
- [qualityofservice](#section-qualityofservice)
- [queues](#section-queues)
- [registration](#section-registration)
- [remotedata](#section-remotedata)
- [scheduler](#section-scheduler)
- [secrets](#section-secrets)
- [server](#section-server)
- [storage](#section-storage)
- [task_resources](#section-task_resources)
- [task_type_whitelist](#section-task_type_whitelist)
- [tasks](#section-tasks)

## Section: admin

### endpoint ([config.URL](#config.url))

For admin types, specify where the uri of the service is located.

**Default Value**:

``` yaml
""
```

### insecure (bool)

Use insecure connection.

**Default Value**:

``` yaml
"false"
```

### insecureSkipVerify (bool)

InsecureSkipVerify controls whether a client verifies the server\'s
certificate chain and host name. Caution : shouldn\'t be use for
production usecases\'

**Default Value**:

``` yaml
"false"
```

### caCertFilePath (string)

Use specified certificate file to verify the admin server peer.

**Default Value**:

``` yaml
""
```

### maxBackoffDelay ([config.Duration](#config.duration))

Max delay for grpc backoff

**Default Value**:

``` yaml
8s
```

### perRetryTimeout ([config.Duration](#config.duration))

gRPC per retry timeout

**Default Value**:

``` yaml
15s
```

### maxRetries (int)

Max number of gRPC retries

**Default Value**:

``` yaml
"4"
```

### maxMessageSizeBytes (int)

The max size in bytes for incoming gRPC messages

**Default Value**:

``` yaml
"0"
```

### authType (uint8)

Type of OAuth2 flow used for communicating with
admin.ClientSecret,Pkce,ExternalCommand are valid values

**Default Value**:

``` yaml
ClientSecret
```

### tokenRefreshWindow ([config.Duration](#config.duration))

Max duration between token refresh attempt and token expiry.

**Default Value**:

``` yaml
0s
```

### useAuth (bool)

Deprecated: Auth will be enabled/disabled based on admin\'s dynamically
discovered information.

**Default Value**:

``` yaml
"false"
```

### clientId (string)

Client ID

**Default Value**:

``` yaml
flytepropeller
```

### clientSecretLocation (string)

File containing the client secret

**Default Value**:

``` yaml
/etc/secrets/client_secret
```

### clientSecretEnvVar (string)

Environment variable containing the client secret

**Default Value**:

``` yaml
""
```

### scopes (\[\]string)

List of scopes to request

**Default Value**:

``` yaml
[]
```

### useAudienceFromAdmin (bool)

Use Audience configured from admins public endpoint config.

**Default Value**:

``` yaml
"false"
```

### audience (string)

Audience to use when initiating OAuth2 authorization requests.

**Default Value**:

``` yaml
""
```

### authorizationServerUrl (string)

This is the URL to your IdP\'s authorization server. It\'ll default to
Endpoint

**Default Value**:

``` yaml
""
```

### tokenUrl (string)

OPTIONAL: Your IdP\'s token endpoint. It\'ll be discovered from flyte
admin\'s OAuth Metadata endpoint if not provided.

**Default Value**:

``` yaml
""
```

### authorizationHeader (string)

Custom metadata header to pass JWT

**Default Value**:

``` yaml
""
```

### pkceConfig ([pkce.Config](#pkce.config))

Config for Pkce authentication flow.

**Default Value**:

``` yaml
refreshTime: 5m0s
timeout: 2m0s
```

### deviceFlowConfig ([deviceflow.Config](#deviceflow.config))

Config for Device authentication flow.

**Default Value**:

``` yaml
pollInterval: 5s
refreshTime: 5m0s
timeout: 10m0s
```

### command (\[\]string)

Command for external authentication token generation

**Default Value**:

``` yaml
[]
```

### proxyCommand (\[\]string)

Command for external proxy-authorization token generation

**Default Value**:

``` yaml
[]
```

### defaultServiceConfig (string)

**Default Value**:

``` yaml
""
```

### httpProxyURL ([config.URL](#config.url))

OPTIONAL: HTTP Proxy to be used for OAuth requests.

**Default Value**:

``` yaml
""
```

#### config.Duration

##### Duration (int64)

**Default Value**:

``` yaml
8s
```

#### config.URL

##### URL ([url.URL](#url.url))

**Default Value**:

``` yaml
ForceQuery: false
Fragment: ""
Host: ""
OmitHost: false
Opaque: ""
Path: ""
RawFragment: ""
RawPath: ""
RawQuery: ""
Scheme: ""
User: null
```

#### url.URL

##### Scheme (string)

**Default Value**:

``` yaml
""
```

##### Opaque (string)

**Default Value**:

``` yaml
""
```

##### User (url.Userinfo)

**Default Value**:

``` yaml
null
```

##### Host (string)

**Default Value**:

``` yaml
""
```

##### Path (string)

**Default Value**:

``` yaml
""
```

##### RawPath (string)

**Default Value**:

``` yaml
""
```

##### OmitHost (bool)

**Default Value**:

``` yaml
"false"
```

##### ForceQuery (bool)

**Default Value**:

``` yaml
"false"
```

##### RawQuery (string)

**Default Value**:

``` yaml
""
```

##### Fragment (string)

**Default Value**:

``` yaml
""
```

##### RawFragment (string)

**Default Value**:

``` yaml
""
```

#### deviceflow.Config

##### refreshTime ([config.Duration](#config.duration))

grace period from the token expiry after which it would refresh the
token.

**Default Value**:

``` yaml
5m0s
```

##### timeout ([config.Duration](#config.duration))

amount of time the device flow should complete or else it will be
cancelled.

**Default Value**:

``` yaml
10m0s
```

##### pollInterval ([config.Duration](#config.duration))

amount of time the device flow would poll the token endpoint if auth
server doesn\'t return a polling interval. Okta and google IDP do return
an interval\'

**Default Value**:

``` yaml
5s
```

#### pkce.Config

##### timeout ([config.Duration](#config.duration))

Amount of time the browser session would be active for authentication
from client app.

**Default Value**:

``` yaml
2m0s
```

##### refreshTime ([config.Duration](#config.duration))

grace period from the token expiry after which it would refresh the
token.

**Default Value**:

``` yaml
5m0s
```

## Section: auth

### httpAuthorizationHeader (string)

**Default Value**:

``` yaml
flyte-authorization
```

### grpcAuthorizationHeader (string)

**Default Value**:

``` yaml
flyte-authorization
```

### disableForHttp (bool)

Disables auth enforcement on HTTP Endpoints.

**Default Value**:

``` yaml
"false"
```

### disableForGrpc (bool)

Disables auth enforcement on Grpc Endpoints.

**Default Value**:

``` yaml
"false"
```

### authorizedUris (\[\]config.URL)

**Default Value**:

``` yaml
null
```

### httpProxyURL ([config.URL](#config.url))

OPTIONAL: HTTP Proxy to be used for OAuth requests.

**Default Value**:

``` yaml
""
```

### userAuth ([config.UserAuthConfig](#config.userauthconfig))

Defines Auth options for users.

**Default Value**:

``` yaml
cookieBlockKeySecretName: cookie_block_key
cookieHashKeySecretName: cookie_hash_key
cookieSetting:
  domain: ""
  sameSitePolicy: DefaultMode
httpProxyURL: ""
idpQueryParameter: ""
openId:
  baseUrl: ""
  clientId: ""
  clientSecretFile: ""
  clientSecretName: oidc_client_secret
  scopes:
  - openid
  - profile
redirectUrl: /console
```

### appAuth ([config.OAuth2Options](#config.oauth2options))

Defines Auth options for apps. UserAuth must be enabled for AppAuth to
work.

**Default Value**:

``` yaml
authServerType: Self
externalAuthServer:
  allowedAudience: []
  baseUrl: ""
  httpProxyURL: ""
  metadataUrl: ""
  retryAttempts: 5
  retryDelay: 1s
selfAuthServer:
  accessTokenLifespan: 30m0s
  authorizationCodeLifespan: 5m0s
  claimSymmetricEncryptionKeySecretName: claim_symmetric_key
  issuer: ""
  oldTokenSigningRSAKeySecretName: token_rsa_key_old.pem
  refreshTokenLifespan: 1h0m0s
  staticClients:
    flyte-cli:
      audience: null
      grant_types:
      - refresh_token
      - authorization_code
      id: flyte-cli
      public: true
      redirect_uris:
      - http://localhost:53593/callback
      - http://localhost:12345/callback
      response_types:
      - code
      - token
      scopes:
      - all
      - offline
      - access_token
    flytectl:
      audience: null
      grant_types:
      - refresh_token
      - authorization_code
      id: flytectl
      public: true
      redirect_uris:
      - http://localhost:53593/callback
      - http://localhost:12345/callback
      response_types:
      - code
      - token
      scopes:
      - all
      - offline
      - access_token
    flytepropeller:
      audience: null
      client_secret: JDJhJDA2JGQ2UFFuMlFBRlUzY0w1VjhNRGtldXVrNjN4dWJxVXhOeGp0ZlB3LkZjOU1nVjZ2cG15T0l5
      grant_types:
      - refresh_token
      - client_credentials
      id: flytepropeller
      public: false
      redirect_uris:
      - http://localhost:3846/callback
      response_types:
      - token
      scopes:
      - all
      - offline
      - access_token
  tokenSigningRSAKeySecretName: token_rsa_key.pem
thirdPartyConfig:
  flyteClient:
    audience: ""
    clientId: flytectl
    redirectUri: http://localhost:53593/callback
    scopes:
    - all
    - offline
```

#### config.OAuth2Options

##### authServerType (int)

**Default Value**:

``` yaml
Self
```

##### selfAuthServer ([config.AuthorizationServer](#config.authorizationserver))

Authorization Server config to run as a service. Use this when using an
IdP that does not offer a custom OAuth2 Authorization Server.

**Default Value**:

``` yaml
accessTokenLifespan: 30m0s
authorizationCodeLifespan: 5m0s
claimSymmetricEncryptionKeySecretName: claim_symmetric_key
issuer: ""
oldTokenSigningRSAKeySecretName: token_rsa_key_old.pem
refreshTokenLifespan: 1h0m0s
staticClients:
  flyte-cli:
    audience: null
    grant_types:
    - refresh_token
    - authorization_code
    id: flyte-cli
    public: true
    redirect_uris:
    - http://localhost:53593/callback
    - http://localhost:12345/callback
    response_types:
    - code
    - token
    scopes:
    - all
    - offline
    - access_token
  flytectl:
    audience: null
    grant_types:
    - refresh_token
    - authorization_code
    id: flytectl
    public: true
    redirect_uris:
    - http://localhost:53593/callback
    - http://localhost:12345/callback
    response_types:
    - code
    - token
    scopes:
    - all
    - offline
    - access_token
  flytepropeller:
    audience: null
    client_secret: JDJhJDA2JGQ2UFFuMlFBRlUzY0w1VjhNRGtldXVrNjN4dWJxVXhOeGp0ZlB3LkZjOU1nVjZ2cG15T0l5
    grant_types:
    - refresh_token
    - client_credentials
    id: flytepropeller
    public: false
    redirect_uris:
    - http://localhost:3846/callback
    response_types:
    - token
    scopes:
    - all
    - offline
    - access_token
tokenSigningRSAKeySecretName: token_rsa_key.pem
```

##### externalAuthServer ([config.ExternalAuthorizationServer](#config.externalauthorizationserver))

External Authorization Server config.

**Default Value**:

``` yaml
allowedAudience: []
baseUrl: ""
httpProxyURL: ""
metadataUrl: ""
retryAttempts: 5
retryDelay: 1s
```

##### thirdPartyConfig ([config.ThirdPartyConfigOptions](#config.thirdpartyconfigoptions))

Defines settings to instruct flyte cli tools (and optionally others) on
what config to use to setup their client.

**Default Value**:

``` yaml
flyteClient:
  audience: ""
  clientId: flytectl
  redirectUri: http://localhost:53593/callback
  scopes:
  - all
  - offline
```

#### config.AuthorizationServer

##### issuer (string)

Defines the issuer to use when issuing and validating tokens. The
default value is <https://>\<requestUri.HostAndPort\>/

**Default Value**:

``` yaml
""
```

##### accessTokenLifespan ([config.Duration](#config.duration))

Defines the lifespan of issued access tokens.

**Default Value**:

``` yaml
30m0s
```

##### refreshTokenLifespan ([config.Duration](#config.duration))

Defines the lifespan of issued access tokens.

**Default Value**:

``` yaml
1h0m0s
```

##### authorizationCodeLifespan ([config.Duration](#config.duration))

Defines the lifespan of issued access tokens.

**Default Value**:

``` yaml
5m0s
```

##### claimSymmetricEncryptionKeySecretName (string)

OPTIONAL: Secret name to use to encrypt claims in authcode token.

**Default Value**:

``` yaml
claim_symmetric_key
```

##### tokenSigningRSAKeySecretName (string)

OPTIONAL: Secret name to use to retrieve RSA Signing Key.

**Default Value**:

``` yaml
token_rsa_key.pem
```

##### oldTokenSigningRSAKeySecretName (string)

OPTIONAL: Secret name to use to retrieve Old RSA Signing Key. This can
be useful during key rotation to continue to accept older tokens.

**Default Value**:

``` yaml
token_rsa_key_old.pem
```

##### staticClients (map\[string\]\*fosite.DefaultClient)

**Default Value**:

``` yaml
flyte-cli:
  audience: null
  grant_types:
  - refresh_token
  - authorization_code
  id: flyte-cli
  public: true
  redirect_uris:
  - http://localhost:53593/callback
  - http://localhost:12345/callback
  response_types:
  - code
  - token
  scopes:
  - all
  - offline
  - access_token
flytectl:
  audience: null
  grant_types:
  - refresh_token
  - authorization_code
  id: flytectl
  public: true
  redirect_uris:
  - http://localhost:53593/callback
  - http://localhost:12345/callback
  response_types:
  - code
  - token
  scopes:
  - all
  - offline
  - access_token
flytepropeller:
  audience: null
  client_secret: JDJhJDA2JGQ2UFFuMlFBRlUzY0w1VjhNRGtldXVrNjN4dWJxVXhOeGp0ZlB3LkZjOU1nVjZ2cG15T0l5
  grant_types:
  - refresh_token
  - client_credentials
  id: flytepropeller
  public: false
  redirect_uris:
  - http://localhost:3846/callback
  response_types:
  - token
  scopes:
  - all
  - offline
  - access_token
```

#### config.ExternalAuthorizationServer

##### baseUrl ([config.URL](#config.url))

This should be the base url of the authorization server that you are
trying to hit. With Okta for instance, it will look something like
<https://company.okta.com/oauth2/abcdef123456789/>

**Default Value**:

``` yaml
""
```

##### allowedAudience (\[\]string)

Optional: A list of allowed audiences. If not provided, the audience is
expected to be the public Uri of the service.

**Default Value**:

``` yaml
[]
```

##### metadataUrl ([config.URL](#config.url))

Optional: If the server doesn\'t support
/.well-known/oauth-authorization-server, you can set a custom metadata
url here.\'

**Default Value**:

``` yaml
""
```

##### httpProxyURL ([config.URL](#config.url))

OPTIONAL: HTTP Proxy to be used for OAuth requests.

**Default Value**:

``` yaml
""
```

##### retryAttempts (int)

Optional: The number of attempted retries on a transient failure to get
the OAuth metadata

**Default Value**:

``` yaml
"5"
```

##### retryDelay ([config.Duration](#config.duration))

Optional, Duration to wait between retries

**Default Value**:

``` yaml
1s
```

#### config.ThirdPartyConfigOptions

##### flyteClient ([config.FlyteClientConfig](#config.flyteclientconfig))

**Default Value**:

``` yaml
audience: ""
clientId: flytectl
redirectUri: http://localhost:53593/callback
scopes:
- all
- offline
```

#### config.FlyteClientConfig

##### clientId (string)

public identifier for the app which handles authorization for a Flyte
deployment

**Default Value**:

``` yaml
flytectl
```

##### redirectUri (string)

This is the callback uri registered with the app which handles
authorization for a Flyte deployment

**Default Value**:

``` yaml
http://localhost:53593/callback
```

##### scopes (\[\]string)

Recommended scopes for the client to request.

**Default Value**:

``` yaml
- all
- offline
```

##### audience (string)

Audience to use when initiating OAuth2 authorization requests.

**Default Value**:

``` yaml
""
```

#### config.UserAuthConfig

##### redirectUrl ([config.URL](#config.url))

**Default Value**:

``` yaml
/console
```

##### openId ([config.OpenIDOptions](#config.openidoptions))

OpenID Configuration for User Auth

**Default Value**:

``` yaml
baseUrl: ""
clientId: ""
clientSecretFile: ""
clientSecretName: oidc_client_secret
scopes:
- openid
- profile
```

##### httpProxyURL ([config.URL](#config.url))

OPTIONAL: HTTP Proxy to be used for OAuth requests.

**Default Value**:

``` yaml
""
```

##### cookieHashKeySecretName (string)

OPTIONAL: Secret name to use for cookie hash key.

**Default Value**:

``` yaml
cookie_hash_key
```

##### cookieBlockKeySecretName (string)

OPTIONAL: Secret name to use for cookie block key.

**Default Value**:

``` yaml
cookie_block_key
```

##### cookieSetting ([config.CookieSettings](#config.cookiesettings))

settings used by cookies created for user auth

**Default Value**:

``` yaml
domain: ""
sameSitePolicy: DefaultMode
```

##### idpQueryParameter (string)

idp query parameter used for selecting a particular IDP for doing user
authentication. Eg: for Okta passing idp=\<IDP-ID\> forces the
authentication to happen with IDP-ID

**Default Value**:

``` yaml
""
```

#### config.CookieSettings

##### sameSitePolicy (int)

OPTIONAL: Allows you to declare if your cookie should be restricted to a
first-party or same-site context.Wrapper around http.SameSite.

**Default Value**:

``` yaml
DefaultMode
```

##### domain (string)

OPTIONAL: Allows you to set the domain attribute on the auth cookies.

**Default Value**:

``` yaml
""
```

#### config.OpenIDOptions

##### clientId (string)

**Default Value**:

``` yaml
""
```

##### clientSecretName (string)

**Default Value**:

``` yaml
oidc_client_secret
```

##### clientSecretFile (string)

**Default Value**:

``` yaml
""
```

##### baseUrl ([config.URL](#config.url))

**Default Value**:

``` yaml
""
```

##### scopes (\[\]string)

**Default Value**:

``` yaml
- openid
- profile
```

## Section: catalog-cache

### type (string)

Catalog Implementation to use

**Default Value**:

``` yaml
noop
```

### endpoint (string)

Endpoint for catalog service

**Default Value**:

``` yaml
""
```

### insecure (bool)

Use insecure grpc connection

**Default Value**:

``` yaml
"false"
```

### max-cache-age ([config.Duration](#config.duration))

Cache entries past this age will incur cache miss. 0 means cache never
expires

**Default Value**:

``` yaml
0s
```

### use-admin-auth (bool)

Use the same gRPC credentials option as the flyteadmin client

**Default Value**:

``` yaml
"false"
```

### max-retries (int)

The max number of retries for event recording.

**Default Value**:

``` yaml
"5"
```

### base-scalar (int)

The base/scalar backoff duration in milliseconds for event recording
retries.

**Default Value**:

``` yaml
"100"
```

### backoff-jitter (string)

A string representation of a floating point number between 0 and 1
specifying the jitter factor for event recording retries.

**Default Value**:

``` yaml
"0.1"
```

### default-service-config (string)

Set the default service config for the catalog gRPC client

**Default Value**:

``` yaml
""
```

## Section: cloudevents

### enable (bool)

**Default Value**:

``` yaml
"false"
```

### type (string)

**Default Value**:

``` yaml
local
```

### aws ([interfaces.AWSConfig](#interfaces.awsconfig))

**Default Value**:

``` yaml
region: ""
```

### gcp ([interfaces.GCPConfig](#interfaces.gcpconfig))

**Default Value**:

``` yaml
projectId: ""
```

### kafka ([interfaces.KafkaConfig](#interfaces.kafkaconfig))

**Default Value**:

``` yaml
brokers: null
saslConfig:
  enabled: false
  handshake: false
  mechanism: ""
  password: ""
  passwordPath: ""
  user: ""
tlsConfig:
  certPath: ""
  enabled: false
  insecureSkipVerify: false
  keyPath: ""
version: ""
```

### eventsPublisher ([interfaces.EventsPublisherConfig](#interfaces.eventspublisherconfig))

**Default Value**:

``` yaml
enrichAllWorkflowEventTypes: false
eventTypes: null
topicName: ""
```

### reconnectAttempts (int)

**Default Value**:

``` yaml
"0"
```

### reconnectDelaySeconds (int)

**Default Value**:

``` yaml
"0"
```

### cloudEventVersion (uint8)

**Default Value**:

``` yaml
v1
```

#### interfaces.AWSConfig

##### region (string)

**Default Value**:

``` yaml
""
```

#### interfaces.EventsPublisherConfig

##### topicName (string)

**Default Value**:

``` yaml
""
```

##### eventTypes (\[\]string)

**Default Value**:

``` yaml
null
```

##### enrichAllWorkflowEventTypes (bool)

**Default Value**:

``` yaml
"false"
```

#### interfaces.GCPConfig

##### projectId (string)

**Default Value**:

``` yaml
""
```

#### interfaces.KafkaConfig

##### version (string)

**Default Value**:

``` yaml
""
```

##### brokers (\[\]string)

**Default Value**:

``` yaml
null
```

##### saslConfig ([interfaces.SASLConfig](#interfaces.saslconfig))

**Default Value**:

``` yaml
enabled: false
handshake: false
mechanism: ""
password: ""
passwordPath: ""
user: ""
```

##### tlsConfig ([interfaces.TLSConfig](#interfaces.tlsconfig))

**Default Value**:

``` yaml
certPath: ""
enabled: false
insecureSkipVerify: false
keyPath: ""
```

#### interfaces.SASLConfig

##### enabled (bool)

**Default Value**:

``` yaml
"false"
```

##### user (string)

**Default Value**:

``` yaml
""
```

##### password (string)

**Default Value**:

``` yaml
""
```

##### passwordPath (string)

**Default Value**:

``` yaml
""
```

##### handshake (bool)

**Default Value**:

``` yaml
"false"
```

##### mechanism (string)

**Default Value**:

``` yaml
""
```

#### interfaces.TLSConfig

##### enabled (bool)

**Default Value**:

``` yaml
"false"
```

##### insecureSkipVerify (bool)

**Default Value**:

``` yaml
"false"
```

##### certPath (string)

**Default Value**:

``` yaml
""
```

##### keyPath (string)

**Default Value**:

``` yaml
""
```

## Section: cluster_resources

### templatePath (string)

**Default Value**:

``` yaml
""
```

### templateData (map\[string\]interfaces.DataSource)

**Default Value**:

``` yaml
{}
```

### refreshInterval ([config.Duration](#config.duration))

**Default Value**:

``` yaml
1m0s
```

### customData (map\[string\]map\[string\]interfaces.DataSource)

**Default Value**:

``` yaml
{}
```

### standaloneDeployment (bool)

Whether the cluster resource sync is running in a standalone deployment
and should call flyteadmin service endpoints

**Default Value**:

``` yaml
"false"
```

## Section: clusterpools

### clusterPoolAssignments (map\[string\]interfaces.ClusterPoolAssignment)

**Default Value**:

``` yaml
{}
```

## Section: clusters

### clusterConfigs (\[\]interfaces.ClusterConfig)

**Default Value**:

``` yaml
null
```

### labelClusterMap (map\[string\]\[\]interfaces.ClusterEntity)

**Default Value**:

``` yaml
null
```

### defaultExecutionLabel (string)

**Default Value**:

``` yaml
""
```

## Section: database

### host (string)

**Default Value**:

``` yaml
""
```

### port (int)

**Default Value**:

``` yaml
"0"
```

### dbname (string)

**Default Value**:

``` yaml
""
```

### username (string)

**Default Value**:

``` yaml
""
```

### password (string)

**Default Value**:

``` yaml
""
```

### passwordPath (string)

**Default Value**:

``` yaml
""
```

### options (string)

**Default Value**:

``` yaml
""
```

### debug (bool)

**Default Value**:

``` yaml
"false"
```

### enableForeignKeyConstraintWhenMigrating (bool)

Whether to enable gorm foreign keys when migrating the db

**Default Value**:

``` yaml
"false"
```

### maxIdleConnections (int)

maxIdleConnections sets the maximum number of connections in the idle
connection pool.

**Default Value**:

``` yaml
"10"
```

### maxOpenConnections (int)

maxOpenConnections sets the maximum number of open connections to the
database.

**Default Value**:

``` yaml
"100"
```

### connMaxLifeTime ([config.Duration](#config.duration))

sets the maximum amount of time a connection may be reused

**Default Value**:

``` yaml
1h0m0s
```

### postgres ([database.PostgresConfig](#database.postgresconfig))

**Default Value**:

``` yaml
dbname: postgres
debug: false
host: localhost
options: sslmode=disable
password: postgres
passwordPath: ""
port: 30001
readReplicaHost: localhost
username: postgres
```

### sqlite ([database.SQLiteConfig](#database.sqliteconfig))

**Default Value**:

``` yaml
file: ""
```

#### database.PostgresConfig

##### host (string)

The host name of the database server

**Default Value**:

``` yaml
localhost
```

##### readReplicaHost (string)

The host name of the read replica database server

**Default Value**:

``` yaml
localhost
```

##### port (int)

The port name of the database server

**Default Value**:

``` yaml
"30001"
```

##### dbname (string)

The database name

**Default Value**:

``` yaml
postgres
```

##### username (string)

The database user who is connecting to the server.

**Default Value**:

``` yaml
postgres
```

##### password (string)

The database password.

**Default Value**:

``` yaml
postgres
```

##### passwordPath (string)

Points to the file containing the database password.

**Default Value**:

``` yaml
""
```

##### options (string)

See <http://gorm.io/docs/connecting_to_the_database.html> for available
options passed, in addition to the above.

**Default Value**:

``` yaml
sslmode=disable
```

##### debug (bool)

Whether or not to start the database connection with debug mode enabled.

**Default Value**:

``` yaml
"false"
```

#### database.SQLiteConfig

##### file (string)

The path to the file (existing or new) where the DB should be created /
stored. If existing, then this will be reused, else a new will be
created

**Default Value**:

``` yaml
""
```

## Section: domains

### id (string)

**Default Value**:

``` yaml
development
```

### name (string)

**Default Value**:

``` yaml
development
```

## Section: event

### type (string)

Sets the type of EventSink to configure \[log/admin/file\].

**Default Value**:

``` yaml
admin
```

### file-path (string)

For file types, specify where the file should be located.

**Default Value**:

``` yaml
""
```

### rate (int64)

Max rate at which events can be recorded per second.

**Default Value**:

``` yaml
"500"
```

### capacity (int)

The max bucket size for event recording tokens.

**Default Value**:

``` yaml
"1000"
```

### max-retries (int)

The max number of retries for event recording.

**Default Value**:

``` yaml
"5"
```

### base-scalar (int)

The base/scalar backoff duration in milliseconds for event recording
retries.

**Default Value**:

``` yaml
"100"
```

### backoff-jitter (string)

A string representation of a floating point number between 0 and 1
specifying the jitter factor for event recording retries.

**Default Value**:

``` yaml
"0.1"
```

## Section: externalevents

### enable (bool)

**Default Value**:

``` yaml
"false"
```

### type (string)

**Default Value**:

``` yaml
local
```

### aws ([interfaces.AWSConfig](#interfaces.awsconfig))

**Default Value**:

``` yaml
region: ""
```

### gcp ([interfaces.GCPConfig](#interfaces.gcpconfig))

**Default Value**:

``` yaml
projectId: ""
```

### eventsPublisher ([interfaces.EventsPublisherConfig](#interfaces.eventspublisherconfig))

**Default Value**:

``` yaml
enrichAllWorkflowEventTypes: false
eventTypes: null
topicName: ""
```

### reconnectAttempts (int)

**Default Value**:

``` yaml
"0"
```

### reconnectDelaySeconds (int)

**Default Value**:

``` yaml
"0"
```

## Section: flyteadmin

### roleNameKey (string)

**Default Value**:

``` yaml
""
```

### metricsScope (string)

**Default Value**:

``` yaml
'flyte:'
```

### metricsKeys (\[\]string)

**Default Value**:

``` yaml
- project
- domain
- wf
- task
- phase
- tasktype
- runtime_type
- runtime_version
- app_name
```

### profilerPort (int)

**Default Value**:

``` yaml
"10254"
```

### metadataStoragePrefix (\[\]string)

**Default Value**:

``` yaml
- metadata
- admin
```

### eventVersion (int)

**Default Value**:

``` yaml
"2"
```

### asyncEventsBufferSize (int)

**Default Value**:

``` yaml
"100"
```

### maxParallelism (int32)

**Default Value**:

``` yaml
"25"
```

### labels (map\[string\]string)

**Default Value**:

``` yaml
null
```

### annotations (map\[string\]string)

**Default Value**:

``` yaml
null
```

### interruptible (bool)

**Default Value**:

``` yaml
"false"
```

### overwriteCache (bool)

**Default Value**:

``` yaml
"false"
```

### assumableIamRole (string)

**Default Value**:

``` yaml
""
```

### k8sServiceAccount (string)

**Default Value**:

``` yaml
""
```

### outputLocationPrefix (string)

**Default Value**:

``` yaml
""
```

### useOffloadedWorkflowClosure (bool)

**Default Value**:

``` yaml
"false"
```

### envs (map\[string\]string)

**Default Value**:

``` yaml
null
```

### featureGates ([interfaces.FeatureGates](#interfaces.featuregates))

Enable experimental features.

**Default Value**:

``` yaml
enableArtifacts: false
```

### consoleUrl (string)

A URL pointing to the flyteconsole instance used to hit this flyteadmin
instance.

**Default Value**:

``` yaml
""
```

### useOffloadedInputs (bool)

Use offloaded inputs for workflows.

**Default Value**:

``` yaml
"false"
```

#### interfaces.FeatureGates

##### enableArtifacts (bool)

Enable artifacts feature.

**Default Value**:

``` yaml
"false"
```

## Section: logger

### show-source (bool)

Includes source code location in logs.

**Default Value**:

``` yaml
"false"
```

### mute (bool)

Mutes all logs regardless of severity. Intended for benchmarks/tests
only.

**Default Value**:

``` yaml
"false"
```

### level (int)

Sets the minimum logging level.

**Default Value**:

``` yaml
"3"
```

### formatter ([logger.FormatterConfig](#logger.formatterconfig))

Sets logging format.

**Default Value**:

``` yaml
type: json
```

#### logger.FormatterConfig

##### type (string)

Sets logging format type.

**Default Value**:

``` yaml
json
```

## Section: namespace_mapping

### mapping (string)

**Default Value**:

``` yaml
""
```

### template (string)

**Default Value**:

``` yaml
'{{ project }}-{{ domain }}'
```

### templateData (map\[string\]interfaces.DataSource)

**Default Value**:

``` yaml
null
```

## Section: notifications

### type (string)

**Default Value**:

``` yaml
local
```

### region (string)

**Default Value**:

``` yaml
""
```

### aws ([interfaces.AWSConfig](#interfaces.awsconfig))

**Default Value**:

``` yaml
region: ""
```

### gcp ([interfaces.GCPConfig](#interfaces.gcpconfig))

**Default Value**:

``` yaml
projectId: ""
```

### publisher ([interfaces.NotificationsPublisherConfig](#interfaces.notificationspublisherconfig))

**Default Value**:

``` yaml
topicName: ""
```

### processor ([interfaces.NotificationsProcessorConfig](#interfaces.notificationsprocessorconfig))

**Default Value**:

``` yaml
accountId: ""
queueName: ""
```

### emailer ([interfaces.NotificationsEmailerConfig](#interfaces.notificationsemailerconfig))

**Default Value**:

``` yaml
body: ""
emailServerConfig:
  apiKeyEnvVar: ""
  apiKeyFilePath: ""
  serviceName: ""
  smtpPasswordSecretName: ""
  smtpPort: ""
  smtpServer: ""
  smtpSkipTLSVerify: false
  smtpUsername: ""
sender: ""
subject: ""
```

### reconnectAttempts (int)

**Default Value**:

``` yaml
"0"
```

### reconnectDelaySeconds (int)

**Default Value**:

``` yaml
"0"
```

#### interfaces.NotificationsEmailerConfig

##### emailServerConfig ([interfaces.EmailServerConfig](#interfaces.emailserverconfig))

**Default Value**:

``` yaml
apiKeyEnvVar: ""
apiKeyFilePath: ""
serviceName: ""
smtpPasswordSecretName: ""
smtpPort: ""
smtpServer: ""
smtpSkipTLSVerify: false
smtpUsername: ""
```

##### subject (string)

**Default Value**:

``` yaml
""
```

##### sender (string)

**Default Value**:

``` yaml
""
```

##### body (string)

**Default Value**:

``` yaml
""
```

#### interfaces.EmailServerConfig

##### serviceName (string)

**Default Value**:

``` yaml
""
```

##### apiKeyEnvVar (string)

**Default Value**:

``` yaml
""
```

##### apiKeyFilePath (string)

**Default Value**:

``` yaml
""
```

##### smtpServer (string)

**Default Value**:

``` yaml
""
```

##### smtpPort (string)

**Default Value**:

``` yaml
""
```

##### smtpSkipTLSVerify (bool)

**Default Value**:

``` yaml
"false"
```

##### smtpUsername (string)

**Default Value**:

``` yaml
""
```

##### smtpPasswordSecretName (string)

**Default Value**:

``` yaml
""
```

#### interfaces.NotificationsProcessorConfig

##### queueName (string)

**Default Value**:

``` yaml
""
```

##### accountId (string)

**Default Value**:

``` yaml
""
```

#### interfaces.NotificationsPublisherConfig

##### topicName (string)

**Default Value**:

``` yaml
""
```

## Section: otel

### type (string)

Sets the type of exporter to configure
\[noop/file/jaeger/otlpgrpc/otlphttp\].

**Default Value**:

``` yaml
noop
```

### file ([otelutils.FileConfig](#otelutils.fileconfig))

Configuration for exporting telemetry traces to a file

**Default Value**:

``` yaml
filename: /tmp/trace.txt
```

### jaeger ([otelutils.JaegerConfig](#otelutils.jaegerconfig))

Configuration for exporting telemetry traces to a jaeger

**Default Value**:

``` yaml
endpoint: http://localhost:14268/api/traces
```

### otlpgrpc ([otelutils.OtlpGrpcConfig](#otelutils.otlpgrpcconfig))

Configuration for exporting telemetry traces to an OTLP gRPC collector

**Default Value**:

``` yaml
endpoint: http://localhost:4317
```

### otlphttp ([otelutils.OtlpHttpConfig](#otelutils.otlphttpconfig))

Configuration for exporting telemetry traces to an OTLP HTTP collector

**Default Value**:

``` yaml
endpoint: http://localhost:4318/v1/traces
```

### sampler ([otelutils.SamplerConfig](#otelutils.samplerconfig))

Configuration for the sampler to use for the tracer

**Default Value**:

``` yaml
parentSampler: always
traceIdRatio: 0.01
```

#### otelutils.FileConfig

##### filename (string)

Filename to store exported telemetry traces

**Default Value**:

``` yaml
/tmp/trace.txt
```

#### otelutils.JaegerConfig

##### endpoint (string)

Endpoint for the jaeger telemetry trace ingestor

**Default Value**:

``` yaml
http://localhost:14268/api/traces
```

#### otelutils.OtlpGrpcConfig

##### endpoint (string)

Endpoint for the OTLP telemetry trace collector

**Default Value**:

``` yaml
http://localhost:4317
```

#### otelutils.OtlpHttpConfig

##### endpoint (string)

Endpoint for the OTLP telemetry trace collector

**Default Value**:

``` yaml
http://localhost:4318/v1/traces
```

#### otelutils.SamplerConfig

##### parentSampler (string)

Sets the parent sampler to use for the tracer

**Default Value**:

``` yaml
always
```

##### traceIdRatio (float64)

**Default Value**:

``` yaml
"0.01"
```

## Section: plugins

### connector-service ([connector.Config](#connector.config))

**Default Value**:

``` yaml
connectorForTaskTypes: null
connectors: null
defaultConnector:
  defaultServiceConfig: '{"loadBalancingConfig": [{"round_robin":{}}]}'
  defaultTimeout: 3s
  endpoint: ""
  insecure: true
  timeouts: null
pollInterval: 10s
resourceConstraints:
  NamespaceScopeResourceConstraint:
    Value: 50
  ProjectScopeResourceConstraint:
    Value: 100
supportedTaskTypes:
- task_type_1
- task_type_2
webApi:
  caching:
    maxSystemFailures: 5
    resyncInterval: 30s
    size: 500000
    workers: 10
  readRateLimiter:
    burst: 100
    qps: 10
  resourceMeta: null
  resourceQuotas:
    default: 1000
  writeRateLimiter:
    burst: 100
    qps: 10
```

### catalogcache ([catalog.Config](#catalog.config))

**Default Value**:

``` yaml
reader:
  maxItems: 10000
  maxRetries: 3
  workers: 10
writer:
  maxItems: 10000
  maxRetries: 3
  workers: 10
```

### connector-service ([connector.Config](#connector.config))

**Default Value**:

``` yaml
connectorForTaskTypes: {}
connectors: {}
defaultConnector:
  defaultServiceConfig: '{"loadBalancingConfig": [{"round_robin":{}}]}'
  defaultTimeout: 10s
  endpoint: ""
  insecure: true
  timeouts: null
pollInterval: 10s
resourceConstraints:
  NamespaceScopeResourceConstraint:
    Value: 50
  ProjectScopeResourceConstraint:
    Value: 100
supportedTaskTypes:
- task_type_3
- task_type_4
webApi:
  caching:
    maxSystemFailures: 5
    resyncInterval: 30s
    size: 500000
    workers: 10
  readRateLimiter:
    burst: 100
    qps: 10
  resourceMeta: null
  resourceQuotas:
    default: 1000
  writeRateLimiter:
    burst: 100
    qps: 10
```

### k8s ([config.K8sPluginConfig](#config.k8spluginconfig))

**Default Value**:

``` yaml
add-tolerations-for-extended-resources: []
co-pilot:
  cpu: 500m
  default-input-path: /var/flyte/inputs
  default-output-path: /var/flyte/outputs
  image: cr.flyte.org/flyteorg/flytecopilot:v0.0.15
  input-vol-name: flyte-inputs
  memory: 128Mi
  name: flyte-copilot-
  output-vol-name: flyte-outputs
  start-timeout: 1m40s
  storage: ""
create-container-config-error-grace-period: 0s
create-container-error-grace-period: 3m0s
default-annotations:
  cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
default-cpus: "1"
default-env-from-configmaps: null
default-env-from-secrets: null
default-env-vars: null
default-env-vars-from-env: null
default-labels: null
default-memory: 1Gi
default-node-selector: null
default-pod-dns-config: null
default-pod-security-context: null
default-pod-template-name: ""
default-pod-template-resync: 30s
default-security-context: null
default-tolerations: null
delete-resource-on-finalize: false
enable-distributed-error-aggregation: false
enable-host-networking-pod: null
gpu-device-node-label: k8s.amazonaws.com/accelerator
gpu-partition-size-node-label: k8s.amazonaws.com/gpu-partition-size
gpu-resource-name: nvidia.com/gpu
gpu-unpartitioned-node-selector-requirement: null
gpu-unpartitioned-toleration: null
image-pull-backoff-grace-period: 3m0s
image-pull-policy: ""
inject-finalizer: false
interruptible-node-selector: null
interruptible-node-selector-requirement: null
interruptible-tolerations: null
non-interruptible-node-selector-requirement: null
pod-pending-timeout: 0s
resource-tolerations: null
scheduler-name: ""
send-object-events: false
update-backoff-retries: 5
update-base-backoff-duration: 10
```

### k8s-array ([k8s.Config](#k8s.config))

**Default Value**:

``` yaml
ErrorAssembler:
  maxItems: 100000
  maxRetries: 5
  workers: 10
OutputAssembler:
  maxItems: 100000
  maxRetries: 5
  workers: 10
logs:
  config:
    cloudwatch-enabled: false
    cloudwatch-log-group: ""
    cloudwatch-region: ""
    cloudwatch-template-uri: ""
    dynamic-log-links: null
    gcp-project: ""
    kubernetes-enabled: true
    kubernetes-template-uri: http://localhost:30082/#!/log/{{ .namespace }}/{{ .podName
      }}/pod?namespace={{ .namespace }}
    kubernetes-url: ""
    stackdriver-enabled: false
    stackdriver-logresourcename: ""
    stackdriver-template-uri: ""
    templates: null
maxArrayJobSize: 5000
maxErrorLength: 1000
namespaceTemplate: ""
node-selector: null
remoteClusterConfig:
  auth:
    certPath: ""
    tokenPath: ""
    type: ""
  enabled: false
  endpoint: ""
  name: ""
resourceConfig:
  limit: 0
  primaryLabel: ""
scheduler: ""
tolerations: null
```

### logs ([logs.LogConfig](#logs.logconfig))

**Default Value**:

``` yaml
cloudwatch-enabled: false
cloudwatch-log-group: ""
cloudwatch-region: ""
cloudwatch-template-uri: ""
dynamic-log-links: null
gcp-project: ""
kubernetes-enabled: true
kubernetes-template-uri: http://localhost:30082/#!/log/{{ .namespace }}/{{ .podName
  }}/pod?namespace={{ .namespace }}
kubernetes-url: ""
stackdriver-enabled: false
stackdriver-logresourcename: ""
stackdriver-template-uri: ""
templates: null
```

#### connector.Config

##### webApi ([webapi.PluginConfig](#webapi.pluginconfig))

Defines config for the base WebAPI plugin.

**Default Value**:

``` yaml
caching:
  maxSystemFailures: 5
  resyncInterval: 30s
  size: 500000
  workers: 10
readRateLimiter:
  burst: 100
  qps: 10
resourceMeta: null
resourceQuotas:
  default: 1000
writeRateLimiter:
  burst: 100
  qps: 10
```

##### resourceConstraints ([core.ResourceConstraintsSpec](#core.resourceconstraintsspec))

**Default Value**:

``` yaml
NamespaceScopeResourceConstraint:
  Value: 50
ProjectScopeResourceConstraint:
  Value: 100
```

##### defaultConnector ([connector.Deployment](#connector.deployment))

The default connector.

**Default Value**:

``` yaml
defaultServiceConfig: '{"loadBalancingConfig": [{"round_robin":{}}]}'
defaultTimeout: 3s
endpoint: ""
insecure: true
timeouts: null
```

##### connectors (map\[string\]\*connector.Deployment)

The connectors.

**Default Value**:

``` yaml
null
```

##### connectorForTaskTypes (map\[string\]string)

**Default Value**:

``` yaml
null
```

##### supportedTaskTypes (\[\]string)

**Default Value**:

``` yaml
- task_type_1
- task_type_2
```

##### pollInterval ([config.Duration](#config.duration))

The interval at which the plugin should poll the connector for metadata
updates.

**Default Value**:

``` yaml
10s
```

#### connector.Deployment

##### endpoint (string)

**Default Value**:

``` yaml
""
```

##### insecure (bool)

**Default Value**:

``` yaml
"true"
```

##### defaultServiceConfig (string)

**Default Value**:

``` yaml
'{"loadBalancingConfig": [{"round_robin":{}}]}'
```

##### timeouts (map\[string\]config.Duration)

**Default Value**:

``` yaml
null
```

##### defaultTimeout ([config.Duration](#config.duration))

**Default Value**:

``` yaml
3s
```

#### core.ResourceConstraintsSpec

##### ProjectScopeResourceConstraint ([core.ResourceConstraint](#core.resourceconstraint))

**Default Value**:

``` yaml
Value: 100
```

##### NamespaceScopeResourceConstraint ([core.ResourceConstraint](#core.resourceconstraint))

**Default Value**:

``` yaml
Value: 50
```

#### core.ResourceConstraint

##### Value (int64)

**Default Value**:

``` yaml
"100"
```

#### webapi.PluginConfig

##### resourceQuotas (webapi.ResourceQuotas)

**Default Value**:

``` yaml
default: 1000
```

##### readRateLimiter ([webapi.RateLimiterConfig](#webapi.ratelimiterconfig))

Defines rate limiter properties for read actions (e.g. retrieve status).

**Default Value**:

``` yaml
burst: 100
qps: 10
```

##### writeRateLimiter ([webapi.RateLimiterConfig](#webapi.ratelimiterconfig))

Defines rate limiter properties for write actions.

**Default Value**:

``` yaml
burst: 100
qps: 10
```

##### caching ([webapi.CachingConfig](#webapi.cachingconfig))

Defines caching characteristics.

**Default Value**:

``` yaml
maxSystemFailures: 5
resyncInterval: 30s
size: 500000
workers: 10
```

##### resourceMeta (interface)

**Default Value**:

``` yaml
<nil>
```

#### webapi.CachingConfig

##### size (int)

Defines the maximum number of items to cache.

**Default Value**:

``` yaml
"500000"
```

##### resyncInterval ([config.Duration](#config.duration))

Defines the sync interval.

**Default Value**:

``` yaml
30s
```

##### workers (int)

Defines the number of workers to start up to process items.

**Default Value**:

``` yaml
"10"
```

##### maxSystemFailures (int)

Defines the number of failures to fetch a task before failing the task.

**Default Value**:

``` yaml
"5"
```

#### webapi.RateLimiterConfig

##### qps (int)

Defines the max rate of calls per second.

**Default Value**:

``` yaml
"10"
```

##### burst (int)

Defines the maximum burst size.

**Default Value**:

``` yaml
"100"
```

#### catalog.Config

##### reader ([workqueue.Config](#workqueue.config))

Catalog reader workqueue config. Make sure the index cache must be big
enough to accommodate the biggest array task allowed to run on the
system.

**Default Value**:

``` yaml
maxItems: 10000
maxRetries: 3
workers: 10
```

##### writer ([workqueue.Config](#workqueue.config))

Catalog writer workqueue config. Make sure the index cache must be big
enough to accommodate the biggest array task allowed to run on the
system.

**Default Value**:

``` yaml
maxItems: 10000
maxRetries: 3
workers: 10
```

#### workqueue.Config

##### workers (int)

Number of concurrent workers to start processing the queue.

**Default Value**:

``` yaml
"10"
```

##### maxRetries (int)

Maximum number of retries per item.

**Default Value**:

``` yaml
"3"
```

##### maxItems (int)

Maximum number of entries to keep in the index.

**Default Value**:

``` yaml
"10000"
```

#### config.K8sPluginConfig

##### inject-finalizer (bool)

Instructs the plugin to inject a finalizer on startTask and remove it on
task termination.

**Default Value**:

``` yaml
"false"
```

##### default-annotations (map\[string\]string)

**Default Value**:

``` yaml
cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
```

##### default-labels (map\[string\]string)

**Default Value**:

``` yaml
null
```

##### default-env-vars (map\[string\]string)

**Default Value**:

``` yaml
null
```

##### default-env-vars-from-env (map\[string\]string)

**Default Value**:

``` yaml
null
```

##### default-env-from-configmaps (\[\]string)

**Default Value**:

``` yaml
null
```

##### default-env-from-secrets (\[\]string)

**Default Value**:

``` yaml
null
```

##### default-cpus ([resource.Quantity](#resource.quantity))

Defines a default value for cpu for containers if not specified.

**Default Value**:

``` yaml
"1"
```

##### default-memory ([resource.Quantity](#resource.quantity))

Defines a default value for memory for containers if not specified.

**Default Value**:

``` yaml
1Gi
```

##### default-tolerations (\[\]v1.Toleration)

**Default Value**:

``` yaml
null
```

##### default-node-selector (map\[string\]string)

**Default Value**:

``` yaml
null
```

##### default-affinity (v1.Affinity)

**Default Value**:

``` yaml
null
```

##### scheduler-name (string)

Defines scheduler name.

**Default Value**:

``` yaml
""
```

##### interruptible-tolerations (\[\]v1.Toleration)

**Default Value**:

``` yaml
null
```

##### interruptible-node-selector (map\[string\]string)

**Default Value**:

``` yaml
null
```

##### interruptible-node-selector-requirement (v1.NodeSelectorRequirement)

**Default Value**:

``` yaml
null
```

##### non-interruptible-node-selector-requirement (v1.NodeSelectorRequirement)

**Default Value**:

``` yaml
null
```

##### resource-tolerations (map\[v1.ResourceName\]\[\]v1.Toleration)

**Default Value**:

``` yaml
null
```

##### co-pilot ([config.FlyteCoPilotConfig](#config.flytecopilotconfig))

Co-Pilot Configuration

**Default Value**:

``` yaml
cpu: 500m
default-input-path: /var/flyte/inputs
default-output-path: /var/flyte/outputs
image: cr.flyte.org/flyteorg/flytecopilot:v0.0.15
input-vol-name: flyte-inputs
memory: 128Mi
name: flyte-copilot-
output-vol-name: flyte-outputs
start-timeout: 1m40s
storage: ""
```

##### delete-resource-on-finalize (bool)

Instructs the system to delete the resource upon successful execution of
a k8s pod rather than have the k8s garbage collector clean it up. This
ensures that no resources are kept around (potentially consuming cluster
resources). This, however, will cause k8s log links to expire as soon as
the resource is finalized.

**Default Value**:

``` yaml
"false"
```

##### create-container-error-grace-period ([config.Duration](#config.duration))

**Default Value**:

``` yaml
3m0s
```

##### create-container-config-error-grace-period ([config.Duration](#config.duration))

**Default Value**:

``` yaml
0s
```

##### image-pull-backoff-grace-period ([config.Duration](#config.duration))

**Default Value**:

``` yaml
3m0s
```

##### image-pull-policy (string)

**Default Value**:

``` yaml
""
```

##### pod-pending-timeout ([config.Duration](#config.duration))

**Default Value**:

``` yaml
0s
```

##### gpu-device-node-label (string)

**Default Value**:

``` yaml
k8s.amazonaws.com/accelerator
```

##### gpu-partition-size-node-label (string)

**Default Value**:

``` yaml
k8s.amazonaws.com/gpu-partition-size
```

##### gpu-unpartitioned-node-selector-requirement (v1.NodeSelectorRequirement)

**Default Value**:

``` yaml
null
```

##### gpu-unpartitioned-toleration (v1.Toleration)

**Default Value**:

``` yaml
null
```

##### gpu-resource-name (string)

**Default Value**:

``` yaml
nvidia.com/gpu
```

##### default-pod-security-context (v1.PodSecurityContext)

**Default Value**:

``` yaml
null
```

##### default-security-context (v1.SecurityContext)

**Default Value**:

``` yaml
null
```

##### enable-host-networking-pod (bool)

**Default Value**:

``` yaml
<invalid reflect.Value>
```

##### default-pod-dns-config (v1.PodDNSConfig)

**Default Value**:

``` yaml
null
```

##### default-pod-template-name (string)

Name of the PodTemplate to use as the base for all k8s pods created by
FlytePropeller.

**Default Value**:

``` yaml
""
```

##### default-pod-template-resync ([config.Duration](#config.duration))

Frequency of resyncing default pod templates

**Default Value**:

``` yaml
30s
```

##### send-object-events (bool)

If true, will send k8s object events in TaskExecutionEvent updates.

**Default Value**:

``` yaml
"false"
```

##### update-base-backoff-duration (int)

Initial delay in exponential backoff when updating a resource in
milliseconds.

**Default Value**:

``` yaml
"10"
```

##### update-backoff-retries (int)

Number of retries for exponential backoff when updating a resource.

**Default Value**:

``` yaml
"5"
```

##### add-tolerations-for-extended-resources (\[\]string)

Name of the extended resources for which tolerations should be added.

**Default Value**:

``` yaml
[]
```

##### enable-distributed-error-aggregation (bool)

If true, will aggregate errors of different worker pods for distributed
tasks.

**Default Value**:

``` yaml
"false"
```

#### config.FlyteCoPilotConfig

##### name (string)

Flyte co-pilot sidecar container name prefix. (additional bits will be
added after this)

**Default Value**:

``` yaml
flyte-copilot-
```

##### image (string)

Flyte co-pilot Docker Image FQN

**Default Value**:

``` yaml
cr.flyte.org/flyteorg/flytecopilot:v0.0.15
```

##### default-input-path (string)

Default path where the volume should be mounted

**Default Value**:

``` yaml
/var/flyte/inputs
```

##### default-output-path (string)

Default path where the volume should be mounted

**Default Value**:

``` yaml
/var/flyte/outputs
```

##### input-vol-name (string)

Name of the data volume that is created for storing inputs

**Default Value**:

``` yaml
flyte-inputs
```

##### output-vol-name (string)

Name of the data volume that is created for storing outputs

**Default Value**:

``` yaml
flyte-outputs
```

##### start-timeout ([config.Duration](#config.duration))

**Default Value**:

``` yaml
1m40s
```

##### cpu (string)

Used to set cpu for co-pilot containers

**Default Value**:

``` yaml
500m
```

##### memory (string)

Used to set memory for co-pilot containers

**Default Value**:

``` yaml
128Mi
```

##### storage (string)

Default storage limit for individual inputs / outputs

**Default Value**:

``` yaml
""
```

#### resource.Quantity

##### i ([resource.int64Amount](#resource.int64amount))

**Default Value**:

``` yaml
{}
```

##### d ([resource.infDecAmount](#resource.infdecamount))

**Default Value**:

``` yaml
<nil>
```

##### s (string)

**Default Value**:

``` yaml
"1"
```

##### Format (string)

**Default Value**:

``` yaml
DecimalSI
```

#### resource.infDecAmount

##### Dec (inf.Dec)

**Default Value**:

``` yaml
null
```

#### resource.int64Amount

##### value (int64)

**Default Value**:

``` yaml
"1"
```

##### scale (int32)

**Default Value**:

``` yaml
"0"
```

#### connector.Config

##### webApi ([webapi.PluginConfig](#webapi.pluginconfig))

Defines config for the base WebAPI plugin.

**Default Value**:

``` yaml
caching:
  maxSystemFailures: 5
  resyncInterval: 30s
  size: 500000
  workers: 10
readRateLimiter:
  burst: 100
  qps: 10
resourceMeta: null
resourceQuotas:
  default: 1000
writeRateLimiter:
  burst: 100
  qps: 10
```

##### resourceConstraints ([core.ResourceConstraintsSpec](#core.resourceconstraintsspec))

**Default Value**:

``` yaml
NamespaceScopeResourceConstraint:
  Value: 50
ProjectScopeResourceConstraint:
  Value: 100
```

##### defaultConnector ([connector.Deployment](#connector.deployment))

The default connector.

**Default Value**:

``` yaml
defaultServiceConfig: '{"loadBalancingConfig": [{"round_robin":{}}]}'
defaultTimeout: 10s
endpoint: ""
insecure: true
timeouts: null
```

##### connectors (map\[string\]\*connector.Deployment)

The connectors.

**Default Value**:

``` yaml
{}
```

##### connectorForTaskTypes (map\[string\]string)

**Default Value**:

``` yaml
{}
```

##### supportedTaskTypes (\[\]string)

**Default Value**:

``` yaml
- task_type_3
- task_type_4
```

##### pollInterval ([config.Duration](#config.duration))

The interval at which the plugin should poll the connector for metadata
updates.

**Default Value**:

``` yaml
10s
```

#### connector.Deployment

##### endpoint (string)

**Default Value**:

``` yaml
""
```

##### insecure (bool)

**Default Value**:

``` yaml
"true"
```

##### defaultServiceConfig (string)

**Default Value**:

``` yaml
'{"loadBalancingConfig": [{"round_robin":{}}]}'
```

##### timeouts (map\[string\]config.Duration)

**Default Value**:

``` yaml
null
```

##### defaultTimeout ([config.Duration](#config.duration))

**Default Value**:

``` yaml
10s
```

#### k8s.Config

##### scheduler (string)

Decides the scheduler to use when launching array-pods.

**Default Value**:

``` yaml
""
```

##### maxErrorLength (int)

Determines the maximum length of the error string returned for the
array.

**Default Value**:

``` yaml
"1000"
```

##### maxArrayJobSize (int64)

Maximum size of array job.

**Default Value**:

``` yaml
"5000"
```

##### resourceConfig ([k8s.ResourceConfig](#k8s.resourceconfig))

**Default Value**:

``` yaml
limit: 0
primaryLabel: ""
```

##### remoteClusterConfig ([k8s.ClusterConfig](#k8s.clusterconfig))

**Default Value**:

``` yaml
auth:
  certPath: ""
  tokenPath: ""
  type: ""
enabled: false
endpoint: ""
name: ""
```

##### node-selector (map\[string\]string)

**Default Value**:

``` yaml
null
```

##### tolerations (\[\]v1.Toleration)

**Default Value**:

``` yaml
null
```

##### namespaceTemplate (string)

**Default Value**:

``` yaml
""
```

##### OutputAssembler ([workqueue.Config](#workqueue.config))

**Default Value**:

``` yaml
maxItems: 100000
maxRetries: 5
workers: 10
```

##### ErrorAssembler ([workqueue.Config](#workqueue.config))

**Default Value**:

``` yaml
maxItems: 100000
maxRetries: 5
workers: 10
```

##### logs ([k8s.LogConfig](#k8s.logconfig))

Config for log links for k8s array jobs.

**Default Value**:

``` yaml
config:
  cloudwatch-enabled: false
  cloudwatch-log-group: ""
  cloudwatch-region: ""
  cloudwatch-template-uri: ""
  dynamic-log-links: null
  gcp-project: ""
  kubernetes-enabled: true
  kubernetes-template-uri: http://localhost:30082/#!/log/{{ .namespace }}/{{ .podName
    }}/pod?namespace={{ .namespace }}
  kubernetes-url: ""
  stackdriver-enabled: false
  stackdriver-logresourcename: ""
  stackdriver-template-uri: ""
  templates: null
```

#### k8s.ClusterConfig

##### name (string)

Friendly name of the remote cluster

**Default Value**:

``` yaml
""
```

##### endpoint (string)

Remote K8s cluster endpoint

**Default Value**:

``` yaml
""
```

##### auth ([k8s.Auth](#k8s.auth))

**Default Value**:

``` yaml
certPath: ""
tokenPath: ""
type: ""
```

##### enabled (bool)

Boolean flag to enable or disable

**Default Value**:

``` yaml
"false"
```

#### k8s.Auth

##### type (string)

Authentication type

**Default Value**:

``` yaml
""
```

##### tokenPath (string)

Token path

**Default Value**:

``` yaml
""
```

##### certPath (string)

Certificate path

**Default Value**:

``` yaml
""
```

#### k8s.LogConfig

##### config ([logs.LogConfig (config)](#logs.logconfig-config))

Defines the log config for k8s logs.

**Default Value**:

``` yaml
cloudwatch-enabled: false
cloudwatch-log-group: ""
cloudwatch-region: ""
cloudwatch-template-uri: ""
dynamic-log-links: null
gcp-project: ""
kubernetes-enabled: true
kubernetes-template-uri: http://localhost:30082/#!/log/{{ .namespace }}/{{ .podName
  }}/pod?namespace={{ .namespace }}
kubernetes-url: ""
stackdriver-enabled: false
stackdriver-logresourcename: ""
stackdriver-template-uri: ""
templates: null
```

#### logs.LogConfig (config)

##### cloudwatch-enabled (bool)

Enable Cloudwatch Logging

**Default Value**:

``` yaml
"false"
```

##### cloudwatch-region (string)

AWS region in which Cloudwatch logs are stored.

**Default Value**:

``` yaml
""
```

##### cloudwatch-log-group (string)

Log group to which streams are associated.

**Default Value**:

``` yaml
""
```

##### cloudwatch-template-uri (string)

Template Uri to use when building cloudwatch log links

**Default Value**:

``` yaml
""
```

##### kubernetes-enabled (bool)

Enable Kubernetes Logging

**Default Value**:

``` yaml
"true"
```

##### kubernetes-url (string)

Console URL for Kubernetes logs

**Default Value**:

``` yaml
""
```

##### kubernetes-template-uri (string)

Template Uri to use when building kubernetes log links

**Default Value**:

``` yaml
http://localhost:30082/#!/log/{{ .namespace }}/{{ .podName }}/pod?namespace={{ .namespace
  }}
```

##### stackdriver-enabled (bool)

Enable Log-links to stackdriver

**Default Value**:

``` yaml
"false"
```

##### gcp-project (string)

Name of the project in GCP

**Default Value**:

``` yaml
""
```

##### stackdriver-logresourcename (string)

Name of the logresource in stackdriver

**Default Value**:

``` yaml
""
```

##### stackdriver-template-uri (string)

Template Uri to use when building stackdriver log links

**Default Value**:

``` yaml
""
```

##### dynamic-log-links (map\[string\]tasklog.TemplateLogPlugin)

**Default Value**:

``` yaml
null
```

##### templates (\[\]tasklog.TemplateLogPlugin)

**Default Value**:

``` yaml
null
```

#### k8s.ResourceConfig

##### primaryLabel (string)

PrimaryLabel of a given service cluster

**Default Value**:

``` yaml
""
```

##### limit (int)

Resource quota (in the number of outstanding requests) for the cluster

**Default Value**:

``` yaml
"0"
```

#### logs.LogConfig

##### cloudwatch-enabled (bool)

Enable Cloudwatch Logging

**Default Value**:

``` yaml
"false"
```

##### cloudwatch-region (string)

AWS region in which Cloudwatch logs are stored.

**Default Value**:

``` yaml
""
```

##### cloudwatch-log-group (string)

Log group to which streams are associated.

**Default Value**:

``` yaml
""
```

##### cloudwatch-template-uri (string)

Template Uri to use when building cloudwatch log links

**Default Value**:

``` yaml
""
```

##### kubernetes-enabled (bool)

Enable Kubernetes Logging

**Default Value**:

``` yaml
"true"
```

##### kubernetes-url (string)

Console URL for Kubernetes logs

**Default Value**:

``` yaml
""
```

##### kubernetes-template-uri (string)

Template Uri to use when building kubernetes log links

**Default Value**:

``` yaml
http://localhost:30082/#!/log/{{ .namespace }}/{{ .podName }}/pod?namespace={{ .namespace
  }}
```

##### stackdriver-enabled (bool)

Enable Log-links to stackdriver

**Default Value**:

``` yaml
"false"
```

##### gcp-project (string)

Name of the project in GCP

**Default Value**:

``` yaml
""
```

##### stackdriver-logresourcename (string)

Name of the logresource in stackdriver

**Default Value**:

``` yaml
""
```

##### stackdriver-template-uri (string)

Template Uri to use when building stackdriver log links

**Default Value**:

``` yaml
""
```

##### dynamic-log-links (map\[string\]tasklog.TemplateLogPlugin)

**Default Value**:

``` yaml
null
```

##### templates (\[\]tasklog.TemplateLogPlugin)

**Default Value**:

``` yaml
null
```

## Section: propeller

### kube-config (string)

Path to kubernetes client config file.

**Default Value**:

``` yaml
""
```

### master (string)

**Default Value**:

``` yaml
""
```

### workers (int)

Number of threads to process workflows

**Default Value**:

``` yaml
"20"
```

### workflow-reeval-duration ([config.Duration](#config.duration))

Frequency of re-evaluating workflows

**Default Value**:

``` yaml
10s
```

### downstream-eval-duration ([config.Duration](#config.duration))

Frequency of re-evaluating downstream tasks

**Default Value**:

``` yaml
30s
```

### limit-namespace (string)

Namespaces to watch for this propeller

**Default Value**:

``` yaml
all
```

### prof-port ([config.Port](#config.port))

Profiler port

**Default Value**:

``` yaml
10254
```

### metadata-prefix (string)

MetadataPrefix should be used if all the metadata for Flyte executions
should be stored under a specific prefix in CloudStorage. If not
specified, the data will be stored in the base container directly.

**Default Value**:

``` yaml
metadata/propeller
```

### rawoutput-prefix (string)

a fully qualified storage path of the form s3://flyte/abc/\..., where
all data sandboxes should be stored.

**Default Value**:

``` yaml
""
```

### queue ([config.CompositeQueueConfig](#config.compositequeueconfig))

Workflow workqueue configuration, affects the way the work is consumed
from the queue.

**Default Value**:

``` yaml
batch-size: -1
batching-interval: 1s
queue:
  base-delay: 0s
  capacity: 10000
  max-delay: 1m0s
  rate: 1000
  type: maxof
sub-queue:
  base-delay: 0s
  capacity: 10000
  max-delay: 0s
  rate: 1000
  type: bucket
type: batch
```

### metrics-prefix (string)

An optional prefix for all published metrics.

**Default Value**:

``` yaml
flyte
```

### metrics-keys (\[\]string)

Metrics labels applied to prometheus metrics emitted by the service.

**Default Value**:

``` yaml
- project
- domain
- wf
- task
```

### enable-admin-launcher (bool)

Enable remote Workflow launcher to Admin

**Default Value**:

``` yaml
"true"
```

### max-workflow-retries (int)

Maximum number of retries per workflow

**Default Value**:

``` yaml
"10"
```

### max-ttl-hours (int)

Maximum number of hours a completed workflow should be retained. Number
between 1-23 hours

**Default Value**:

``` yaml
"23"
```

### gc-interval ([config.Duration](#config.duration))

Run periodic GC every 30 minutes

**Default Value**:

``` yaml
30m0s
```

### leader-election ([config.LeaderElectionConfig](#config.leaderelectionconfig))

Config for leader election.

**Default Value**:

``` yaml
enabled: false
lease-duration: 15s
lock-config-map:
  Name: ""
  Namespace: ""
renew-deadline: 10s
retry-period: 2s
```

### publish-k8s-events (bool)

Enable events publishing to K8s events API.

**Default Value**:

``` yaml
"false"
```

### max-output-size-bytes (int64)

Deprecated! Use storage.limits.maxDownloadMBs instead

**Default Value**:

``` yaml
"-1"
```

### enable-grpc-latency-metrics (bool)

Enable grpc latency metrics. Note Histograms metrics can be expensive on
Prometheus servers.

**Default Value**:

``` yaml
"false"
```

### kube-client-config ([config.KubeClientConfig](#config.kubeclientconfig))

Configuration to control the Kubernetes client

**Default Value**:

``` yaml
burst: 25
qps: 100
timeout: 30s
```

### node-config ([config.NodeConfig](#config.nodeconfig))

config for a workflow node

**Default Value**:

``` yaml
default-deadlines:
  node-active-deadline: 0s
  node-execution-deadline: 0s
  workflow-active-deadline: 0s
default-max-attempts: 1
enable-cr-debug-metadata: false
ignore-retry-cause: false
interruptible-failure-threshold: -1
max-node-retries-system-failures: 3
```

### max-streak-length (int)

Maximum number of consecutive rounds that one propeller worker can use
for one workflow - \>1 =\> turbo-mode is enabled.

**Default Value**:

``` yaml
"8"
```

### event-config ([config.EventConfig](#config.eventconfig))

Configures execution event behavior.

**Default Value**:

``` yaml
fallback-to-output-reference: false
raw-output-policy: reference
```

### include-shard-key-label (\[\]string)

Include the specified shard key label in the k8s FlyteWorkflow CRD label
selector

**Default Value**:

``` yaml
[]
```

### exclude-shard-key-label (\[\]string)

Exclude the specified shard key label from the k8s FlyteWorkflow CRD
label selector

**Default Value**:

``` yaml
[]
```

### include-project-label (\[\]string)

Include the specified project label in the k8s FlyteWorkflow CRD label
selector

**Default Value**:

``` yaml
[]
```

### exclude-project-label (\[\]string)

Exclude the specified project label from the k8s FlyteWorkflow CRD label
selector

**Default Value**:

``` yaml
[]
```

### include-domain-label (\[\]string)

Include the specified domain label in the k8s FlyteWorkflow CRD label
selector

**Default Value**:

``` yaml
[]
```

### exclude-domain-label (\[\]string)

Exclude the specified domain label from the k8s FlyteWorkflow CRD label
selector

**Default Value**:

``` yaml
[]
```

### cluster-id (string)

Unique cluster id running this flytepropeller instance with which to
annotate execution events

**Default Value**:

``` yaml
propeller
```

### create-flyteworkflow-crd (bool)

Enable creation of the FlyteWorkflow CRD on startup

**Default Value**:

``` yaml
"false"
```

### node-execution-worker-count (int)

Number of workers to evaluate node executions, currently only used for
array nodes

**Default Value**:

``` yaml
"8"
```

### array-node-config ([config.ArrayNodeConfig](#config.arraynodeconfig))

Configuration for array nodes

**Default Value**:

``` yaml
default-parallelism-behavior: unlimited
event-version: 0
use-map-plugin-logs: false
```

### literal-offloading-config ([config.LiteralOffloadingConfig](#config.literaloffloadingconfig))

config used for literal offloading.

**Default Value**:

``` yaml
Enabled: false
max-size-in-mb-for-offloading: 1000
min-size-in-mb-for-offloading: 10
supported-sdk-versions:
  FLYTE_SDK: 1.13.14
```

### admin-launcher ([launchplan.AdminConfig](#launchplan.adminconfig))

**Default Value**:

``` yaml
burst: 10
cache-resync-duration: 30s
cacheSize: 10000
tps: 100
workers: 10
```

### resourcemanager ([config.Config](#config.config))

**Default Value**:

``` yaml
redis:
  hostKey: ""
  hostPath: ""
  hostPaths: []
  maxRetries: 0
  primaryName: ""
resourceMaxQuota: 1000
type: noop
```

### workflowstore ([workflowstore.Config](#workflowstore.config))

**Default Value**:

``` yaml
policy: ResourceVersionCache
```

#### config.ArrayNodeConfig

##### event-version (int)

ArrayNode eventing version. 0 =\> legacy (drop-in replacement for
maptask), 1 =\> new

**Default Value**:

``` yaml
"0"
```

##### default-parallelism-behavior (string)

Default parallelism behavior for array nodes

**Default Value**:

``` yaml
unlimited
```

##### use-map-plugin-logs (bool)

Override subNode log links with those configured for the map plugin logs

**Default Value**:

``` yaml
"false"
```

#### config.CompositeQueueConfig

##### type (string)

Type of composite queue to use for the WorkQueue

**Default Value**:

``` yaml
batch
```

##### queue ([config.WorkqueueConfig](#config.workqueueconfig))

Workflow workqueue configuration, affects the way the work is consumed
from the queue.

**Default Value**:

``` yaml
base-delay: 0s
capacity: 10000
max-delay: 1m0s
rate: 1000
type: maxof
```

##### sub-queue ([config.WorkqueueConfig](#config.workqueueconfig))

SubQueue configuration, affects the way the nodes cause the top-level
Work to be re-evaluated.

**Default Value**:

``` yaml
base-delay: 0s
capacity: 10000
max-delay: 0s
rate: 1000
type: bucket
```

##### batching-interval ([config.Duration](#config.duration))

Duration for which downstream updates are buffered

**Default Value**:

``` yaml
1s
```

##### batch-size (int)

**Default Value**:

``` yaml
"-1"
```

#### config.WorkqueueConfig

##### type (string)

Type of RateLimiter to use for the WorkQueue

**Default Value**:

``` yaml
maxof
```

##### base-delay ([config.Duration](#config.duration))

base backoff delay for failure

**Default Value**:

``` yaml
0s
```

##### max-delay ([config.Duration](#config.duration))

Max backoff delay for failure

**Default Value**:

``` yaml
1m0s
```

##### rate (int64)

Bucket Refill rate per second

**Default Value**:

``` yaml
"1000"
```

##### capacity (int)

Bucket capacity as number of items

**Default Value**:

``` yaml
"10000"
```

#### config.Config

##### type (string)

Which resource manager to use, redis or noop. Default is noop.

**Default Value**:

``` yaml
noop
```

##### resourceMaxQuota (int)

Global limit for concurrent Qubole queries

**Default Value**:

``` yaml
"1000"
```

##### redis ([config.RedisConfig](#config.redisconfig))

Config for Redis resourcemanager.

**Default Value**:

``` yaml
hostKey: ""
hostPath: ""
hostPaths: []
maxRetries: 0
primaryName: ""
```

#### config.RedisConfig

##### hostPaths (\[\]string)

Redis hosts locations.

**Default Value**:

``` yaml
[]
```

##### primaryName (string)

Redis primary name, fill in only if you are connecting to a redis
sentinel cluster.

**Default Value**:

``` yaml
""
```

##### hostPath (string)

Redis host location

**Default Value**:

``` yaml
""
```

##### hostKey (string)

Key for local Redis access

**Default Value**:

``` yaml
""
```

##### maxRetries (int)

See Redis client options for more info

**Default Value**:

``` yaml
"0"
```

#### config.EventConfig

##### raw-output-policy (string)

How output data should be passed along in execution events.

**Default Value**:

``` yaml
reference
```

##### fallback-to-output-reference (bool)

Whether output data should be sent by reference when it is too large to
be sent inline in execution events.

**Default Value**:

``` yaml
"false"
```

##### ErrorOnAlreadyExists (bool)

**Default Value**:

``` yaml
"false"
```

#### config.KubeClientConfig

##### qps (float32)

**Default Value**:

``` yaml
"100"
```

##### burst (int)

Max burst rate for throttle. 0 defaults to 10

**Default Value**:

``` yaml
"25"
```

##### timeout ([config.Duration](#config.duration))

Max duration allowed for every request to KubeAPI before giving up. 0
implies no timeout.

**Default Value**:

``` yaml
30s
```

#### config.LeaderElectionConfig

##### enabled (bool)

Enables/Disables leader election.

**Default Value**:

``` yaml
"false"
```

##### lock-config-map ([types.NamespacedName](#types.namespacedname))

ConfigMap namespace/name to use for resource lock.

**Default Value**:

``` yaml
Name: ""
Namespace: ""
```

##### lease-duration ([config.Duration](#config.duration))

Duration that non-leader candidates will wait to force acquire
leadership. This is measured against time of last observed ack.

**Default Value**:

``` yaml
15s
```

##### renew-deadline ([config.Duration](#config.duration))

Duration that the acting master will retry refreshing leadership before
giving up.

**Default Value**:

``` yaml
10s
```

##### retry-period ([config.Duration](#config.duration))

Duration the LeaderElector clients should wait between tries of actions.

**Default Value**:

``` yaml
2s
```

#### types.NamespacedName

##### Namespace (string)

**Default Value**:

``` yaml
""
```

##### Name (string)

**Default Value**:

``` yaml
""
```

#### config.LiteralOffloadingConfig

##### Enabled (bool)

**Default Value**:

``` yaml
"false"
```

##### supported-sdk-versions (map\[string\]string)

Maps flytekit and union SDK names to minimum supported version that can
handle reading offloaded literals.

**Default Value**:

``` yaml
FLYTE_SDK: 1.13.14
```

##### min-size-in-mb-for-offloading (int64)

Size of a literal at which to trigger offloading

**Default Value**:

``` yaml
"10"
```

##### max-size-in-mb-for-offloading (int64)

Size of a literal at which to fail fast

**Default Value**:

``` yaml
"1000"
```

#### config.NodeConfig

##### default-deadlines ([config.DefaultDeadlines](#config.defaultdeadlines))

Default value for timeouts

**Default Value**:

``` yaml
node-active-deadline: 0s
node-execution-deadline: 0s
workflow-active-deadline: 0s
```

##### max-node-retries-system-failures (int64)

Maximum number of retries per node for node failure due to infra issues

**Default Value**:

``` yaml
"3"
```

##### interruptible-failure-threshold (int32)

number of failures for a node to be still considered interruptible.
Negative numbers are treated as complementary (ex. -1 means last attempt
is non-interruptible).\'

**Default Value**:

``` yaml
"-1"
```

##### default-max-attempts (int32)

Default maximum number of attempts for a node

**Default Value**:

``` yaml
"1"
```

##### ignore-retry-cause (bool)

Ignore retry cause and count all attempts toward a node\'s max attempts

**Default Value**:

``` yaml
"false"
```

##### enable-cr-debug-metadata (bool)

Collapse node on any terminal state, not just successful terminations.
This is useful to reduce the size of workflow state in etcd.

**Default Value**:

``` yaml
"false"
```

#### config.DefaultDeadlines

##### node-execution-deadline ([config.Duration](#config.duration))

Default value of node execution timeout that includes the time spent to
run the node/workflow

**Default Value**:

``` yaml
0s
```

##### node-active-deadline ([config.Duration](#config.duration))

Default value of node timeout that includes the time spent queued.

**Default Value**:

``` yaml
0s
```

##### workflow-active-deadline ([config.Duration](#config.duration))

Default value of workflow timeout that includes the time spent queued.

**Default Value**:

``` yaml
0s
```

#### config.Port

##### port (int)

**Default Value**:

``` yaml
"10254"
```

#### launchplan.AdminConfig

##### tps (int64)

The maximum number of transactions per second to flyte admin from this
client.

**Default Value**:

``` yaml
"100"
```

##### burst (int)

Maximum burst for throttle

**Default Value**:

``` yaml
"10"
```

##### cacheSize (int)

Maximum cache in terms of number of items stored.

**Default Value**:

``` yaml
"10000"
```

##### workers (int)

Number of parallel workers to work on the queue.

**Default Value**:

``` yaml
"10"
```

##### cache-resync-duration ([config.Duration](#config.duration))

Frequency of re-syncing launchplans within the auto refresh cache.

**Default Value**:

``` yaml
30s
```

#### workflowstore.Config

##### policy (string)

Workflow Store Policy to initialize

**Default Value**:

``` yaml
ResourceVersionCache
```

## Section: qualityofservice

### tierExecutionValues (map\[string\]interfaces.QualityOfServiceSpec)

**Default Value**:

``` yaml
{}
```

### defaultTiers (map\[string\]string)

**Default Value**:

``` yaml
{}
```

## Section: queues

### executionQueues (interfaces.ExecutionQueues)

**Default Value**:

``` yaml
[]
```

### workflowConfigs (interfaces.WorkflowConfigs)

**Default Value**:

``` yaml
[]
```

## Section: registration

### maxWorkflowNodes (int)

**Default Value**:

``` yaml
"100"
```

### maxLabelEntries (int)

**Default Value**:

``` yaml
"0"
```

### maxAnnotationEntries (int)

**Default Value**:

``` yaml
"0"
```

### workflowSizeLimit (string)

**Default Value**:

``` yaml
""
```

## Section: remotedata

### scheme (string)

**Default Value**:

``` yaml
none
```

### region (string)

**Default Value**:

``` yaml
""
```

### signedUrls ([interfaces.SignedURL](#interfaces.signedurl))

**Default Value**:

``` yaml
durationMinutes: 0
enabled: false
signingPrincipal: ""
```

### maxSizeInBytes (int64)

**Default Value**:

``` yaml
"2097152"
```

### inlineEventDataPolicy (int)

Specifies how inline execution event data should be saved in the backend

**Default Value**:

``` yaml
Offload
```

#### interfaces.SignedURL

##### enabled (bool)

Whether signed urls should even be returned with GetExecutionData,
GetNodeExecutionData and GetTaskExecutionData response objects.

**Default Value**:

``` yaml
"false"
```

##### durationMinutes (int)

**Default Value**:

``` yaml
"0"
```

##### signingPrincipal (string)

**Default Value**:

``` yaml
""
```

## Section: scheduler

### profilerPort ([config.Port](#config.port))

**Default Value**:

``` yaml
10254
```

### eventScheduler ([interfaces.EventSchedulerConfig](#interfaces.eventschedulerconfig))

**Default Value**:

``` yaml
aws: null
local: {}
region: ""
scheduleNamePrefix: ""
scheduleRole: ""
scheme: local
targetName: ""
```

### workflowExecutor ([interfaces.WorkflowExecutorConfig](#interfaces.workflowexecutorconfig))

**Default Value**:

``` yaml
accountId: ""
aws: null
local:
  adminRateLimit:
    burst: 10
    tps: 100
  useUTCTz: false
region: ""
scheduleQueueName: ""
scheme: local
```

### reconnectAttempts (int)

**Default Value**:

``` yaml
"0"
```

### reconnectDelaySeconds (int)

**Default Value**:

``` yaml
"0"
```

#### interfaces.EventSchedulerConfig

##### scheme (string)

**Default Value**:

``` yaml
local
```

##### region (string)

**Default Value**:

``` yaml
""
```

##### scheduleRole (string)

**Default Value**:

``` yaml
""
```

##### targetName (string)

**Default Value**:

``` yaml
""
```

##### scheduleNamePrefix (string)

**Default Value**:

``` yaml
""
```

##### aws (interfaces.AWSSchedulerConfig)

**Default Value**:

``` yaml
null
```

##### local ([interfaces.FlyteSchedulerConfig](#interfaces.flyteschedulerconfig))

**Default Value**:

``` yaml
{}
```

#### interfaces.FlyteSchedulerConfig

#### interfaces.WorkflowExecutorConfig

##### scheme (string)

**Default Value**:

``` yaml
local
```

##### region (string)

**Default Value**:

``` yaml
""
```

##### scheduleQueueName (string)

**Default Value**:

``` yaml
""
```

##### accountId (string)

**Default Value**:

``` yaml
""
```

##### aws (interfaces.AWSWorkflowExecutorConfig)

**Default Value**:

``` yaml
null
```

##### local ([interfaces.FlyteWorkflowExecutorConfig](#interfaces.flyteworkflowexecutorconfig))

**Default Value**:

``` yaml
adminRateLimit:
  burst: 10
  tps: 100
useUTCTz: false
```

#### interfaces.FlyteWorkflowExecutorConfig

##### adminRateLimit ([interfaces.AdminRateLimit](#interfaces.adminratelimit))

**Default Value**:

``` yaml
burst: 10
tps: 100
```

##### useUTCTz (bool)

**Default Value**:

``` yaml
"false"
```

#### interfaces.AdminRateLimit

##### tps (float64)

**Default Value**:

``` yaml
"100"
```

##### burst (int)

**Default Value**:

``` yaml
"10"
```

## Section: secrets

### secrets-prefix (string)

Prefix where to look for secrets file

**Default Value**:

``` yaml
/etc/secrets
```

### env-prefix (string)

Prefix for environment variables

**Default Value**:

``` yaml
FLYTE_SECRET_
```

## Section: server

### httpPort (int)

On which http port to serve admin

**Default Value**:

``` yaml
"8088"
```

### grpcPort (int)

deprecated

**Default Value**:

``` yaml
"0"
```

### grpcServerReflection (bool)

deprecated

**Default Value**:

``` yaml
"false"
```

### kube-config (string)

Path to kubernetes client config file, default is empty, useful for
incluster config.

**Default Value**:

``` yaml
""
```

### master (string)

The address of the Kubernetes API server.

**Default Value**:

``` yaml
""
```

### security ([config.ServerSecurityOptions](#config.serversecurityoptions))

**Default Value**:

``` yaml
allowCors: true
allowedHeaders:
- Content-Type
- flyte-authorization
allowedOrigins:
- '*'
auditAccess: false
insecureCookieHeader: false
secure: false
ssl:
  certificateFile: ""
  keyFile: ""
useAuth: false
```

### grpc ([config.GrpcConfig](#config.grpcconfig))

**Default Value**:

``` yaml
enableGrpcLatencyMetrics: false
maxMessageSizeBytes: 0
port: 8089
serverReflection: true
```

### thirdPartyConfig ([config.ThirdPartyConfigOptions](#config.thirdpartyconfigoptions))

Deprecated please use auth.appAuth.thirdPartyConfig instead.

**Default Value**:

``` yaml
flyteClient:
  audience: ""
  clientId: ""
  redirectUri: ""
  scopes: []
```

### dataProxy ([config.DataProxyConfig](#config.dataproxyconfig))

Defines data proxy configuration.

**Default Value**:

``` yaml
download:
  maxExpiresIn: 1h0m0s
upload:
  defaultFileNameLength: 20
  maxExpiresIn: 1h0m0s
  maxSize: 6Mi
  storagePrefix: ""
```

### readHeaderTimeoutSeconds (int)

The amount of time allowed to read request headers.

**Default Value**:

``` yaml
"32"
```

### kubeClientConfig ([config.KubeClientConfig (kubeClientConfig)](#config.kubeclientconfig-kubeclientconfig))

Configuration to control the Kubernetes client

**Default Value**:

``` yaml
burst: 25
qps: 100
timeout: 30s
```

#### config.DataProxyConfig

##### upload ([config.DataProxyUploadConfig](#config.dataproxyuploadconfig))

Defines data proxy upload configuration.

**Default Value**:

``` yaml
defaultFileNameLength: 20
maxExpiresIn: 1h0m0s
maxSize: 6Mi
storagePrefix: ""
```

##### download ([config.DataProxyDownloadConfig](#config.dataproxydownloadconfig))

Defines data proxy download configuration.

**Default Value**:

``` yaml
maxExpiresIn: 1h0m0s
```

#### config.DataProxyDownloadConfig

##### maxExpiresIn ([config.Duration](#config.duration))

Maximum allowed expiration duration.

**Default Value**:

``` yaml
1h0m0s
```

#### config.DataProxyUploadConfig

##### maxSize ([resource.Quantity](#resource.quantity))

Maximum allowed upload size.

**Default Value**:

``` yaml
6Mi
```

##### maxExpiresIn ([config.Duration](#config.duration))

Maximum allowed expiration duration.

**Default Value**:

``` yaml
1h0m0s
```

##### defaultFileNameLength (int)

Default length for the generated file name if not provided in the
request.

**Default Value**:

``` yaml
"20"
```

##### storagePrefix (string)

Storage prefix to use for all upload requests.

**Default Value**:

``` yaml
""
```

#### config.GrpcConfig

##### port (int)

On which grpc port to serve admin

**Default Value**:

``` yaml
"8089"
```

##### serverReflection (bool)

Enable GRPC Server Reflection

**Default Value**:

``` yaml
"true"
```

##### maxMessageSizeBytes (int)

The max size in bytes for incoming gRPC messages

**Default Value**:

``` yaml
"0"
```

##### enableGrpcLatencyMetrics (bool)

Enable grpc latency metrics. Note Histograms metrics can be expensive on
Prometheus servers.

**Default Value**:

``` yaml
"false"
```

#### config.KubeClientConfig (kubeClientConfig)

##### qps (int32)

Max QPS to the master for requests to KubeAPI. 0 defaults to 5.

**Default Value**:

``` yaml
"100"
```

##### burst (int)

Max burst rate for throttle. 0 defaults to 10

**Default Value**:

``` yaml
"25"
```

##### timeout ([config.Duration](#config.duration))

Max duration allowed for every request to KubeAPI before giving up. 0
implies no timeout.

**Default Value**:

``` yaml
30s
```

#### config.ServerSecurityOptions

##### secure (bool)

**Default Value**:

``` yaml
"false"
```

##### ssl ([config.SslOptions](#config.ssloptions))

**Default Value**:

``` yaml
certificateFile: ""
keyFile: ""
```

##### useAuth (bool)

**Default Value**:

``` yaml
"false"
```

##### insecureCookieHeader (bool)

**Default Value**:

``` yaml
"false"
```

##### auditAccess (bool)

**Default Value**:

``` yaml
"false"
```

##### allowCors (bool)

**Default Value**:

``` yaml
"true"
```

##### allowedOrigins (\[\]string)

**Default Value**:

``` yaml
- '*'
```

##### allowedHeaders (\[\]string)

**Default Value**:

``` yaml
- Content-Type
- flyte-authorization
```

#### config.SslOptions

##### certificateFile (string)

**Default Value**:

``` yaml
""
```

##### keyFile (string)

**Default Value**:

``` yaml
""
```

## Section: storage

### type (string)

Sets the type of storage to configure \[s3/minio/local/mem/stow\].

**Default Value**:

``` yaml
s3
```

### connection ([storage.ConnectionConfig](#storage.connectionconfig))

**Default Value**:

``` yaml
access-key: ""
auth-type: iam
disable-ssl: false
endpoint: ""
region: us-east-1
secret-key: ""
```

### stow ([storage.StowConfig](#storage.stowconfig))

Storage config for stow backend.

**Default Value**:

``` yaml
{}
```

### container (string)

Initial container (in s3 a bucket) to create -if it doesn\'t exist-.\'

**Default Value**:

``` yaml
""
```

### enable-multicontainer (bool)

If this is true, then the container argument is overlooked and
redundant. This config will automatically open new connections to new
containers/buckets as they are encountered

**Default Value**:

``` yaml
"false"
```

### cache ([storage.CachingConfig](#storage.cachingconfig))

**Default Value**:

``` yaml
max_size_mbs: 0
target_gc_percent: 0
```

### limits ([storage.LimitsConfig](#storage.limitsconfig))

Sets limits for stores.

**Default Value**:

``` yaml
maxDownloadMBs: 2
```

### defaultHttpClient ([storage.HTTPClientConfig](#storage.httpclientconfig))

Sets the default http client config.

**Default Value**:

``` yaml
headers: null
timeout: 0s
```

### signedUrl ([storage.SignedURLConfig](#storage.signedurlconfig))

Sets config for SignedURL.

**Default Value**:

``` yaml
{}
```

#### storage.CachingConfig

##### max_size_mbs (int)

Maximum size of the cache where the Blob store data is cached in-memory.
If not specified or set to 0, cache is not used

**Default Value**:

``` yaml
"0"
```

##### target_gc_percent (int)

Sets the garbage collection target percentage.

**Default Value**:

``` yaml
"0"
```

#### storage.ConnectionConfig

##### endpoint ([config.URL](#config.url))

URL for storage client to connect to.

**Default Value**:

``` yaml
""
```

##### auth-type (string)

Auth Type to use \[iam,accesskey\].

**Default Value**:

``` yaml
iam
```

##### access-key (string)

Access key to use. Only required when authtype is set to accesskey.

**Default Value**:

``` yaml
""
```

##### secret-key (string)

Secret to use when accesskey is set.

**Default Value**:

``` yaml
""
```

##### region (string)

Region to connect to.

**Default Value**:

``` yaml
us-east-1
```

##### disable-ssl (bool)

Disables SSL connection. Should only be used for development.

**Default Value**:

``` yaml
"false"
```

#### storage.HTTPClientConfig

##### headers (map\[string\]\[\]string)

**Default Value**:

``` yaml
null
```

##### timeout ([config.Duration](#config.duration))

Sets time out on the http client.

**Default Value**:

``` yaml
0s
```

#### storage.LimitsConfig

##### maxDownloadMBs (int64)

Maximum allowed download size (in MBs) per call.

**Default Value**:

``` yaml
"2"
```

#### storage.SignedURLConfig

##### stowConfigOverride (map\[string\]string)

**Default Value**:

``` yaml
null
```

#### storage.StowConfig

##### kind (string)

Kind of Stow backend to use. Refer to github/flyteorg/stow

**Default Value**:

``` yaml
""
```

##### config (map\[string\]string)

Configuration for stow backend. Refer to github/flyteorg/stow

**Default Value**:

``` yaml
{}
```

## Section: task_resources

### defaults ([interfaces.TaskResourceSet](#interfaces.taskresourceset))

**Default Value**:

``` yaml
cpu: "2"
ephemeralStorage: "0"
gpu: "0"
memory: 200Mi
```

### limits ([interfaces.TaskResourceSet](#interfaces.taskresourceset))

**Default Value**:

``` yaml
cpu: "2"
ephemeralStorage: "0"
gpu: "1"
memory: 1Gi
```

#### interfaces.TaskResourceSet

##### cpu ([resource.Quantity](#resource.quantity))

**Default Value**:

``` yaml
"2"
```

##### gpu ([resource.Quantity](#resource.quantity))

**Default Value**:

``` yaml
"0"
```

##### memory ([resource.Quantity](#resource.quantity))

**Default Value**:

``` yaml
200Mi
```

##### ephemeralStorage ([resource.Quantity](#resource.quantity))

**Default Value**:

``` yaml
"0"
```

## Section: tasks

### task-plugins ([config.TaskPluginConfig](#config.taskpluginconfig))

Task plugin configuration

**Default Value**:

``` yaml
default-for-task-types: {}
enabled-plugins: []
```

### max-plugin-phase-versions (int32)

Maximum number of plugin phase versions allowed for one phase.

**Default Value**:

``` yaml
"100000"
```

### backoff ([config.BackOffConfig](#config.backoffconfig))

Config for Exponential BackOff implementation

**Default Value**:

``` yaml
base-second: 2
max-duration: 20s
```

### maxLogMessageLength (int)

Deprecated!!! Max length of error message.

**Default Value**:

``` yaml
"0"
```

#### config.BackOffConfig

##### base-second (int)

The number of seconds representing the base duration of the exponential
backoff

**Default Value**:

``` yaml
"2"
```

##### max-duration ([config.Duration](#config.duration))

The cap of the backoff duration

**Default Value**:

``` yaml
20s
```

#### config.TaskPluginConfig

##### enabled-plugins (\[\]string)

Plugins enabled currently

**Default Value**:

``` yaml
[]
```

##### default-for-task-types (map\[string\]string)

**Default Value**:

``` yaml
{}
```
