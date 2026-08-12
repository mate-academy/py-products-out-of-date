import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, date, result",
    [
        (
            [
                {
                    "name": "fat",
                    "expiration_date": datetime.date.today(),
                    "price": 600,
                }
            ],
            datetime.date.today(),
            [],
        ),
        (
            [
                {
                    "name": "orange",
                    "expiration_date": datetime.date.today()
                    - datetime.timedelta(days=1),
                    "price": 600,
                }
            ],
            datetime.date.today(),
            ["orange"],
        ),
    ],
)
def test_outdated_products(
    products: list, date: "datetime", result: str
) -> None:
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr("datetime.datetime", lambda args: date)
    assert outdated_products(products) == result
