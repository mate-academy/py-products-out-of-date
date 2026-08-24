import datetime
from unittest.mock import Mock

import pytest
from app import main


@pytest.mark.parametrize(
    "products,correct_output",
    [
        pytest.param(
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
            id="test: yesterday is outdated"
        ),
        pytest.param(
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 160,
                },
            ],
            [],
            id="test: today is not outdated"
        ),
    ],
)
def test_date_yesterday(
        products: list[dict],
        correct_output: list,
        monkeypatch: callable
) -> None:
    mock_date = Mock()
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)
    monkeypatch.setattr(main, "datetime", mock_date)
    assert main.outdated_products(products) == correct_output
