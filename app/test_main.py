from datetime import date
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.date")
def test_outdated_products():
    date.today.return_value = date(2022, 2, 2)
    result = outdated_products([
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
    ])
    assert result == ["duck"]


