import datetime
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.fixture()
def mocked_datetime() -> mock:
    with mock.patch("app.main.datetime") as date:
        yield date


@pytest.mark.parametrize(
    "products, result",
    [
        ([
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
        ], ["duck"])
    ]
)
def test_should_return_correct_answer(
        products: list,
        result: list,
        mocked_datetime: mock
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == result
