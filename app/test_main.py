import datetime
from unittest.mock import patch

from app.main import outdated_products


class MockDate(datetime.date):
    _mock_today: datetime.date

    @classmethod
    def today(cls) -> datetime.date:
        return cls._mock_today


@patch("datetime.date", MockDate)
def test_outdated_products_edge_cases() -> None:
    MockDate._mock_today = datetime.date(2022, 2, 15)

    products = [
        {
            "name": "venceu_ontem",
            "expiration_date": datetime.date(2022, 2, 14),
            "price": 100,
        },
        {
            "name": "vence_hoje",
            "expiration_date": datetime.date(2022, 2, 15),
            "price": 100,
        },
        {
            "name": "vence_amanha",
            "expiration_date": datetime.date(2022, 2, 16),
            "price": 100,
        },
    ]

    result = outdated_products(products)

    assert "venceu_ontem" in result
    assert "vence_hoje" not in result
    assert "vence_amanha" not in result
