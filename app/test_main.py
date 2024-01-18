import pytest

from unittest.mock import MagicMock, patch

from typing import List

from app.main import outdated_products


@pytest.fixture()
def mock_datetime_date() -> MagicMock:
    with patch("app.main.datetime.date") as mock_date:
        yield mock_date


@pytest.mark.parametrize(
    "products, check_date, expired_products",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": (2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": (2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": (2022, 2, 1),
                    "price": 160
                }
            ],
            (2022, 2, 2),
            ["duck"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": (2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": (2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": (2022, 2, 2),
                    "price": 160
                }
            ],
            (2022, 2, 2),
            []
        ),
    ]
)
def test_outdated_products(
        products: List[dict],
        check_date: tuple,
        expired_products: list,
        mock_datetime_date: MagicMock
) -> None:
    mock_datetime_date.today.return_value = check_date
    assert outdated_products(products) == expired_products
