from app.main import outdated_products
import datetime


def test_returns_empty() -> None:
    products = [{
        "name": "duck",
        "expiration_date": datetime.date.today(),
        "price": 160
    }]

    assert outdated_products(products) == []


def test_returns_name_of_expired_product() -> None:
    products = [{
        "name": "duck",
        "expiration_date": (datetime.date.today() - datetime.timedelta(1)),
        "price": 160
    }]

    assert outdated_products(products) == ["duck"]
