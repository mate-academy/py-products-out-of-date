from datetime import date
from unittest import mock

from app.main import outdated_products


@mock.patch("datetime.date")
def test_outdated_products(mocked_daytime_today: date) -> None:
    mocked_daytime_today.today.return_value = date(2023, 2, 11)
    test_value = [
        {
            "name": "salmon",
            "expiration_date": date(2023, 2, 11),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2023, 2, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2024, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(test_value) == ["chicken"]
