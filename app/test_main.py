import datetime

import pytest

from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "product_list,exception_data",
    [
        ([{
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
        }], "duck"
        )
    ]
)
def test_outdated_products(
        product_list: list,
        exception_data: str
) -> None:
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(product_list) == [exception_data]
