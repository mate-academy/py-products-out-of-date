from unittest import mock
from datetime import date

from app.main import outdated_products


tested_list = [
    {
        "name": "salmon",
        "expiration_date": date(2024, 4, 7),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": date(2024, 4, 7),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": date(2024, 4, 7),
        "price": 160
    }]


def test_is_outdated_today() -> None:
    with mock.patch("datetime.date") as mocked_today:
        mocked_today.today.return_value = date(2024, 4, 7)
        mocked_today.side_effect = lambda *args, **kw: date(*args, **kw)
        assert outdated_products(tested_list) == []


def test_is_outdated_next_day() -> None:
    with mock.patch("datetime.date") as mocked_today:
        mocked_today.today.return_value = date(2024, 4, 8)
        mocked_today.side_effect = lambda *args, **kw: date(*args, **kw)
        assert outdated_products(tested_list) == ["salmon", "chicken", "duck"]
