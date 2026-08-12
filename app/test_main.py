import datetime

from unittest.mock import MagicMock

from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_function_should_work_correctly(mock_today: MagicMock) -> None:
    mock_today.date.today.return_value = datetime.date(2022, 1, 30)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),  # Сьогодні
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),  # Позавчора
            "price": 160
        }
    ]

    assert outdated_products(products) == []
