import datetime
from types import TracebackType
from typing import Optional, Type

import app.main as main
from app.main import outdated_products


class FreezeDate:

    def __init__(self, year: int, month: int, day: int) -> None:
        self.frozen_date = datetime.date(year, month, day)
        self._orig_date_cls: Optional[type[datetime.date]] = None

    def __enter__(self) -> datetime.date:
        class MockDate(datetime.date):
            @classmethod
            def today(cls) -> datetime.date:
                return self.frozen_date  # type: ignore[attr-defined]

        self._orig_date_cls = main.datetime.date
        main.datetime.date = MockDate
        return self.frozen_date

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self._orig_date_cls is not None:
            main.datetime.date = self._orig_date_cls


def test_outdated_products_one_expired() -> None:
    with FreezeDate(2022, 2, 2):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 600,
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120,
            },
        ]
        assert outdated_products(products) == ["salmon"]


def test_outdated_products_all_expired() -> None:
    with FreezeDate(2022, 2, 15):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600,
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120,
            },
        ]
        assert outdated_products(products) == ["salmon", "chicken"]


def test_outdated_products_none_expired() -> None:
    with FreezeDate(2022, 1, 20):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600,
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120,
            },
        ]
        assert outdated_products(products) == []


def test_expiration_day_today_not_outdated() -> None:
    with FreezeDate(2022, 2, 5):
        products = [
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120,
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 4),
                "price": 160,
            },
        ]
        assert outdated_products(products) == ["duck"]


def test_outdated_products_empty_list() -> None:
    with FreezeDate(2022, 2, 2):
        assert outdated_products([]) == []
