from datetime import date
from unittest import mock
from unittest.mock import MagicMock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: MagicMock) -> None:
    mocked_datetime.date.today.return_value = date(year=2023, month=2, day=2)

    products: list[dict] = [
        {
            "name": "milk",
            "expiration_date": date(
                year=2023,
                month=2,
                day=1,
            ),
        },
        {
            "name": "ice cream",
            "expiration_date": date(
                year=2023,
                month=2,
                day=2,
            ),
        },
        {
            "name": "cake",
            "expiration_date": date(
                year=2023,
                month=2,
                day=3,
            ),
        },
    ]

    assert outdated_products(products) == ["milk"]
