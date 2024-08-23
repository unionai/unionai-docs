# CLI authentication types

The command line tools [`union`](../api/union-cli) or [`uctl`](../api/uctl-cli) must authenticate to Union in order to perform operations on the platform.
The authentication type is configured in the `config.yaml` file used by the command line tool.
There are three authentication types available: **PKCE**, **DeviceFlow**, and **ClientSecret**.

:::{note}
To create a basic `config.yaml` file, see the [`union` CLI](../api/union-cli.md#configuration) or [`uctl` CLI](../api/uctl-cli/index.md#configuration) documentation.
:::

## PKCE

Proof Key of Code Exchange (PKCE) is the default type.
It opens a browser window allowing the user to log in. The PKCE authentication flow works like this:

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
The DeviceFlow authentication flow works like this:

* The user invokes `union` or `uctl` to perform an operation in Union.
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

The ClientSecret authentication flow works like this:

* The user (or machine bot) invokes `uctl` or `union` to perform an operation in Union.
* Internally the tool authenticates to using the configured secret.
* Upon successful authentication, the command-line action completes.

With this authentication type, you need to first set up an application.
Create the app as described in [Applications](./applications), assigning it a `clientId` and recording the `AppSecret` that is returned.

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