from app.main import outdated_products
from unittest import mock
import pytest
import datetime

list_of_products = [
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
    "not_true_time, expected_result",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 3, 5), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 1, 5), [])
    ]
)
def test_outdated_products(
        not_true_time: datetime.date | list[str],
        expected_result: list[str] | list
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = not_true_time
        assert outdated_products(
            list_of_products
        ) == expected_result
