import pytest
import datetime
from app.main import outdated_products
from unittest.mock import patch


@pytest.fixture()
def product_list() -> list:
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


@pytest.mark.parametrize(
    "date_today, expected_result", [
        (datetime.date(2022, 1, 1), []),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 15), ["salmon", "chicken", "duck"])
    ]
)
def test_return_list_with_expected_data(
        date_today: datetime.date,
        expected_result: list,
        product_list: list
) -> None:
    with patch("app.main.datetime") as mocked_function:
        mocked_function.date.today.return_value = date_today
        assert outdated_products(product_list) == expected_result
