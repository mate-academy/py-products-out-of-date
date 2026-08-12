import datetime
from unittest import mock
from app.main import outdated_products

product_list = [
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


def test_should_return_expired_products() -> None:
    test_today = datetime.date(2025, 10, 13)

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = test_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(
            *args, **kwargs)
        assert outdated_products(product_list) == ["salmon", "chicken", "duck"]


def test_should_not_return_products_when_expired_today() -> None:
    test_today = datetime.date(2022, 2, 10)

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = test_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(
            *args, **kwargs)
        assert outdated_products(product_list) == ["chicken", "duck"]


def test_should_return_products_when_expired_yesterday() -> None:
    test_today = datetime.date(2022, 2, 2)
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = test_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(
            *args, **kwargs)
        assert outdated_products(product_list) == ["duck"]
