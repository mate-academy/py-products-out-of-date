import datetime
from unittest.mock import MagicMock
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_result",
    [
        (
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2024, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2024, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2024, 2, 1),
                 "price": 160}
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(products: list, expected_result: list) -> None:
    datetime_date_mock = MagicMock()
    datetime_date_mock.today = MagicMock(
        return_value=datetime.date(2024, 2, 3))
    datetime.date = datetime_date_mock
    result = outdated_products(products)
    assert result == expected_result
