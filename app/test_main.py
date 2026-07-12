import datetime
from unittest.mock import patch

from app.main import outdated_products


class MockDate(datetime.date):
    _mock_today: datetime.date

    @classmethod
    def today(cls) -> datetime.date:
        return cls._mock_today


@patch("datetime.date", MockDate)
def test_outdated_products_one_expired() -> None:
    MockDate._mock_today = datetime.date(2022, 2, 15)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
    ]

    result = outdated_products(products)
    assert result == ["salmon", "chicken"]


@patch("datetime.date", MockDate)
def test_outdated_products_all_valid() -> None:
    MockDate._mock_today = datetime.date(2022, 1, 1)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
    ]

    result = outdated_products(products)
    assert result == []


@patch("datetime.date", MockDate)
def test_outdated_products_empty_list() -> None:
    MockDate._mock_today = datetime.date(2022, 2, 15)

    result = outdated_products([])
    assert result == []
