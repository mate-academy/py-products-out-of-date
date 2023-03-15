import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    mocked_today = datetime.date.today()
    return [
        {
            "name": "salmon",
            "expiration_date": mocked_today,
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": mocked_today - datetime.timedelta(days=1),
            "price": 120
        },
    ]


def test_today_products(products_template: list) -> None:
    assert "salmon" not in outdated_products(products_template)


def test_yesterday_products(products_template: list) -> None:
    assert "chicken" in outdated_products(products_template)
