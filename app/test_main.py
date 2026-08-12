from datetime import date
from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_inside(mock_date: date) -> None:
    mock_date.date.today.return_value = date(2022, 2, 2)
    assert outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ]) == ["duck"]
