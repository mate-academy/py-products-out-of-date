import datetime
from unittest import mock


from app.main import outdated_products

@mock.patch("app.main.datetime.date.today")
def test_outdated_products(mock_date) -> None:
    mock_date.return_value = datetime.date(2021, 2, 2)
    test_list = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2021, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2021, 2, 2),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2021, 2, 1),
        "price": 160
    }
    ]

    assert outdated_products(test_list) == ["duck"]
