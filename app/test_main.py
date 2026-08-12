from unittest import mock
from datetime import date

from app.main import outdated_products


product_list = [
    {
        "name": "salmon",
        "expiration_date": date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": date(2022, 2, 2),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": date(2022, 2, 1),
        "price": 160
    },
    {
        "name": "fish",
        "expiration_date": date.today(),
        "price": 800
    }
]


@mock.patch("datetime.date")
def test_outdated_products_on_mocked_date(mocked_date: mock.MagicMock) -> None:
    mocked_date.today.return_value = date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]
