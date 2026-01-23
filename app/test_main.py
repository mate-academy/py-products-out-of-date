import pytest
import datetime
from unittest import mock

from app.main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    }
]


@pytest.mark.parametrize(
    "expected_result,today_date",
    [
        pytest.param(
            ["salmon"],
            datetime.date(2022, 2, 11),
            id="there is outdated product"
        ),
        pytest.param(
            [],
            datetime.date(2022, 2, 10),
            id="there is no outdated products"
        ),
    ],
)
def test_function_results(
    expected_result: list,
    today_date: datetime.date
) -> None:
    with mock.patch("app.main.datetime.date") as func:
        func.today = lambda: today_date
        print(today_date)
        assert outdated_products(products) == expected_result
