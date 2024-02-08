from app.main import outdated_products
import pytest
import datetime
from unittest import mock


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "products,result,today",
        [
            pytest.param(
                [
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
                ],
                ["duck"],
                datetime.date(2022, 2, 2),
            ),
        ]
    )
    def test_outdated_products(
            self,
            products: [dict],
            result: [str],
            today: datetime,
    ) -> None:
        with mock.patch("app.main.datetime") as mocked_data:
            mocked_data.date.today.return_value = today
            assert outdated_products(products) == result
