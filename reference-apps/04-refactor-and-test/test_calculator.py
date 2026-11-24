from calculator import by_category, total_pence


EXPENSES = [{"category": "food", "amount_pence": 350}, {"category": "travel", "amount_pence": 275}]


def test_total_pence(): assert total_pence(EXPENSES) == 625
def test_by_category(): assert by_category(EXPENSES, "food") == [EXPENSES[0]]
def test_missing_category_returns_empty_list(): assert by_category(EXPENSES, "bills") == []
