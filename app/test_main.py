import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture
def mocked_datetime_today():
    with mock.patch("app.main.datetime") as mocked_time:
        yield mocked_time


def test_function_correct_work(mocked_datetime_today):
    mocked_datetime_today.date.today.return_value = datetime.date(2022, 2, 2)
    a = [{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    }, {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    }, {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }]
    result = outdated_products(a)
    assert result == ["duck"]
