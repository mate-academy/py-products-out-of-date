import datetime
from unittest import mock
import pytest
from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
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

    with mock.patch("app.main.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == ["duck"]

        mock_date.today.return_value = datetime.date(2022, 2, 6)
        assert outdated_products(products) == ["chicken", "duck"]

        mock_date.today.return_value = datetime.date(2022, 2, 11)
        assert outdated_products(products) == ["salmon", "chicken", "duck"]

        mock_date.today.return_value = datetime.date(2022, 1, 30)
        assert outdated_products(products) == []


if __name__ == "__main__":
    pytest.main()
