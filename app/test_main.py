import pytest
from datetime import date
import app.main


@pytest.fixture()
def today(today=date.today()):
    from datetime import date

    class FakeDateType(type):
        def __instancecheck__(self, instance):
            return isinstance(instance, date)

    class FakeDate(date):
        __metaclass__ = FakeDateType

        def __new__(cls, *args, **kwargs):
            return date.__new__(date, *args, **kwargs)

        @staticmethod
        def today():
            return today.today()

    return today.today()


@pytest.fixture()
def products():
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


def test_outdated_products(products, today) -> list:
    res_list = []
    d = today
    for product in products:
        print(d)
        if product["expiration_date"] > d:
            res_list.append(product)
    assert res_list == app.main.outdated_products(products), \
        f"Should be {res_list}"
