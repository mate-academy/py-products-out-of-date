from app.main import outdated_products
from unittest import mock
import datetime


def test_outdated_products() -> None:
    with mock.patch("datetime.date.today") as mock_datetime:
        mock_datetime.return_value = datetime.date(2022, 2, 1)
        assert outdated_products(outdated_products([
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
        ])

        ) == ["duck"]
