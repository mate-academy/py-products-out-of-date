import pytest
from unittest import mock
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, today, result",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 23),
                    "price": 600
                }
            ],
            datetime.date(2022, 2, 22),
            [],
            id="check valid date"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 22),
                    "price": 600
                }
            ],
            datetime.date(2022, 2, 22),
            [],
            id="check exp_date = today"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 21),
                    "price": 600
                }
            ],
            datetime.date(2022, 2, 22),
            ["salmon"],
            id="check expired"
        ),
        pytest.param(
            [
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2024, 4, 22),
                    "price": 600
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2024, 4, 27),
                    "price": 600
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2024, 7, 7),
                    "price": 600
                },
                {
                    "name": "soda",
                    "expiration_date": datetime.date(2020, 2, 21),
                    "price": 600
                },
            ],
            datetime.date(2024, 4, 24),
            ["bread", "soda"],
            id="check multiple products"
        ),
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_date: mock.Mock,
        products: list,
        today: datetime.date,
        result: list
) -> None:
    mocked_date.today.return_value = today
    assert outdated_products(products) == result


TODAY = datetime.date(2024, 4, 22)


@mock.patch("app.main.datetime.date")
def test_if_called(mocked_date: mock.Mock) -> None:
    mocked_date.today.return_value = TODAY
    outdated_products(
        [
            {
                "name": "bread",
                "expiration_date": TODAY,
                "price": 600
            }
        ]
    )
    mocked_date.today.assert_called_once()
