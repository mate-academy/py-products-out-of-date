import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture(scope="function")
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 2, 10),
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
def test_should_return_correct_list(
        mocked_datetime: mock,
        products_template: list[dict]
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2023, 1, 25)
    assert outdated_products(products_template) == ["chicken", "duck"]
