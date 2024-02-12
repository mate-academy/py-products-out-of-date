import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,expected_result,today",
    [
        (
            [
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
            ],
            ["duck"],
            datetime.date(2022, 2, 2)
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_date: mock.MagicMock,
        products: list,
        expected_result: list,
        today: datetime.date
) -> None:
    mocked_date.date.today.return_value = today
    assert outdated_products(products) == expected_result
