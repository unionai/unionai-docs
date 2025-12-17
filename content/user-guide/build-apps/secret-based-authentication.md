---
title: Secret-based authentication
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Secret-based authentication

In this guide, we'll deploy a FastAPI app that uses API key authentication with Flyte secrets. This allows you to invoke the endpoint from the public internet in a secure manner without exposing API keys in your code.

## Create the secret

Before defining and deploying the app, you need to create the `API_KEY` secret in Flyte. This secret will store your API key securely.

Create the secret using the Flyte CLI:

```bash
flyte create secret API_KEY <your-api-key-value>
```

For example:

```bash
flyte create secret API_KEY my-secret-api-key-12345
```

> [!NOTE]
> The secret name `API_KEY` must match the key specified in the `flyte.Secret()` call in your code. The secret will be available to your app as the environment variable specified in `as_env_var`.

## Define the FastAPI app

Here's a simple FastAPI app that uses `HTTPAuthorizationCredentials` to authenticate requests using a secret stored in Flyte:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/basic_auth.py" lang=python >}}

As you can see, we:

1. Define a `FastAPI` app
2. Create a `verify_token` function that verifies the API key from the Bearer token
3. Define endpoints that use the `verify_token` function to authenticate requests
4. Configure the `FastAPIAppEnvironment` with:
   - `requires_auth=False` - This allows the endpoint to be reached without going through Flyte's authentication, since we're handling authentication ourselves using the `API_KEY` secret
   - `secrets=flyte.Secret(key="API_KEY", as_env_var="API_KEY")` - This injects the secret value into the `API_KEY` environment variable at runtime

The key difference from using `env_vars` is that secrets are stored securely in Flyte's secret store and injected at runtime, rather than being passed as plain environment variables.

## Deploy the FastAPI app

Once the secret is created, you can deploy the FastAPI app. Make sure your `config.yaml` file is in the same directory as your script, then run:

```bash
python basic_auth.py
```

Or use the Flyte CLI:

```bash
flyte serve basic_auth.py
```

Deploying the application will stream the status to the console and display the app URL:

```
✨ Deploying Application: authenticated-api
🔎 Console URL: https://<union-tenant>/console/projects/my-project/domains/development/apps/fastapi-with-auth
[Status] Pending: App is pending deployment
[Status] Started: Service is ready
🚀 Deployed Endpoint: https://rough-meadow-97cf5.apps.<union-tenant>
```

## Invoke the endpoint

Once deployed, you can invoke the authenticated endpoint using curl:

```bash
curl -X GET "https://rough-meadow-97cf5.apps.<union-tenant>/protected" \
  -H "Authorization: Bearer <your-api-key-value>"
```

Replace `<your-api-key-value>` with the actual API key value you used when creating the secret.

For example, if you created the secret with value `my-secret-api-key-12345`:

```bash
curl -X GET "https://rough-meadow-97cf5.apps.<union-tenant>/protected" \
  -H "Authorization: Bearer my-secret-api-key-12345"
```

You should receive a response:

```json
{
  "message": "This is protected",
  "user": "my-secret-api-key-12345"
}
```

## Authentication for vLLM and SGLang apps

Both vLLM and SGLang apps support API key authentication through their native `--api-key` argument. This allows you to secure your LLM endpoints while keeping them accessible from the public internet.

### Create the authentication secret

Create a secret to store your API key:

```bash
flyte create secret AUTH_SECRET <your-api-key-value>
```

For example:

```bash
flyte create secret AUTH_SECRET my-llm-api-key-12345
```

### Deploy vLLM app with authentication

Here's how to deploy a vLLM app with API key authentication:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/vllm/vllm_with_auth.py" lang=python >}}

Key points:

1. **`requires_auth=False`** - Disables Union's platform-level authentication so the endpoint can be accessed from the public internet
2. **`secrets=flyte.Secret(key="AUTH_SECRET", as_env_var="AUTH_SECRET")`** - Injects the secret as an environment variable
3. **`extra_args=["--api-key", "$AUTH_SECRET"]`** - Passes the API key to vLLM's `--api-key` argument. The `$AUTH_SECRET` will be replaced with the actual secret value at runtime

