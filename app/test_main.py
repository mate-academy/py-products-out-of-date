import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize("products, expected_result", [
    (
        [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1),
             "price": 160}
        ],
        ["duck"]
    ),
])
def test_outdated_products(
        products: list[dict],
        expected_result: list[str]
) -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == expected_result
