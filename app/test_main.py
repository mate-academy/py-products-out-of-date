import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def mocked_date() -> mock:
    with mock.patch("app.main.datetime") as mocked_date_test:
        yield mocked_date_test.date.today


def test_return_duck_if_due_date_is_feb_2(mocked_date: mock) -> None:
    products = [
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

    mocked_date.return_value = datetime.date(2022, 2, 10)

    assert outdated_products(products) == ["chicken", "duck"]
