import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize("test_input, expected", [
    (
        [
            {
                "name": "losos",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 600
            }
        ],
        ["losos"]
    ),

    (
        [
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 3),
                "price": 160
            }
        ],
        []
    ),
    (
        [],
        []
    ),
    (
        [
            {
                "name": "meat",
                "expiration_date": datetime.date(2022, 2, 2,),
                "price": 250
            }
        ],
        []
    )
])
def test_outdated_products(test_input: list, expected: list) -> None:
    mock_today_date = datetime.date(2022, 2, 2)

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = mock_today_date
        assert outdated_products(test_input) == expected
