from app.main import outdated_products
import datetime
from unittest import mock


@mock.patch("app.main.datetime")
def test_if_the_expiration_date_is_today(mock_date: datetime) -> None:
    mock_date.date.today.return_value = datetime.date(2023, 7, 28)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 7, 28),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 7, 27),
            "price": 120
        },
        {
            "name": "butter",
            "expiration_date": datetime.date(2023, 7, 29),
            "price": 120
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2022, 7, 28),
            "price": 120
        },
        {
            "name": "bread",
            "expiration_date": datetime.date(2024, 7, 28),
            "price": 120
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2023, 8, 28),
            "price": 120
        },
        {
            "name": "oysters",
            "expiration_date": datetime.date(2022, 6, 28),
            "price": 120
        }
    ]

    assert outdated_products(products) == ["chicken", "beef", "oysters"]
