# app/test_main.py
import datetime
from unittest import mock

from app.main import outdated_products


REAL_DATE = datetime.date


@mock.patch("app.main.datetime.date")
def test_some_products_outdated(
    mocked_date: mock.MagicMock,
) -> None:
    mocked_date.today.return_value = REAL_DATE(2022, 2, 2)
    mocked_date.side_effect = lambda *a, **kw: REAL_DATE(*a, **kw)

    products = [
        {
            "name": "salmon",
            "expiration_date": REAL_DATE(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": REAL_DATE(2022, 2, 2),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": REAL_DATE(2022, 2, 1),
            "price": 160,
        },
    ]
    result = outdated_products(products)
    # Product expiring today ("chicken") is not outdated
    assert result == ["duck"]


@mock.patch("app.main.datetime.date")
def test_no_products_outdated(
    mocked_date: mock.MagicMock,
) -> None:
    mocked_date.today.return_value = REAL_DATE(2022, 2, 1)
    mocked_date.side_effect = lambda *a, **kw: REAL_DATE(*a, **kw)

    products = [
        {
            "name": "salmon",
            "expiration_date": REAL_DATE(2022, 2, 10),
            "price": 600,
        },
    ]
    result = outdated_products(products)
    assert result == []


@mock.patch("app.main.datetime.date")
def test_all_products_outdated(
    mocked_date: mock.MagicMock,
) -> None:
    mocked_date.today.return_value = REAL_DATE(2022, 3, 1)
    mocked_date.side_effect = lambda *a, **kw: REAL_DATE(*a, **kw)

    products = [
        {
            "name": "apple",
            "expiration_date": REAL_DATE(2022, 2, 15),
            "price": 10,
        },
        {
            "name": "banana",
            "expiration_date": REAL_DATE(2022, 2, 20),
            "price": 12,
        },
    ]
    result = outdated_products(products)
    assert result == ["apple", "banana"]
