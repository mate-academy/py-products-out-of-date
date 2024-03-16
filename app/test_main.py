import datetime
import pytest
from app.main import outdated_products


@pytest.fixture
def mock_today(monkeypatch):
    class MockDate:
        @staticmethod
        def today():
            return datetime.date(2022, 2, 2)  # Mocking today's date to 2nd February 2022

    monkeypatch.setattr(datetime, "date", MockDate)


def test_outdated_products_with_today(mock_today):
    products = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1), "price": 160},
    ]
    assert outdated_products(products) == ["duck"]


def test_outdated_products_with_empty_list(mock_today):
    assert outdated_products([]) == []


def test_outdated_products_with_future_dates(mock_today):
    products = [
        {"name": "milk", "expiration_date": datetime.date(2022, 3, 10), "price": 50},
        {"name": "bread", "expiration_date": datetime.date(2022, 3, 15), "price": 30},
    ]
    assert outdated_products(products) == []


def test_outdated_products_with_past_dates(mock_today):
    products = [
        {"name": "cheese", "expiration_date": datetime.date(2021, 12, 25), "price": 80},
        {"name": "yogurt", "expiration_date": datetime.date(2021, 11, 20), "price": 40},
    ]
    assert outdated_products(products) == ["cheese", "yogurt"]


def test_outdated_products_with_mixed_dates(mock_today):
    products = [
        {"name": "apple", "expiration_date": datetime.date(2022, 2, 1), "price": 10},
        {"name": "orange", "expiration_date": datetime.date(2022, 2, 5), "price": 20},
        {"name": "banana", "expiration_date": datetime.date(2022, 2, 3), "price": 15},
    ]
    assert outdated_products(products) == ["apple"]
