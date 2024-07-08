# Enabling Google Secret Manager

Access to a secret stored in Secret Manager in the same GCP project as the data plane is enabled by default.
All you need to do is:

* Create your secrets in Secret Manager.
* Retrieve your secrets from within your task code.

To access a secret stored in Secret Manager in a GCP project _other than the one that holds your data plane_ requires one additional step:
Granting the `<UserFlyteGSA>` (see [Enabling GCP resources](./index)) access to top the secret in the other projects.

## Create your secrets

Create your secrets in **Secret Manager** (see the [Secret Manager documentation](https://cloud.google.com/secret-manager/docs) for details):

* Go to **Security > Secret Manager**.
* Select **CREATE SECRET** at the top of the page.
* Fill in the **Name**, **Value,** and (optionally) the other parameters.
* Select **CREATE SECRET** at the bottom of the page.

Your secret should now be on the secrets list:

![](/_static/images/secret-manager.png)

Above we see a secret named `example-secret`.
Clicking on it will bring us to the **Secret details** page:

![](/_static/images/secret-details.png)

The secret has three important identifiers:

* The **GCP secret name**, in this case `example-secret`.
You will need this if you are accessing a secret in the same project as your data plane.
* The **GCP secret path**, in this case `projects/956281974034/secrets/example-secret`.
You will need this if you are accessing a secret in a different project from your data plane project.
* The **GCP secret version**, in this case `1`.
This is required for both same- and cross-project cases.

## Same-project secrets

If your secret is stored in the Secret Manager of the same project as your data plane then the `<UserFlyteGSA>` will have access to it out-of-the-box.
No further configuration is necessary.

To use a same-project GCP secret in your task code, do the following:

* Define a `Secret` object where
  * `Secret.group` is the **GCP secret name**, in this case `example-secret`(optionally, you can use the **GCP secret path** instead, but the simple name is sufficient).
  * `Secret.group_version` is the **GCP secret version** (in this case `1`)
  * `Secret.mount_requirement` is `Secret.MountType.FILE`
* Pass that `Secret` object in the `secret_requests` parameter of the `@task` decorator.
* Inside the task code, retrieve the value of the secret with a call to
`flytekit.current_context().secrets.get(SECRET_GROUP, group_version=SECRET_GROUP_VERSION)`.

Here is an example:

```{code-block} python
import flytekit
from flytekit import task, workflow, Secret

SECRET_GROUP = "example-secret"
SECRET_GROUP_VERSION = "1"
SECRET_REQUEST = Secret(
            group=SECRET_GROUP,
            group_version=SECRET_GROUP_VERSION,
            mount_requirement=Secret.MountType.FILE
        )

@task(secret_requests=[SECRET_REQUEST])
def t1():
    secret_val = flytekit.current_context().secrets.get(
        SECRET_GROUP,
        group_version=SECRET_GROUP_VERSION
    )
```

## Cross-project secrets

If your secret is stored in the Secret Manager of a project other than the one containing your data plane, then you will first need to grant the `<UserFlyteGSA>` permission to access it:

* Find the **email identifier** of the `<UserFlyteGSA>` in your data plane GCP project (see [Enabling GCP resources](./index) for details).
* Go to **Security > Secret Manager** in the GCP project that contains your secret.
* Select the secret that you want to access and select **GRANT ACCESS**.
* In the subsequent panel, under **Add principals**, paste in the email identifier of the `<UserFlyteGSA>` that you found above.
* Under **Assign roles** add at least the role **Secret Manager Secret Accessor**.
* Save the changes.

At this point, your task code will have access to the secret in the other project. To use that secret in your task code, do the following:

* Define a `Secret` object where
  * `Secret.group` is the **GCP secret path** (in this case, `projects/956281974034/secrets/example-secret`)
  * `Secret.group_version` is the **GCP secret version** (in this case `1`)
  * `Secret.mount_requirement` is `Secret.MountType.FILE`
* Pass that `Secret` object in the `secret_requests` parameter of the `@task` decorator.
* Inside the task code, retrieve the value of the secret with a call to\
`flytekit.current_context().secrets.get(SECRET_GROUP, group_version=SECRET_GROUP_VERSION)`

:::{admonition} GCP secret name vs GCP secret path

In your task code, the only difference between using a same-project secret and a cross-project secret is

* With a _same-project secret,_ you can use either the **GCP secret name** or the **GCP secret path** as the value of the parameter `flytekit.Secret.group`.
* With a _cross-project secret,_ you must use the **GCP secret path** as the value of the parameter `flytekit.Secret.group`.

:::

Here is an example:

```{code-block} python
import flytekit
from flytekit import task, workflow, Secret

SECRET_GROUP = "projects/956281974034/secrets/example-secret"
SECRET_GROUP_VERSION = "1"
SECRET_REQUEST = Secret(
            group=SECRET_GROUP,
            group_version=SECRET_GROUP_VERSION,
            mount_requirement=Secret.MountType.FILE
        )

@task(secret_requests=[SECRET_REQUEST])
def t1():
    secret_val = flytekit.current_context().secrets.get(
        SECRET_GROUP,
        group_version=SECRET_GROUP_VERSION
    )
```
