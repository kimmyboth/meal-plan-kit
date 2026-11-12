---
name: get-started
description: First-time setup for the meal-plan kit. Interviews the user about who they cook for, which meals to plan, targets, foods they won't eat, kitchen, prep style, store, budget and where their shopping list goes, then writes me.md and the empty files the other skills need. Use when me.md doesn't exist, when they type /get-started, or when they want to redo their setup.
---

# Get started

You're setting up a weekly meal planner for someone who isn't technical.
Keep it friendly and quick. They should feel set up within ten minutes.

## 1. Check what's there

- If `me.md` exists, read it. Tell them you'll update it and ask what's
  changed, or offer to go through it all again. Then interview only for what's
  changing, and finish at step 3.
- If not, say in two sentences what's about to happen: a few questions, then
  the first week can be planned.

## 2. Interview

Ask about one topic at a time, with at most two short questions per message.
Skip anything they've already told you. They may answer several at once.

1. **Household.** Who they cook for, including kids and their ages. Whether
   dinner is a family meal they eat a portion of.
2. **Meals to plan.** Just dinners, or breakfast, lunch and snacks too.
   Anything that's the same every day, like breakfast. Get the exact items and
   amounts, so its numbers can be worked out.
3. **Targets.** Only if they track: calories, protein, carbs, fat, fibre.
   Also any timing rules, like "most of my protein before lunch". If they
   don't track, that's fine. Don't push numbers, and never suggest targets.
4. **Won't eat.** Allergies, foods they won't eat, and textures. Whose rules
   are whose: a rule for them only, versus one for the whole household.
5. **Other rules.** Spice level for the kids, how long food must keep, no
   leftovers, and anything else.
6. **Kitchen and prep.** The appliances they have. How they like to prep: one
   bigger session (which day, how long), plus how many minutes on weeknights.
7. **Shopping.** Store and suburb or town (PAK'nSAVE, New World, Woolworths
   or other), weekly food budget, and whether they shop online or in store.
8. **Rhythm.** How many nights a week they usually don't need dinner planned.
   Mornings or lunches they're usually out.
9. **Recipes.** Favourite recipe sites. If they have none, suggest RecipeTin
   Eats (recipetineats.com) and Simple Home Edit (simplehomeedit.com). Foods
   and cuisines they love.
10. **The list.** Where they want the shopping list: Apple Reminders (Mac
    only, and which list), Google Keep, or just on screen. Whether they use
    the **Week on a Plate** page on claude.ai.

## 3. Write the files

Write `me.md` in exactly this shape. Leave a line as "not set" rather than
guessing.

```markdown
# Me

Updated: <date>

## Household
<who they cook for, kids' ages, whether dinner is a family meal>

## Meals to plan
- Plan: <e.g. Dinner only / Breakfast, lunch, snack and dinner>
- Fixed meals: <exact items and amounts, or none>
- Usually out: <mornings or lunches, or none>
- Nights off a week: <number> (which nights changes weekly; ask each week)

## Targets (theirs, not advice)
- Daily: <kcal> kcal · <g> protein · <g> carbs · <g> fat · <g> fibre, or "doesn't track"
- Timing: <e.g. 70g protein before lunch, or none>

## Won't eat
- <allergy or food> (whole household / just them)

## Rules
- <e.g. kids eat mild, heat at the table>
- Make-ahead food must keep for the days it's eaten.

## Loves
- <foods, cuisines>

## Kitchen and prep
- Appliances: <list>
- Prep: <e.g. one Sunday session of about 90 min, plus 20-minute weeknights>

## Shopping
- Store: <store and town>
- Shops: <online delivery / click & collect / in store>
- Budget: $<n> <currency> a week
- Deals page: <the store's deals link from plan-week's list>

## Recipes
- Favourite sites: <sites>

## The list
- Goes to: <Apple Reminders, list "<name>" / Google Keep / screen>
- Week on a Plate: <yes, with link / no>
```

Then create anything missing:

- `regulars.md`, with a heading and an empty table:
  `| Item | Usual qty | Shops (of total) | Last paid | Last bought | Store |`
- `recipes/index.md`, with a heading and an empty table:
  `| Recipe | Slot | Serves | Fridge days | Kids | Protein/serve | Last made |`

## 4. Wrap up

Summarise `me.md` in a few short lines and ask them to correct anything.
Then suggest the next steps, in this order:

1. Add three or four favourite dinners with **/add-recipe**. A dish name is
   enough.
2. Add two or three recent receipts with **/add-receipt**, so prices and
   brands are real.
3. Type **/plan-week** when they're ready for their first week.
