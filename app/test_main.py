import pytest
from pytest import MonkeyPatch
from app.main import outdated_products
import datetime


@pytest.mark.parametrize(
    "products,date,expected_result",
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
            datetime.date(2022, 2, 2),
            ["duck"]
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
            datetime.date(2022, 2, 10),
            ["chicken", "duck"]
        ),
    ]
)
def test_outdated_products(
        monkeypatch: MonkeyPatch,
        products: dict,
        date: datetime.date,
        expected_result: bool
) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return date

    monkeypatch.setattr(datetime, "date", MockDate)
    assert (
        outdated_products(products) == expected_result
    ), "Invalid products selected"
