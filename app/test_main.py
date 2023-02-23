import datetime
import pytest
from unittest import mock
from app.main import outdated_products

test_list_products = [
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
    "products_test, today_test, expected",
    [
        pytest.param(
            test_list_products,
            datetime.date(2022, 2, 1),
            [],
            id="test expiration date for product is today",
        ),
        pytest.param(
            test_list_products,
            datetime.date(2022, 2, 3),
            ["duck"],
            id="test expiration date for product was few day ago for one item",
        ),
        pytest.param(
            test_list_products,
            datetime.date(2022, 2, 7),
            ["chicken", "duck"],
            id="test expiration date for product was  ago for two item",
        ),
        pytest.param(
            test_list_products,
            datetime.date(2022, 10, 1),
            ["salmon", "chicken", "duck"],
            id="test expiration date for all product was long time ago  ago ",
        ),
    ],
)
def test_outdated_products(
    products_test: list, today_test: datetime, expected: list
) -> bool:
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = today_test
        assert outdated_products(products_test) == expected
