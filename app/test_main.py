import datetime
from datetime import date
from unittest.mock import patch

from app.main import outdated_products


def test_outdated_products() -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        assert datetime.date.today() == date(2022, 2, 2)
        assert outdated_products([
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
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 155
            },
            {
                "name": "duck_2",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]) == ["duck_2"]

        assert outdated_products([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 1, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 1, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 1, 1),
                "price": 160
            }
        ]) == ["salmon", "chicken", "duck"]

        assert outdated_products([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 8),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 160
            }
        ]) == []
