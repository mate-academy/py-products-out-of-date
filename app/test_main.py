"""Tests for the outdated_products function."""
import pytest
from datetime import date
from typing import Generator
from app.main import outdated_products


@pytest.fixture(name="products")
def fix_products() -> Generator[list[dict[str, str | date | int]], None, None]:
    """Fixture providing a list of test products."""
    yield [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "today, expected",
    [
        (date(2022, 2, 10), ["chicken", "duck"]),
        (date(2022, 2, 5), ["duck"]),
        (date(2022, 2, 1), []),
    ]
)
def test_outdated_products(
    products: Generator[dict[str, str | date | int], None, None],
    today: date,
    expected: list[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test the outdated_products function."""

    class MockDate:
        """Mocked date class for deterministic testing."""

        @staticmethod
        def today() -> date:
            """Return the mocked current date for tests.

            This method is used to replace datetime.date.today during
            testing so that results are deterministic.
            """
            return today

        @staticmethod
        def fromtimestamp(timestamp: int) -> date:
            """Return a date corresponding to a POSIX timestamp.

            This docstring satisfies linters that require function
            documentation in tests.
            """
            return date.fromtimestamp(timestamp)

    class MockDatetime:
        """Mocked datetime class for deterministic testing."""
        date = MockDate

    monkeypatch.setattr("app.main.datetime", MockDatetime)
    assert outdated_products(products) == expected
