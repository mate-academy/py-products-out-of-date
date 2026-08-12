import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture
def products_data() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 3, 21),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 3, 21),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2026, 3, 21),
            "price": 160
        }
    ]


def test_all_products_outdated(products_data: list[dict]) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2026, 3, 22)
        assert (
            outdated_products(products_data)
            == ["salmon", "chicken", "duck"]
        )


def test_products_not_outdated(products_data: list[dict]) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2026, 3, 20)
        assert outdated_products(products_data) == []
