import datetime
import pytest
from unittest import mock

from app.main import outdated_products


class CustomDate(datetime.date):
    @classmethod
    def today(cls) -> "CustomDate":
        return cls(2023, 1, 12)


@pytest.fixture()
def products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 1, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 1, 13),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 1, 11),
            "price": 160
        }
    ]


def test_products_with_today_data_is_not_outdated(
        products: list[dict]
) -> None:
    with mock.patch("datetime.date", CustomDate):
        assert outdated_products(products) == ["duck"]
