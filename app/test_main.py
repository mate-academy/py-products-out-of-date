import datetime
from typing import List, Dict
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.fixture
def sample_products_some_outdated() -> List[Dict]:
    return [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]


@pytest.fixture
def sample_products_all_outdated() -> List[Dict]:
    return [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 1),
         "price": 600},
        {"name": "chicken", "expiration_date": datetime.date(2022, 1, 28),
         "price": 120},
    ]


@pytest.fixture
def sample_products_none_outdated() -> List[Dict]:
    return [
        {"name": "milk", "expiration_date": datetime.date(2022, 2, 10),
         "price": 50},
        {"name": "bread", "expiration_date": datetime.date(2022, 2, 15),
         "price": 20},
    ]


def test_no_outdated_products(
        sample_products_none_outdated: List[Dict]
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 5)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result: List[str] = outdated_products(sample_products_none_outdated)
    assert result == []


def test_some_outdated_products(
        sample_products_some_outdated: List[Dict]
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result: List[str] = outdated_products(sample_products_some_outdated)
    assert result == ["duck"]


def test_all_outdated_products(
        sample_products_all_outdated: List[Dict]
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result: List[str] = outdated_products(sample_products_all_outdated)
    assert result == ["salmon", "chicken"]


def test_empty_products_list() -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result: List[str] = outdated_products([])
    assert result == []
