import pytest

from datetime import date

from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def template_products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


def test_with_expired_date(template_products: list) -> None:
    with mock.patch("datetime.date") as mocked_datetime:
        mocked_datetime.today.return_value = date(2022, 2, 2)

        assert outdated_products(template_products) == ["duck"]


def test_with_expiration_date_today(template_products: list) -> None:
    with mock.patch("datetime.date") as mocked_datetime:
        mocked_datetime.today.return_value = date(2022, 2, 1)

        assert outdated_products(template_products) == []
