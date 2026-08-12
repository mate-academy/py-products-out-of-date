from typing import Callable
import datetime
import pytest

from app.main import outdated_products


class DummyDate(datetime.date):
    @classmethod
    def today(cls) -> "DummyDate":
        return cls._today


@pytest.fixture
def mock_today(monkeypatch: pytest.MonkeyPatch) -> None:
    def _set(date_value: datetime.date) -> None:
        DummyDate._today = DummyDate(
            date_value.year,
            date_value.month,
            date_value.day
        )
        monkeypatch.setattr(datetime, "date", DummyDate)
    return _set


def test_one_outdated(
    mock_today: Callable[[datetime.date], None]
) -> None:
    mock_today(datetime.date(2022, 2, 2))

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chiken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        },
    ]

    assert outdated_products(products) == ["duck"]


def test_no_outdated(
    mock_today: Callable[[datetime.date], None]
) -> None:
    mock_today(datetime.date(2022, 2, 2))

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 3)
        },
        {
            "name": "bread",
            "expiration_date": datetime.date(2022, 2, 10)
        },
    ]

    assert outdated_products(products) == []


def test_all_outdated(mock_today: Callable[[datetime.date], None]) -> None:
    mock_today(datetime.date(2022, 2, 25))

    products = [
        {
            "name": "a",
            "expiration_date": datetime.date(2022, 2, 1)
        },
        {
            "name": "b",
            "expiration_date": datetime.date(2022, 2, 20)
        },
    ]

    assert outdated_products(products) == ["a", "b"]


def test_empty_list(
    mock_today: Callable[[datetime.date], None]
) -> None:
    mock_today(datetime.date(2022, 2, 2))

    assert outdated_products([]) == []


def test_boundary_equal_date(
    mock_today: Callable[[datetime.date], None]
) -> None:
    mock_today(datetime.date(2022, 2, 2))

    products = [
        {"name": "x", "expiration_date": datetime.date(2022, 2, 2)},
        {"name": "y", "expiration_date": datetime.date(2022, 2, 1)},
    ]

    assert outdated_products(products) == ["y"]
