from unittest import mock
import datetime
import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    products_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 2, 25),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 23),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 160
        }
    ]
    return products_list


@pytest.mark.parametrize(
    "date_now,result",
    [
        pytest.param(datetime.date(2022, 2, 9), []),
        pytest.param(datetime.date(2022, 2, 12), ["duck"]),
        pytest.param(datetime.date(2022, 2, 24), ["chicken", "duck"]),
        pytest.param(datetime.date(2022, 2, 10), []),
    ]

)
@mock.patch("datetime.date")
def test_expired(date_mocked: mock,
                 date_now: datetime,
                 result: list,
                 products: list) -> None:
    date_mocked.today.return_value = date_now
    assert outdated_products(products) == result
