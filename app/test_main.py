import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def template() -> None:
    yield [
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


@pytest.mark.parametrize("mocked_date, expected",
                         [
                             (datetime.date(2022, 2, 10), ["chicken", "duck"]),
                             (datetime.date(2022, 2, 5), ["duck"]),
                             (datetime.date(2022, 1, 1), []),
                             (datetime.date(2021, 2, 10), []),
                             (datetime.date(2024, 2, 10),
                              ["salmon", "chicken", "duck"])
                         ])
@mock.patch("app.main.datetime")
def test_returning_outdated_products_with_different_dates(
        mocked: mock.Mock, mocked_date: datetime.date,
        expected: list, template: list) -> None:
    mocked.date.today.return_value = mocked_date
    assert outdated_products(template) == expected
