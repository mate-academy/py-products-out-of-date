import datetime

from app.main import outdated_products


def test_outdated_products_corrected_result() -> None:
    assert outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2023, 6, 11),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date.today(),
                "price": 120
            }
        ]
    ) == ["salmon"]
