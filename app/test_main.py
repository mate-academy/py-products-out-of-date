import pytest
from unittest import mock
import datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, result, today",
    [
        (
            [
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
                }
            ],
            ["duck"],
            datetime.date(2022, 2, 2),
        )
    ]
)
def test_out_products(products: list, result: list, today: datetime) -> list:
    with mock.patch("app.main.datetime") as mocked_data:
        mocked_data.date.today.return_value = today
        assert outdated_products(products) == result
