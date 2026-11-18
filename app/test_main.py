import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected",
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
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 40,
                },
            ],
            [],
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 30,
                },
            ],
            ["bread"],
        ),
        (
            datetime.date(2025, 5, 10),
            [
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2025, 5, 9),
                    "price": 100,
                },
                {
                    "name": "yogurt",
                    "expiration_date": datetime.date(2025, 5, 10),
                    "price": 50,
                },
                {
                    "name": "juice",
                    "expiration_date": datetime.date(2025, 5, 11),
                    "price": 70,
                },
            ],
            ["cheese"],
        ),
        (
            datetime.date(2022, 2, 2),
            [],
            [],
        ),
    ],
)
def test_outdated_products(
    monkeypatch: pytest.MonkeyPatch,
    today: datetime.date,
    products: list,
    expected: list,
) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return today

    monkeypatch.setattr("app.main.datetime.date", MockDate)

    assert outdated_products(products) == expected
