import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
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


@pytest.mark.parametrize(
    "today_date, expired_list", [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 1), [])
    ],
    ids=["yesterday expiration date is outdated",
         "today expiration date is valid"]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_date: mock,
                           today_date: datetime,
                           expired_list: list,
                           products_template: list) -> None:

    mocked_date.date.today.return_value = today_date
    assert outdated_products(products_template) == expired_list
