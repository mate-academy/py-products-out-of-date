import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products_returns_empty_list_when_no_products() -> None:
    fixed_today = datetime.date(2025, 1, 1)

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.side = lambda *args, **kwargs: datetime.date(*args, **kwargs)
        mock_date.today.return_value = fixed_today

        result = outdated_products([])
        assert result == []


def test_outdated_products_filters_correctly() -> None:
    products = [
        {"name": "Milk", "expiration_date": datetime.date(2024, 12, 31)},
        {"name": "Cheese", "expiration_date": datetime.date(2025, 1, 2)},
        {"name": "Bread", "expiration_date": datetime.date(2025, 1, 1)},
    ]
    fixed_today = datetime.date(2025, 1, 1)

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.side = lambda *args, **kwargs: datetime.date(*args, **kwargs)
        mock_date.today.return_value = fixed_today

        result = outdated_products(products)
        assert result == ["Milk"]


def test_outdated_products_multiple_outdated() -> None:
    products = [
        {"name": "Eggs", "expiration_date": datetime.date(2024, 12, 30)},
        {"name": "Yogurt", "expiration_date": datetime.date(2024, 12, 15)},
        {"name": "Juice", "expiration_date": datetime.date(2025, 1, 5)},
    ]
    fixed_today = datetime.date(2025, 1, 1)

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.side = lambda *args, **kwargs: datetime.date(*args, **kwargs)
        mock_date.today.return_value = fixed_today

        result = outdated_products(products)
        assert set(result) == {"Eggs", "Yogurt"}
