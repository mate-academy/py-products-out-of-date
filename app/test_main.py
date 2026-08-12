from app.main import outdated_products

import datetime

from unittest.mock import patch

test_date = [
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
]


def test_should_return_correct_list() -> None:
    with patch("app.main.datetime") as mocked_date_class:
        mocked_date_class.date.today.return_value = datetime.date(2022, 2, 5)
        assert outdated_products(test_date) == ["duck"]
