from datetime import timedelta, date

from app.main import outdated_products


products = [
    {"name": "salmon", "expiration_date": date(2026, 12, 22)},
    {"name": "chicken", "expiration_date": date(2026, 10, 22)},
    {"name": "Meal", "expiration_date": date(2024, 10, 22)},
    {"name": "milk", "expiration_date": date.today()},
    {"name": "butter", "expiration_date": date(2027, 1, 10)},
    {"name": "fish", "expiration_date": date.today() - timedelta(days=1)},
]
expected = ["chicken", "Meal", "fish"]


def test_outdated_products() -> None:
    assert outdated_products(products) == expected
