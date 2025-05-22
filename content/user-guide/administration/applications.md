---
title: Applications
weight: 4
variants: -flyte -serverless +byoc +selfmanaged
---

# Applications

A {{< key product_name >}} application is an identity through which external systems can perform actions in the system.
An application can be bound to policies and granted permissions just like a human user.

Applications are managed through the [`uctl` CLI](../../api-reference/uctl-cli).

## List existing apps

```shell
$ uctl get apps
```

Output:

```text
 -------------------- --------------------- ---------------- ----------------------------------------
| ID (4)             | CLIENT NAME        | RESPONSE TYPES | GRANT TYPES                             |
 -------------------- -------------------- ---------------- -----------------------------------------
| contoso-flyteadmin | contoso flyteadmin | [CODE]         | [CLIENT_CREDENTIALS AUTHORIZATION_CODE] |
 -------------------- -------------------- ---------------- -----------------------------------------
| contoso-uctl       | contoso uctl       | [CODE]         | [AUTHORIZATION_CODE]                    |
 -------------------- -------------------- ---------------- -----------------------------------------
| contoso-operator   | contoso operator   | [CODE]         | [CLIENT_CREDENTIALS AUTHORIZATION_CODE] |
 -------------------- -------------------- ---------------- -----------------------------------------
```

> [!NOTE]
> These 3 apps are built into the system.
> Modifying these by editing, deleting or recreating them will disrupt the system.

## Exporting the spec of an existing app

```shell
$ uctl get apps contoso-operator --appSpecFile app.yaml
```

Output:

```yaml
clientId: contoso-operator
clientName: contoso operator
grantTypes:
  - CLIENT_CREDENTIALS
  - AUTHORIZATION_CODE
redirectUris:
  - http://localhost:8080/authorization-code/callback
responseTypes:
  - CODE
tokenEndpointAuthMethod: CLIENT_SECRET_BASIC
```

## Creating a new app

First, create a specification file called `app.yaml` (for example) with the following contents (you can adjust the `clientId` and `clientName` to your requirements):

```yaml
clientId: example-operator
clientName: Example Operator
grantTypes:
- CLIENT_CREDENTIALS
- AUTHORIZATION_CODE
redirectUris:
- http://localhost:8080/authorization-code/callback
responseTypes:
- CODE
tokenEndpointAuthMethod: CLIENT_SECRET_BASIC
```

Now, create the app using the specification file:

```shell
$ uctl create app --appSpecFile app.yaml
```

The response should look something like this:

```text
 ------------------ ------------------- ------------- ---------
| NAME             | CLIENT NAME       | SECRET      | CREATED |
 ------------------ ------------------- ------------- ---------
| example-operator |  Example Operator | <AppSecret> |         |
 ------------------ ------------------- ------------- ---------
```

Copy the `<AppSecret>` to an editor for later use.
This is the only time that the secret will be displayed.
The secret is not stored by {{< key product_name >}}.

## Update an existing app

To update an existing app, update its specification file as desired while leaving the `clientId` the same, to identify which app is to be updated, and then do:

```shell
$ uctl apply app --appSpecFile app.yaml
```

## Delete an app

To delete an app use the `uctl delete app` command and specify the app by ID:

```shell
$ uctl delete app example-operator
```
