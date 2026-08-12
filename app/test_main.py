import datetime

import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result_ls,test_date",
    [
        (
            [
                {
                    "name": "yogurt",
                    "expiration_date": datetime.date(2023, 3, 13),
                    "price": 3
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2023, 3, 14),
                    "price": 1
                },
                {
                    "name": "salt",
                    "expiration_date": datetime.date(2023, 3, 15),
                    "price": 2
                }
            ],
            ["yogurt"],
            (2023, 3, 14)
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products_func(
        mock_datetime: mock,
        products: list[dict],
        result_ls: list,
        test_date: set
) -> None:

    mock_datetime.date.today.return_value = datetime.date(*test_date)
    assert outdated_products(products=products) == result_ls
