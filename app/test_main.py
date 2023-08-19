from unittest import mock
from app.main import outdated_products
import datetime


@mock.patch("app.main.datetime")
def test_check_outdated(mock_date: mock.MagicMock) -> None:
    mock_date.date.today.return_value = datetime.date(
        2023, 7, 10
    )

    list_to_check = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 7, 14),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 7, 17),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 7, 9),
            "price": 160
        }
    ]
    products = outdated_products(list_to_check)

    assert products == ["duck"]
