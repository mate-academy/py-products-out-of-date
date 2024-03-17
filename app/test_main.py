from unittest import mock

import pytest
import datetime
from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "list_product,out_date_product",
    [
        pytest.param(
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
        )
    ]
)
@patch("app.main.datetime")
def test_outdated_products(
        mock_datetime: mock.MagicMock,
        list_product: list,
        out_date_product: list) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(list_product) == out_date_product
