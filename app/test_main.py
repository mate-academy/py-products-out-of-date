import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, year, month, day, expected_result",
    [
        (
            [
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
            ],
            2023,
            4,
            1,
            ["salmon", "chicken", "duck"],
        ),
        (
            [
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
            ],
            2022,
            2,
            2,
            ["duck"],
        ),
        (
            [
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
            ],
            2022,
            2,
            1,
            [],
        )
    ]
)
def test_outdated_products(
        monkeypatch: monkeypatch,
        products: list,
        year: int,
        month: int,
        day: int,
        expected_result: list
) -> None:

    new_date = datetime.date

    class FakeToday:
        @classmethod
        def today(cls) -> datetime.date:
            return new_date(year, month, day)

    monkeypatch.setattr(datetime, "date", FakeToday)
    assert outdated_products(products) == expected_result
