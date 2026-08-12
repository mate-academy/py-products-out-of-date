import pytest
from unittest import mock
from app.main import datetime, outdated_products


@pytest.mark.parametrize(
    "date, result",
    [
        (datetime.date(2022, 2, 2), []),
        (datetime.date(2022, 2, 6), ["duck"]),
        (datetime.date(2022, 2, 9), ["chicken", "duck"]),
        (datetime.date(2022, 2, 10), ["salmon", "chicken", "duck"]),
    ]
)
@mock.patch("app.main.datetime")
def test_function_has_called(
        mocked_time: mock.MagicMock,
        date: datetime.datetime,
        result: list) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 9),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 6),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 160,
        },
    ]
    mocked_time.date.today.return_value = date
    assert outdated_products(products) == result
