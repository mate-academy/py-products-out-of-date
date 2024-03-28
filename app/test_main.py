import datetime
from unittest.mock import patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: str) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products([
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
            "expiration_date": datetime.date(2022, 2, 7),
            "price": 160
        }
    ]) == []

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 1),
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
    ]) == ["salmon", "duck"]

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]) == ["salmon", "chicken", "duck"]

    assert outdated_products([]) == []
