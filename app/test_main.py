import datetime
from unittest.mock import patch, MagicMock

import app.main


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
        }
    ]

    result = app.main.outdated_products(products)

    assert result == ["duck"]
