import datetime
from app.main import outdated_products


def test_outdated_products_should_return_wright_data() -> None:
    today = datetime.date.today()
    today + datetime.timedelta(days=1)
    data = [
        {
            "name": "salmon",
            "expiration_date": today + datetime.timedelta(days=8),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": today + datetime.timedelta(days=3),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": today + datetime.timedelta(days=-1),
            "price": 160
        }
    ]
    assert outdated_products(data) == ["duck"]


def test_outdated_products_should_return_wright_data_not_outdated() -> None:
    today = datetime.date.today()
    today + datetime.timedelta(days=1)
    data = [
        {
            "name": "salmon",
            "expiration_date": today + datetime.timedelta(days=8),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": today + datetime.timedelta(days=3),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": today,
            "price": 160
        }
    ]
    assert outdated_products(data) == []


def test_outdated_products_should_return_empty_list() -> None:
    assert outdated_products([]) == []
