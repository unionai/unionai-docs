# uctl CLI

While the `union` CLI provides the primary mechanism for interacting with Union,
another CLI, called `uctl`, is also provided.

`uctl` provides the same functionality as `union` but also includes
additional functionality for managing Union-specific entities like users, roles, and Union configurations.

In addition, `uctl` is a compiled binary, which makes it faster and more efficient than the Python-based
`union` CLI and more suitable for situations like running in CI/CD environment where you might want to
avoid the overhead of large Python dependencies.

## Installing `uctl`

To install `uctl`, you can use Homebrew on macOS or `curl` on macOS, Linux, or Windows:

::::{tab-set}

:::{tab-item} macOS
To use [Homebrew](https://brew.sh/), do this:

```{code-block} shell
$ brew tap unionai/homebrew-tap
$ brew install uctl
```

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::

:::{tab-item} Linux
To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::

:::{tab-item} Windows
To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::
::::

:::{note}
`uctl` is an enhanced version of `flytectl`, [the Flyte command-line tool](https://docs.flyte.org/en/latest/flytectl/docs_index.html),
that lets you manage not only Flyte entities (projects, domains, workflows, tasks, and launch plans)
but also Union-specific entities like users, roles, and Union configurations.
:::

## Configuring `uctl`

To configure `uctl` to connect to your Union instance, run the following command:

```{code-block} shell
$ uctl config init --host <union-host-url>
```

Where `<union-host-url>` is the URL of your Union instance.

This will create a new configuration file at `~/.union/config.yaml`:

```{code-block} yaml
union:
  connection:
    host: dns:///<union-host-url>
    insecure: false
  auth:
    type: Pkce
admin:
  endpoint: dns:///<union-host-url>
  insecure: false
  authType: Pkce
```

The `uctl` CLI will use this configuration file to connect to your Union instance by default unless you override it.
The search order for finding the configuration file is:

* `--config <path-to-config>` flag.
* `UNION_CONFIG` environment variable: the same variable as used by the `union CLI`.
* `UCTL_CONFIG` environment variable: for backward compatibility with earlier versions of `uctl`.
* `~/.union/config.yaml`: the default, and the one created by the command above.
* `~/.uctl/config.yaml`: for backward compatibility with earlier versions of `uctl`.

For details on the parameters in the configuration file, see [CLI Authentication](./cli-authentication).

For details on the `union` CLI, see [union CLI](../api/union-cli).
