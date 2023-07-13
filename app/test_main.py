import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products() -> None:
    assert outdated_products([]) == []

    today_date = datetime.date(2022, 2, 2)
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
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == []

    today_date = datetime.date(2022, 2, 2)
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
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 300
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == ["duck"]
