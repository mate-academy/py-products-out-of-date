import pytest
import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products

real_dat = datetime.date


@pytest.mark.parametrize(
    "products, test_date, expected",
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
            (2022, 2, 6),
            ["chicken", "duck"],
            id="outdated chicken duck"
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
            (2022, 2, 5),
            ["duck"],
            id="outdated only duck"
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
            (2022, 1, 12),
            [],
            id="no one are outdated"
        ),
        pytest.param(
            [],
            (2022, 1, 12),
            [],
            id="products are empty"
        )
    ]
)
@patch("app.main.datetime.date")
def test_main(
        mocked_date: MagicMock,
        products: list,
        test_date: tuple,
        expected: list
) -> None:
    mocked_date.today.return_value = real_dat(*test_date)
    mocked_date.side_effect = lambda *args, **kwargs: real_dat(*args, **kwargs)
    assert outdated_products(products) == expected
