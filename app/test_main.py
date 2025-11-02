import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture
def products() -> list[dict]:
    return [
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
        }
    ]


@pytest.mark.parametrize(
    "tested_date, expected",
    [
        (
            datetime.date(2025, 11, 2),
            ["salmon", "chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 9),
            ["chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 4),
            ["duck"]
        ),
        (
            datetime.date(2022, 1, 1),
            []
        )
    ]
)
def test_outdated_products(products: list,
                           tested_date: datetime,
                           expected: list) -> None:
    with patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = tested_date
        assert outdated_products(products) == expected
