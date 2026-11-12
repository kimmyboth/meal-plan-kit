"""Add a week's shopping list to Apple Reminders (Mac only).

Reads weeks/<monday>.shopping.json (written by the plan-week skill) and adds
each item to a Reminders list, with the quantity, price and section in the
reminder's notes. The list is created if it doesn't exist. Items already open
on the list with the same name are skipped, and so are items ticked off in
the last 7 days (already bought). Nothing on the list is changed or removed.

Usage: python3 tools/push_reminders.py 2026-11-16 ["Shopping List"]
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SCRIPT = """
on run argv
    set listName to item 1 of argv
    set itemName to item 2 of argv
    set itemBody to item 3 of argv
    tell application "Reminders"
        if not (exists list listName) then make new list with properties {name:listName}
        set theList to list listName
        if (count of (reminders of theList whose name is itemName and completed is false)) > 0 then return "skip"
        set weekAgo to (current date) - (7 * days)
        if (count of (reminders of theList whose name is itemName and completed is true and completion date > weekAgo)) > 0 then return "skip"
        make new reminder at end of theList with properties {name:itemName, body:itemBody}
        return "added"
    end tell
end run
"""


def lines(monday):
    items = json.loads((ROOT / "weeks" / f"{monday}.shopping.json").read_text())
    for it in items:
        name = str(it.get("item", "")).strip()
        if not name:
            continue
        qty = str(it.get("qty", "")).strip()
        price = it.get("price")
        source = str(it.get("source", "est.")).strip()
        bits = [qty] if qty else []
        if isinstance(price, (int, float)) and price:
            bits.append(f"${price:.2f} {source}".strip())
        if it.get("section"):
            bits.append(str(it["section"]))
        yield name, " · ".join(bits)


def main(monday, list_name="Shopping List"):
    added = skipped = 0
    for name, body in lines(monday):
        out = subprocess.run(["osascript", "-e", SCRIPT, list_name, name, body],
                             capture_output=True, text=True, check=True).stdout.strip()
        if out == "added":
            added += 1
        else:
            skipped += 1
    print(f"{list_name}: {added} added, {skipped} already there")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], *sys.argv[2:3])
