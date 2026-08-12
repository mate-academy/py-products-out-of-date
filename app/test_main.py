from unittest import mock

import pytest
from app.main import outdated_products


@pytest.mark.parametrize("fake_today, products, expected", [
    ("2025-12-22",
     [
         {"name": "salmon", "expiration_date": "2025-12-22"},
         {"name": "duck", "expiration_date": "2025-12-21"}
     ],
     ["duck"]
     ),
    ("2025-12-22",
     [
         {"name": "chicken", "expiration_date": "2025-12-20"},
         {"name": "apple", "expiration_date": "2025-12-25"}
     ],
     ["chicken"]
     )
])
def test_products_date(
        fake_today: str,
        products: list,
        expected: list
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        assert outdated_products(products) == expected
