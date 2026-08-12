import datetime
import pytest

from app.main import outdated_products


@pytest.fixture
def products() -> list:
    return [
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


@pytest.mark.parametrize(
    "today_date,expected",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 20), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"])
    ],
    ids=[
        "only-duck-expired",
        "no-product-expired",
        "all-expired",
        "chicken-duck-expired"
    ]
)
def test_outdated_products(
    monkeypatch: pytest.MonkeyPatch,
    products: list,
    today_date: datetime.date,
    expected: list
) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return today_date

    monkeypatch.setattr(datetime, "date", FakeDate)
    result = outdated_products(products)
    assert result == expected
