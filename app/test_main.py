import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products():
    yield [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 1, 3),
            "price": 400
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 1, 2),
            "price": 100
        }
    ]


@pytest.mark.parametrize(
    "date,expected",
    [
        pytest.param(datetime.date(2022, 1, 1),
                     [],
                     id="all expired"),
        pytest.param(datetime.date(2022, 1, 5),
                     ["salmon", "chicken"],
                     id="all frash"),
        pytest.param(datetime.date(2022, 1, 3),
                     ["chicken"],
                     id="one is frash"),
    ]
)
@mock.patch("app.main.datetime")
def test_products(mocked_today, date, expected, products):
    mocked_today.date.today.return_value = date
    assert outdated_products(products) == expected
