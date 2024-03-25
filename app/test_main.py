import pytest
from datetime import date
from unittest.mock import Mock, patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, products, expected_outdated",
    [
        (date(2022, 2, 2),
         [
             {
                 "name": "salmon",
                 "expiration_date": date(2022, 2, 10),
                 "price": 600
             },
             {
                 "name": "chicken",
                 "expiration_date": date(2022, 2, 5),
                 "price": 120
             },
             {
                 "name": "duck",
                 "expiration_date": date(2022, 2, 1),
                 "price": 160
             }],
         ["duck"]
         ),
        (date(2022, 2, 2),
         [
             {
                 "name": "salmon",
                 "expiration_date": date(2022, 2, 10),
                 "price": 600
             },
             {
                 "name": "chicken",
                 "expiration_date": date(2022, 2, 5),
                 "price": 120
             },
             {
                 "name": "duck",
                 "expiration_date": date(2022, 2, 15),
                 "price": 160
             }],
         []
         )
    ]
)
@patch("app.main.datetime")
def test_outdated_products(
        mock_datetime: Mock,
        today_date: date,
        products: list[dict],
        expected_outdated: list
) -> None:
    mock_datetime.date.today.return_value = today_date
    assert outdated_products(products) == expected_outdated
