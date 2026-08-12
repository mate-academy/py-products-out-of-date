import datetime
from unittest.mock import patch
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
    current_date = datetime.date(2024, 2, 3)
    with patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = current_date
        result = outdated_products(products)
    assert result == expected_result
