import datetime
import pytest
from app.main import outdated_products
from unittest import mock


@pytest.fixture()
def product_list():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "year,month,day,result",
    [
        (2022, 1, 30, []),
        (2022, 2, 3, ["duck"]),
        (2022, 2, 7, ["chicken", "duck", ]),
        (2022, 2, 12, ["salmon", "chicken", "duck"])
    ]
)
def test_outdated_products(product_list, year, month, day, result):  # test_date,
    exp_date = datetime.date(year, month, day)
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = exp_date
        assert outdated_products(product_list) == result
