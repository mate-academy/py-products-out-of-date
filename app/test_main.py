from app.main import outdated_products
import datetime
from unittest import mock


@mock.patch("app.main.datetime")
def test_if_the_expiration_date_is_today(mock_date: datetime) -> None:
    mock_date.date.today.return_value = datetime.date(2023, 8, 7)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 8, 7),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 8, 6),
            "price": 120
        },
        {
            "name": "butter",
            "expiration_date": datetime.date(2023, 8, 9),
            "price": 120
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2022, 8, 7),
            "price": 120
        },
        {
            "name": "bread",
            "expiration_date": datetime.date(2024, 8, 7),
            "price": 120
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2023, 9, 7),
            "price": 120
        },
        {
            "name": "oysters",
            "expiration_date": datetime.date(2022, 7, 7),
            "price": 120
        }
    ]

    assert outdated_products(products) == ["chicken", "beef", "oysters"]
