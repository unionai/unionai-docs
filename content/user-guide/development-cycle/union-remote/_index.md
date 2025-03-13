---
title: UnionRemote
weight: 1
variants: +flyte +serverless +byoc +byok
---

# UnionRemote

The `UnionRemote` Python API supports functionality similar to that of the `union` CLI, enabling you to manage Union workflows, tasks, launch plans and artifacts from within your Python code.

{{< note >}}
The primary use case of `UnionRemote` is to automate the deployment of Union entities. As such, it is intended for use within scripts *external* to actual Union workflow and task code, for example CI/CD pipeline scripts.

In other words: _Do not use `UnionRemote` within task code._
{{< /note >}}

## Creating a `UnionRemote` object

Ensure that you have the `union` SDK installed, import the `UnionRemote` class and create the object like this:

```python
from union import UnionRemote

remote = UnionRemote()
```

By default, when created with a no-argument constructor, `UnionRemote` will use the prevailing configuration in the local environment to connect to Union, that is, the same configuration as would be used by the `union` CLI in that environment (see [Union CLI > `union` CLI configuration search path](../../../api-reference/union-cli.md#union-cli-configuration-search-path)).

In the default case, as with the `union` CLI, all operations will be applied to the default project, `{@= default_project =@}` and default domain, `development`.

{{< if-variant byoc byok flyte >}}

Alternatively, you can initialize `UnionRemote` by explicitly specifying a `flytekit.configuration.Config` object with connection information to a Union instance, a project, and a domain. Additionally the constructor supports specifying a file upload location (equivalent to a default raw data prefix):

```python
from union import UnionRemote
from flytekit.configuration import Config

remote = UnionRemote(
    config=Config.for_endpoint(endpoint="union.example.com"),
    default_project="my-project",
    default_domain="my-domain",
    data_upload_location="<s3|gs|abs>://my-bucket/my-prefix",
)
```

Here we use the `Config.for_endpoint` method to specify the URL to connect to.
There are number of other ways to configure the `Config` object.
In general, you have all the same options as you would when specifying a connection for the `union` CLI using a `config.yaml` file.

### Authenticating using a client secret

In some cases, you may be running a script with `UnionRemote` in a CI/CD pipeline or via SSH, where you don't have access to a browser for the default authentication flow. In such scenarios, you can use the [client secret](../../administration/cli-authentication-types.md#clientsecret) authentication method to establish a connection to Union. After [creating an API key](../managing-api-keys.md), you can initialize `UnionRemote` as follows:

```python
from union import UnionRemote
from flytekit.configuration import Config, PlatformConfig

remote = FlyteRemote(
        config=Config(
            platform=PlatformConfig(
                endpoint="union.example.com",
                insecure=False,
                client_id="<your-client-id>",  # this is the api-key name
                client_credentials_secret="<your-client-secret>",  # this is the api-key
                auth_mode="client_credentials",
            )
        ),
    )
```


For details see [the API docs for `flytekit.configuration.Config`](../../../api-reference/union-sdk/configuration/index.md)

{{< /if-variant >}}
{{< if-variant serverless >}}

Alternatively, you can initialize `UnionRemote` by explicitly specifying a project, and a domain:

```python
from union import UnionRemote

remote = UnionRemote(
    default_project="my-project",
    default_domain="my-domain",
)
```

{{< /if-variant >}}

