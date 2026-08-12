import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
    ]


@pytest.mark.parametrize(
    "date_today,expected_list",
    [
        pytest.param(
            datetime.date(2022, 2, 9), ["chicken", "duck"]
        ),
        pytest.param(
            datetime.date(2022, 2, 10), ["chicken", "duck"]
        ),
        pytest.param(
            datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]
        ),
        pytest.param(
            datetime.date(2022, 1, 30), []
        ),
    ],
    ids=[
        "today < expiration date",
        "today = expiration date",
        "today > expiration date",
        "all products outdate"
    ],
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
    mocked_date: mock,
    products_template: list,
    date_today: datetime.date,
    expected_list: list,
) -> None:
    mocked_date.today.return_value = date_today
    products = outdated_products(products_template)
    assert products == expected_list
