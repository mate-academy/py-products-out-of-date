import datetime
from unittest import mock

import pytest

from app.main import outdated_products


test_data = [
    (
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
        ], ["duck"]
    )
]


@pytest.fixture()
def mocked_time() -> mock:
    with mock.patch("app.main.datetime") as mock_time:
        yield mock_time


@pytest.mark.parametrize("product_list, result", test_data)
def test_outdated_products(
        mocked_time: callable,
        product_list: list[dict],
        result: list[str]
) -> None:
    mocked_time.date.today.return_value = datetime.date(2022, 2, 2)
    func_result = outdated_products(product_list)
    assert func_result == result
