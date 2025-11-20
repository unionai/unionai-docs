---
title: "Where uctl CLI Arguments Are Defined"
weight: 100
---

# Where uctl CLI Arguments Are Defined

This document explains where to find the definitions of `uctl` CLI arguments across the Union.ai organization repositories.

## Overview

`uctl` (Union Control Tool) is an enhanced version of `flytectl`, the Flyte command-line tool. It extends `flytectl` with Union-specific functionality while maintaining compatibility with standard Flyte commands.

## Source Code Location

### Primary Repository

The `uctl` CLI is distributed through the **[unionai/uctl](https://github.com/unionai/uctl)** repository:
- **Repository URL**: https://github.com/unionai/uctl
- **Purpose**: Distribution, installation scripts, and documentation
- **Contents**: Binary releases, Homebrew tap configuration, and README

**Important Note**: The `unionai/uctl` repository contains the installation scripts and binaries but does not contain the full source code. The CLI is built from `flytectl` with Union-specific enhancements.

### Binary Releases

Pre-compiled binaries for `uctl` are available in the [releases section](https://github.com/unionai/uctl/releases) for:
- macOS (ARM64 and x86_64)
- Linux (ARM64 and x86_64)
- Windows (ARM64, i386, and x86_64)

## CLI Argument Documentation

### Official Documentation

The complete reference for `uctl` CLI arguments and options is available in the Union.ai documentation:

1. **Self-Managed Installations**:
   - URL: https://www.union.ai/docs/v1/selfmanaged/api-reference/uctl-cli/uctl/
   - Contains: All command-line flags, options, and subcommands

2. **BYOC (Bring Your Own Cloud)**:
   - URL: https://www.union.ai/docs/byoc/api-reference/uctl-cli/
   - Contains: BYOC-specific CLI reference

3. **Serverless**:
   - URL: https://www.union.ai/docs/v1/serverless/api-reference/
   - Contains: Serverless API and CLI reference

### Common Arguments

Key arguments and flags include:

- **Authentication & Connection**:
  - `--admin.endpoint`: Endpoint URL for the Union/Flyte backend
  - `--admin.authType`: Authentication type (default: `pkce`)
  - `--admin.insecure`: Use insecure connection (no TLS)
  - `--admin.audience`: OAuth2 audience setting

- **Configuration**:
  - `--config`: Path to configuration file
  - Environment variables: `UNION_CONFIG`, `UCTL_CONFIG`

- **Resource Management**:
  - `uctl register`: Register workflows and tasks
  - `uctl get`: Retrieve resources
  - `uctl create`: Create resources (projects, users, apps, etc.)
  - `uctl delete`: Delete resources
  - `uctl launch`: Launch workflow executions

## Configuration

### Configuration File

`uctl` uses a YAML configuration file, typically located at `~/.union/config.yaml`. The file can be created with:

```bash
uctl config init --host <union-host-url>
```

### Configuration Search Order

The CLI searches for configuration in this order:
1. `--config <path>` command-line flag
2. `UNION_CONFIG` environment variable
3. `UCTL_CONFIG` environment variable (backward compatibility)
4. `~/.union/config.yaml` (default location)
5. `~/.uctl/config.yaml` (backward compatibility)

## Related Resources

### Flytectl Source

Since `uctl` is based on `flytectl`, you can find the underlying CLI framework in:
- **Repository**: https://github.com/flyteorg/flytectl
- **Documentation**: https://docs.flyte.org/en/latest/flytectl/docs_index.html

### Additional Documentation

- **CLI Authentication**: https://docs.union.ai/byoc/administration/cli-authentication.html
- **Running Code**: https://www.union.ai/docs/byoc/user-guide/development-cycle/running-your-code/
- **CI/CD Deployment**: https://www.union.ai/docs/selfmanaged/user-guide/development-cycle/ci-cd-deployment/

## Examples

### Example Commands

```bash
# Register workflows
uctl register files --project <project> --domain <domain> --archive <file>.tgz --version <ver>

# Create an application spec
uctl create app --appSpecFile app.yaml

# List projects
uctl get project

# Get workflow details
uctl get workflow --project <project> --domain <domain> <workflow-name>
```

### Viewing Help

To see all available commands and arguments:

```bash
# View top-level help
uctl --help

# View help for a specific command
uctl register --help

# View help for a subcommand
uctl create app --help
```

## Summary

To find where `uctl` CLI arguments are defined:

1. **For Usage and Reference**: Check the official Union.ai documentation at https://www.union.ai/docs/
2. **For Installation**: Use the [unionai/uctl](https://github.com/unionai/uctl) repository
3. **For Source Code**: The tool is based on [flytectl](https://github.com/flyteorg/flytectl) with Union-specific enhancements
4. **For Binary Releases**: Download from https://github.com/unionai/uctl/releases

The arguments are implemented in the compiled binary and documented in the official documentation rather than being defined in a single source file in a public repository.
