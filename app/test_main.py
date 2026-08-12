from unittest import mock
from app.main import outdated_products
from datetime import date


@mock.patch("app.main.datetime")
def test_outdated_products_on_all_correct(m_date: object) -> None:
    m_date.date.today.return_value = date(2022, 2, 2)
    products =\
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            }
        ]
    result = outdated_products(products)
    assert result == []


@mock.patch("app.main.datetime")
def test_outdated_products_on_one_mistake(m_date: object) -> None:
    m_date.date.today.return_value = date(2022, 2, 2)
    products =\
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ]
    result = outdated_products(products)
    assert result == ["duck"]


@mock.patch("app.main.datetime")
def test_outdated_products_on_all_mistake(m_date: object) -> None:
    m_date.date.today.return_value = date(2022, 2, 2)
    products =\
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 1, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 1, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 1, 1),
                "price": 160
            }
        ]
    result = outdated_products(products)
    assert result == ["salmon", "chicken", "duck"]
