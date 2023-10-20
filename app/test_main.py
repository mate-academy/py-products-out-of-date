import datetime
from app.main import outdated_products


def test_outdated_products_should_return_list_with_products() -> None:
    assert outdated_products(
        [
            {
                "name": "chicken",
                "expiration_date": datetime.date(2023, 10, 20),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2023, 10, 19),
                "price": 160
            }
        ]
    ) == ["duck"]
