import pytest
import datetime
from unittest.mock import patch
from app.main import outdated_products
from typing import List, Dict


@pytest.mark.parametrize("mock_today_value, products, expected", [
    (datetime.date(2022, 2, 2), [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
        },
    ],
        ["duck"]
    ),

    (datetime.date(2022, 2, 11), [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
        },
    ],
        ["salmon", "chicken", "duck"]
    ),
])
def test_outdated_products(
        mock_today_value: datetime.date,
        products: List[Dict[str, object]],
        expected: List[str]
) -> None:
    with patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = mock_today_value
        result = outdated_products(products)
        assert result == expected
