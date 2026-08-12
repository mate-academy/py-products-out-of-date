import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture
def mocked_datetime() -> mock.MagicMock:
    with mock.patch("app.main.datetime") as mocked_func:
        yield mocked_func


@pytest.fixture
def products_dict() -> dict:
    data = {
        "products_list": [
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
        "outdated_products_list": ["duck"]
    }
    return data


def test_outdated_products(
        mocked_datetime: mock.MagicMock,
        products_dict: dict
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert (
        outdated_products(products_dict["products_list"])
        == products_dict["outdated_products_list"]
    )
