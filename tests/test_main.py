from freezegun import freeze_time
from app.main import outdated_products
import datetime

@freeze_time("2022-02-02")
class TestOutdatedProducts:
    def test_should_return_only_outdated_products_name(self):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]
        assert outdated_products(products) == ["duck"]


