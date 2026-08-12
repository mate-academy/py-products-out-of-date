import datetime

from app.main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 2),
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
]


def test_date():
    class NewDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2022, 2, 2)

    datetime.date = NewDate

    assert outdated_products(products) == ['duck']
