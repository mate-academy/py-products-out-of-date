import pytest
import datetime

from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
    yield [
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
    "expected_result, date",
    [
        ([], datetime.date(2022, 1, 30)),
        ([], datetime.date(2022, 2, 1)),
        (
            ["duck"],
            datetime.date(2022, 2, 2),
        ),
        (["salmon", "chicken", "duck"], datetime.date(2022, 2, 11)),
    ],
)
def test_product_checker(
    expected_result: list, date: datetime, products: list[dict]
) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = date
        assert outdated_products(products) == expected_result
