import datetime
from app.main import outdated_products


def test_outdated_products_sould_return_bad_product() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": (
                datetime.date.today() - datetime.timedelta(days=1)
            ),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date.today(),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["salmon", "duck"]
