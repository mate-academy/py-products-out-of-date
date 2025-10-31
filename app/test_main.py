import pytest
import datetime

from unittest import mock

from app.main import outdated_products


@pytest.fixture
def products() -> list:
    return [
        {"name": "salmon",
         "expiration_date": datetime.date(2025, 11, 10)},
        {"name": "chicken",
         "expiration_date": datetime.date(2025, 10, 15)},
        {"name": "duck",
         "expiration_date": datetime.date(2025, 11, 1)},
        {"name": "mushrooms",
         "expiration_date": datetime.date(2025, 11, 11)},
    ]


@pytest.mark.parametrize(
    "today, expected",
    [
        (datetime.date(2025, 11, 5),
         ["chicken", "duck"]),
        (datetime.date(2025, 10, 14),
         []),
        (datetime.date(2025, 12, 14),
         ["salmon", "chicken", "duck", "mushrooms"]),
    ],
)
def test_cryptocurrency_action(products: list,
                               today: str,
                               expected: list) -> None:
    print(products, today, expected)
    with mock.patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today

        assert outdated_products(products) == expected
