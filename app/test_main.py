import datetime
import pytest

from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list[dict]:
    yield [
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
def test_outdated_products(
        mocked_today: object,
        products_template: list[dict]
) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products_template) == ["duck"]
