import datetime

import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
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
    "datetime_return_value,result",
    [
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 6), ["duck", "chicken"]),
        (datetime.date(2022, 2, 11), ["duck", "chicken", "salmon"])
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_datetime: mock.Mock,
        products: list,
        datetime_return_value: datetime.date,
        result: list
) -> None:
    mocked_datetime.today.return_value = datetime_return_value
    mocked_datetime.side_effect = \
        lambda *args, **kwargs: datetime.date(*args, **kwargs)
    assert sorted(outdated_products(products)) == sorted(result)
