import pytest
from app.main import outdated_products
from datetime import date
from unittest import mock


@pytest.mark.parametrize(
    "initial_data, expected_result",
    [
        pytest.param(
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
                }
            ],
            ["duck"],
            id="should return list of products out of date"
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime: mock.MagicMock,
                           initial_data: list,
                           expected_result: list
                           ) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 2)
    assert outdated_products(initial_data) == expected_result
