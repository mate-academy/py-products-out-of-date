import pytest
from app.main import outdated_products
from freezegun import freeze_time
import datetime


@pytest.mark.parametrize("date, expected_result", [
    ("2022, 02, 02", ["duck"]),
    ("2022, 02, 06", ["chicken", "duck"]),
    (datetime.date.today(), ["salmon", "chicken", "duck"])
])
def test_outdated_products(date: datetime, expected_result: list[str]) -> None:
    with freeze_time(date):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            },
            {
                "name": "duck",
                "expiration_date": datetime.date.today(),
                "price": 160
            }
        ]
        assert outdated_products(products) == expected_result
