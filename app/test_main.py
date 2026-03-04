import datetime
import pytest
from unittest.mock import patch

from app.main import outdated_products


@pytest.fixture
def product_template() -> list:
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


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 2)


def test_outdated_products(product_template: list) -> None:
    with patch("app.main.datetime.date", FakeDate):
        assert outdated_products(product_template) == ["duck"]


def test_outdated_exp_date_eq_today(product_template: list) -> None:
    product_template[2]["expiration_date"] = datetime.date(2022, 2, 2)
    with patch("app.main.datetime.date", FakeDate):
        assert outdated_products(product_template) == []
