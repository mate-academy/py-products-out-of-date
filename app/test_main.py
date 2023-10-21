import pytest
from unittest import mock
import datetime

from app.main import outdated_products


@pytest.mark.parametrize("products, expected_result", [
    ([
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 1), "price": 160},
        {"name": "today_product", "expiration_date":
            datetime.date(2022, 2, 6), "price": 80},
    ], ["chicken", "duck"]),
    ([
        {"name": "beef", "expiration_date":
            datetime.date(2023, 3, 15), "price": 250},
        {"name": "pork", "expiration_date":
            datetime.date(2023, 4, 5), "price": 180}
    ], []),
    ([], []),
])
@mock.patch("datetime.date", wraps=datetime.date)
def test_outdated_products(
        mock_date: mock.MagicMock,
        products: list,
        expected_result: list
) -> None:
    mock_date.today.return_value = datetime.date(
        2022, 2, 6
    )  # Fixed date for testing

    result = outdated_products(products)
    assert result == expected_result
