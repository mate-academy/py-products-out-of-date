import pytest
import datetime
from unittest.mock import patch, Mock
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
    "datetime_return_value, expected_result",
    [
        (
            datetime.date(2022, 2, 3), ["duck"]
        )
    ]
)
@patch("app.main.datetime")
def test_outdated_products(
        mocked_datetime: Mock,
        datetime_return_value: datetime.date,
        expected_result: list,
        products: list
) -> None:
    mocked_datetime.date.today.return_value = datetime_return_value
    assert outdated_products(products) == expected_result
