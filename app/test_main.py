import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.fixture()
@mock.patch("app.main.datetime")
def mocked_date_today(mocked_date: mock) -> None:
    mocked_date.return_value = datetime.date(2023, 5, 11)
    yield mocked_date


class TestOutDatedProducts:
    @pytest.mark.parametrize(
        "products, result",
        [
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2023, 5, 12),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2023, 5, 11),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2023, 5, 10),
                        "price": 160
                    }
                ],
                ["duck"],
                id="only 1 product out of date"

            )
        ]
    )
    def test_outdated_product(
            self,
            products: list[dict],
            result: list[str],
            mocked_date_today: mock
    ) -> None:
        assert outdated_products(products) == result
