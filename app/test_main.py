from unittest import mock
from datetime import date

from app.main import outdated_products


@mock.patch("datetime.date")
def test_should_return_outdated_products(mocked_date: mock.MagicMock) -> None:
    mocked_date.today.return_value = date(2022, 7, 8)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": date(2022, 7, 8),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 7, 7),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 7, 3),
            "price": 160
        },
    ]) == ["chicken", "duck"]
