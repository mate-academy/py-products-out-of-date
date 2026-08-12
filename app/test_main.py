from unittest.mock import patch
import datetime
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: callable) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    result = outdated_products([
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
    ])

    assert result == ["duck"]
