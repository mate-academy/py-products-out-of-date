from __future__ import annotations

import datetime
from unittest import mock

from app.main import outdated_products


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> FakeDate:
        return cls(2025, 10, 28)


@mock.patch("app.main.datetime.date", new=FakeDate)
def test_outdated_products_two_normal_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 11, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 12, 10),
            "price": 120
        }
    ]
    assert (
        outdated_products(products) == []
    )


def test_outdated_products_two_outdated_products() -> None:
    with mock.patch("app.main.datetime.date", new=FakeDate):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 12, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2025, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 11),
                "price": 160
            }
        ]
        assert (
            outdated_products(products) == ["chicken", "duck"]
        )


@mock.patch("app.main.datetime.date", new=FakeDate)
def test_outdated_products_exp_date_is_equal_to_today_date() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 10, 28),
            "price": 600
        },
    ]
    assert (
        outdated_products(products) == []
    )


@mock.patch("app.main.datetime.date", new=FakeDate)
def test_outdated_products_exp_date_is_yesterday() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 10, 27),
            "price": 600
        },
    ]
    assert (
        outdated_products(products) == ["salmon"]
    )
