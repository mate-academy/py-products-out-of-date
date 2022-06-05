import datetime

from app.main import outdated_products


class NewDate(datetime.date):
    @classmethod
    def today(cls):
        return cls(2022, 2, 2)


def test_outdated_products():
    products = [
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
    ]
    datetime.date = NewDate

    assert outdated_products(products) == ["duck"], (
        f"Function should return ['duck'],"
        f"when products equal {products}"
    )
