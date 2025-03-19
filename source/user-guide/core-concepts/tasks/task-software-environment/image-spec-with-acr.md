# ImageSpec with ACR

In this section we explain how to use [Azure Container Registry (ACR)](https://azure.microsoft.com/en-us/products/container-registry) to build and deploy task container images using `ImageSpec`.

Before proceeding, make sure that you have [enabled Azure Container Registry](../../../integrations/enabling-azure-resources/enabling-azure-container-registry.md) for you Union.ai installation.

## Authenticate to the registry

Authenticate with the container registry

```bash
az login
az acr login --name <acrName>
```

Refer to [Individual login with Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#individual-login-with-microsoft-entra-id) in the Azure documentation for additional details.

## Register your workflow to Union.ai

You can now register tasks with `ImageSpec` declarations that reference this repository.

For example, to use an existing ACR repository, we would alter the Python code in the [previous section](./index.md), to have the following `ImageSpec` declaration:

```{code-block} python
image_spec = union.ImageSpec(
    registry="<AZURE_CONTAINER_REGISTRY_NAME>.azurecr.io",
    name="my-repository/simple-example-image",
    base_image="ghcr.io/flyteorg/flytekit:py3.11-latest",
    requirements="image-requirements.txt"
)
```
