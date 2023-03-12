import datetime
from typing import Callable

import pytest

from app.main import outdated_products


@pytest.fixture
def products() -> list:
    return [{"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1),
             "price": 160}]


@pytest.mark.parametrize(
    "mocked_date,result",
    [
        pytest.param(datetime.date(2022, 2, 1), []),
        pytest.param(datetime.date(2022, 2, 2), ["duck"]),
        pytest.param(datetime.date(2022, 2, 10), ["chicken", "duck"]),
    ]
)
def test_outdated_products(monkeypatch: Callable,
                           products: list,
                           mocked_date: datetime.date,
                           result: list) -> None:
    class MyDate:
        @staticmethod
        def today() -> datetime.date:
            return mocked_date
    monkeypatch.setattr("app.main.datetime.date", MyDate)
    assert outdated_products(products) == result, "unexpected result"
