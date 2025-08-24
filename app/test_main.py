import datetime
import pytest

from unittest import mock
from typing import Iterator, Type

from app.main import outdated_products


@pytest.fixture()
def mock_today() -> Iterator[Type[datetime.date]]:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return datetime.date(2022, 2, 2)

    with mock.patch("app.main.datetime.date", MockDate):
        yield MockDate


@pytest.mark.parametrize(
    "products,expected",
    [
        pytest.param([
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
            ["duck"],
            id="test_one_product_is_outdated"
        ),
        pytest.param(
            [
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 50
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 30
                }
            ],
            [],
            id="test_all_products_are_in_date"
        ),
        pytest.param([
            {
                "name": "cheese",
                "expiration_date": datetime.date(2022, 1, 30),
                "price": 200
            },
            {
                "name": "ham",
                "expiration_date": datetime.date(2022, 1, 31),
                "price": 150
            }
        ],
            ["cheese", "ham"],
            id="test_all_products_are_outdated"
        ),
        pytest.param([
            {
                "name": "yogurt",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 25
            }
        ],
            [],
            id="test_product_expiration_date_is_today"
        ),
        pytest.param([], [], id="test_if_no_products")
    ]
)
def test_outdated_products(
        products: list[dict],
        expected: list[str],
        mock_today: Type[datetime.date]
) -> None:
    result = outdated_products(products)
    assert result == expected
