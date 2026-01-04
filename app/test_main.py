import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
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
                },
            ],
            [
                "salmon", "chicken", "duck"
            ]
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
                    "expiration_date": datetime.date(2022, 2, 20),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            [
                "salmon", "duck"
            ]
        ),
        (
            [
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 2, 14),
                    "price": 20
                },
                {
                    "name": "egg",
                    "expiration_date": datetime.date(2022, 2, 15),
                    "price": 10
                },
            ],
            [
                "milk"
            ]
        ),
        (
            [
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 2, 20),
                    "price": 50
                },
                {
                    "name": "butter",
                    "expiration_date": datetime.date(2022, 2, 25),
                    "price": 60
                },
            ],
            []
        )
    ]
)
def test_outdated_products(
        monkeypatch: pytest.MonkeyPatch,
        products: list[dict],
        expected: list
) -> None:

    class MyDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 15)

    monkeypatch.setattr("app.main.datetime.date", MyDate)
    assert outdated_products(products) == expected
