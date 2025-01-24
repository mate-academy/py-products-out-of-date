import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "fake_today, salmon, chicken, duck", [
        (datetime.date(2022, 2, 2),
         datetime.date(2022, 2, 10),
         datetime.date(2022, 2, 2),
         datetime.date(2022, 2, 1))
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        date: object,
        fake_today: object,
        salmon: object,
        chicken: object,
        duck: object
) -> None:
    date.today.return_value = fake_today
    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": salmon,
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": chicken,
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": duck,
            "price": 160
        }
    ]) == ["duck"]
