import datetime
from unittest import mock
import pytest

from app.main import outdated_products


class TestOutdatedProduct():
    @pytest.mark.parametrize(
        "product,result,today",
        [
            pytest.param([
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 7),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 8),
                    "price": 50
                }
            ],
                ["chicken", "duck"],
                datetime.date(2022, 2, 8)
            )
        ]
    )
    def test_expiration_day_yesterday_outdated(
            self,
            product: list,
            result: list,
            today: datetime.datetime
    ) -> None:
        with mock.patch("app.main.datetime") as mock_date:
            mock_date.date.today.return_value = today
            assert outdated_products(product) == result
