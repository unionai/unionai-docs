---
title: flytectl demo status
variants: +flyte -serverless -byoc -selfmanaged
---

# flytectl demo status

Gets the status of the demo environment.

## Synopsis

Retrieves the status of the demo environment. Currently, Flyte demo runs
as a local Docker container.

Usage:

```shell
$ flytectl demo status
```

## Options

| Option | Type | Description |
|--------|------|-------------|
| `-h`, `--help` | help for status |

### Options inherited from parent commands

| Option | Type | Description |
|--------|------|-------------|
| `--admin.audience` | string | Audience to use when initiating OAuth2 authorization requests. |
| `--admin.authType` | string | Type of OAuth2 flow used for communicating with admin.ClientSecret, Pkce, ExternalCommand are valid values (default "ClientSecret") |
| `--admin.authorizationHeader` | string | Custom metadata header to pass JWT |
| `--admin.authorizationServerUrl` | string | This is the URL to your IdP's authorization server. It'll default to Endpoint |
| `--admin.caCertFilePath` | string | Use specified certificate file to verify the admin server peer. |
| `--admin.clientId` | string | Client ID (default "flytepropeller") |
| `--admin.clientSecretEnvVar` | string | Environment variable containing the client secret |
| `--admin.clientSecretLocation` | string | File containing the client secret (default "/etc/secrets/client_secret") |
| `--admin.command` | strings | Command for external authentication token generation |
| `--admin.defaultOrg` | string | OPTIONAL: Default org to use to support non-org based cli's.'. |
| `--admin.defaultServiceConfig` | string |  |
| `--admin.deviceFlowConfig.pollInterval` | string | amount of time the device flow would poll the token endpoint if auth server doesn't return a polling interval. Okta and google IDP do return an interval' (default "5s") |
| `--admin.deviceFlowConfig.refreshTime` | string | grace period from the token expiry after which it would refresh the token. (default "5m0s") |
| `--admin.deviceFlowConfig.timeout` | string | amount of time the device flow should complete or else it will be cancelled. (default "10m0s") |
| `--admin.endpoint` | string | For admin types,  specify where the uri of the service is located. |
| `--admin.httpProxyURL` | string | OPTIONAL: HTTP Proxy to be used for OAuth requests. |
| `--admin.insecure` | | Use insecure connection. |
| `--admin.insecureSkipVerify` | | InsecureSkipVerify controls whether a client verifies the server's certificate chain and host name.Caution: shouldn't be use for production usecases' |
| `--admin.maxBackoffDelay` | string | Max delay for grpc backoff (default "8s") |
| `--admin.maxMessageSizeBytes` | int | The max size in bytes for incoming gRPC messages |
| `--admin.maxRetries` | int | Max number of gRPC retries (default 4) |
| `--admin.perRetryTimeout` | string | gRPC per retry timeout (default "15s") |
| `--admin.pkceConfig.refreshTime` | string | grace period from the token expiry after which it would refresh the token. (default "5m0s") |
| `--admin.pkceConfig.timeout` | string | Amount of time the browser session would be active for authentication from client app. (default "2m0s") |
| `--admin.proxyCommand` | strings | Command for external proxy-authorization token generation |
| `--admin.scopes` | strings | List of scopes to request |
| `--admin.tokenRefreshWindow` | string | Max duration between token refresh attempt and token expiry. (default "0s") |
| `--admin.tokenUrl` | string | OPTIONAL: Your IdP's token endpoint. It'll be discovered from flyte admin's OAuth Metadata endpoint if not provided. |
| `--admin.useAudienceFromAdmin` | | Use Audience configured from admins public endpoint config. |
| `--admin.useAuth` | | Deprecated: Auth will be enabled/disabled based on admin's dynamically discovered information. |
| `--auth.appAuth.externalAuthServer.allowedAudience` | strings | Optional: A list of allowed audiences. If not provided,  the audience is expected to be the public Uri of the service. |
| `--auth.appAuth.externalAuthServer.baseUrl` | string | This should be the base url of the authorization server that you are trying to hit. With Okta for instance,  it will look something like https://company.okta.com/oauth2/abcdef123456789/ |
| `--auth.appAuth.externalAuthServer.httpProxyURL` | string | OPTIONAL: HTTP Proxy to be used for OAuth requests. |
| `--auth.appAuth.externalAuthServer.metadataUrl` | string | Optional: If the server doesn't support /.well-known/oauth-authorization-server,  you can set a custom metadata url here.' |
| `--auth.appAuth.externalAuthServer.retryAttempts` | int | Optional: The number of attempted retries on a transient failure to get the OAuth metadata (default 5) |
| `--auth.appAuth.externalAuthServer.retryDelay` | string | Optional,  Duration to wait between retries (default "1s") |
| `--auth.appAuth.selfAuthServer.accessTokenLifespan` | string | Defines the lifespan of issued access tokens. (default "30m0s") |
| `--auth.appAuth.selfAuthServer.authorizationCodeLifespan` | string | Defines the lifespan of issued access tokens. (default "5m0s") |
| `--auth.appAuth.selfAuthServer.claimSymmetricEncryptionKeySecretName` | string | OPTIONAL: Secret name to use to encrypt claims in authcode token. (default "claim_symmetric_key") |
| `--auth.appAuth.selfAuthServer.issuer` | string | Defines the issuer to use when issuing and validating tokens. The default value is https://{requestUri.HostAndPort}/ |
| `--auth.appAuth.selfAuthServer.oldTokenSigningRSAKeySecretName` | string | OPTIONAL: Secret name to use to retrieve Old RSA Signing Key. This can be useful during key rotation to continue to accept older tokens. (default "token_rsa_key_old.pem") |
| `--auth.appAuth.selfAuthServer.refreshTokenLifespan` | string | Defines the lifespan of issued access tokens. (default "1h0m0s") |
| `--auth.appAuth.selfAuthServer.tokenSigningRSAKeySecretName` | string | OPTIONAL: Secret name to use to retrieve RSA Signing Key. (default "token_rsa_key.pem") |
| `--auth.appAuth.thirdPartyConfig.flyteClient.audience` | string | Audience to use when initiating OAuth2 authorization requests. |
| `--auth.appAuth.thirdPartyConfig.flyteClient.clientId` | string | public identifier for the app which handles authorization for a Flyte deployment (default "flytectl") |
| `--auth.appAuth.thirdPartyConfig.flyteClient.redirectUri` | string | This is the callback uri registered with the app which handles authorization for a Flyte deployment (default "http://localhost:53593/callback") |
| `--auth.appAuth.thirdPartyConfig.flyteClient.scopes` | strings | Recommended scopes for the client to request. (default [all,offline]) |
| `--auth.disableForGrpc` | | Disables auth enforcement on Grpc Endpoints. |
| `--auth.disableForHttp` | | Disables auth enforcement on HTTP Endpoints. |
| `--auth.grpcAuthorizationHeader` | string | (default "flyte-authorization") |
| `--auth.httpAuthorizationHeader` | string | (default "flyte-authorization") |
| `--auth.httpProxyURL` | string | OPTIONAL: HTTP Proxy to be used for OAuth requests. |
| `--auth.tokenEndpointProxyPath` | string | The path used to proxy calls to the TokenURL |
| `--auth.userAuth.cookieBlockKeySecretName` | string | OPTIONAL: Secret name to use for cookie block key. (default "cookie_block_key") |
| `--auth.userAuth.cookieHashKeySecretName` | string | OPTIONAL: Secret name to use for cookie hash key. (default "cookie_hash_key") |
| `--auth.userAuth.cookieSetting.domain` | string | OPTIONAL: Allows you to set the domain attribute on the auth cookies. |
| `--auth.userAuth.cookieSetting.sameSitePolicy` | string | OPTIONAL: Allows you to declare if your cookie should be restricted to a first-party or same-site context.Wrapper around http.SameSite. (default "DefaultMode") |
| `--auth.userAuth.httpProxyURL` | string | OPTIONAL: HTTP Proxy to be used for OAuth requests. |
| `--auth.userAuth.idpQueryParameter` | string | idp query parameter used for selecting a particular IDP for doing user authentication. Eg: for Okta passing idp={IDP-ID} forces the authentication to happen with IDP-ID |
| `--auth.userAuth.openId.baseUrl` | string |  |
| `--auth.userAuth.openId.clientId` | string |  |
| `--auth.userAuth.openId.clientSecretFile` | string |  |
| `--auth.userAuth.openId.clientSecretName` | string | (default "oidc_client_secret") |
| `--auth.userAuth.openId.scopes` | strings | (default [openid,profile]) |
| `--auth.userAuth.redirectUrl` | string | (default "/console") |
| `--authorizer.internalCommunicationConfig.enabled` | | Enables authorization decisions for internal communication. (default true) |
| `--authorizer.internalCommunicationConfig.ingressIdentity` | string | IngressIdentity used in the cluster. Needed to exclude the communication coming from ingress. (default "ingress-nginx.ingress-nginx.serviceaccount.identity.linkerd.cluster.local") |
| `--authorizer.internalCommunicationConfig.tenantUrlPatternIdentity` | string | UrlPatternIdentity of the internal tenant service endpoint identities. (default "{{ service }}.{{ org }}.serviceaccount.identity.linkerd.cluster.local") |
| `--authorizer.internalCommunicationConfig.urlPatternIdentity` | string | UrlPatternIdentity of the internal service endpoint identities. (default "{{ service }}-helmchart.{{ service }}.serviceaccount.identity.linkerd.cluster.local") |
| `--authorizer.mode` | string | (default "Active") |
| `--authorizer.organizationConfig.PolicyConfig.adminPolicyDescription` | string | description for the boilerplate admin policy (default "Contributor permissions and full admin permissions to manage users and view usage dashboards") |
| `--authorizer.organizationConfig.PolicyConfig.contributorPolicyDescription` | string | description for the boilerplate contributor policy (default "Viewer permissions and permissions to create workflows, tasks, launch plans, and executions") |
| `--authorizer.organizationConfig.PolicyConfig.defaultUserPolicyRoleType` | string | name of the role type to determine which default policy new users added to the organization should be assigned (default "Viewer") |
| `--authorizer.organizationConfig.PolicyConfig.serverlessContributorPolicyDescription` | string | description for the boilerplate serverless contributor policy (default "Viewer permissions and permissions to create workflows, tasks, launch plans, and executions") |
| `--authorizer.organizationConfig.PolicyConfig.serverlessViewerPolicyDescription` | string | description for the boilerplate serverless viewer policy (default "Permissions to view Flyte entities") |
| `--authorizer.organizationConfig.PolicyConfig.viewerPolicyDescription` | string | description for the boilerplate viewer policy (default "Permissions to view Flyte entities") |
| `--authorizer.organizationConfig.defaultPolicyCacheDuration` | string | Cache entry duration for the store of the default policy per organization (default "10m0s") |
| `--authorizer.syncRuleRefreshInterval` | string | (default "1m0s") |
| `--authorizer.type` | string | (default "UserClouds") |
| `--authorizer.userCloudsClient.cache.redis.ttl.edgeTypes` | string | Specifies how long edge types remain in the cache.. (default "30m0s") |
| `--authorizer.userCloudsClient.cache.redis.ttl.edges` | string | Specifies how long edges remain in the cache. (default "30m0s") |
| `--authorizer.userCloudsClient.cache.redis.ttl.objectTypes` | string | Specifies how long object types remain in the cache. (default "30m0s") |
| `--authorizer.userCloudsClient.cache.redis.ttl.objects` | string | Specifies how long objects remain in the cache. (default "30m0s") |
| `--authorizer.userCloudsClient.cache.type` | string | Cache type to use. (default "none") |
| `--authorizer.userCloudsClient.clientID` | string | UserClouds client id |
| `--authorizer.userCloudsClient.clientSecretName` | string | UserCloud client secret name to read from the secret manager. (default "userclouds-client-secret") |
| `--authorizer.userCloudsClient.enableLogging` | | Enable userclouds client's internal logging. Calls to post logs take 250-350 ms and will impact p99 latency,  enable with caution. |
| `--authorizer.userCloudsClient.tenantID` | string | UserClouds tenant id. Should be a UUID. |
| `--authorizer.userCloudsClient.tenantUrl` | string | Something like https://{yourtenant}.tenant.userclouds.com |
| `--config` | string | config file (default is /Users/andrew/.union/config.yaml) |
| `--connection.environment` | string |  |
| `--connection.region` | string |  |
| `--connection.rootTenantURLPattern` | string | Pattern for tenant url. (default "dns:///{{ organization }}.cloud-staging.union.ai") |
| `--console.endpoint` | string | Endpoint of console,  if different than flyte admin |
| `--database.connMaxLifeTime` | string | sets the maximum amount of time a connection may be reused (default "1h0m0s") |
| `--database.enableForeignKeyConstraintWhenMigrating` | | Whether to enable gorm foreign keys when migrating the db |
| `--database.maxIdleConnections` | int | maxIdleConnections sets the maximum number of connections in the idle connection pool. (default 10) |
| `--database.maxOpenConnections` | int | maxOpenConnections sets the maximum number of open connections to the database. (default 100) |
| `--database.postgres.dbname` | string | The database name (default "postgres") |
| `--database.postgres.debug` | |  |
| `--database.postgres.host` | string | The host name of the database server (default "localhost") |
| `--database.postgres.options` | string | See http://gorm.io/docs/connecting_to_the_database.html for available options passed,  in addition to the above. (default "sslmode=disable") |
| `--database.postgres.password` | string | The database password. (default "postgres") |
| `--database.postgres.passwordPath` | string | Points to the file containing the database password. |
| `--database.postgres.port` | int | The port name of the database server (default 30001) |
| `--database.postgres.readReplicaHost` | string | The host name of the read replica database server (default "localhost") |
| `--database.postgres.username` | string | The database user who is connecting to the server. (default "postgres") |
| `--database.sqlite.file` | string | The path to the file (existing or new) where the DB should be created / stored. If existing,  then this will be re-used,  else a new will be created |
| `--db.connectionPool.maxConnectionLifetime` | string | (default "0s") |
| `--db.connectionPool.maxIdleConnections` | int |  |
| `--db.connectionPool.maxOpenConnections` | int |  |
| `--db.dbname` | string | (default "postgres") |
| `--db.debug` | |  |
| `--db.host` | string | (default "postgres") |
| `--db.log_level` | int | (default 4) |
| `--db.options` | string | (default "sslmode=disable") |
| `--db.password` | string |  |
| `--db.passwordPath` | string |  |
| `--db.port` | int | (default 5432) |
| `--db.username` | string | (default "postgres") |
| `-d`, `--domain` | string | Specifies the Flyte project's domain. |
| `--files.archive` | | Pass in archive file either an http link or local path. |
| `--files.assumableIamRole` | string | Custom assumable iam auth role to register launch plans with. |
| `--files.continueOnError` | | Continue on error when registering files. |
| `--files.destinationDirectory` | string | Location of source code in container. |
| `--files.dryRun` | | Execute command without making any modifications. |
| `--files.enableSchedule` | | Enable the schedule if the files contain schedulable launchplan. |
| `--files.force` | | Force use of version number on entities registered with flyte. |
| `--files.k8ServiceAccount` | string | Deprecated. Please use `--K8sServiceAccount`|
| `--files.k8sServiceAccount` | string | Custom kubernetes service account auth role to register launch plans with. |
| `--files.outputLocationPrefix` | string | Custom output location prefix for offloaded types (files/schemas). |
| `--files.sourceUploadPath` | string | Deprecated: Update flyte admin to avoid having to configure storage access from flytectl. |
| `--files.version` | string | Version of the entity to be registered with flyte which are un-versioned after serialization. |
| `--logger.formatter.type` | string | Sets logging format type. (default "json") |
| `--logger.level` | int | Sets the minimum logging level. (default 3) |
| `--logger.mute` | | Mutes all logs regardless of severity. Intended for benchmarks/tests only. |
| `--logger.show-source` | | Includes source code location in logs. |
| `--org` | string | Organization to work on. If not set,  default to user's org. |
| `--otel.file.filename` | string | Filename to store exported telemetry traces (default "/tmp/trace.txt") |
| `--otel.jaeger.endpoint` | string | Endpoint for the jaeger telemetry trace ingestor (default "http://localhost:14268/api/traces") |
| `--otel.otlpgrpc.endpoint` | string | Endpoint for the OTLP telemetry trace collector (default "http://localhost:4317") |
| `--otel.otlphttp.endpoint` | string | Endpoint for the OTLP telemetry trace collector (default "http://localhost:4318/v1/traces") |
| `--otel.sampler.parentSampler` | string | Sets the parent sampler to use for the tracer (default "always") |
| `--otel.type` | string | Sets the type of exporter to configure [noop/file/jaeger/otlpgrpc/otlphttp]. (default "noop") |
| `-o`, `--output` | string | Specifies the output type - supported formats [TABLE JSON YAML DOT DOTURL]. NOTE: dot, doturl are only supported for Workflow (default "table") |
| `--plugins.catalogcache.reader.maxItems` | int | Maximum number of entries to keep in the index. (default 10000) |
| `--plugins.catalogcache.reader.maxRetries` | int | Maximum number of retries per item. (default 3) |
| `--plugins.catalogcache.reader.workers` | int | Number of concurrent workers to start processing the queue. (default 10) |
| `--plugins.catalogcache.writer.maxItems` | int | Maximum number of entries to keep in the index. (default 10000) |
| `--plugins.catalogcache.writer.maxRetries` | int | Maximum number of retries per item. (default 3) |
| `--plugins.catalogcache.writer.workers` | int | Number of concurrent workers to start processing the queue. (default 10) |
| `-p`, `--project` | string | Specifies the Flyte project. |
| `--rediscache.passwordSecretName` | string | Name of secret with Redis password. |
| `--rediscache.primaryEndpoint` | string | Primary endpoint for the redis cache that can be used for both reads and writes. |
| `--rediscache.replicaEndpoint` | string | Replica endpoint for the redis cache that can be used for reads. |
| `--secrets.env-prefix` | string | Prefix for environment variables (default "FLYTE_SECRET_") |
| `--secrets.secrets-prefix` | string | Prefix where to look for secrets file (default "/etc/secrets") |
| `--secrets.type` | string | Sets the type of storage to configure [local]. (default "local") |
| `--server.dataProxy.download.maxExpiresIn` | string | Maximum allowed expiration duration. (default "1h0m0s") |
| `--server.dataProxy.upload.defaultFileNameLength` | int | Default length for the generated file name if not provided in the request. (default 20) |
| `--server.dataProxy.upload.maxExpiresIn` | string | Maximum allowed expiration duration. (default "1h0m0s") |
| `--server.dataProxy.upload.maxSize` | string | Maximum allowed upload size. (default "6Mi") |
| `--server.dataProxy.upload.storagePrefix` | string | Storage prefix to use for all upload requests. |
| `--server.grpc.enableGrpcLatencyMetrics` | | Enable grpc latency metrics. Note Histograms metrics can be expensive on Prometheus servers. |
| `--server.grpc.maxMessageSizeBytes` | int | The max size in bytes for incoming gRPC messages |
| `--server.grpc.port` | int | On which grpc port to serve admin (default 8089) |
| `--server.grpc.serverReflection` | | Enable GRPC Server Reflection (default true) |
| `--server.grpcPort` | int | deprecated |
| `--server.grpcServerReflection` | | deprecated |
| `--server.httpPort` | int | On which http port to serve admin (default 8088) |
| `--server.kube-config` | string | Path to kubernetes client config file,  default is empty,  useful for incluster config. |
| `--server.kubeClientConfig.burst` | int | Max burst rate for throttle. 0 defaults to 10 (default 25) |
| `--server.kubeClientConfig.qps` | int32 | Max QPS to the master for requests to KubeAPI. 0 defaults to 5. (default 100) |
| `--server.kubeClientConfig.timeout` | string | Max duration allowed for every request to KubeAPI before giving up. 0 implies no timeout. (default "30s") |
| `--server.master` | string | The address of the Kubernetes API server. |
| `--server.readHeaderTimeoutSeconds` | int | The amount of time allowed to read request headers. (default 32) |
| `--server.security.allowCors` | | (default true) |
| `--server.security.allowedHeaders` | strings | (default [Content-Type,flyte-authorization]) |
| `--server.security.allowedOrigins` | strings | (default [*]) |
| `--server.security.auditAccess` | |  |
| `--server.security.secure` | |  |
| `--server.security.ssl.certificateFile` | string |  |
| `--server.security.ssl.keyFile` | string |  |
| `--server.security.useAuth` | |  |
| `--server.thirdPartyConfig.flyteClient.audience` | string | Audience to use when initiating OAuth2 authorization requests. |
| `--server.thirdPartyConfig.flyteClient.clientId` | string | public identifier for the app which handles authorization for a Flyte deployment |
| `--server.thirdPartyConfig.flyteClient.redirectUri` | string | This is the callback uri registered with the app which handles authorization for a Flyte deployment |
| `--server.thirdPartyConfig.flyteClient.scopes` | strings | Recommended scopes for the client to request. |
| `--server.watchService.maxActiveClusterConnections` | int | (default 5) |
| `--server.watchService.maxPageSize` | int | (default 50000) |
| `--server.watchService.nonTerminalStatusUpdatesInterval` | string | (default "1m0s") |
| `--server.watchService.pollInterval` | string | (default "1s") |
| `--sharedservice.connectPort` | string | On which connect port to serve admin (default "8080") |
| `--sharedservice.grpc.grpcMaxResponseStatusBytes` | int32 | specifies the maximum (uncompressed) size of header list that the client is prepared to accept on grpc calls (default 32000) |
| `--sharedservice.grpc.maxConcurrentStreams` | int | Limit on the number of concurrent streams to each ServerTransport. (default 100) |
| `--sharedservice.grpc.maxMessageSizeBytes` | int | Limit on the size of message that can be received on the server. (default 10485760) |
| `--sharedservice.grpcServerReflection` | | Enable GRPC Server Reflection (default true) |
| `--sharedservice.httpPort` | string | On which http port to serve admin (default "8089") |
| `--sharedservice.kubeConfig` | string | Path to kubernetes client config file. |
| `--sharedservice.master` | string | The address of the Kubernetes API server. |
| `--sharedservice.metrics.enableClientGrpcHistograms` | | Enable client grpc histograms (default true) |
| `--sharedservice.metrics.enableGrpcHistograms` | | Enable grpc histograms (default true) |
| `--sharedservice.metrics.scope` | string | Scope to emit metrics under (default "service:") |
| `--sharedservice.port` | string | On which grpc port to serve admin (default "8080") |
| `--sharedservice.profiler.enabled` | | Enable Profiler on server |
| `--sharedservice.profilerPort` | string | Profile port to start listen for pprof and metric handlers on. (default "10254") |
| `--sharedservice.security.allowCors` | |  |
| `--sharedservice.security.allowLocalhostAccess` | | Whether to permit localhost unauthenticated access to the server |
| `--sharedservice.security.allowedHeaders` | strings |  |
| `--sharedservice.security.allowedOrigins` | strings |  |
| `--sharedservice.security.auditAccess` | |  |
| `--sharedservice.security.orgOverride` | string | Override org in identity context if localhost access enabled |
| `--sharedservice.security.secure` | |  |
| `--sharedservice.security.ssl.certificateAuthorityFile` | string |  |
| `--sharedservice.security.ssl.certificateFile` | string |  |
| `--sharedservice.security.ssl.keyFile` | string |  |
| `--sharedservice.security.useAuth` | |  |
| `--sharedservice.sync.syncInterval` | string | Time interval to sync (default "5m0s") |
| `--storage.cache.max_size_mbs` | int | Maximum size of the cache where the Blob store data is cached in-memory. If not specified or set to 0,  cache is not used |
| `--storage.cache.target_gc_percent` | int | Sets the garbage collection target percentage. |
| `--storage.connection.access-key` | string | Access key to use. Only required when authtype is set to accesskey. |
| `--storage.connection.auth-type` | string | Auth Type to use [iam, accesskey]. (default "iam") |
| `--storage.connection.disable-ssl` | | Disables SSL connection. Should only be used for development. |
| `--storage.connection.endpoint` | string | URL for storage client to connect to. |
| `--storage.connection.region` | string | Region to connect to. (default "us-east-1") |
| `--storage.connection.secret-key` | string | Secret to use when accesskey is set. |
| `--storage.container` | string | Initial container (in s3 a bucket) to create -if it doesn't exist-.' |
| `--storage.defaultHttpClient.timeout` | string | Sets time out on the http client. (default "0s") |
| `--storage.enable-multicontainer` | | If this is true,  then the container argument is overlooked and redundant. This config will automatically open new connections to new containers/buckets as they are encountered |
| `--storage.limits.maxDownloadMBs` | int | Maximum allowed download size (in MBs) per call. (default 2) |
| `--storage.stow.config` | stringToString | Configuration for stow backend. Refer to github/flyteorg/stow (default []) |
| `--storage.stow.kind` | string | Kind of Stow backend to use. Refer to github/flyteorg/stow |
| `--storage.type` | string | Sets the type of storage to configure [s3/minio/local/mem/stow]. (default "s3") |
| `--union.auth.authorizationMetadataKey` | string | Authorization Header to use when passing Access Tokens to the server (default "flyte-authorization") |
| `--union.auth.clientId` | string | Client ID |
| `--union.auth.clientSecretEnvVar` | string | Environment variable containing the client secret |
| `--union.auth.clientSecretLocation` | string | File containing the client secret |
| `--union.auth.deviceFlow.pollInterval` | string | amount of time the device flow would poll the token endpoint if auth server doesn't return a polling interval. Okta and google IDP do return an interval' (default "5s") |
| `--union.auth.deviceFlow.refreshTime` | string | grace period from the token expiry after which it would refresh the token. (default "5m0s") |
| `--union.auth.deviceFlow.timeout` | string | amount of time the device flow should complete or else it will be cancelled. (default "10m0s") |
| `--union.auth.enable` | | Whether to enable an authenticated conenction when communicating with admin. (default true) |
| `--union.auth.externalAuth.command` | strings | Command for external authentication token generation |
| `--union.auth.pkce.refreshTime` | string | grace period from the token expiry after which it would refresh the token. (default "5m0s") |
| `--union.auth.pkce.timeout` | string | Amount of time the browser session would be active for authentication from client app. (default "15s") |
| `--union.auth.scopes` | strings | List of scopes to request |
| `--union.auth.tokenRefreshWindow` | string | Max duration between token refresh attempt and token expiry. (default "1h0m0s") |
| `--union.auth.tokenUrl` | string | OPTIONAL: Your IdP's token endpoint. It'll be discovered from flyte admin's OAuth Metadata endpoint if not provided. |
| `--union.auth.type` | string | Type of OAuth2 flow used for communicating with admin. (default "Pkce") |
| `--union.cache.maxItemsCount` | int | Maximum number of items to keep in the cache before evicting. (default 1000) |
| `--union.connection.host` | string | Host to connect to (default "dns:///utt-mgdp-stg-us-east-2.cloud-staging.union.ai") |
| `--union.connection.insecure` | | Whether to connect over insecure channel |
| `--union.connection.insecureSkipVerify` | | InsecureSkipVerify controls whether a client verifies the server's certificate chain and host name.Caution: shouldn't be use for production usecases' |
| `--union.connection.keepAliveConfig.permitWithoutStream` | | If true,  client sends keepalive pings even with no active RPCs. |
| `--union.connection.keepAliveConfig.time` | string | After a duration of this time if the client doesn't see any activity it pings the server to see if the transport is still alive. (default "20s") |
| `--union.connection.keepAliveConfig.timeout` | string | After having pinged for keepalive check,  the client waits for a duration of Timeout and if no activity is seen even after that the connection is closed. (default "2m0s") |
| `--union.connection.maxBackoffDelay` | string | Max delay for grpc backoff (default "8s") |
| `--union.connection.maxRecvMsgSize` | int | Maximum size of a message in bytes of a gRPC message (default 10485760) |
| `--union.connection.maxRetries` | int | Max number of gRPC retries (default 4) |
| `--union.connection.minConnectTimeout` | string | Minimum timeout for establishing a connection (default "20s") |
| `--union.connection.perRetryTimeout` | string | gRPC per retry timeout (default "15s") |
| `--union.connection.serviceConfig` | string | Defines gRPC experimental JSON Service Config (default "{"loadBalancingConfig": [{"round_robin":{}}]}") |
| `--union.connection.trustedIdentityClaims.enabled` | | Enables passing of trusted claims while making inter service calls |
| `--union.connection.trustedIdentityClaims.externalIdentityClaim` | string | External identity claim of the service which is authorized to make internal service call. These are verified against userclouds actions |
| `--union.connection.trustedIdentityClaims.externalIdentityTypeClaim` | string | External identity type claim of app or user to use for the current service identity. It should be an 'app' for inter service communication |
| `--union.internalConnectionConfig.-` | stringToString | (default []) |
| `--union.internalConnectionConfig.enabled` | | Enables internal service to service communication instead of going through ingress. |
| `--union.internalConnectionConfig.urlPattern` | string | UrlPattern of the internal service endpoints. (default "{{ service }}-helmchart.{{ service }}.svc.cluster.local:80") |
| `--webhook.awsSecretManager.sidecarImage` | string | Specifies the sidecar docker image to use (default "docker.io/amazon/aws-secrets-manager-secret-sidecar:v0.1.4") |
| `--webhook.certDir` | string | Certificate directory to use to write generated certs. Defaults to /etc/webhook/certs/ (default "/etc/webhook/certs") |
| `--webhook.embeddedSecretManagerConfig.awsConfig.region` | string | AWS region |
| `--webhook.embeddedSecretManagerConfig.fileMountInitContainer.image` | string | Specifies init container image to use for mounting secrets as files. (default "busybox:1.28") |
| `--webhook.embeddedSecretManagerConfig.gcpConfig.project` | string | GCP project to be used for secret manager |
| `--webhook.embeddedSecretManagerConfig.type` | string | (default "AWS") |
| `--webhook.gcpSecretManager.sidecarImage` | string | Specifies the sidecar docker image to use (default "gcr.io/google.com/cloudsdktool/cloud-sdk:alpine") |
| `--webhook.listenPort` | int | The port to use to listen to webhook calls. Defaults to 9443 (default 9443) |
| `--webhook.localCert` | | write certs locally. Defaults to false |
| `--webhook.metrics-prefix` | string | An optional prefix for all published metrics. (default "flyte:") |
| `--webhook.secretName` | string | Secret name to write generated certs to. (default "flyte-pod-webhook") |
| `--webhook.serviceName` | string | The name of the webhook service. (default "flyte-pod-webhook") |
| `--webhook.servicePort` | int32 | The port on the service that hosting webhook. (default 443) |
| `--webhook.vaultSecretManager.role` | string | Specifies the vault role to use (default "flyte") |
