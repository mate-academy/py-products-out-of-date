import datetime
from unittest.mock import patch

import pytest

from app.main import outdated_products


@pytest.fixture
def mocked_products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 8, 15),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 8, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2026, 8, 6),
            "price": 160
        }
    ]


class TestProducts:
    @pytest.mark.parametrize(
        "today,product_names",
        [
            pytest.param(
                datetime.date(2026, 8, 7),
                ["duck"],
                id="should return only duck product",
            ),
            pytest.param(
                datetime.date(2026, 8, 20),
                ["salmon", "chicken", "duck"],
                id="should return list with all product names",
            ),
            pytest.param(
                datetime.date(2026, 8, 1),
                [],
                id="should return empty list",
            ),
            pytest.param(
                datetime.date(2026, 8, 15),
                ["chicken", "duck"],
                id="should not contain a product with today's expiration date",
            ),
        ],
    )
    def test_outdated_products(
        self,
        mocked_products: list[dict],
        today: datetime.date,
        product_names: list[dict],
    ) -> None:
        with patch("app.main.datetime.date") as mocked_date:
            mocked_date.today.return_value = today
            result = outdated_products(mocked_products)
            mocked_date.today.assert_called()
            assert mocked_date.today.call_count == len(mocked_products), (
                f"`today` should be called {len(mocked_products)} times."
            )
            assert result == product_names
