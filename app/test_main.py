import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def get_product_list() -> list[dict]:
    return [
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
    ]


@mock.patch("app.main.datetime")
def test_outdated_product_work_correctly(
        mocked_datetime: mock.MagicMock,
        get_product_list: list[dict]
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    result = outdated_products(products=get_product_list)
    assert result == ["duck"]
