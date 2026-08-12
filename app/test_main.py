from typing import Any

import app.main
import datetime

from app.main import outdated_products


def test_func_outdated_products(monkeypatch: Any) -> None:
    products_list = [
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
    mydt = datetime.date

    class MyDate:
        @staticmethod
        def today() -> datetime:
            return mydt(2022, 2, 2)

    monkeypatch.setattr(app.main.datetime, "date", MyDate)
    assert outdated_products(products_list) == ["duck"]


def test_func_outdated_products_today(monkeypatch: Any) -> None:
    products_list = [
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
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 160
        }
    ]
    mydt = datetime.date

    class MyDate:
        @staticmethod
        def today() -> datetime:
            return mydt(2022, 2, 2)

    monkeypatch.setattr(app.main.datetime, "date", MyDate)
    assert outdated_products(products_list) == []
