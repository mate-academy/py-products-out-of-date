import datetime
from unittest.mock import patch
import pytest
from app.main import outdated_products


@pytest.fixture
def mock_today():
    with patch("app.test_main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        yield mock_datetime.date.today


def test_outdated_products(mock_today):
    products = [
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
    ]

    result = outdated_products(products)
    assert result == ["duck"]

    products = [
        {
            "name": "apple",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 1
        },
        {
            "name": "banana",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 2
        }
    ]

    result = outdated_products(products)
    assert result == []

    # Test case 3: No products
    products = []

    result = outdated_products(products)
    assert result == []


if __name__ == "__main__":
    pytest.main()
