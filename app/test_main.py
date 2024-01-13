from freezegun import freeze_time
from app.main import outdated_products
import datetime


@freeze_time("2022-02-02 12:00:00")
def test_outdated_products() -> None:
    products = [{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    }, {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    }, {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }, {
        "name": "eag",
        "expiration_date": datetime.date(2022, 2, 2),
        "price": 160
    }
    ]

    assert outdated_products(products) == ["duck"]
