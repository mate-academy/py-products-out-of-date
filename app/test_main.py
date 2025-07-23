import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,expected_result",
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(
        monkeypatch: pytest.MonkeyPatch,
        products: list,
        expected_result: list
) -> None:
    class MyDate(datetime.date):
        @classmethod
        def today(cls) -> datetime:
            return datetime.date(2022, 2, 2)
    monkeypatch.setattr(datetime, "date", MyDate)
    assert outdated_products(products) == expected_result
