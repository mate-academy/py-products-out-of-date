import pytest
import datetime
from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize("products, expected_result", [([{
    "name": "salmon",
    "expiration_date": datetime.date(2023, 11, 6),
    "price": 600
}], []), ([{
    "name": "chicken",
    "expiration_date": datetime.date(2023, 11, 4),
    "price": 120
}], ["chicken"]), ([{
    "name": "duck",
    "expiration_date": datetime.date(2023, 11, 5),
    "price": 220
}], [])], ids=["expiration date > today",
               "expiration date < today",
               "expiration date = today"])
def test_outdated_products(products: list, expected_result: list) -> None:
    with patch("datetime.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date.today()
        assert outdated_products(products) == expected_result
