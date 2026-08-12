import datetime
import pytest

from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, date, outdated",
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
            datetime.date(2022, 2, 2),
            [
                "duck"
            ]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            datetime.date(2022, 2, 2),
            [
                "duck"
            ]
        )
    ]
)
def test_outdated_products(
        products: list[dict],
        date: datetime,
        outdated: list[str]
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date
        assert outdated_products(products) == outdated
