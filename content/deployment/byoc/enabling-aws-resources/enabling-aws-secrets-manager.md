---
title: Enabling AWS Secrets Manager
description: Let task code read secrets from AWS Secrets Manager.
icon: safe
weight: 3
variants: -flyte +union
---

# Enabling AWS Secrets Manager

> [!NOTE]
> This documentation is for customers who must use AWS Secrets Manager for organizational reasons. For everyone else, we strongly recommend using the
> [{{< key product_name >}} secrets manager](../../../user-guide/tasks/task-configuration/secrets) to manage secrets rather than AWS Secrets Manager.

To enable your code to access secrets from AWS Secrets Manager you will need to

* Make sure AWS Secrets Manager is enabled.
* Create your secrets in AWS Secrets Manager.
* Create an AWS policy granting access to your secrets.
* Bind that policy to the User Flyte Role in your {{< key product_name >}} data plane.
* Retrieve your secrets from within your workflow code.

## Ensure that AWS Secrets Manager is enabled

The first step is to make sure that AWS Secrets Manager is enabled in your AWS environment.
Contact the {{< key product_name >}} team if you are unsure.

## Create your secrets

> [!NOTE]
> Secrets must be defined within the same region as your {{< key product_name >}} data plane.
> For example, if your {{< key product_name >}} data plane is located in `us-west-2`, ensure that the secrets are also in `us-west-2`.

Create your secrets in **AWS Secrets Manager** (see the [AWS documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) for details):

* Go to **AWS Secrets Manager**.
* Select **Store a new secret**.
* Under **Choose Secret type**:
  * Select **Other type of secret**.
  * Select **Plaintext** (**Key/value** is not supported).
  * Enter your **secret value**.
  * For **Encryption key,** leave the default setting: `aws/secretmanager`.
  * Select **Next**.
* Under **Configure secret**:
  * For **Secret name**, enter a string (this string will form part of the `SECRET_KEY` that you will use to access your secret from within your code).
  * Select **Next**.
* Under **Configure rotation** adjust the settings if needed, or skip the section if not. Then select **Next**.
* Under **Review** check that everything is correct and then select **Store**.

## Get the secret ARN

Once you have created a secret, navigate to **AWS Secrets Manager > Secrets** and select the secret you just created.
From there select **Secret ARN** and record the ARN.
Do this for each secret that you create.

A secret ARN looks like this:

```bash
arn:aws:secretsmanager:<Region>:<AccountId>:secret:<SecretName>-<SixRandomCharacters>
```

> [!NOTE]
> You will need your secret ARN when you access your secret from within your code.
> Specifically, you will need to divide it into two strings:
>
> * **`SECRET_GROUP`**: The part of the ARN up to and including `:secret:`
> Above, it is `arn:aws:secretsmanager:<Region>:<AccountId>:secret:`.
>
> * **`SECRET_KEY`**: The part of the ARN after `:secret:`
> Above, it is `<SecretName>-<SixRandomCharacters>`.
>
> See [Using AWS secrets in your code](./enabling-aws-secrets-manager#using-aws-secrets-in-your-task-code) for details on how these are used.

## Create a policy providing access to your secrets

To provide access to your newly created secrets in your code, you will first need to create a policy that grants read access to those secrets:

* Go to **IAM > Access management > Policies**.
* Select **Create Policy**.
* Open the **JSON** tab and paste in the following definition:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:<Region>:<AccountId>:secret:*"
    }
  ]
}
```

> [!NOTE]
> The`Resource`entry takes a wildcard string that must match the ARNs of the secrets in your environment that you want to grant access to.
> This can be all the secrets in your environment (as shown above) or some subset (achieved by making the wildcard match more specific).
> Be sure to substitute the appropriate`<Region>`and`<AccountNumber>`.

* Select **Next: Tags** and add tags if you wish.
* Select **Next: Review** and enter a **Name** for the policy
* Select **Create Policy**.
* Find your newly created policy in the policy list that comes up next and select it.
* Record the **Policy Name** and **Policy ARN** of your newly created policy.
It should be at the top of the policy summary page.
We will refer to the name as `<SecretManagerPolicyName>` and the ARN as `<SecretManagerPolicyArn>`.

> [!NOTE]
> Alternatively, you can create the policy from the command line like this (remember to substitute the`<Region>`and`<AccountId>`appropriately):
>
> ```bash
> $ aws iam create-policy \
>       --policy-name <YourPolicyName> \
>       --policy-document \
>       { \
>         "Version": "2012-10-17", \
>         "Statement": [ \
>           { \
>             "Effect": "Allow", \
>             "Action": "secretsmanager:GetSecretValue", \
>             "Resource": "arn:aws:secretsmanager:<Region>:<AccountId>:secret:*" \
>           } \
>         ]\
>       }
> ```

## Bind the policy to the user Flyte role

To grant your code the permissions defined in the policy above, you must bind that policy to the `<UserFlyteRole>` used in your {{< key product_name >}} data plane.
The precise name of this role differs by organization.
You will need this name as well as the ARN of the policy (`<SecretManagerPolicyArn>`, above) to perform the binding.
See [the binding directions](./_index) for details. Once the binding is done, your secrets are now accessible from within your Flyte code.

## Using AWS secrets in your task code

To use an AWS secret in your task code, do the following:

* Declare a `flyte.Secret` in the `secrets` of your `TaskEnvironment`, with `group` set to the `SECRET_GROUP` and `key` set to the `SECRET_KEY` derived from the secret ARN, above.
* Set `mount="/etc/flyte/secrets"`. AWS secrets can only be delivered as files. Without `mount`, `flyte.Secret` tries to deliver the secret as an environment variable named after the group and key, and raises an error because an ARN is not a valid variable name.
* Inside the task, read the secret from the file `/etc/flyte/secrets/<SECRET_GROUP>/<SECRET_KEY>`, with both parts in lower case.

Here is an example:

```python
import pathlib

import flyte

SECRET_GROUP = "arn:aws:secretsmanager:<Region>:<AccountId>:secret:"
SECRET_KEY = "<SecretName>-<SixRandomCharacters>"

env = flyte.TaskEnvironment(
    name="aws-secrets",
    secrets=[flyte.Secret(key=SECRET_KEY, group=SECRET_GROUP, mount="/etc/flyte/secrets")],
)

@env.task
def t1():
    secret_file = pathlib.Path("/etc/flyte/secrets") / SECRET_GROUP.lower() / SECRET_KEY.lower()
    secret_val = secret_file.read_text()
    # do something with the secret. For example, communication with an external API.
    ...
```

> [!WARNING]
> Do not return secret values from tasks. Returned values are stored in plaintext in your data plane's object store and shown in the UI and to downstream tasks, defeating the secret store's protections.
