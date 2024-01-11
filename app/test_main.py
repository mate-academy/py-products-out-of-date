import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, input_products, expected_result",
    [
        (
            datetime.date(2022, 2, 2),
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
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "tomato",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 600,
                },
                {
                    "name": "mayo",
                    "expiration_date": datetime.date(2022, 1, 5),
                    "price": 120,
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 1, 29),
                    "price": 160,
                },
            ],
            ["mayo", "bread"],
        ),
    ],
)
def test_outdated_product(
    today_date: datetime.date, input_products: list, expected_result: list
) -> None:
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today_date
        assert outdated_products(input_products) == expected_result
