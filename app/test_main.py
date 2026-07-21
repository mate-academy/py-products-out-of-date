import datetime
from unittest.mock import patch
from app.main import outdated_products


class MockDate(datetime.date):
    """Mock date class to replace datetime.date in tests."""

    @classmethod
    def today(cls) -> datetime.date:
        return cls._today

    @classmethod
    def set_today(cls, date: datetime.date) -> None:
        cls._today = date


class TestOutdatedProducts:
    """Test cases for the outdated_products function."""

    def test_outdated_products_basic_case(self) -> None:
        """Test basic case with some outdated products."""
        mock_today = datetime.date(2022, 2, 2)

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

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products(products)

        assert result == ["duck"]

    def test_outdated_products_all_expired(self) -> None:
        """Test when all products are expired."""
        mock_today = datetime.date(2022, 2, 15)

        products = [
            {
                "name": "milk",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 50
            },
            {
                "name": "bread",
                "expiration_date": datetime.date(2022, 2, 12),
                "price": 30
            },
            {
                "name": "eggs",
                "expiration_date": datetime.date(2022, 2, 14),
                "price": 80
            }
        ]

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products(products)

        assert result == ["milk", "bread", "eggs"]

    def test_outdated_products_none_expired(self) -> None:
        """Test when no products are expired."""
        mock_today = datetime.date(2022, 2, 1)

        products = [
            {
                "name": "cheese",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 200
            },
            {
                "name": "yogurt",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 60
            }
        ]

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products(products)

        assert result == []

    def test_outdated_products_expire_today(self) -> None:
        """Test products that expire exactly today.
        Should not be considered outdated.
        """
        mock_today = datetime.date(2022, 2, 5)

        products = [
            {
                "name": "butter",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "cream",
                "expiration_date": datetime.date(2022, 2, 4),
                "price": 80
            },
            {
                "name": "juice",
                "expiration_date": datetime.date(2022, 2, 6),
                "price": 100
            }
        ]

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products(products)

        assert result == ["cream"]

    def test_outdated_products_empty_list(self) -> None:
        """Test with empty products list."""
        mock_today = datetime.date(2022, 2, 1)

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products([])

        assert result == []

    def test_outdated_products_mixed_dates(self) -> None:
        """Test with a mix of dates from different years and months."""
        mock_today = datetime.date(2022, 6, 15)

        products = [
            {
                "name": "old_product",
                "expiration_date": datetime.date(2021, 12, 31),
                "price": 100
            },
            {
                "name": "recent_expired",
                "expiration_date": datetime.date(2022, 6, 10),
                "price": 150
            },
            {
                "name": "future_product",
                "expiration_date": datetime.date(2023, 1, 1),
                "price": 200
            },
            {
                "name": "next_month",
                "expiration_date": datetime.date(2022, 7, 1),
                "price": 75
            }
        ]

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products(products)

        assert result == ["old_product", "recent_expired"]

    def test_outdated_products_single_expired_item(self) -> None:
        """Test with a single expired product."""
        mock_today = datetime.date(2022, 3, 1)

        products = [
            {
                "name": "expired_item",
                "expiration_date": datetime.date(2022, 2, 28),
                "price": 50
            }
        ]

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products(products)

        assert result == ["expired_item"]

    def test_outdated_products_single_fresh_item(self) -> None:
        """Test with a single fresh product."""
        mock_today = datetime.date(2022, 2, 1)

        products = [
            {
                "name": "fresh_item",
                "expiration_date": datetime.date(2022, 2, 28),
                "price": 50
            }
        ]

        with patch("app.main.datetime.date", MockDate):
            MockDate.set_today(mock_today)
            result = outdated_products(products)

        assert result == []
