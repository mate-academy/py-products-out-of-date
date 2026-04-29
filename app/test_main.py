import datetime
from unittest import mock


from app.main import outdated_products

#@mock.patch("datetime.date.today")
def test_outdated_products() -> None:
    test_list = [
    {
        "name": "salmon",
        "expiration_date": datetime.date.today() + datetime.timedelta(days=1),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date.today(),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date.today() + datetime.timedelta(days=-1),
        "price": 160
    }
    ]

    #mock_date.return_value = datetime.date.today()

    assert outdated_products(test_list) == ["duck"]

