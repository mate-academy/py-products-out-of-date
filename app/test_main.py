import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def templates_products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2026, 2, 1),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
def test_expiration_day_yesterday(
    mok_date: mock.MagicMock,
    templates_products: list[dict]
) -> None:

    mok_date.date.today.return_value = datetime.date(2026, 2, 2)

    assert (
        outdated_products(templates_products) == ["duck"]
    ), "The expiration date is being compared incorrectly."


@mock.patch("app.main.datetime")
def test_expiration_day_today(
    mok_date: mock.MagicMock,
    templates_products: list[dict]
) -> None:

    mok_date.date.today.return_value = datetime.date(2026, 2, 5)

    assert (
        outdated_products(templates_products) == ["duck"]
    ), "The expiration date is being compared incorrectly."


@mock.patch("app.main.datetime")
def test_expiration_day_tommorow(
    mok_date: mock.MagicMock,
    templates_products: list[dict]
) -> None:

    mok_date.date.today.return_value = datetime.date(2026, 1, 2)

    assert (
        outdated_products(templates_products) == []
    ), "The expiration date is being compared incorrectly."
