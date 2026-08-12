import pytest
from app.main import outdated_products
from unittest.mock import patch
import datetime


@pytest.mark.parametrize(
    "today_date, products, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 400},
            ],
            ["salmon"]
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "milk",
                 "expiration_date": datetime.date(2022, 2, 2),
                 "price": 50},
            ],
            [],
        )
    ]
)
def test_outdated_products(today_date: any,
                           products: list,
                           expected: list) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        mock_date.side_effect = datetime.date

        result = outdated_products(products)

    assert result == expected
