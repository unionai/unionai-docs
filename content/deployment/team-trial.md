---
title: Team trial
description: Track the days and credit left in your organization's Team trial, upgrade to Team by adding a card, and see what the Union.ai UI does when the trial ends.
icon: hourglass-split
weight: 3
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

If you can upgrade, the card also has an **Upgrade** button (see [Upgrade to Team](#upgrade-to-team)).
Once a card is on file, the trial card shows "Team starts when days or credit run out", with the trial's end date.

The card disappears once the trial converts to Team.
If you [subscribed through a cloud marketplace](./sign-up), the trial converts to Team when it ends and the marketplace bills you, so your organization doesn't become read-only.

## Trial on Settings → Plan & Invoices

The **Plan** tab of **Settings → Plan & Invoices** opens with the trial:

- **Team trial**: "Every Team plan feature, free until the days or the credit run out." After the trial ends, this row reads **Team trial ended** and "This organization is read-only until it upgrades to Team."
  If you can upgrade, this row has an **Upgrade to Team** button.
- **Days left**: days used and left, and the end date, "unless the credit runs out first".
- **Credit left**: credit used and left, with "Compute and Union usage count against it."
- **Enterprise**, with **Talk to us**, which opens an email to Union.ai support.

Once the trial converts, members who can view billing (among the built-in policies, **Admin**) see a single **Team** row in place of the trial rows, and **Enterprise · Talk to us** stays.

## Upgrade to Team

If you subscribed through a cloud marketplace, there's no **Upgrade** button.

If you signed up directly, admins (the **Admin** policy, see [User management](../user-guide/user-management)) see an **Upgrade** button until a card is on file.
It appears in three places:

- **Upgrade** on the trial card.
- **Upgrade to Team** on the read-only banner, after the trial ends.
- **Upgrade to Team** in the trial section of the **Plan** tab.

Each one opens the **Upgrade** drawer on **Settings → Plan & Invoices**:

- **Team**: select **Add card**, enter the card, and select **Save card**.
- **Enterprise**: select **Talk to us**, which opens an email to Union.ai support. No card is needed.

What adding a card does depends on where the trial is:

- **While the trial runs:** the trial keeps running, and the organization converts to Team when the trial ends. Billing starts then.
- **After the trial has ended:** the organization converts to Team as soon as Stripe confirms the card, and read-only lifts. Billing starts that day.

### Payments tab

If you signed up directly, your organization also has a **Payments** tab on **Settings → Plan & Invoices**, which admins see:

- **Payment method**: the card Stripe charges for each invoice, with **Add card** or **Replace card**, and **Manage saved cards**.
- **Invoice history**: the invoices Stripe has sent the organization, newest first, with **Open Stripe billing portal**.

A card added here upgrades the trial the same way as one added in the drawer.

## When the trial ends

When the trial ends without converting, the organization is read-only in the Union.ai UI:

- Every page shows a red banner: "Your Team trial has ended. Everything is read-only."
- Buttons that create or run something are disabled: for example, running a task, connecting a cluster, starting an app, and creating a project, trigger, secret, or queue.
  Hover over a disabled button to see the reason: "Your Team trial has ended, so this organization is read-only. Upgrade to Team to make changes."
- You can still view your organization's projects, runs, and settings, and open **Settings → Plan & Invoices**.

To keep using Union.ai:

- If you're an admin and you signed up directly, select **Upgrade to Team** on the banner or **Upgrade** on the trial card, and add a card (see [Upgrade to Team](#upgrade-to-team)).
  If you're not an admin, ask an admin to upgrade.
- To move to Enterprise, select **Talk to us** on **Settings → Plan & Invoices**.
