from app.main import outdated_products
import datetime


def test_outdated_products_date() -> None:
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    products = [
        {
            "name": "Tomato",
            "price": 100,
            "expiration_date": tomorrow
        },
        {
            "name": "Kinder",
            "price": 1,
            "expiration_date": today - datetime.timedelta(days=1)
        },
        {
            "name": "Bier",
            "price": 30,
            "expiration_date": today - datetime.timedelta(days=1)
        },
        {
            "name": "Bred",
            "price": 15,
            "expiration_date": today
        },
    ]
    result = outdated_products(products)
    assert len(result) == 2
    assert result == ["Kinder", "Bier"]
