from .main import outdated_products
import pytest
import datetime
from unittest import mock


@pytest.mark.parametrize(
    "argument, mock_today, expected",
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
                },
                {
                    "name": "goose",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 500
                },
            ],
            datetime.date(2022, 2, 2), ["duck"]
        )
    ]
)
def test_outdated_products(
        argument: list,
        mock_today: datetime,
        expected: list
) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime:
            return mock_today

    with mock.patch("app.main.datetime.date", MockDate):
        assert outdated_products(argument) == expected
