from unittest.mock import patch
import datetime
from app.main import outdated_products
MOCK_TODAY = datetime.date(2026, 6, 2)


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return MOCK_TODAY


@patch("app.main.datetime.date", MockDate)
def test_outdated_products_expired() -> None:
    products = [
        {"name": "Leite Vencido",
         "expiration_date": datetime.date(2026, 6, 1)},
        {"name": "Iogurte Vencido",
         "expiration_date": datetime.date(2026, 5, 20)}
    ]
    result = outdated_products(products)
    assert len(result) == 2
    assert result[0] == "Leite Vencido"
    assert result[1] == "Iogurte Vencido"


@patch("app.main.datetime.date", MockDate)
def test_expiration_day_yesterday_outdated() -> None:
    products = [
        {"name": "Produto de Ontem",
         "expiration_date": datetime.date(2026, 6, 1)}
    ]
    result = outdated_products(products)
    assert len(result) == 1, \
        "Product with expiration date equals yesterday is outdated."
    assert result[0] == "Produto de Ontem"


@patch("app.main.datetime.date", MockDate)
def test_outdated_products_within_shelf_life() -> None:
    products = [
        {"name": "Arroz Válido",
         "expiration_date": datetime.date(2026, 6, 10)}
    ]
    result = outdated_products(products)
    assert len(result) == 0


@patch("app.main.datetime.date", MockDate)
def test_expiration_day_today_not_outdated() -> None:
    products = [
        {"name": "Queijo de Hoje",
         "expiration_date": datetime.date(2026, 6, 2)}
    ]
    result = outdated_products(products)
    assert len(result) == 0, \
        "Product with expiration date equals today is not outdated."


@patch("app.main.datetime.date", MockDate)
def test_outdated_products_empty_list() -> None:
    products = []
    result = outdated_products(products)
    assert result == []
