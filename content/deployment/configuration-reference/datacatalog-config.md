---
title: Datacatalog configuration
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
---

# Flyte Datacatalog Configuration

- [application](#section-application)
- [database](#section-database)
- [datacatalog](#section-datacatalog)
- [logger](#section-logger)
- [otel](#section-otel)
- [storage](#section-storage)

## Section: application

### grpcPort (int)

On which grpc port to serve Catalog

**Default Value**:

``` yaml
"8081"
```

### grpcServerReflection (bool)

Enable GRPC Server Reflection

**Default Value**:

``` yaml
"true"
```

### grpcMaxRecvMsgSizeMBs (int)

The max receive message size; if unset defaults to gRPC server default
value

**Default Value**:

``` yaml
"0"
```

### httpPort (int)

On which http port to serve Catalog

**Default Value**:

``` yaml
"8080"
```

### secure (bool)

Whether to run Catalog in secure mode or not

**Default Value**:

``` yaml
"false"
```

### readHeaderTimeoutSeconds (int)

The amount of time allowed to read request headers.

**Default Value**:

``` yaml
"32"
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

#### config.Duration

##### Duration (int64)

**Default Value**:

``` yaml
1h0m0s
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

## Section: datacatalog

### storage-prefix (string)

StoragePrefix specifies the prefix where DataCatalog stores offloaded
ArtifactData in CloudStorage. If not specified, the data will be stored
in the base container directly.

**Default Value**:

``` yaml
metadata
```

### metrics-scope (string)

Scope that the metrics will record under.

**Default Value**:

``` yaml
datacatalog
```

### profiler-port (int)

Port that the profiling service is listening on.

**Default Value**:

``` yaml
"10254"
```

### heartbeat-grace-period-multiplier (int)

Number of heartbeats before a reservation expires without an extension.

**Default Value**:

``` yaml
"3"
```

### max-reservation-heartbeat ([config.Duration](#config.duration))

The maximum available reservation extension heartbeat interval.

**Default Value**:

``` yaml
10s
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
