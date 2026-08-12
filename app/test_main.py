from unittest import mock
import datetime

from app.main import outdated_products


def test_check_outdated_products_with_mocked_date() -> None:
    mocked_date = datetime.date(2022, 2, 10)

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
        },
        {
            "name": "salami",
            "expiration_date": datetime.date(2022, 2, 9),
            "price": 100
        }
    ]

    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = mocked_date

        result = outdated_products(products)

    assert result == ["chicken", "duck", "salami"]
