import pytest
import datetime

from app.main import outdated_products


def test_should_return_a_duck_because_it_is_expired() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": (datetime.date.today()
                                + datetime.timedelta(days=8)),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": (datetime.date.today()
                                + datetime.timedelta(days=3)),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": (datetime.date.today()
                                - datetime.timedelta(days=1)),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["duck"]


def test_dont_have_to_return_the_chicken_because_it_is_overdue_today() -> None:
    products = [
        {
            "name": "chicken",
            "expiration_date": datetime.date.today(),
            "price": 120
        }
    ]

    assert outdated_products(products) == []


def test_should_raise_error_if_name_key_not_exist() -> None:
    products = [
        {
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }
    ]
    with pytest.raises(KeyError):
        outdated_products(products)


def test_should_raise_error_if_expiration_date_key_not_exist() -> None:
    products = [
        {
            "name": "salmon",
            "price": 600
        }
    ]
    with pytest.raises(KeyError):
        outdated_products(products)
