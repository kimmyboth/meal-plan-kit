# Meal plan

A personal meal-planning kit. The person using it comes in each week to plan
their food, the household's dinners and the shop. The aim is eating well with
minimal decisions and minimal prep.

## Start here, every session

- Read `me.md` first. It holds their household, targets, food rules, kitchen,
  prep style, store, budget and how they like their list. Everything here plans
  to it. If something you need isn't in it, ask, then add the answer to `me.md`.
- No `me.md` yet? Run the **get-started** skill before anything else.
- When they tell you something has changed ("we've gone off mushrooms",
  "budget's $250 now"), update `me.md` straight away and say so in one line.
- They aren't technical. Never ask them to run a command, open a terminal or
  edit a file. Do it yourself and say in plain words what you did.

## Skills

- **/get-started**: the setup interview. It writes `me.md`, and they can run it
  again any time.
- **/plan-week**: the weekly routine. It covers this week's specials, the plan,
  the prep cook-along, the shopping list, and getting the list onto their phone.
- **/add-recipe**: turns a link, caption, pasted recipe, screenshot or dish
  name into a full recipe card.
- **/add-receipt**: reads a past shop (pasted text, photos, screenshots or a
  PDF) into `receipts/` and updates `regulars.md`.

## Folder layout

- `me.md`: their profile (written by get-started).
- `recipes/`: one Markdown file per recipe, in the shape of
  `recipes/_template.md`. `recipes/index.md` is the catalogue, one row per
  recipe. Keep it in step whenever a recipe is added or made.
- `weeks/YYYY-MM-DD.md`: one file per week, named for Monday's date. It holds
  the plan, the prep session and the shopping list. Beside it,
  `weeks/YYYY-MM-DD.shopping.json` holds the list for the tools.
- `receipts/`: one file per past shop. `regulars.md` is what they actually
  buy: brands, usual quantities and last-paid prices.
- `tools/push_reminders.py`: adds a week's list to Apple Reminders (Mac only).

## Numbers

- Figures they have tracked, or read off a pack label, are the truth. Never
  invent or estimate a number they've tracked. If one is missing, ask.
- Every other number is labelled **est.**, both macros and prices.
- They set their own targets. Plan to them, and never suggest targets or give
  medical or dietary advice. If they don't track, plan for balanced, filling
  meals and skip the numbers.

## Rules for every plan

- Everything under "Won't eat" and "Rules" in `me.md` is absolute. Check every
  recipe against them, and when one breaks a rule, offer a specific swap.
- **Prep lists and dinner methods are cook-alongs.** Every step carries its
  own quantities (metric, with the spoon or cup equivalent), times and
  temperatures, in the order to do them, so they never have to open a recipe.
- Anything made ahead must keep in the fridge for the days it's eaten.
- Variety matters. Don't repeat a recipe within two weeks unless they ask, and
  add at most one new recipe a week. While their collection has fewer than
  five dinners, suggest as many as the week needs.
- Recipes they saved come first. Then their favourite recipe sites (in
  `me.md`).
- If `me.md` says the kids eat mild, cook mild and add heat at the table.
- Use their kitchen (in `me.md`) and their prep style: one prep session plus
  quick weeknights, unless they say otherwise.

## Shopping

- Shop at their store (in `me.md`). Plan around this week's specials where
  they fit the rules.
- Every price says where it came from: **special** (this week's deals),
  **last paid** (from `regulars.md`) or **est.**
- Show the total against their budget. If a week runs over, say so once,
  without nagging.
- On supermarket websites, only read the deals pages. Never sign in, add to
  cart, place an order or pay.

## Output

UK English, NZ date format, metric, and their currency (NZD unless `me.md`
says otherwise). Plain, warm and short. Lead with the point, and stop when
it's made.
