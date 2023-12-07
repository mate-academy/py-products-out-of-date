from unittest import mock

import pytest

import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, result",
    [
        (
            [
                {
                    "name": "salmon1",
                    "expiration_date": datetime.date(2022, 12, 6),
                    "price": 600
                },
                {
                    "name": "salmon2",
                    "expiration_date": datetime.date(2023, 12, 5),
                    "price": 600
                },
                {
                    "name": "salmon3",
                    "expiration_date": datetime.date(2020, 12, 6),
                    "price": 600
                }
            ],
            ["salmon3"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 2, 10),
                    "price": 600
                },
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 11),
                    "price": 600
                },
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 3, 10),
                    "price": 600
                }
            ],
            []
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_date: any,
        products: list[dict],
        result: list[dict]) -> None:

    mock_date.date.today.return_value = datetime.date(2022, 2, 10)

    assert (
        outdated_products(products) == result
    )
    # mock_date.assert_called()
