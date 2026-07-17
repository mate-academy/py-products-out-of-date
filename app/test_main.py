from datetime import datetime, timedelta


from app.main import outdated_products


def test_if_the_product_is_expired() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date.today() - timedelta(days=1),
            "price": 600
        }
    ]
    assert outdated_products(products) == ["salmon"]


def test_if_the_due_date_is_today() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date.today(),
            "price": 600
        }
    ]
    assert outdated_products(products) == []
