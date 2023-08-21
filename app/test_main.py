from typing import List

import pytest
from unittest.mock import patch
import datetime
import app.main as main


@pytest.mark.parametrize(
    "mock_today, input_list, output_list",
    [
        pytest.param(
            datetime.date(2022, 2, 2),
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
            id="test past: 2 February 2022",
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
            [],
            [],
            id="test empty input list",
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "tomato",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 70,
                },
                {
                    "name": "lettuce",
                    "expiration_date": datetime.date(2022, 3, 1),
                    "price": 40,
                },
            ],
            [],
            id="test future: 2 February 2022",
        ),
    ],
)
def test_main(
    mock_today: datetime.date, input_list: List[dict], output_list: List[str]
) -> None:
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = mock_today
        assert main.outdated_products(input_list) == output_list
