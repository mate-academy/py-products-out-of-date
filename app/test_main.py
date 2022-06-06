import pytest
from unittest import mock
import datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    "product,ans",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                }
            ],
            []
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                }
            ],
            []
        ),
        pytest.param(
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked, product, ans):
    mocked.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product) == ans
