---
title: Team trial
description: Track the days and credit left in your organization's Team trial, see it on Settings → Plan & Invoices, and what the Union.ai UI does when the trial ends.
icon: hourglass-split
weight: 1
variants: -flyte +union
---

# Team trial

A new self-service organization starts on a Team trial, the first month with the Team minimum waived (see [Product tiers](./product-tiers#your-first-month)).
The trial has a number of days and an amount of credit, and it ends when either one runs out.
The Union.ai UI shows what's left in the sidebar and on **Settings → Plan & Invoices**, and every member of the organization can see both.

## Trial card in the sidebar

While the trial runs, and after it ends, a card sits near the bottom of the sidebar.
Select it to open **Settings → Plan & Invoices**.
Its meter shows how much is used of the limit you're on course to reach first: days, or credit if you're spending faster than the days pass.

| State | Card text | Meter |
|---|---|---|
| Running | **Team trial**, with the days and credit left, for example "12 days · $612 left" | Blue |
| Ending soon | For example, "Trial ends in 4 days" and "$188 of credit left", the closer limit first | Orange |
| Ended | **Trial ended**, "Read-only. Upgrade to run again." | Red |

The card disappears once the trial converts to Team.
If you subscribed on [AWS Marketplace](./sign-up/aws-marketplace), the trial converts to Team when it ends, so your organization doesn't become read-only.

## Trial on Settings → Plan & Invoices

The **Plan** tab of **Settings → Plan & Invoices** opens with the trial:

- **Team trial**: "Every Team plan feature, free until the days or the credit run out." After the trial ends, this row reads **Team trial ended** and "This organization is read-only until it upgrades to Team."
- **Days left**: days used and left, and the end date, "unless the credit runs out first".
- **Credit left**: credit used and left, with "Compute and Union usage count against it."
- **Enterprise**, with **Talk to us**, which opens an email to Union.ai support.

## When the trial ends

When the trial ends without converting, the organization is read-only in the Union.ai UI:

- Every page shows a red banner: "Your Team trial has ended. Everything is read-only."
- Buttons that create or run something are disabled: for example, running a task, connecting a cluster, starting an app, and creating a project, trigger, secret, or queue.
  Hover over a disabled button to see the reason: "Your Team trial has ended, so this organization is read-only. Upgrade to Team to make changes."
- You can still view your organization's projects, runs, and settings, and open **Settings → Plan & Invoices**.

The card and the disabled-button tooltip mention upgrading.
If you don't see an **Upgrade** button, select **Talk to us** on **Settings → Plan & Invoices** to keep using Union.ai.
