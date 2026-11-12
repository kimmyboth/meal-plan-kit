---
name: add-receipt
description: Reads a past supermarket shop (pasted order-email text, photos, screenshots or a PDF invoice) into receipts/, then updates regulars.md with what the user actually buys, their usual quantities and last-paid prices. Use when they type /add-receipt or share a receipt or order confirmation.
---

# Add a receipt

## 1. Read it

They may paste text from an online order email, attach photos or
screenshots, or give you a PDF invoice. Read every product line:

- Tidy each name into plain words, with brand and size, e.g.
  "Anchor Blue Top Milk 3L". If it matches an item already in `regulars.md`,
  use that exact name.
- Record the quantity and the price paid for the line, after any line
  discount.
- Leave out bags, delivery and service fees, deposits and subtotals. Note the
  fees separately.
- If part of it is unreadable, skip that part and tell them what you skipped.
  Never guess a price.
- Note the store, date and total.

Several receipts at once is fine: handle each one in turn.

## 2. Check it's new

If `receipts/` already has a shop with the same store, date and total, say
so and stop, unless they say it's a different shop.

## 3. Save it

Write `receipts/<YYYY-MM-DD>-<store-slug>.md`:

```markdown
# <Store>, <date>

Total $<total> · fees $<fees> · <n> items

| Item | Qty | Price |
|---|---|---|
| Anchor Blue Top Milk 3L | 2 | $11.40 |
```

## 4. Update regulars.md

Rebuild `regulars.md` from every file in `receipts/`:

- One row per item: usual quantity per shop, how many shops it appeared on
  out of the total (e.g. "5 of 6"), the last price paid for one, the date
  last bought, and the store.
- Sort by how often it's bought, most often first.
- Mark anything on at least half of their shops as **usual**. The plan-week
  skill adds these to the list when they want their usual buys included.

## 5. Tell them

One or two lines: how many items you read, how many were new to
`regulars.md`, and any big price changes since last time (more than 10%).
