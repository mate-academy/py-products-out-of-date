import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,today_date,expected_result",
    [
        (
            [
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
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
        ),
        (
            [
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
            ],
            datetime.date(2022, 2, 1),
            [],
        ),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(
    mocked_datetime_date: datetime.date,
    products: list,
    today_date: datetime.date,
    expected_result: list,
) -> None:

    mocked_datetime_date.today.return_value = today_date
    result = outdated_products(products)
    assert result == expected_result
