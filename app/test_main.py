import datetime

from unittest.mock import patch, MagicMock
from app import main


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 1, 15),
            "price": 50
        }
    ]

    result = main.outdated_products(products)

    assert result == ["duck", "milk"]


def test_outdated_products_empty_list() -> None:
    assert main.outdated_products([]) == []
