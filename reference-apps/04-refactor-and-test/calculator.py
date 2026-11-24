def total_pence(expenses: list[dict]) -> int:
    return sum(expense["amount_pence"] for expense in expenses)


def by_category(expenses: list[dict], category: str) -> list[dict]:
    return [expense for expense in expenses if expense["category"] == category]
