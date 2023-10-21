import pytest
import datetime

from app.main import outdated_products


@pytest.fixture
def mock_datetime_today(date: datetime.date,
                        monkeypatch: pytest.MonkeyPatch) -> None:
    class DatetimeMock(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return date

    monkeypatch.setattr(datetime, "date", DatetimeMock)


@pytest.mark.parametrize(
    "date, products, expected_output",
    [
        (
            datetime.date(2023, 10, 21),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 10, 21),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 10, 26),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2023, 10, 25),
                    "price": 160
                }
            ],
            [],
        ),
        (
            datetime.date(2023, 10, 21),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 10, 20),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 10, 15),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2023, 10, 25),
                    "price": 160
                }
            ],
            ["salmon", "chicken"],
        ),
        (
            datetime.date(2023, 10, 21),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 10, 26),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 10, 27),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2023, 10, 29),
                    "price": 160
                }
            ],
            [],
        ),
    ],
    ids=[
        "Expiration_date = today",
        "Expiration_date < today",
        "Expiration_date > today",
    ]
)
def test_outdated_products(date: datetime.date,
                           products: list,
                           expected_output: list,
                           mock_datetime_today: callable) -> None:
    assert outdated_products(products) == expected_output
