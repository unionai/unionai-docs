---
title: PingOne (Ping Identity)
description: Configure PingOne (Ping Identity) as your OIDC identity provider for single sign-on.
icon: shield-check
weight: 3
variants: -flyte +union
---

# PingOne (Ping Identity)

{{< key product_name >}} supports [PingOne](https://www.pingidentity.com/en/platform/pingone.html) (and PingFederate) as an external OpenID Connect (OIDC) identity provider for single sign-on (SSO).

When onboarding a new BYOC or managed tenant via the {{< key product_name >}} **Self-Serve Tenant Provisioning Console** (`https://selfserve-console.apps.union-internal.hosted.unionai.cloud/`), PingOne can be wired directly as the organization's SSO identity provider via the **SSO Override** configuration.

---

## 1. Register an OIDC Web Application in PingOne

Log in to the [PingOne Admin Console](https://admin.pingone.com/) and ensure you are in the target environment for your workforce users.

### Step 1: Create the Application
1. In the left navigation, go to **Applications &rarr; Applications**.
2. Click the **`+` (Add Application)** button.
3. Select **WEB APP** as the application type.
4. Click **Configure**.
5. Set the **Application Name** (e.g. `Union Cloud Production`).
6. Click **Save**.

### Step 2: Configure OIDC Protocol Settings
Select the created application and open the **Configuration** tab:
1. Under **General**:
   * **Enabled**: Ensure the toggle is switched **ON**.
2. Under **Response Types**:
   * Select **Code**.
3. Under **Grant Types**:
   * Select **Authorization Code** and **Refresh Token**.
4. Under **Redirect URIs**:
   * Add your tenant callback URL:
     ```
     https://<your-org>.hosted.unionai.cloud/callback
     ```
     *(If using the shared signin broker, also include: `https://signin.hosted.unionai.cloud/oauth2/v1/authorize/callback`)*.
5. Under **Signoff URLs**:
   * Add your tenant logout URL:
     ```
     https://<your-org>.hosted.unionai.cloud/logout
     ```
6. Under **Token Endpoint Authentication Method**:
   * Select **Client Secret Basic** or **Client Secret Post**.
7. Click **Save**.

### Step 3: Grant Resource Scopes
1. Click the **Access** (or **Resource Grants**) tab for the application.
2. Under **OpenID Connect**, ensure the following scopes are enabled:
   * `openid`
   * `profile`
   * `email`
   * `offline_access`
3. Click **Save**.

### Step 4: Configure Attribute Mappings
Open the **Attribute Mappings** tab and verify the standard OIDC claims:
* `sub` &rarr; `${user.id}`
* `email` &rarr; `${user.email}`
* `preferred_username` &rarr; `${user.email}`
* `identitytype` &rarr; Expression `"user"` (literal string)

---

## 2. Obtain Credentials and Issuer URL

From the **Configuration** tab of your PingOne application and environment:
1. **Issuer URL**:
   ```
   https://auth.pingone.com/<your-environment-id>/as
   ```
   *(You can find your Environment ID in the PingOne top navigation bar or under **Settings &rarr; Environment**)*.
2. **Client ID**: Copy the generated UUID from the application's Configuration tab.
3. **Client Secret**: Copy the client secret value.

---

## 3. Provisioning via the Self-Serve Tenant Console

When provisioning your tenant in the {{< key product_name >}} **Self-Serve Tenant Provisioning Console** (`https://selfserve-console.apps.union-internal.hosted.unionai.cloud/`):

1. Fill out the standard tenant parameters (**Organization Name**, **Primary Admin Email**, **Environment**, **Region**).
2. Check the box for **Enable SSO Override**.
3. Fill in the PingOne connection details:
   * **Provider Name**: `PingOne` (or e.g. `Lockheed Martin PingOne`)
   * **Issuer**: `https://auth.pingone.com/<your-environment-id>/as`
   * **Client ID**: The PingOne Web Application Client ID
   * **Client Secret**: The PingOne Web Application Client Secret
   * **Scopes**: `openid,profile,email`
4. Click **Start Provisioning**.

The provisioning engine automatically sets up the generic OIDC identity provider integration and attaches it to your organization's custom login policy, routing interactive browser logins directly through your PingOne instance.

---

## 4. Alternative: Secure Credential Exchange with {{% key product_name %}}

If the {{< key product_name >}} team is provisioning the tenant on your behalf:

1. Download the {{< key product_name >}} public PGP key: {{< download "/_static/public/public-key.txt" >}}.
2. Use an encryption tool (such as [PGP Tool](https://pgptool.net)) to encrypt your:
   * **PingOne Issuer URL**
   * **Client ID**
   * **Client Secret**
3. Share the encrypted text securely with the {{< key product_name >}} team over Slack.
