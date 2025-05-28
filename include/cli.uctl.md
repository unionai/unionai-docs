---
title: Uctl CLI
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
toc_max: 2
---

# Uctl CLI

The `uctl` CLI provides functionality for Union administrators to manage Union-specific entities like users, roles, and Union configuration.

It also includes much of the functionality of the [`union` CLI](../union-cli.md), but since it is a compiled binary (written in Go), it is faster and more efficient than the Python-based `union` CLI and more suitable for situations like running in a CI/CD environment where you might want to avoid the overhead of large Python dependencies.

> [!NOTE]
> If you are not a Union administrator, or if you will be interacting with Union in an environment where
> Python is installed, you should use the [`union` CLI](../union-cli.md) instead.

## Installation

{{< tabs >}}
{{< tab "macOS" >}}
{{< markdown >}}

To install `uctl` on a Mac, use [Homebrew](https://brew.sh/), `curl`, or manually download the binary.

**Homebrew**

```shell
$ brew tap unionai/homebrew-tap
$ brew install uctl
```

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Linux" >}}
{{< markdown >}}

To install `uctl` on Linux, use `curl` or manually download the binary.

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Windows" >}}
{{< markdown >}}

To install `uctl` on Windows, use `curl` or manually download the binary.

**curl**

To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Configuration

{{< variant serverless >}}
{{< markdown >}}

`uctl` will automatically connect to Union Serverless. You do not need to create a configuration file.

> [!WARNING]
> If you have previously used Union, you may have existing configuration files that will interfere with command line access to Union Serverless.
>
> To avoid connection errors, remove any configuration files in the `~/.unionai/` or `~/.union/` directories and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG`.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

To create a configuration file that contains your Union connection information, run the following command, replacing `<union-host-url>` with the URL of your Union instance:

```shell
$ uctl config init --host <union-host-url>
```

This will create a new configuration file at `~/.union/config.yaml`:

```yaml
admin:
  endpoint: dns:///<union-host-url>
  insecure: false
  authType: Pkce
```

> [!NOTE]
> PKCE is the default authentication type. To specify a different authentication type in the configuration file,
> see [Authentication](../../development-cycle/authenticaiton).

### Configuration file location hierarchy

By default, the `uctl` CLI will use the configuration file at `~/.union/config.yaml` to connect to your Union instance unless you override it. `uctl` searches for configuration files in the following order:

* `--config <path-to-config>` flag
* `UNION_CONFIG` environment variable
* `UCTL_CONFIG` environment variable
* `~/.union/config.yaml` file
* `~/.uctl/config.yaml` file

{{< /markdown >}}
{{< /variant >}}

---

