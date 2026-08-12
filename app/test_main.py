from unittest import mock
import pytest
import datetime

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
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
    "datetime_return_value, result",
    [
        (datetime.date(2022, 2, 2), ["duck"])
    ]
)
@mock.patch("datetime.date")
def test_product_with_expiration_date(
        mocked_datetime: datetime.date,
        datetime_return_value: datetime.date,
        products: list,
        result: list
) -> None:
    mocked_datetime.today.return_value = datetime_return_value
    assert outdated_products(products) == result
