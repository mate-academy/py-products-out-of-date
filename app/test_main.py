import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def template_list() -> list:
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


@mock.patch("app.main.datetime")
def test_should_return_list_only_of_not_outdated_products(
        mocked_today: mock,
        template_list: list
) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(template_list) == ["duck"]
