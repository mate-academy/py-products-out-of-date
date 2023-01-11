import datetime
from app.main import outdated_products


class NewDate(datetime.date):
    @classmethod
    def today(cls) -> object:
        return cls(2022, 2, 2)


def test_outdated_products() -> None:
    datetime.date = NewDate
    product = ([
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
    ])
    assert outdated_products(product) == ["duck"]
