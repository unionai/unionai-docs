---
title: Authenticating
weight: 12
variants: -flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Authenticating with Union

Union supports three authentication modes to suit different environments and use cases. This guide will help you choose the right authentication method and configure it correctly.

## Quick start

For most users getting started with Union:

1. Create a configuration file:
    ```bash
      flyte create config --endpoint https://your-endpoint.unionai.cloud
    ```

    Optionally, you can also add a default project and domain.
    ```bash
      flyte create config --endpoint http://your-endpoint.unionai.cloud --project flytesnacks --domain development
    ```

2. Run any command to authenticate:
   ```bash
   flyte get project
   ```

This will automatically open your browser to complete authentication.

## Authentication modes

### PKCE authentication (browser-based) {#pkce}

**Default mode** - Uses OAuth2 PKCE flow with automatic browser authentication.

#### When to use

- Interactive development on your laptop or workstation
- Jupyter notebooks running locally or on machines with browser access
- Any environment where you can open a web browser

#### How it works

When you run any Flyte command, Union automatically:
1. Opens your default web browser
2. Prompts you to authenticate
3. Stores credentials securely in your system's keyring that auto-refresh every few hours

> [!NOTE]
> Tokens are stored securely in your system's native keyring (e.g., Keychain Access on macOS). On systems without keyring support, see the [Token storage and keyring](#token-storage) section.

#### Configuration

This is the default authentication type when you create a configuration from the `flyte create config` command.  The generated file has the effect of:

```yaml
admin:
  endpoint: dns:///your-endpoint.hosted.unionai.cloud
  authType: Pkce
  insecure: false
```

Since the PKCE method is default, it's omitted from the generated file, as is disabling SSL.

#### CLI usage

Simply run any command - authentication happens automatically:

```bash
flyte get project
flyte run app.py main
flyte deploy app.py
```

#### Programmatic usage

```python
import flyte
import flyte.remote as remote

# Initialize with PKCE authentication (default)
flyte.init(endpoint="dns:///your-endpoint.hosted.unionai.cloud")

print([t for t in remote.Task.listall(project="flytesnacks", domain="development")])
```

If your configuration file is accessible, you can also initialize with `init_from_config`:

```python
import flyte

flyte.init_from_config("/path/to/config.yaml")
```

Or omitting if you just want to pick up from the default locations.

```python
flyte.init_from_config()
```

### Device flow authentication {#device-flow}

**For headless or browser-restricted environments** - Uses OAuth2 device flow with code verification.

#### When to use

- Remote servers without GUI/browser access
- Hosted notebook environments (Google Colab, AWS SageMaker, Azure ML)
- SSH sessions or terminal-only environments
- Docker containers where browser redirect isn't possible

#### How it works

When you run a command, Union displays a URL and user code. You:
1. Open the URL on any browser (on any device)
2. Enter the displayed code
3. Complete authentication
4. Return to your terminal - the session is now authenticated

Tokens are stored securely in your system's keyring. On systems without keyring support (common in headless Linux environments), see the [Token storage and keyring](#token-storage) section.

#### Configuration

Create or update your config to use device flow:

```bash
flyte create config --endpoint http://your-endpoint.unionai.cloud --auth-type headless
```

Your config file will contain:

```yaml
admin:
  authType: DeviceFlow
  endpoint: dns:///your-endpoint.hosted.unionai.cloud
```

#### CLI usage

When you run a command, you'll see:

```bash
$ flyte get app

To Authenticate, navigate in a browser to the following URL:
https://signin.hosted.unionai.cloud/activate?user_code=TKBJXFFW
```

Open that URL on any device with a browser, enter the code, and authentication completes.

#### Programmatic usage

```python
import flyte

# Initialize with device flow authentication
flyte.init(endpoint="dns:///your-union-endpoint", headless=True)

# Your code here
@flyte.task
def my_task():
    return "Hello Union!"
```

**Example: Google Colab**

```python
# In a Colab notebook
import flyte

# This will display a URL and code in the cell output
flyte.init(
    endpoint="dns:///your-union-endpoint",
    headless=True
)

# Define and run your workflows
@flyte.task
def process_data(data: str) -> str:
    return f"Processed: {data}"
```

### API key authentication (OAuth2 app credentials) {#api-key}

**For automated and CI/CD environments** - Uses OAuth2 client credentials encoded as an API key.

#### When to use

- CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins)
- Automated deployment scripts
- Production workloads
- Any non-interactive environment
- Service-to-service authentication

#### How it works

Union encodes OAuth2 client credentials (client ID and client secret) into a single API key string. This key contains all information needed to connect to Union, including the endpoint.

> [!NOTE]
> **Security Note:** API keys are sensitive credentials. Treat them like passwords:
> - Store them in secret management systems (GitHub Secrets, AWS Secrets Manager, etc.)
> - Never commit them to version control
> - Rotate them regularly
> - Use different keys for different environments

#### Setup

1. Install the Union plugin:

   ```bash
   pip install flyteplugins-union
   ```

