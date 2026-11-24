"""Reference build for Project 2. Money is stored as whole pennies, never floats."""
import csv
import json
from datetime import date
from pathlib import Path

DATA = Path("expenses.json")


def load() -> list[dict]:
    try:
        return json.loads(DATA.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save(expenses: list[dict]) -> None:
    DATA.write_text(json.dumps(expenses, indent=2))


def add(expenses: list[dict]) -> None:
    try:
        pennies = round(float(input("Amount (£): ")) * 100)
    except ValueError:
        print("Amount must be a number."); return
    expenses.append({"id": (max((e["id"] for e in expenses), default=0) + 1),
                     "date": str(date.today()), "description": input("Description: ").strip(),
                     "category": input("Category: ").strip().lower(), "amount_pence": pennies})
    save(expenses)


def show(expenses: list[dict]) -> None:
    for e in expenses:
        print(f'#{e["id"]} {e["date"]} {e["category"]:12} £{e["amount_pence"] / 100:.2f} {e["description"]}')
    print(f'Total: £{sum(e["amount_pence"] for e in expenses) / 100:.2f}')


def export(expenses: list[dict]) -> None:
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "date", "description", "category", "amount_pence"])
        writer.writeheader(); writer.writerows(expenses)
    print("Wrote expenses.csv")


def main() -> None:
    expenses = load()
    while True:
        choice = input("\n[a]dd [l]ist [f]ilter [e]xport [q]uit: ").lower()
        if choice == "q": return
        if choice == "a": add(expenses)
        elif choice == "l": show(expenses)
        elif choice == "f": show([e for e in expenses if e["category"] == input("Category: ").lower()])
        elif choice == "e": export(expenses)
        else: print("Unknown choice.")


if __name__ == "__main__": main()
