import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products , result",
    [
        (
            [
                {
                    "name": "rabbit",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 150
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
                    "name": "veal",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 200
                }
            ],
            ["duck"]
        ),
        (
            [
                {
                    "name": "turkey",
                    "expiration_date": datetime.date(2022, 2, 9),
                    "price": 180
                },
                {
                    "name": "beef",
                    "expiration_date": datetime.date(2022, 2, 7),
                    "price": 250
                }
            ],
            [],
        )
    ]
)
def test_outdated_products(products: list, result: list) -> None:
    today_date = datetime.date(2022, 2, 2)
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == result
