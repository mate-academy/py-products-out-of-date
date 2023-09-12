import datetime

from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mock_date: mock.MagicMock) -> None:
    mock_date.date.today.return_value = datetime.date(2023, 9, 13)

    product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 9, 15),
            "price": 120
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2023, 9, 13),
            "price": 150
        }
    ]
    products = outdated_products(product_list)
    assert products == ["salmon"]
