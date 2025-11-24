---
title: CI/CD deployment
weight: 17
variants: -flyte -serverless +byoc +selfmanaged
---

# CI/CD deployment

So far we have covered the steps of deploying a project manually from the command line.
In many cases, you will want to automate this process through a CI/CD system.
In this section, we explain how to set up a CI/CD system to register, execute and promote workflows on {{< key product_name >}}.
We will use GitHub Actions as the example CI/CD system.

## Create a {{< key product_name >}} API key

An API key is registered in your {{< key product_name >}} control plane to enable external systems to perform actions on your behalf.
To allow your CI/CD system to authenticate with {{< key product_name >}}, create a {{< key product_name >}} API key.
See [Managing API keys](./managing-api-keys.md) for details.

```shell
$ {{< key cli >}} create api-key admin --name my-cicd-key
```

Copy the `UNION_API_KEY` value for later use; this is the only time the secret is displayed.

## Store the secret in your CI/CD secrets store

Store the secret in your CI/CD secrets store.
In GitHub, from the repository page:

1. Select **Settings > Secrets and variables > Actions**.
2. Select the **Secrets** tab and click **New repository secret**.
3. Give a meaningful name to the secret, like `{{< key env_prefix >}}_CICD_API_KEY`.
4. Paste in the string from above as the value.
5. Click **Add secret**.

## Configure your CI/CD workflow file

Create the CI/CD workflow file. For GitHub Actions, you might add `example-project/.github/workflows/deploy.yaml` similar to:

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}
```yaml
name: Deploy

on:
  push:
    branches:
      - main

env:
  PROJECT: flytesnacks
  DOMAIN: production

jobs:
  build_and_register:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Install python & uv 
        run: |
          sudo apt-get install python3
          curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync
      - name: Register to Union
        env:
          UNION_API_KEY: ${{ secrets.CICD_API_KEY }}
        run: |
          source .venv/bin/activate
          union register --version ${{ github.sha }} -p ${{ env.PROJECT }} \
          -d ${{ env.DOMAIN }} --activate-launchplans ./launchplans
```
{{< /markdown >}}
> [!NOTE]
> The `Register to Union` step registers the launch plans and related Flyte entities in the `launchplans` directory. It sets the project and domain, activates launch plans automatically, and pins the version to the Git commit SHA for traceability across all registered Flyte entities. See {{< key cli >}} [register](../../api-reference/union-cli.md#register) for additional options.
{{< /variant >}}
{{< variant  flyte >}}
{{< markdown >}}
```yaml
name: Deploy

on:
  push:
    branches:
      - main

env:
  REGISTRY: ghcr.io
  PROJECT: onboarding

jobs:
  build_and_register:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Build & Push Docker Image to Github Registry
        uses: whoan/docker-build-with-cache-action@v5
        with:
          # https://docs.github.com/en/packages/learn-github-packages/publishing-a-package
          username: ${{ secrets.{{< key env_prefix >}}_BOT_USERNAME }}
          password: ${{ secrets.{{< key env_prefix >}}_BOT_PASSWORD }}
          image_name: ${{ github.repository }}
          image_tag: ${{ env.PROJECT }}-${{ github.sha }},${{ env.PROJECT }}-latest
          registry: ${{ env.REGISTRY }}
          context: ./${{ env.PROJECT }}
          dockerfile: Dockerfile

      - name: Setup flyte
        run: |
          sudo apt-get install python3
          pip install -r ${{ env.PROJECT }}/requirements.txt
      - name: Setup flytectl
        run: |
          curl -sL https://ctl.flyte.org/install | bash
      - name: Package
        working-directory: ./${{ env.PROJECT }}
        run: |
          {{< key cli >}} --pkgs workflows package \
            --output ./flyte-package.tgz \
            --image ${{ env.REGISTRY }}/${{ github.repository_owner }}/${{ github.repository }}:${{ env.PROJECT }}-latest
      - name: Register
        env:
          {{< key env_prefix >}}_APP_SECRET: ${{ secrets.{{< key env_prefix >}}_APP_SECRET }}
        run: |
          bin/flytectl --config ./ci-config.yaml \
            register files \
            --project onboarding \
            --domain production \
            --archive ./${{ env.PROJECT }}/flyte-package.tgz \
            --version ${{ github.sha }}
```
{{< /markdown >}}
> [!NOTE]
> Note this section:
>
> ```yaml
> - name: Register
>   env:
>     {{< key env_prefix >}}_APP_SECRET: ${{ secrets.{{< key env_prefix >}}_APP_SECRET }}
> ```
>
> The first instance of `{{< key env_prefix >}}_APP_SECRET` must match the value specified in `ci-config.yaml` for `clientSecretEnvVar`.
>
> Because the CI/CD secret uses the same name, the retrieved value is `secrets.{{< key env_prefix >}}_APP_SECRET.`
>
> You will also see other secrets and environment variables accessed in this configuration file.
> These are related to the container build process, project name and so forth.
> For details, have a look at the GitHub docs and the docs for the tool used above, `whoan/docker-build-with-cache-action`.
{{< /variant >}}

Once this is set up, every push to the main branch in your repository will build and deploy your project to {{< key product_name >}}.
