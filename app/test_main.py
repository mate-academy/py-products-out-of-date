from unittest.mock import MagicMock
from unittest import mock
from app.main import outdated_products
import datetime


@mock.patch("app.main.datetime.date.today")
def test_outdated_products(mock_date_pro: MagicMock) -> None:
    mock_date_pro.return_value = datetime.date(2022, 2, 15)
    test_print = (outdated_products([
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
    ]))
    assert test_print == ["duck"]
