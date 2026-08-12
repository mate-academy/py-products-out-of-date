import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "data,expected",
    [
        ({"name": "salmon",
          "expiration_date": datetime.date(2025, 5, 21),
          "price": 600}, []),
        ({"name": "chicken",
          "expiration_date": datetime.date(2025, 5, 20),
          "price": 120}, ["chicken"]),
        ({"name": "duck",
          "expiration_date": datetime.date(2025, 5, 25),
          "price": 160}, [])
    ]
)
def test_return_expired_products_names(
        data: dict,
        expected: list
) -> list:
    fake_today = datetime.date(2025, 5, 21)
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        assert outdated_products([data]) == expected
