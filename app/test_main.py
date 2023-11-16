import pytest
from unittest import mock
from datetime import date

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_result, my_today",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"],
            date(2022, 2, 2)
        )
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
    mocked_date_today: mock.MagicMock,
    products: list[dict],
    expected_result: list[str],
    my_today: date
) -> None:
    mocked_date_today.today.return_value = my_today
    result = outdated_products(products)
    assert result == expected_result
