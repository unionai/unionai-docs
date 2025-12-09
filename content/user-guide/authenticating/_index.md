---
title: Authenticating
weight: 1
variants: +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Authenticating with Union

Union supports three authentication modes to suit different environments and use cases. This guide will help you choose the right authentication method and configure it correctly.

## Quick Start

For most users getting started with Union:

1. Create a configuration file:
```bash
   flyte create config --endpoint dns:///your-union-endpoint
```

2. Run any command to authenticate:
   ```bash
   flyte get project
   ```

This will automatically open your browser to complete authentication.

## Authentication Modes

### PKCE Authentication (Browser-based) {#pkce}

**Default mode** - Uses OAuth2 PKCE flow with automatic browser authentication.

#### When to Use

- Interactive development on your laptop or workstation
- Jupyter notebooks running locally or on machines with browser access
- Any environment where you can open a web browser

#### How It Works

When you run any Flyte command, Union automatically:
1. Opens your default web browser
2. Prompts you to authenticate
3. Stores credentials that auto-refresh every few hours

#### Configuration

This is the default authentication type when you create a config:

```bash
flyte create config --endpoint dns:///your-union-endpoint
```

Your config file will contain:

```yaml
admin:
  authType: pkce
  endpoint: dns:///your-union-endpoint
image:
  builder: remote
task:
  domain: development
  org: your-org
  project: your-project
```

#### CLI Usage

Simply run any command - authentication happens automatically:

```bash
flyte get project
flyte run app.py main
flyte deploy app.py
```

#### Programmatic Usage

```python
import flyte

# Initialize with PKCE authentication (default)
flyte.init(endpoint="dns:///your-union-endpoint")

# Your code here
@flyte.task
def my_task():
    return "Hello Union!"
```

---

### Device Flow Authentication {#device-flow}

**For headless or browser-restricted environments** - Uses OAuth2 device flow with code verification.

#### When to Use

- Remote servers without GUI/browser access
- Hosted notebook environments (Google Colab, AWS SageMaker, Azure ML)
- SSH sessions or terminal-only environments
- Docker containers where browser redirect isn't possible

#### How It Works

When you run a command, Union displays a URL and user code. You:
1. Open the URL on any browser (on any device)
2. Enter the displayed code
3. Complete authentication
4. Return to your terminal - the session is now authenticated

#### Configuration

Create or update your config to use device flow:

```bash
flyte create config --endpoint dns:///your-union-endpoint --auth-type device-flow
```

Your config file will contain:

```yaml
admin:
  authType: device-flow
  endpoint: dns:///your-union-endpoint
image:
  builder: remote
task:
  domain: development
  org: your-org
  project: your-project
```

#### CLI Usage

When you run a command, you'll see:

```bash
$ flyte get app

To Authenticate, navigate in a browser to the following URL:
https://signin.hosted.unionai.cloud/activate?user_code=TKBJXFFW
```

Open that URL on any device with a browser, enter the code, and authentication completes.

#### Programmatic Usage

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

---

### API Key Authentication (OAuth2 App Credentials) {#api-key}

**For automated and CI/CD environments** - Uses OAuth2 client credentials encoded as an API key.

#### When to Use

- CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins)
- Automated deployment scripts
- Production workloads
- Any non-interactive environment
- Service-to-service authentication

#### How It Works

Union encodes OAuth2 client credentials (client ID and client secret) into a single API key string. This key contains all information needed to connect to Union, including the endpoint.

API keys are sensitive credentials. Treat them like passwords:
- Store them in secret management systems (GitHub Secrets, AWS Secrets Manager, etc.)
- Never commit them to version control
- Rotate them regularly
- Use different keys for different environments

#### Setup

1. Install the Union plugin:

   ```bash
   pip install flyteplugins-union
   ```

2. Create an API key:

   ```bash
   flyte create api-key --name my-ci-key
   ```

   This outputs an API key that looks like:
   ```
   union_api_key_abc123def456...
   ```

3. Store this key securely (e.g., in GitHub Secrets, environment variables, secret manager)

#### Managing API Keys

List existing keys:
```bash
flyte get api-key
```

Delete a key:
```bash
flyte delete api-key my-ci-key
```

#### CLI Usage

Set the API key as an environment variable:

```bash
export FLYTE_API_KEY="union_api_key_abc123def456..."
flyte deploy app.py
```

Or pass it directly:

```bash
flyte --api-key="union_api_key_abc123def456..." deploy app.py
```

#### Programmatic Usage

```python
import flyte
import os

# Initialize with API key - endpoint is embedded in the key
api_key = os.getenv("FLYTE_API_KEY")
flyte.init(api_key=api_key)

# Your code here
@flyte.task
def my_task():
    return "Hello Union!"
```

**Example: GitHub Actions**

```yaml
name: Deploy to Union

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install flyte flyteplugins-union

      - name: Deploy to Union
        env:
          FLYTE_API_KEY: ${{ secrets.UNION_API_KEY }}
        run: |
          flyte deploy app.py
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

---

## Comparison Table

| Feature | PKCE | Device Flow | API Key |
|---------|------|-------------|---------|
| **Environment** | Browser available | Headless/remote | Fully automated |
| **Authentication** | Automatic browser | Manual code entry | Non-interactive |
| **Token Refresh** | Automatic | Automatic | Automatic |
| **Best For** | Local development | Remote notebooks | CI/CD, production |
| **Setup Complexity** | Minimal | Minimal | Moderate (requires plugin) |
| **Security** | User credentials | User credentials | App credentials |

## Switching Between Authentication Modes

You can switch authentication modes by updating your config file:

```bash
# Switch to PKCE
flyte create config --endpoint dns:///your-union-endpoint --auth-type pkce

# Switch to device flow
flyte create config --endpoint dns:///your-union-endpoint --auth-type device-flow
```

Or manually edit your `~/.flyte/config.yaml`:

```yaml
admin:
  authType: pkce  # or device-flow
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

### Permission denied errors

Your API key or user account may not have sufficient permissions. Contact your Union administrator to:
- Check project/domain access
- Verify role assignments
- Confirm organization membership

## Best Practices

1. **Local Development**: Use PKCE authentication for the best experience
2. **Remote Development**: Use device flow for hosted notebooks and SSH sessions
3. **Production/CI**: Always use API keys for automated environments
4. **API Key Security**:
   - Store in secret managers (GitHub Secrets, AWS Secrets Manager, Vault)
   - Never commit to version control
   - Rotate regularly
   - Use different keys per environment (dev, staging, prod)
5. **Config Management**: Keep your `~/.flyte/config.yaml` in source control (without secrets) to maintain consistent settings across your team

