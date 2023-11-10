import datetime
from app.main import outdated_products
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "products_list, expected_list", [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5)
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1)
                },
            ], ["duck"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_check_expiration_date(
        mocked_datetime: mock,
        products_list: list,
        expected_list: list
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products_list) == expected_list
