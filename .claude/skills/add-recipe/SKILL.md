---
name: add-recipe
description: Turns a recipe link, Instagram or TikTok caption, pasted recipe, screenshot or plain dish name into a full recipe card in recipes/, checked against the user's rules in me.md, with a cook-along method, and adds it to recipes/index.md. Use when they type /add-recipe or share a recipe they want to keep.
---

# Add a recipe

Read `me.md` first, for their household, won't-eat list, rules, kitchen and
targets.

## 1. Get the recipe

- **A link to a recipe site:** open it and read the recipe. Use the built-in
  browser if the page needs it.
- **Instagram, TikTok or Facebook:** these usually can't be read. Ask for the
  caption or a screenshot.
- **A screenshot or photo:** read it.
- **Just a dish name or notes:** write a sensible standard version, preferably
  from one of their favourite sites (in `me.md`), and say where it's from.

If they pasted several recipes, do each one in turn.

## 2. Review it

- Check every ingredient against **Won't eat** and **Rules**. If it breaks
  one, write a specific swap, and use the swap in the card if it's a clear
  improvement. Otherwise mark the rule check "breaks".
- If the kids eat mild, keep it mild, and say where to add heat at the table.
- Fridge life: how many days it keeps. Does it freeze? Is it portable (fine
  cold or at room temperature in a lunchbox)?
- Macros per serve are your estimate, labelled **est.**, unless the source
  gives figures. Those are still **est.** until they log it themselves.

## 3. Write the card

Save `recipes/<slug>.md`, where the slug is the title in lowercase with
hyphens. Follow `recipes/_template.md` exactly:

- Ingredients in metric, one per line, with the spoon or cup equivalent in
  brackets where it helps.
- The method is a **cook-along**: numbered steps in the order to do them, and
  every step carries its own quantities, times and temperatures (oven, air
  fryer or pan heat), so they never need to look back at the ingredient list.
- Source: `saved <date>` plus the link, `suggested by Claude <date>`, or
  `family recipe <date>`.
- Last made: `never`.

If a recipe with the same title already exists, ask whether to replace it or
save this as a variation.

## 4. Add it to the index

Add a row to `recipes/index.md`, keeping the table sorted by slot, then
title:

`| [Title](slug.md) | Dinner | 4 | 4 | yes | 32g est. | never |`

## 5. Tell them

One or two lines: the title, the slot, how long it takes, how many days it
keeps, and any rule it breaks along with the swap you made or suggest.
