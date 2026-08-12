import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_return_list",
    [
        (
            [
                {
                    "name": "salomon",
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
        )
    ]
)
@mock.patch("app.main.datetime")
def test_should_return_correct_result(mock_datetime: mock,
                                      products: list,
                                      expected_return_list: list) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected_return_list
