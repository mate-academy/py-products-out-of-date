from app.main import outdated_products
import datetime


def test_should_check_today() -> None:
    assert outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2023, 1, 4),
                "price": 600
            }
        ]
    ) == []


def test_should_check_yesterday() -> None:
    assert outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2023, 1, 3),
                "price": 600
            }
        ]
    ) == ["salmon"]
