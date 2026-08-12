from app.main import outdated_products
from datetime import date, timedelta


def test_today_not_outdated() -> None:
    """
    Тест перевіряє, що продукт зі сьогоднішньою датою не вважається застарілим.
    """
    products = [{"name": "Milk", "expiration_date": date.today()}]
    assert outdated_products(products) == []


def test_yesterday_outdated() -> None:
    """
    Тест перевіряє, що продукт з учорашньою датою вважається застарілим.
    """
    products = [
        {"name": "Bread", "expiration_date": date.today() - timedelta(days=1)}
    ]
    assert outdated_products(products) == ["Bread"]
