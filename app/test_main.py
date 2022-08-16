from app.main import outdated_products
import datetime


def test_expiration_all_dates_less_date():
    list_products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 8, 6),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 8, 9),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 8, 2),
            "price": 160
        }
    ]
    assert outdated_products(list_products) == ["salmon", "chicken", "duck"]


def test_expiration_all_dates_norm_date():
    list_products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 8, 31),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 9, 9),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 8, 22),
            "price": 160
        }
    ]

    assert outdated_products(list_products) == []


def test_expiration_dates_are_yesterday_date():
    list_products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 8, 16),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 8, 29),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 8, 15),
            "price": 160
        }
    ]
    assert outdated_products(list_products) == ["duck"]
