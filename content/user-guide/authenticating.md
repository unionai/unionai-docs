---
title: Authenticating
weight: 7
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
3. Stores credentials that auto-refresh every few hours

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