2. Ensure the API key is there:

   ```bash
   flyte get api-key my-ci-key
   ```

3. Store this key securely (e.g., in GitHub Secrets, secret manager)

#### Managing API keys

List existing keys:
```bash
flyte get api-key
```

Delete a key:
```bash
flyte delete api-key my-ci-key
```

#### Programmatic usage

```python
import flyte
import os

# Initialize with API key - endpoint is embedded in the key
api_key = os.getenv("FLYTE_API_KEY")
flyte.init(api_key=api_key)
```

**Example: Automated Script**

```python
#!/usr/bin/env python3
import flyte
import os

# Read API key from environment
api_key = os.getenv("FLYTE_API_KEY")
if not api_key:
    raise ValueError("FLYTE_API_KEY environment variable not set")

# Initialize - no endpoint needed
flyte.init(api_key=api_key)

# Deploy or run workflows
@flyte.task
def automated_task():
    return "Deployed from automation"
```

## Comparison table

| Feature | PKCE | Device Flow | API Key |
|---------|------|-------------|---------|
| **Environment** | Browser available | Headless/remote | Fully automated |
| **Authentication** | Automatic browser | Manual code entry | Non-interactive |
| **Token refresh** | Automatic | Automatic | Automatic |
| **Best for** | Local development | Remote notebooks | CI/CD, production |
| **Setup complexity** | Minimal | Minimal | Moderate (requires plugin) |
| **Security** | User credentials | User credentials | App credentials |

## Switching between authentication modes

You can switch authentication modes by updating your config file:

```bash
# Switch to PKCE
flyte create config --endpoint dns:///your-endpoint.hosted.unionai.cloud

# Switch to device flow
flyte create config --endpoint dns:///your-endpoint.hosted.unionai.cloud --auth-type headless
```

Or manually edit your `~/.flyte/config.yaml`:

```yaml
admin:
  authType: Pkce  # or DeviceFlow
  endpoint: dns:///your-union-endpoint
```

## Token storage and keyring {#token-storage}

Flyte stores authentication tokens securely using your system's native keyring. This provides secure credential storage and allows you to stay authenticated across CLI commands and interactive sessions without re-authenticating.

### How it works

When you authenticate using PKCE or device flow, Flyte stores your OAuth tokens in:
- **macOS**: Keychain Access
- **Windows**: Windows Credential Manager
- **Linux**: Secret Service API (GNOME Keyring, KWallet, etc.)

These tokens are automatically refreshed as needed, providing a seamless experience across multiple commands and sessions.

### Systems without keyring support

Some environments, particularly headless Linux systems like remote desktops, Docker containers, or minimal server installations, may not have a keyring service available.

**Symptoms:**
- You are prompted to re-authenticate every time you run a Flyte command
- You need to authenticate again each time you start a new interactive Python session
- You see warnings about keyring access failures

### Solution: Install keyrings.alt

For systems without native keyring support, install the `keyrings.alt` package:

```bash
pip install keyrings.alt
```

This package provides an alternative keyring backend that stores credentials in an encrypted file on disk, allowing token persistence across sessions.

**Installation in different environments:**

```bash
# Standard installation
pip install keyrings.alt

# With UV
uv pip install keyrings.alt

# In a Docker container (add to your Dockerfile)
RUN pip install keyrings.alt
```

After installing `keyrings.alt`, Flyte will automatically use it to store tokens, eliminating the need for repeated authentication.

> [!NOTE]
> While `keyrings.alt` is less secure than native keyring systems, it's significantly better than re-authenticating for every command and is appropriate for headless development environments.

### Verifying keyring functionality

To check if keyring is working correctly:

```python
import keyring
print(keyring.get_keyring())
```

You should see output indicating which keyring backend is active:
- Native keyring: `keyring.backends.OS_X.Keyring` (macOS), `keyring.backends.Windows.WinVaultKeyring` (Windows), etc.
- Alternative keyring: `keyrings.alt.file.PlaintextKeyring` or similar

## Troubleshooting

### Browser doesn't open for PKCE

If the browser doesn't open automatically:
1. Copy the URL shown in your terminal
2. Open it manually in your browser
3. Complete the authentication flow

Alternatively, switch to device flow if you're in a headless environment.

### Device flow code expires

Device flow codes typically expire after a few minutes. If your code expires:
1. Run the command again to get a new code
2. Authenticate more quickly

### API key doesn't work

Ensure you've installed the required plugin:
```bash
pip install flyteplugins-union
```

Verify your API key is set correctly:
```bash
echo $FLYTE_API_KEY
```

## Best practices

1. **Local development**: Use PKCE authentication for the best experience
2. **Remote development**: Use device flow for hosted notebooks and SSH sessions
3. **Production/CI**: Always use API keys for automated environments
4. **API key security**:
   - Store in secret managers (GitHub Secrets, AWS Secrets Manager, Vault)
   - Never commit to version control
   - Rotate regularly
   - Use different keys per environment (dev, staging, prod)
5. **Config management**: Keep your `~/.flyte/config.yaml` in source control (without secrets) to maintain consistent settings across your team
