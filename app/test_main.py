from app.main import outdated_products
import datetime
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "today_date,products,expected",
    [
        (
            datetime.date(2022, 2, 1),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ], []
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ], ["duck"]
        ),

        (datetime.date(2022, 2, 1), [], [])
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: mock.MagicMock,
        today_date: datetime.date,
        products: list,
        expected: list
) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(products) == expected
