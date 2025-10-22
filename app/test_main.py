import datetime
from unittest.mock import patch
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, products, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 1),
            [
                {
                    "name": "apple",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 20,
                },
                {
                    "name": "banana",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 15,
                },
            ],
            [],
        ),
        (
            datetime.date(2022, 2, 10),
            [
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 2, 8),
                    "price": 30,
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 2, 9),
                    "price": 50,
                },
            ],
            ["milk", "cheese"],
        ),
        # --- продукт з датою сьогодні ---
        (
            datetime.date(2022, 2, 5),
            [
                {
                    "name": "yogurt",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 10,
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 2, 4),
                    "price": 5,
                },
            ],
            ["bread"],
        ),
    ],
)
def test_outdated_products(
    today_date: datetime.date,
    products: list[dict],
    expected: list[str],
) -> None:
    """
    Test outdated_products function using mocked current date.
    Ensures that only products with expiration_date < today are returned.
    """
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(
            *args, **kwargs
        )
        result: list[str] = outdated_products(products)
        assert result == expected


def test_empty_list() -> None:
    """Test that function returns empty list when no products provided."""
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 1, 1)
        result: list[str] = outdated_products([])
        assert result == []
