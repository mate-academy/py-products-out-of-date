import pytest
import datetime
from _pytest.monkeypatch import MonkeyPatch

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, product, expected",
    [
        (
            datetime.date(2025, 10, 5),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 10, 4),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 10, 5),
                    "price": 160
                }
            ],
            [
                "salmon",
                "chicken"
            ]
        )
    ]
)
def test_outdated_products(
        monkeypatch: MonkeyPatch,
        today_date: datetime.date,
        product: list,
        expected: list

) -> None:

    class MockDate:

        @staticmethod
        def today() -> datetime.date:
            return today_date

    monkeypatch.setattr(
        "app.main.datetime.date", MockDate
    )

    assert outdated_products(product) == expected
