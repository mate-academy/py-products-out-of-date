import datetime
from unittest.mock import patch
import pytest
from app.main import outdated_products


def test_outdated_products_empty_list() -> None:
    result: list = outdated_products([])
    assert result == []


def test_outdated_products_no_outdated() -> None:
    products: list[dict] = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 3, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 3, 5),
            "price": 120
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = datetime.date
        result: list = outdated_products(products)
        assert result == []


def test_outdated_products_all_outdated() -> None:
    products: list[dict] = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 1, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 1, 5),
            "price": 120
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = datetime.date
        result: list = outdated_products(products)
        assert result == ["salmon", "chicken"]


def test_outdated_products_some_outdated() -> None:
    products: list[dict] = [
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
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = datetime.date
        result: list = outdated_products(products)
        assert result == ["duck"]


def test_outdated_products_expiration_today() -> None:
    products: list[dict] = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 120
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = datetime.date
        result: list = outdated_products(products)
        assert result == ["chicken"]


def test_outdated_products_edge_case_same_day() -> None:
    products: list[dict] = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 3, 15),
            "price": 80
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 3, 15)
        mock_datetime.date.side_effect = datetime.date
        result: list = outdated_products(products)
        assert result == []


def test_outdated_products_large_list() -> None:
    products: list[dict] = [
        {"name": f"product_{i}",
         "expiration_date": datetime.date(2022, 3, i),
         "price": i * 10}
        for i in range(1, 31)
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 3, 15)
        mock_datetime.date.side_effect = datetime.date
        result: list = outdated_products(products)
        expected: list = [f"product_{i}" for i in range(1, 15)]
        assert result == expected


def test_outdated_products_order_preserved() -> None:
    products: list[dict] = [
        {
            "name": "zucchini",
            "expiration_date": datetime.date(2022, 1, 20),
            "price": 50
        },
        {
            "name": "apple",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 30
        },
        {
            "name": "banana",
            "expiration_date": datetime.date(2022, 1, 15),
            "price": 40
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = datetime.date
        result: list = outdated_products(products)
        assert result == ["zucchini", "banana"]


def test_outdated_products_missing_required_fields() -> None:
    products: list[dict] = [
        {
            "name": "salmon",
            "price": 600
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = datetime.date
        with pytest.raises(KeyError):
            outdated_products(products)


def test_outdated_products_wrong_date_format() -> None:
    products: list[dict] = [
        {
            "name": "salmon",
            "expiration_date": "2022-02-01",
            "price": 600
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = datetime.date
        with pytest.raises(TypeError):
            outdated_products(products)
