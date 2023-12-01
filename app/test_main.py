import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products() -> None:
    today_date = datetime.date(2022, 2, 2)

    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today_date

        products = [
            {"name": "Salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600
             },
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120
             },
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1),
             "price": 160
             }
        ]

        result = outdated_products(products)

        assert result == ["duck"]
