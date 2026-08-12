import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,today_date,result",
    [
        pytest.param(
            [
                {
                    "name": "chicken leg",
                    "expiration_date": datetime.date(2020, 2, 2),
                    "price": 120
                },
                {
                    "name": "pork pate",
                    "expiration_date": datetime.date(2024, 3, 7),
                    "price": 80
                }
            ],
            datetime.date(2023, 1, 2),
            ["chicken leg"],
            id="One expired other not"
        ),
        pytest.param(
            [
                {
                    "name": "Pig's ears",
                    "expiration_date": datetime.date(2019, 9, 2),
                    "price": 30
                },
                {
                    "name": "Chocolate `Roshen`",
                    "expiration_date": datetime.date(2018, 5, 4),
                    "price": 18
                }
            ],
            datetime.date(2020, 2, 2),
            ["Pig's ears", "Chocolate `Roshen`"],
            id="All products has expired"
        ),
        pytest.param(
            [
                {
                    "name": "Jelly candy `Shalena bdzhilka",
                    "expiration_date": datetime.date(2025, 5, 27),
                    "price": 8
                },
                {
                    "name": "Beer `Obolon`",
                    "expiration_date": datetime.date(2024, 7, 24),
                    "price": 15
                },
                {
                    "name": "Icecream 'Khreshchatyk",
                    "expiration_date": datetime.date(2023, 3, 4),
                    "price": 12
                }
            ],
            datetime.date(2020, 2, 17),
            [],
            id="All products have not expired"
        )
    ]
)
@mock.patch("app.main.datetime")
def test_different_correct_products_expiration_date(
        mocked_date_now: object,
        products: list[dict],
        today_date: datetime.date,
        result: list[str]
) -> None:
    mocked_date_now.date.today.return_value = today_date
    assert (
        outdated_products(products) == result
    ), f"List of expired product's should be equal to: {result}"
