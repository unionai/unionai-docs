---
title: Getting support
description: How to reach Union.ai support, the support plan that comes with each Union.ai plan, the severity levels, and the response time targets per support plan.
icon: life-preserver
weight: 9
variants: -flyte +union
---

# Getting support

Every Union.ai organization has a support plan. You can reach the support team through any of the channels below, for all severity levels.

> [!NOTE] Urgent (Sev 1) issues
> For a blocking issue that needs immediate attention, include **Sev 1 - Urgent** in your request through the shared Slack channel, the support portal, or email. On Premier and Mission Critical, Sev 1 and Sev 2 issues are covered 24×7.

## Support plans

Your support plan follows your Union.ai plan. Team includes Standard support, and Enterprise includes Premier. Enterprise organizations can upgrade to Mission Critical.

| Support plan | Included with | Coverage | Channels and people |
|---|---|---|---|
| Standard | Team | 12×5, Pacific time | Email, the support portal, and **Help** in the console. A shared Slack channel for your first three months. |
| Premier | Enterprise | 24×7 for Sev 1 and Sev 2; 12×5 for Sev 3 and Sev 4 | Email and the support portal. A shared Slack or Microsoft Teams channel. A shared AI Solutions Engineer and a quarterly review. |
| Mission Critical | Enterprise, as a paid upgrade | 24×7 for Sev 1 and Sev 2; 12×5 for Sev 3 and Sev 4 | A private Slack or Microsoft Teams channel, and video calls. A dedicated AI Solutions Engineer and a monthly review. |

Support covers what Union.ai provides: the control plane, the data plane components Union.ai installs, and the SDK. It doesn't cover your own code, your cloud resources outside the components Union.ai manages, or third-party software.

## Severity levels

| Severity | Description |
|----------|-------------|
| {{< badge "danger" >}}Sev 1 - Urgent{{< /badge >}} | Platform is down, inoperable, inaccessible, or unavailable; operation has materially ceased. No workaround available. |
| {{< badge "warning" >}}Sev 2 - High{{< /badge >}} | Platform is severely limited or degraded; major functions are not performing properly; situation is significantly impacting operations. |
| {{< badge "primary" >}}Sev 3 - Medium{{< /badge >}} | Minor issues with the platform. Issues may have viable workarounds immediately available. |
| {{< badge "success" >}}Sev 4 - Low{{< /badge >}} | Events have no impact on the platform; includes feature requests. Workaround works well for any functionality issues. |

## Response time targets

First response time targets by severity level and support plan:

| Severity | Standard | Premier | Mission Critical |
|----------|----------|---------|------------------|
| {{< badge "danger" >}}Sev 1 - Urgent{{< /badge >}} | 4 business hrs | 1 hr | 30 min |
| {{< badge "warning" >}}Sev 2 - High{{< /badge >}} | 8 business hrs | 4 hrs | 2 hrs |
| {{< badge "primary" >}}Sev 3 - Medium{{< /badge >}} | 1 business day | 12 hrs | 4 hrs |
| {{< badge "success" >}}Sev 4 - Low{{< /badge >}} | 2 business days | 24 hrs | 12 hrs |

> [!NOTE] Contracts signed before these plans
> If your contract names a different support tier, such as Advanced or Priority, the support terms in your contract apply until it renews.

## Shared Slack channel

If you have a shared Slack channel with Union, opening a support ticket is easy. Simply tag `@union` or react to any message with a 🎫 emoji. Doing so will open a form where you can add additional details and set the severity.

## Support portal

The support portal at [support.union.ai](https://support.union.ai) lets you file tickets and view the status of open and closed requests. Log in with your company email address and click the **Create Ticket** button in the top right to submit a new request.

## Union Cloud console

If you created your organization yourself by [signing up](../deployment/sign-up/_index) (a self-serve organization), click **Help** in the console's navigation sidebar, then choose **Contact support** or **Report a bug or send feedback**. For organizations that Union.ai set up for you, the console shows a **Documentation** link there instead and has no support option. If your sidebar has no **Help** item, use one of the other channels on this page.

## Email

Send an email to [support@union.ai](mailto:support@union.ai) with the severity level in the subject line and all relevant details in the body: a summary and description of the issue, intended vs. actual behavior, error messages, logs, and a link to the relevant execution if applicable.
