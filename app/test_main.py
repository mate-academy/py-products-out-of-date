from app.main import outdated_products
import datetime
from unittest import mock


@mock.patch("app.main.datetime")
def test_outdated_products(mock_date: datetime) -> None:
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
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)

    result = outdated_products(products)
    assert result == ["duck"]
