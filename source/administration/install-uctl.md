# Install the Union.ai CLI `uctl`

While the `unionai` CLI provides the primary mechanism for interacting with Union,
another CLI, called `uctl`, is also provided.

`uctl` provides the same functionality as `unionai` but also includes
additional functionality for managing Union-specific entities like users, roles, and Union configurations.

In addition, `uctl` is a compiled binary, which makes it faster and more efficient than the Python-based
`unionai` CLI and more suitable for situations like running in CI/CD environment where you might want to
avoid the overhead of large Python dependencies.

To install `uctl`, you can use Homebrew on macOS or `curl` on macOS, Linux, or Windows:

::::{tab-set}

:::{tab-item} macOS
To use [Homebrew](https://brew.sh/), do this:

```{code-block} shell
$ brew tap unionai/homebrew-tap
$ brew install uctl
```

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and do this:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::

:::{tab-item} Linux
To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and do this:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::

:::{tab-item} Windows
To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and do this:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::
::::

:::{note}
`uctl`is an enhanced version of `flytectl`, [the Flyte command-line tool](https://docs.flyte.org/en/latest/flytectl/docs_index.html).
It adds Union-specific functionality, letting you manage not only Flyte entities (projects, domains, workflows, tasks, and launch plans) but also Union-specific entities like users, roles, and Union configurations.
:::