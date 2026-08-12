import datetime
from unittest.mock import patch
from app.main import outdated_products

template = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 2),  # Expiring today
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 1),  # Expired yesterday
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 3),  # Expiring tomorrow
        "price": 160
    },
]


def test_outdated_products() -> None:
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

        assert "chicken" in outdated_products(template)

        assert "salmon" not in outdated_products(template)

        assert "duck" not in outdated_products(template)