Deploy the app:

```bash
python vllm_with_auth.py
```

Or use the Flyte CLI:

```bash
flyte serve vllm_with_auth.py
```

### Deploy SGLang app with authentication

Here's how to deploy a SGLang app with API key authentication:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/sglang/sglang_with_auth.py" lang=python >}}

The configuration is similar to vLLM:

1. **`requires_auth=False`** - Disables Union's platform-level authentication
2. **`secrets=flyte.Secret(key="AUTH_SECRET", as_env_var="AUTH_SECRET")`** - Injects the secret as an environment variable
3. **`extra_args=["--api-key", "$AUTH_SECRET"]`** - Passes the API key to SGLang's `--api-key` argument

Deploy the app:

```bash
python sglang_with_auth.py
```

Or use the Flyte CLI:

```bash
flyte serve sglang_with_auth.py
```

### Invoke authenticated LLM endpoints

Once deployed, you can invoke the authenticated endpoints using the OpenAI-compatible API format. Both vLLM and SGLang expose OpenAI-compatible endpoints.

For example, to make a chat completion request:

```bash
curl -X POST "https://your-app-url/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your-api-key-value>" \
  -d '{
    "model": "qwen3-0.6b",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ]
  }'
```

Replace `<your-api-key-value>` with the actual API key value you used when creating the secret.

For example, if you created the secret with value `my-llm-api-key-12345`:

```bash
curl -X POST "https://your-app-url/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer my-llm-api-key-12345" \
  -d '{
    "model": "qwen3-0.6b",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ]
  }'
```

You should receive a response with the model's completion.

> [!NOTE]
> The `$AUTH_SECRET` syntax in `extra_args` is automatically replaced with the actual secret value at runtime. This ensures the API key is never exposed in your code or configuration files.

## Accessing Swagger documentation

The app also includes a public health check endpoint and Swagger UI documentation:

- **Health check**: `https://your-app-url/health`
- **Swagger UI**: `https://your-app-url/docs`
- **ReDoc**: `https://your-app-url/redoc`

The Swagger UI will show an "Authorize" button where you can enter your Bearer token to test authenticated endpoints directly from the browser.

## Security best practices

1. **Use strong API keys**: Generate cryptographically secure random strings for your API keys
2. **Rotate keys regularly**: Periodically rotate your API keys for better security
3. **Scope secrets appropriately**: Use project/domain scoping when creating secrets if you want to limit access:
   ```bash
   flyte create secret --project my-project --domain development API_KEY my-secret-value
   ```
4. **Never commit secrets**: Always use Flyte secrets for API keys, never hardcode them in your code
5. **Use HTTPS**: Always use HTTPS in production (Flyte apps are served over HTTPS by default)

## Troubleshooting

**Authentication failing:**
- Verify the secret exists: `flyte get secret API_KEY`
- Check that the secret key name matches exactly (case-sensitive)
- Ensure you're using the correct Bearer token value
- Verify the `as_env_var` parameter matches the environment variable name in your code

**Secret not found:**
- Make sure you've created the secret before deploying the app
- Check the secret scope (organization vs project/domain) matches your app's project/domain
- Verify the secret name matches exactly (should be `API_KEY`)

**App not starting:**
- Check container logs for errors
- Verify all dependencies are installed in the image
- Ensure the secret is accessible in the app's project/domain

**LLM app authentication not working:**
- Verify the secret exists: `flyte get secret AUTH_SECRET`
- Check that `$AUTH_SECRET` is correctly specified in `extra_args` (note the `$` prefix)
- Ensure the secret name matches exactly (case-sensitive) in both the `flyte.Secret()` call and `extra_args`
- For vLLM, verify the `--api-key` argument is correctly passed
- For SGLang, verify the `--api-key` argument is correctly passed
- Check that `requires_auth=False` is set to allow public access

## Next steps

- Learn more about [managing secrets](../task-configuration/secrets) in Flyte
- See [app usage patterns](./app-usage-patterns#call-task-from-app-webhooks--apis) for webhook examples and authentication patterns
- Learn about [vLLM apps](./vllm-app) and [SGLang apps](./sglang-app) for serving LLMs

