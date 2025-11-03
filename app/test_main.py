import datetime
from typing import List, Dict, Any
from unittest import mock
from app.main import outdated_products


class FixedDate(datetime.date):
    """Subclasse de datetime.date que permite fixar o retorno de today()."""

    @classmethod
    def today(cls) -> datetime.date:
        """Sobrescreve datetime.date.today() para retornar uma data fixa."""
        return cls(2022, 2, 2)


def test_one_product_expired() -> None:
    """Deve retornar apenas o produto vencido."""
    with mock.patch("datetime.date", FixedDate):
        products: List[Dict[str, Any]] = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600,
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120,
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160,
            },
        ]
        result = outdated_products(products)
        assert result == ["duck"]


def test_no_products_expired() -> None:
    """Nenhum produto deve ser considerado vencido."""

    class FixedDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 1)

    with mock.patch("datetime.date", FixedDate):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600,
            }
        ]
        result = outdated_products(products)
        assert result == []


def test_all_products_expired() -> None:
    """Todos os produtos estão vencidos."""

    class FixedDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 3, 1)

    with mock.patch("datetime.date", FixedDate):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600,
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120,
            },
        ]
        result = outdated_products(products)
        assert result == ["salmon", "chicken"]


def test_empty_list() -> None:
    """Lista vazia deve retornar lista vazia."""
    with mock.patch("datetime.date", FixedDate):
        result = outdated_products([])
        assert result == []


def test_product_expires_today_not_outdated() -> None:
    """Produto que vence hoje não deve ser considerado vencido."""

    class FixedDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 10)

    with mock.patch("datetime.date", FixedDate):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600,
            }
        ]
        result = outdated_products(products)
        assert result == []
