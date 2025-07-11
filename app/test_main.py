from __future__ import annotations

import datetime
from typing import Any
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10), "price": 600}
    ]


def mock_today_date(mock_today: Any) -> Any:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> MockDate:
            return mock_today

    return MockDate


def test_outdated_products_if_date_is_ok(products_template: list) -> None:
    mock_date = mock_today_date(datetime.date(2022, 2, 10))
    with mock.patch("app.main.datetime.date", mock_date):
        assert outdated_products(products_template) == []


def test_outdated_products_if_date_is_expired(products_template: list) -> None:
    mock_date = mock_today_date(datetime.date(2022, 2, 11))
    with mock.patch("app.main.datetime.date", mock_date):
        assert outdated_products(products_template) == ["salmon"]
