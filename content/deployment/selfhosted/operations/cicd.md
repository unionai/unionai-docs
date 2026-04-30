---
title: CI/CD integration
weight: 1
variants: -flyte +union
---

# CI/CD integration

This guide covers how to authenticate `flyte deploy` from a CI/CD pipeline (GitHub Actions, Jenkins, GitLab CI, etc.) against a self-hosted {{< key product_name >}} deployment.

In serverless and BYOC deployments, `flyte create api-key` mints an API key automatically. Self-hosted deployments don't have access to the identity service that backs this command. Instead, you create a dedicated OAuth application in your identity provider and encode its credentials as an API key manually.

For `flyte deploy` usage, flags, and workflow examples, see the [CI/CD deployments]({{< docs_home union >}}/user-guide/project-patterns/cicd/) guide.

## Prerequisites

- [Authentication](../authentication) is configured and working (Apps 1-5)
- The `flyte` CLI is installed (`pip install flyte` or `uv pip install flyte`)
- You have admin access to your identity provider to create a new OAuth application

## Step 1: Create a CI/CD OAuth application

Create a new confidential (service) application in your identity provider. This is the same type of application as the service-to-service app (App 3) documented in the [authentication guide](../authentication), but dedicated to CI/CD so you can manage its lifecycle and permissions independently.

{{< tabs >}}
{{< tab "Okta" >}}
{{< markdown >}}
1. In the Okta Admin Console, go to **Applications > Create App Integration**
2. Select **API Services** (machine-to-machine)
3. Name it descriptively (e.g., `union-cicd` or `union-jenkins`)
4. After creation, note the **Client ID** and **Client Secret**
5. Go to your custom authorization server (**Security > API > Authorization Servers**)
6. Under **Access Policies**, ensure the CI/CD app is allowed the `client_credentials` grant with the `all` scope

> [!NOTE]
> If you want per-team or per-project CI/CD keys, create separate OAuth apps for each and assign different access policies.
{{< /markdown >}}
{{< /tab >}}
{{< tab "Entra ID" >}}
{{< markdown >}}
1. In the Azure portal, go to **Microsoft Entra ID > App registrations > New registration**
2. Name it descriptively (e.g., `union-cicd`)
3. Set **Supported account types** to **Single tenant**
4. No redirect URI is needed — this app uses client credentials only
5. After creation, go to **Certificates & secrets > New client secret** and save the secret value
6. Go to the **Union API app registration** (the one with "Expose an API" configured — typically App 1):
   - Under **Expose an API > Authorized client applications**, add the CI/CD app's Client ID
   - Under **App roles**, ensure an `all` role exists
7. Back on the CI/CD app registration:
   - Go to **API permissions > Add a permission > My APIs**
   - Select the Union API app and grant the `all` Application permission
8. **Grant admin consent**: Go to **Enterprise Applications > CI/CD app > Permissions > Grant admin consent for \<tenant\>**

> [!WARNING]
> Without admin consent, client_credentials token requests will fail with an `AADSTS` error. This is the most common setup issue.
{{< /markdown >}}
{{< /tab >}}
{{< tab "Generic OIDC" >}}
{{< markdown >}}
1. Create a new **confidential client** in your identity provider
2. Enable the `client_credentials` grant type
3. Assign the appropriate scope (typically `all` or the scope configured on your authorization server)
4. Note the **Client ID** and **Client Secret**

If your provider requires explicit audience configuration, set the audience to match the `allowedAudience` configured in your control plane Helm values.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Step 2: Build the API key

Encode the credentials as a base64 string in the format `<domain>:<client-id>:<client-secret>:` — note the **trailing colon**:

```shell
echo -n "<your-domain>:<client-id>:<client-secret>:" | base64
```

For example:

```shell
echo -n "union.example.com:abc123:secret456:" | base64
# dW5pb24uZXhhbXBsZS5jb206YWJjMTIzOnNlY3JldDQ1Njo=
```

The four fields are:
1. **Domain** — your control plane ingress domain (without `https://`)
2. **Client ID** — from the OAuth app you just created
3. **Client secret** — from the OAuth app you just created
4. **Organization** — leave empty for self-hosted (the trailing colon is still required)

## Step 3: Store in your CI secret manager

Add the base64 string to your CI system's secret store and expose it as the `FLYTE_API_KEY` environment variable:

