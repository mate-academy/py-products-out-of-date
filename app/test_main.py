from app.main import outdated_products
import datetime
from unittest import mock

real_date = datetime.date


@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_date: mock.MagicMock) -> None:
    mock_date.today.return_value = real_date(2026, 6, 11)
    mock_date.side_effect = lambda *args, **kwargs: real_date(*args, **kwargs)

    products = [
        {
            "name": "salmon",
            "expiration_date": real_date(2025, 10, 2),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": real_date(2022, 10, 22),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": real_date(2026, 6, 9),
            "price": 160
        },
        {
            "name": "bread",
            "expiration_date": real_date(2026, 6, 10),
            "price": 50
        },
        {
            "name": "milk",
            "expiration_date": real_date(2026, 6, 11),
            "price": 80
        }
    ]

    result = outdated_products(products)
    assert result == ["salmon", "chicken", "duck", "bread"]
