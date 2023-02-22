import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "test_date,products,expected_outdated",
    [
        (
            datetime.date(2023, 2, 22),
            [
                {
                    "name": "Product A",
                    "expiration_date": datetime.date(2023, 2, 22),
                    "price": 500
                },
                {
                    "name": "Product B",
                    "expiration_date": datetime.date(2023, 2, 23),
                    "price": 400
                },
                {
                    "name": "Product C",
                    "expiration_date": datetime.date(2023, 2, 24),
                    "price": 300
                },
            ],
            [],
        ),
        (
            datetime.date(2023, 2, 22),
            [
                {
                    "name": "Product X",
                    "expiration_date": datetime.date(2023, 2, 21),
                    "price": 200
                },
                {
                    "name": "Product Y",
                    "expiration_date": datetime.date(2022, 5, 24),
                    "price": 100
                },
                {
                    "name": "Product Z",
                    "expiration_date": datetime.date(2021, 12, 31),
                    "price": 50
                },
            ],
            ["Product X", "Product Y", "Product Z"],
        ),
    ],
    ids=["not-outdated", "outdated"],
)
def test_outdated_products(
        test_date: datetime.date,
        products: list,
        expected_outdated: list
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = test_date
        assert outdated_products(products) == expected_outdated
