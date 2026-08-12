import pytest
import datetime
import app.main
from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
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


def test_outdated_products(monkeypatch: pytest.MonkeyPatch,
                           products: list[dict]) -> None:
    def mock_get_today() -> datetime.date:
        return datetime.date(2022, 2, 2)

    monkeypatch.setattr(app.main, "get_today", mock_get_today)
    assert outdated_products(products) == ["duck"]
