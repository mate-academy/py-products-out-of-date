import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


def test_for_december_3(template: list) -> None:
    expected = ["salmon", "chicken", "duck"]
    assert outdated_products(template) == expected


def test_with_date_yesterday(template: list) -> None:
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    template = [{"name": "milk", "expiration_date": yesterday, "price": 50}]
    expected = ["milk"]
    assert outdated_products(template) == expected


def test_with_date_today(template: list) -> None:
    today = datetime.date.today()
    template = [{"name": "milk", "expiration_date": today, "price": 50}]
    expected = []
    assert outdated_products(template) == expected
