import pytest
from unittest.mock import patch
import datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, mock_today_date, expected_result",
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
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 160,
                },
            ],
            datetime.date(2022, 2, 2),
            ["chicken"],
        ),

    ],
    ids=[
        "1st case",
        "2nd case"
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products_with_mocked_today(mock_date: datetime.date,
                                             products: list,
                                             mock_today_date: datetime.date,
                                             expected_result: list) -> None:
    mock_date.today.return_value = mock_today_date
    result = outdated_products(products)
    assert result == expected_result
