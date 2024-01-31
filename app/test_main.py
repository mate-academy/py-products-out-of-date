import pytest
import datetime
from typing import List
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture
def user_template() -> None:
    user_template = [
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
            "name": "it is a chicken right?",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 160
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    return user_template


def test_outdated_products(
        user_template: List[dict]
) -> None:
    date_today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date_today
        assert outdated_products(user_template) == ["duck"]
