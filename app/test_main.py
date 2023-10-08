from unittest import mock
import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    yield [
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
    "date_today, expected_result",
    [
        (datetime.date(2022, 1, 1), []),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 15), ["salmon", "chicken", "duck"])
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
    mocked_datetime_date_today: callable,
    date_today: datetime.date,
    expected_result: list,
    products: list
) -> None:
    mocked_datetime_date_today.date.today.return_value = date_today
    assert outdated_products(products) == expected_result
