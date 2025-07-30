import pytest
import datetime
from app.main import outdated_products
from unittest import mock


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
    ]


@mock.patch("app.main.datetime")
def test_should_return_outdated_products(
        mocked_date: mock.MagicMock,
        products_template: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2025, 2, 5)
    mocked_date.date.side_effect = \
        lambda *args, **kwargs: datetime.date(*args, **kwargs)
    assert outdated_products(products_template) == ["chicken"]


@mock.patch("app.main.datetime")
def test_should_return_empty_list_if_all_products_are_good(
        mocked_date: mock.MagicMock,
        products_template: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2021, 2, 5)
    mocked_date.date.side_effect = \
        lambda *args, **kwargs: datetime.date(*args, **kwargs)
    assert outdated_products(products_template) == []


@mock.patch("app.main.datetime")
def test_should_return_empty_list_if_all_products_expiration_date_are_today(
        mocked_date: mock.MagicMock,
        products_template: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 5)
    mocked_date.date.side_effect = \
        lambda *args, **kwargs: datetime.date(*args, **kwargs)
    assert outdated_products(products_template) == []


@mock.patch("app.main.datetime")
def test_outdated_if_expiration_date_equal_yesterday(
        mocked_date: mock.MagicMock,
        products_template: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 6)
    mocked_date.date.side_effect = \
        lambda *args, **kwargs: datetime.date(*args, **kwargs)
    assert outdated_products(products_template) == []
