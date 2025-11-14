import datetime
import pytest

from unittest import mock

from app.main import outdated_products


@pytest.fixture
def product_with_mocked_today() -> dict:
    product = {
        "name": "chicken",
        "expiration_date": datetime.date(2025, 5, 10),
        "price": 150
    }

    real_date = datetime.date

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.side_effect = lambda *a, **kw: real_date(*a, **kw)

        def set_today(date: real_date) -> None:
            mock_date.today.return_value = date

        yield product, set_today


def test_outdated_product_same_date(product_with_mocked_today: dict) -> None:
    product, set_today = product_with_mocked_today
    set_today(datetime.date(2025, 5, 10))
    assert outdated_products([product]) == []


def test_outdated_product_day_before(product_with_mocked_today: dict) -> None:
    product, set_today = product_with_mocked_today
    set_today(datetime.date(2025, 5, 9))
    assert outdated_products([product]) == []


def test_outdated_product_after_date(product_with_mocked_today: dict) -> None:
    product, set_today = product_with_mocked_today
    set_today(datetime.date(2025, 5, 11))
    assert outdated_products([product]) == ["chicken"]
