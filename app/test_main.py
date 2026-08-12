import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,expected_result",
    [
        (
            [{"name": "salmon",
              "expiration_date": datetime.date(2022, 2, 10)}],
            []
        ),
        (
            [{"name": "salmon",
              "expiration_date": datetime.date(2022, 2, 2)}],
            ["salmon"]
        )
    ],
    ids=[
        "Valid product",
        "Outdated product"
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_date: mock,
                           products: list,
                           expected_result: list) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 5)
    assert outdated_products(products) == expected_result
