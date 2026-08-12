import datetime
from app.main import outdated_products


def test_outdated_products_empty_list() -> None:
    products = []
    expected_outdated = []
    assert outdated_products(products) == expected_outdated


def test_outdated_products_single_outdated() -> None:
    today = datetime.date.today()
    products = [
        {
            "name": "salmon",
            "expiration_date": today
        },
        {
            "name": "chicken",
            "expiration_date": today - datetime.timedelta(days=5)
        },
        {
            "name": "duck",
            "expiration_date": today - datetime.timedelta(days=10)
        },
    ]
    expected_outdated = ["chicken", "duck"]
    assert outdated_products(products) == expected_outdated


def test_outdated_products_no_outdated() -> None:
    today = datetime.date.today()
    products = [
        {
            "name": "salmon",
            "expiration_date": today + datetime.timedelta(days=1)
        },
        {
            "name": "chicken",
            "expiration_date": today + datetime.timedelta(days=5)
        },
    ]
    expected_outdated = []
    assert outdated_products(products) == expected_outdated


def test_outdated_products_all_outdated() -> None:
    today = datetime.date.today()
    products = [
        {
            "name": "salmon",
            "expiration_date": today - datetime.timedelta(days=2)
        },
        {
            "name": "chicken",
            "expiration_date": today - datetime.timedelta(days=7)
        },
    ]
    expected_outdated = ["salmon", "chicken"]
    assert outdated_products(products) == expected_outdated


def test_outdated_products_expiration_yesterday() -> None:
    today = datetime.date.today()
    products = [
        {
            "name": "salmon",
            "expiration_date": today - datetime.timedelta(days=1)
        },
    ]
    expected_outdated = ["salmon"]
    assert outdated_products(products) == expected_outdated
