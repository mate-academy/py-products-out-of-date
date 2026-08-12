import pytest
from unittest import mock
from datetime import date

from app.main import outdated_products


@pytest.fixture()
def mocked_products() -> None:
    with mock.patch("app.main.datetime") as mocked_product:
        yield mocked_product


def test_products_out_of_date(mocked_products: mocked_products) -> None:
    mocked_products.date.today.return_value = date(2022, 2, 3)
    result_list = outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ]
    )
    assert result_list == ["duck"]
