import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def mocked_date_today() -> datetime.date.today:
    with mock.patch("app.main.datetime") as mocked_day:
        yield mocked_day


@pytest.fixture()
def products_template() -> list:
    products_list = [
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
    yield products_list


def test_should_return_outdated(mocked_date_today: datetime.date.today,
                                products_template: list) -> None:
    mocked_date_today.date.today.return_value = datetime.date(2022, 2, 7)
    assert outdated_products(products_template) == ["chicken", "duck"]
