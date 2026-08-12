from datetime import date, timedelta

from app.main import outdated_products


def test_return_correct() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2025, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["salmon", "duck"]


def test_expiration_day_yesterday_outdated() -> None:
    today = date.today()
    yesterday = today - timedelta(days=1)
    products = [
        {
            "name": "salmon",
            "expiration_date": today,
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": yesterday,
            "price": 120
        },
    ]

    assert outdated_products(products) == ["chicken"]
