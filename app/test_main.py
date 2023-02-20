import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products() -> None:
    today = datetime.date.today()
    products = [
        {"name": "salmon",
         "expiration_date": today - datetime.timedelta(days=1)},
        {"name": "chicken",
         "expiration_date": today - datetime.timedelta(days=2)},
        {"name": "duck",
         "expiration_date": today + datetime.timedelta(days=1)},
        {"name": "fresh_duck",
         "expiration_date": today}
    ]

    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today
        outdated = outdated_products(products)

        assert len(outdated) == 2
        assert "salmon" in outdated
        assert "chicken" in outdated
