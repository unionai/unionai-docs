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

## Create a {{< key product_name >}} Api Key

An api key is registered in your {{< key product_name >}} control plane that enables external systems to perform actions on your behalf.
To enable your CI/CD system to authenticate with {{< key product_name >}}, you need to create a {{< key product_name >}} api key.
See [Managing API keys](./managing-api-keys.md).

```shell
$ {{< key cli >}} create api-key admin --name my-cicd-key
```

Copy the `UNION_API_KEY` to an editor for later use.
This is the only time that the secret will be displayed.

## Store the secret in your CI/CD secrets store

Store the secret in your CI/CD secrets store.
In GitHub, from the repository page:

1. Select **Settings > Secrets and variables > Actions**.
2. Select the **Secrets** tab and click **New repository secret**.
3. Give a meaningful name to the secret, like `{{< key env_prefix >}}_CICD_API_KEY`.
4. Paste in the string from above as the value.
5. Click **Add secret**.

## Set up your CI/CD configuration file

Finally, you need to set up the CI/CD configuration file. For GitHub Actions you might create the file `example-project/.github/workflows/deploy.yaml` that looks like this:

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
          UNION_API_KEY: ${{ secrets.UNION_CICD_API_KEY }}
        run: |
          source .venv/bin/activate
          union register \
            -p ${{ env.PROJECT }} -d ${{ env.DOMAIN }} ./launchplans
      
```
{{< /markdown >}}
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
{{< /variant >}}
> [!NOTE]
> Note this section:
>
> ```yaml
> - name: Register
>   env:
>     {{< key env_prefix >}}_APP_SECRET: ${{ secrets.{{< key env_prefix >}}_APP_SECRET }}
> ```
>
> The first instance of the name`{{< key env_prefix >}}_APP_SECRET`must be the same as that specified in the `ci-config.yaml` file as the value of `clientSecretEnvVar`.
>
> Because we have followed the practice of using the same name for the secret stored in the CI/CD secret store, the value being retrieved here has the same name, `secrets.{{< key env_prefix >}}_APP_SECRET.`
>
> You will also see other secrets and environment variables accessed in this configuration file.
> These are related to the container build process, project name and so forth.
> For details, have a look at the GitHub docs and the docs for the tool used above, `whoan/docker-build-with-cache-action`.

Once this is set up, every push to the main branch in you repository will build and deploy your project to {{< key product_name >}}.
