import pytest
from datetime import date, timedelta


from app.main import outdated_products


@pytest.fixture()
def initialize_products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date.today(),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2027, 2, 1),
            "price": 160
        },
        {
            "name": "pig",
            "expiration_date": date.today() - timedelta(days=1),
            "price": 160
        },
    ]


def test_outdated_products_return_expired_product(
    initialize_products: list[dict],
) -> None:
    assert outdated_products([initialize_products[0]]) == ["salmon"]


def test_outdated_products_skips_expired_today(
        initialize_products: list[dict]
) -> None:
    assert outdated_products([initialize_products[1]]) == []


def test_outdated_products_return_expired_yesterday(
        initialize_products: list[dict]
) -> None:
    assert outdated_products([initialize_products[3]]) == ["pig"]


def test_outdated_products_not_return_unexpired(
    initialize_products: list[dict],
) -> None:
    assert outdated_products([initialize_products[2]]) == []


def test_outdated_products_return_only_expired_in_multiple_scenario(
    initialize_products: list[dict],
) -> None:
    assert outdated_products(initialize_products) == ["salmon", "pig"]
