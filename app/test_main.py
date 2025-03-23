import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,today_date,result",
    [
        pytest.param(
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
            datetime.date(2025, 2, 1),
            ["salmon", "chicken", "duck"],
            id="test everything is outdated"
        ),
        pytest.param(
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
            datetime.date(1200, 2, 1),
            [],
            id="test nothing is outdated"
        ),
        pytest.param(
            [],
            datetime.date(2025, 2, 1),
            [],
            id="test empty produc list"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                }
            ],
            datetime.date(2022, 2, 11),
            ["salmon"],
            id="test yesteday's product is outdated"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                }
            ],
            datetime.date(2022, 2, 9),
            [],
            id="test tomorrow's product is not outdated"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 9),
                    "price": 600
                }
            ],
            datetime.date(2022, 2, 9),
            [],
            id="test today's product is not outdated"
        ),
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_date: mock.MagicMock,
        products: list[dict],
        today_date: datetime.date,
        result: list) -> None:
    mocked_date.today.return_value = today_date
    assert outdated_products(products) == result


@pytest.mark.parametrize(
    "products,error",
    [
        pytest.param(
            [
                {
                    "expiration_date": datetime.date(2022, 2, 9),
                    "price": 600
                }
            ],
            KeyError,
            id="test key name in not in the product's dict"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "price": 600
                }
            ],
            KeyError,
            id="test key expiration_date in not in the product's dict"
        ),
    ]
)
def test_outdated_products_errors(
        products: list[dict],
        error: Exception) -> None:
    with pytest.raises(error):
        outdated_products(products)
