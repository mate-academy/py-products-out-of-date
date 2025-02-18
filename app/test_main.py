import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products , expected_result",
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
                },
                {
                    "name": "pork",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 300
                }
            ],
            ["duck"]
        ),
        (
            [
                {
                    "name": "pork",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 300
                },
                {
                    "name": "beer",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 100
                }
            ],
            [],
        )
    ]
)
def test_outdated_products(products: list, expected_result: list) -> None:
    fake_today = datetime.date(2022, 2, 2)
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        assert outdated_products(products) == expected_result
