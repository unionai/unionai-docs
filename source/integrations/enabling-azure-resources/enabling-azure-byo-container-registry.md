<!-- Placeholder documentation for Union managed BYOC -->

### Union managed ACR

Union, by default, will create a container registry for image storage.

By default this ACR instance:

* Will be created within the same Subscription and Resource group of the Azure Kubernetes Cluster instance.
* Union will create necessary permissions for the Azure Kubernetes Cluster to pull images from the container registry.
* Container registry will be created with "Basic" service tier.
* In order to mitigate excessive storage costs, Union creates a weekly [scheduled container registry task](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-scheduled) to [purge](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auto-purge#use-the-purge-command) **all** images with last modified dates older then 7 days. As a symptom, some 7 day old images will be rebuilt.z

Upon request, Union can:

* Not create a ACR instance.
* Configure the [Container Registry service tier](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus).
* Configure the purge task to run daily, weekly, and monthly deleting tasks with last modified dates older then 1, 7, and 30 days respectively.
* Configure a [regexp2 with RE2 compatiblity](https://github.com/dlclark/regexp2) regular expression to filter for which repository to purge. For example, `^(?!keep-repo).*` will keep all images with repositories prefixed with keep-repo, E.G., `<CONTAINER_REGISTRY_NAME/keep-repo/my-image:my-tag>`.

Union will provide the created container registry Name and Login server for Docker authentication.
