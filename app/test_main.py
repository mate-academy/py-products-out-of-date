import pytest
import datetime

from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products_list, expected_list",
    [
        (
                [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 3, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 7, 11),
                    "price": 160
                }
                ], ["salmon", "chicken"]
        ),
        (
                [
                {
                    "name": "crab",
                    "expiration_date": datetime.date(2025, 10, 20),
                    "price": 900
                },
                {
                    "name": "tuna",
                    "expiration_date": datetime.date(2025, 7, 4),
                    "price": 590
                },
                {
                    "name": "cow",
                    "expiration_date": datetime.date(2025, 5, 7),
                    "price": 320
                }
                ], ["cow"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_datetime: mock.Mock,
        products_list: list,
        expected_list: list
) -> None:
    fake_time = datetime.date(2025, 6, 15)
    mock_datetime.date.today.return_value = fake_time
    assert outdated_products(products_list) == expected_list
