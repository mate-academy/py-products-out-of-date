import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def product_list() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date.today(),
            "price": 600,
        }
    ]


def test_if_exp_date_is_today_not_outdated(product_list: list) -> None:
    assert outdated_products(product_list) == []


def test_if_exp_date_is_yesterday_not_outdated(product_list: list) -> None:
    product_list[0]["expiration_date"] -= datetime.timedelta(days=1)
    assert outdated_products(product_list) == ["salmon"]
