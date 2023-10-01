import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products() -> None:
    product = [
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
    with mock.patch("app.main.datetime") as mocked_data:
        mocked_data.date.today.return_value = datetime.date(2022, 2, 3)
        result = outdated_products(product)

        assert result == ["duck"]
