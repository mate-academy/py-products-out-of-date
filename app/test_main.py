import datetime
from unittest.mock import patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: datetime.date) -> None:

    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products1 = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120},
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 6),
            "price": 160},
    ]
    assert outdated_products(products1) == []

    products2 = [
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
            "price": 160},
    ]
    assert outdated_products(products2) == ["duck"]

    products3 = [
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
        },
    ]
    assert outdated_products(products3) == ["salmon", "duck"]

    assert outdated_products([]) == []
