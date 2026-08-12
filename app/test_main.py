import datetime
from app.main import outdated_products
from unittest import mock


def test_out_date_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022,
                                             2,
                                             10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022,
                                             2,
                                             5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022,
                                             2,
                                             1),
            "price": 160
        }
    ]
    with mock.patch("app.main.datetime") as mocked_file:
        mocked_file.date.today.return_value = datetime.date(2022, 2, 5)
        assert (
            outdated_products(products) == ["duck"]
        )
