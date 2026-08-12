from unittest import mock
import pytest

from .main import outdated_products


@pytest.fixture()
def mock_date() -> any:
    with mock.patch("datetime.date") as mock_time:
        yield mock_time


def test_outdated_products_02_01(mock_date: any) -> None:
    mock_date.today.return_value = (2022, 2, 1)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": (2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": (2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": (2022, 2, 1),
            "price": 160
        }
    ]) == []


def test_outdated_products_02_02(mock_date: any) -> None:
    mock_date.today.return_value = (2022, 2, 2)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": (2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": (2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": (2022, 2, 1),
            "price": 160
        }
    ]) == ["duck"]


def test_outdated_products_02_05(mock_date: any) -> None:
    mock_date.today.return_value = (2022, 2, 5)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": (2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": (2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": (2022, 2, 1),
            "price": 160
        }
    ]) == ["duck"]


def test_outdated_products_02_06(mock_date: any) -> None:
    mock_date.today.return_value = (2022, 2, 6)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": (2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": (2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": (2022, 2, 1),
            "price": 160
        }
    ]) == ["chicken", "duck"]


def test_outdated_products_02_10(mock_date: any) -> None:
    mock_date.today.return_value = (2022, 2, 10)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": (2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": (2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": (2022, 2, 1),
            "price": 160
        }
    ]) == ["chicken", "duck"]


def test_outdated_products_02_11(mock_date: any) -> None:
    mock_date.today.return_value = (2022, 2, 11)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": (2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": (2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": (2022, 2, 1),
            "price": 160
        }
    ]) == ["salmon", "chicken", "duck"]
