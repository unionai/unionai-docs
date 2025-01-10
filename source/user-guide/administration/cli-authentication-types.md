# CLI authentication types

The command line tools `uctl` or `union` must authenticate to Union in order to perform operations on the platform.
The authentication mechanism is configured in the `config.yaml` file used by the command line tool.

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`. (See [union CLI](../../api-reference/union-cli.md) for more details.)
You can override this behavior to specify a different configuration file by setting the `UNION_CONFIG` environment variable:

```{code-block} shell
export UNION_CONFIG=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `union` by using the `--config` flag:

```{code-block} shell
$ union --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

```{warning}
If you have previously used Union, you may have configuration files left over that will interfere with access to Union Serverless through the `union` CLI tool.
Make sure to remove any files in `~/.unionai/` or `~/.union/` and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG` to avoid conflicts.
```

There are three authentication mechanisms available: **PKCE**, **DeviceFlow**, and **ClientSecret**.

## PKCE

Proof Key of Code Exchange (PKCE) is the default mechanism.
It opens a browser window allowing the user to login. The authentication flow with this mechanism works like this:

* The user invokes `uctl` or `union` to perform an operation in Union.
* A browser window opens allowing the user to log in.
* On successful login, the command-line action completes.

Here is an example `config.yaml` that uses PKCE:

```{code-block} yaml
admin:
  endpoint: https://<YourOrg>.hosted.unionai.cloud
  insecure: false
  authType: Pkce
logger:
  show-source: true
  level: 0
union:
  connection:
    host: https://<YourOrg>.hosted.unionai.cloud
    insecure: false
  auth:
    type: Pkce
```

## DeviceFlow

With DeviceFlow the command line tool returns a URL that the user can then navigate to.
The authentication flow with this mechanism works like this:

* The user invokes `uctl` or `union` to perform an operation in Union.
* The command returns a URL.
* The user navigates to that URL and follows the instructions.
* Upon successful login, the command-line action completes.

Here is an example `config.yaml` that uses DeviceFlow:

```{code-block} yaml
admin:
  endpoint: dns:///<YourOrg>.hosted.unionai.cloud
  insecure: false
  authType: DeviceFlow
logger:
  show-source: true
  level: 0
union:
  connection:
    host: dns:///<YourOrg>.hosted.unionai.cloud
    insecure: false
  auth:
    type: DeviceFlow
```

:::{note}
During authentication, Union attempts to store an authentication token on the keyring service of the operating system.
If you are authenticating from within an SSH session on a Linux based machine, there may not be a keyring service by default.
If you find that browser based authentication is required every time you run or register your workflows, you may need to run
`pip install keyring` or `pip install keyrings.alt` to install a keyring service on your machine.
:::

## ClientSecret

This is the headless option. It is useful for CIs and other bots.

The authentication flow with ClientSecret works like this:

* The user (or machine bot) invokes `uctl` or `union` to perform an operation in Union.
* Internally the tool authenticates to using the configured secret.
* Upon successful authentication, the command-line action completes.

With this mechanism, you need to first set up an application.
Create the app as described in [Applications](./applications.md), assigning it a `clientId` and recording the `AppSecret` that is returned.

You then store the `AppSecret` in either a local file or an environment variable and set up your `config.yaml` to reference it.

Here is an example `config.yaml` that uses ClientSecret with a file:

```{code-block} yaml
admin:
  endpoint: dns:///<YourOrg>.hosted.unionai.cloud
  insecure: false
  authType: ClientSecret
  clientId: <YourAppId>
  clientSecretLocation: /path/to/secret.txt
logger:
  show-source: true
  level: 0
union:
  connection:
    host: dns:///<YourOrg>.hosted.unionai.cloud
    insecure: false
  auth:
    type: ClientSecret
    clientId: <YourAppId>
    clientSecretLocation: /path/to/secret.txt
```

Here is an example that uses ClientSecret with an environment variable:

```{code-block} yaml
admin:
  endpoint: dns:///<YourOrg>.hosted.unionai.cloud
  insecure: false
  authType: ClientSecret
  clientId: <YourAppId>
  clientSecretEnvVar: YOUR_APP_SECRET
logger:
  show-source: true
  level: 0
union:
  connection:
    host: dns:///<YourOrg>.hosted.unionai.cloud
    insecure: false
  auth:
    type: ClientSecret
    clientId: <YourAppId>
    clientSecretEnvVar: YOUR_APP_SECRET
```