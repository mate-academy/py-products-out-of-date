import datetime
from app.main import outdated_products


def test_product_is_outdated() -> None:
    product = [{
        "name": "salmon",
        "expiration_date": datetime.date(2021, 2, 10),
        "price": 600
    }]

    assert outdated_products(product) == ["salmon"]


def test_product_is_not_outdated() -> None:
    product = [{
        "name": "makaron",
        "expiration_date": datetime.date(2026, 2, 2),
        "price": 100
    }]

    assert outdated_products(product) == []


def test_product_expiration_date_equals_today_is_not_outdated() -> None:
    product = [{
        "name": "makaron",
        "expiration_date": datetime.date.today(),
        "price": 100
    }]

    assert outdated_products(product) == []


def test_product_expiration_date_equals_yesterday_is_not_outdated() -> None:
    product = [{
        "name": "makaron",
        "expiration_date": datetime.date(2025, 3, 3),
        "price": 100
    }]

    assert outdated_products(product) == ["makaron"]
