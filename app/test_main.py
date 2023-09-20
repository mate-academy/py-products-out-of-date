import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize("test_input, expected", [
    (
            [
                {
                    "name": "лосось",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600
                }
            ],
            ['лосось']
    ),

    (
            [
                {
                    "name": "утка",
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
                    "name": "говядина",
                    "expiration_date": datetime.date(2022, 2, 2,),
                    "price": 250
                }
            ],
            []
    )
])
def test_outdated_products(test_input, expected):
    mock_today_date = datetime.date(2022, 2, 2)

    with patch('app.main.datetime.date') as mock_date:
        mock_date.today.return_value = mock_today_date
        assert outdated_products(test_input) == expected
