import datetime
import pytest

from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "products, expected",
    [
        ([{"name": "salmon",
          "expiration_date": datetime.date(2022, 2, 10),
            "price": 600},
         {"name": "chicken",
          "expiration_date": datetime.date(2022, 2, 5),
          "price": 120},
         {"name": "duck",
          "expiration_date": datetime.date(2022, 2, 1),
          "price": 160}], ["duck"])
    ]
)
def test_outdated_products(datetime_mocked: mock,
                           products: list,
                           expected: list) -> None:
    datetime_mocked.date.today.return_value = datetime.date(2022, 2, 5)
    assert outdated_products(products) == expected
