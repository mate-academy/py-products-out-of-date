import pytest
from unittest.mock import MagicMock, patch
from app.main import outdated_products
import datetime


class TestOutdatedProducts:
    @patch("app.main.datetime")
    @pytest.mark.parametrize(
        "product, expected",
        [
            ([{"name": "salmon", "expiration_date":
                datetime.date(2022, 2, 10)}], []),
            ([{"name": "chicken", "expiration_date":
                datetime.date(2022, 2, 5)}], ["chicken"]),
            ([{"name": "duck", "expiration_date":
                datetime.date(2022, 2, 1)}], ["duck"])
        ],
        ids=[
            "All products is not outdated",
            "Chicken is outdated",
            "Duck is outdated"
        ]
    )
    def test_outdated_products(self,
                               mocked_function: MagicMock,
                               product: list[dict],
                               expected: list) -> None:
        mocked_function.date.today.return_value = datetime.date(2022, 2, 10)
        assert outdated_products(product) == expected