{{< tabs >}}
{{< tab "GitHub Actions" >}}
{{< markdown >}}
1. Go to **Settings > Secrets and variables > Actions > New repository secret**
2. Name: `FLYTE_API_KEY`
3. Value: the base64 string from Step 2

In your workflow:
```yaml
- name: Deploy workflows
  env:
    FLYTE_API_KEY: ${{ secrets.FLYTE_API_KEY }}
  run: flyte deploy ...
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Jenkins" >}}
{{< markdown >}}
1. Go to **Manage Jenkins > Credentials > Add Credentials**
2. Kind: **Secret text**
3. Secret: the base64 string from Step 2
4. ID: `flyte-api-key`

In your Jenkinsfile:
```groovy
environment {
    FLYTE_API_KEY = credentials('flyte-api-key')
}
stages {
    stage('Deploy') {
        steps {
            sh 'flyte deploy ...'
        }
    }
}
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "GitLab CI" >}}
{{< markdown >}}
1. Go to **Settings > CI/CD > Variables > Add variable**
2. Key: `FLYTE_API_KEY`
3. Value: the base64 string from Step 2
4. Check **Mask variable** and **Protect variable**

In your `.gitlab-ci.yml`:
```yaml
deploy:
  script:
    - flyte deploy ...
```

The `FLYTE_API_KEY` variable is automatically available to all jobs.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Step 4: Configure `flyte deploy`

Create a `config.yaml` in your repository pointing at your self-hosted deployment:

```yaml
admin:
  endpoint: dns:///<your-domain>
  insecure: false    # Set to true if using self-signed certificates
image:
  builder: remote    # Or "local" if you pre-build images
task:
  project: <your-project>
  domain: <your-domain-name>
```

When `FLYTE_API_KEY` is set, the CLI uses it for authentication automatically — it overrides any other auth mode configured in `config.yaml` (including `ExternalCommand`-based SSO flows). No config changes are needed to switch between interactive and CI authentication.

## Step 5: Test

Verify the credentials work before wiring them into your pipeline:

```shell
# 1. Test token acquisition (replace with your IdP's token endpoint)
curl -s -X POST "<token-endpoint>" \
  -d "grant_type=client_credentials" \
  -d "client_id=<client-id>" \
  -d "client_secret=<client-secret>" \
  -d "scope=<scope>" | jq .access_token
```

{{< tabs >}}
{{< tab "Okta" >}}
{{< markdown >}}
```shell
curl -s -X POST "https://<okta-domain>/oauth2/<auth-server-id>/v1/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=<client-id>" \
  -d "client_secret=<client-secret>" \
  -d "scope=all" | jq .access_token
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Entra ID" >}}
{{< markdown >}}
```shell
curl -s -X POST "https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=<client-id>" \
  -d "client_secret=<client-secret>" \
  -d "scope=api://<app-name>/.default" | jq .access_token
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Generic OIDC" >}}
{{< markdown >}}
```shell
curl -s -X POST "<issuer-url>/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=<client-id>" \
  -d "client_secret=<client-secret>" \
  -d "scope=all" | jq .access_token
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

If you receive a valid JWT, test the full flow:

```shell
export FLYTE_API_KEY="<base64-string>"
flyte deploy --config config.yaml --copy-style none --version test-$(date +%s) \
  --project <project> --domain <domain> path/to/tasks.py
```

## Permissions and RBAC

The CI/CD app's access depends on your [authorization](../authorization) configuration:

- **Noop mode**: The app has full access to all projects and domains
- **External authorization**: Configure your external authz service to grant the CI/CD app's identity appropriate permissions
- **Union RBAC**: Create a role scoped to the target project/domain and bind it to the CI/CD app's identity

For teams sharing a cluster, create **separate OAuth apps per team or per repository** so that one team's CI key cannot deploy to another team's project. See the [CI/CD deployments]({{< docs_home union >}}/user-guide/project-patterns/cicd/#key-scope-and-rotation) guide for more on permission scoping.

## Key rotation

Rotate CI/CD credentials on a regular schedule (90 days recommended):

1. Create a new client secret in your identity provider (don't delete the old one yet)
2. Re-encode with the new secret: `echo -n "<domain>:<client-id>:<new-secret>:" | base64`
3. Update the `FLYTE_API_KEY` secret in your CI system
4. Verify a deploy succeeds with the new key
5. Delete the old client secret from your identity provider
