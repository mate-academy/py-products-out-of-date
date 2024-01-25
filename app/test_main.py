import pytest
from unittest import mock
from app.main import outdated_products
import datetime


@pytest.mark.parametrize(
    "now_data,list_product,value_return",
    [
        (
            datetime.date(2022, 2, 5),
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
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 8),
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
            ["chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 11),
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
            ["salmon", "chicken", "duck"]
        ),
    ]
)
@mock.patch("datetime.date")
def test_out_of_date(mock_today: mock.MagicMock,
                     now_data: datetime,
                     list_product: list,
                     value_return: list) -> None:
    mock_today.today.return_value = now_data
    assert outdated_products(list_product) == value_return
