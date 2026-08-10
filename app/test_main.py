import datetime

import pytest

from app import main


REAL_DATE = datetime.date


class MockDate(REAL_DATE):
    @classmethod
    def today(cls) -> REAL_DATE:
        return cls(2022, 2, 2)


@pytest.mark.parametrize(
    "products, expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": REAL_DATE(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": REAL_DATE(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": REAL_DATE(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
            id="only_product_before_today_is_outdated",
        ),
        pytest.param(
            [
                {
                    "name": "milk",
                    "expiration_date": REAL_DATE(2022, 2, 2),
                    "price": 50,
                },
            ],
            [],
            id="product_expiring_today_is_not_outdated",
        ),
        pytest.param(
            [
                {
                    "name": "bread",
                    "expiration_date": REAL_DATE(2022, 2, 1),
                    "price": 30,
                },
            ],
            ["bread"],
            id="product_expired_yesterday_is_outdated",
        ),
        pytest.param(
            [
                {
                    "name": "cheese",
                    "expiration_date": REAL_DATE(2022, 2, 3),
                    "price": 200,
                },
            ],
            [],
            id="product_expiring_tomorrow_is_not_outdated",
        ),
        pytest.param(
            [],
            [],
            id="empty_products_list",
        ),
    ],
)
def test_outdated_products(
    monkeypatch: pytest.MonkeyPatch,
    products: list[dict],
    expected: list[str],
) -> None:
    monkeypatch.setattr(datetime, "date", MockDate)

    assert main.outdated_products(products) == expected
