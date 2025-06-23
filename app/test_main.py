from app.main import outdated_products
from unittest import mock
import pytest
import datetime


@pytest.fixture()
def fixed_dict_list() -> None:
    my_list = [
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
    return my_list


@pytest.mark.parametrize(
    "expiration_date, result",
    [
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2023, 2, 11), ["salmon", "chicken", "duck"]),
        (datetime.date(2021, 2, 11), [])
    ]
)
def test_outdated_products(fixed_dict_list: list[dict],
                           expiration_date: object,
                           result: list) -> None:
    with mock.patch("datetime.date") as mocked_datetime:
        mocked_datetime.today.return_value = expiration_date
        assert outdated_products(fixed_dict_list) == result
