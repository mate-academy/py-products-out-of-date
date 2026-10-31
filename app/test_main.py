import datetime
import pytest
from unittest import mock
from typing import Generator

from app.main import outdated_products


class TestOutdatedProducts():
    @pytest.fixture
    def moked_datetime_date_today(
            self
    ) -> Generator[mock.MagicMock, None, None]:
        tested_date = datetime.date
        with mock.patch("app.main.datetime.date") as mocked_date:
            mocked_date.today.return_value = tested_date(2022, 2, 2)
            yield mocked_date

    @pytest.mark.parametrize(
        "products,expected",
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
                id="should return outdated duck"
            ),
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2021, 2, 1),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2022, 2, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 160
                    }
                ],
                ["salmon"],
                id="should return outdated salmon"
            ),
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 5),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2022, 1, 1),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 160
                    }
                ],
                ["chicken"],
                id="should return outdated chicken"
            ),
            pytest.param(
                [
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 2),
                        "price": 160
                    }
                ],
                [],
                id="expiration day today should not be outdated"
            ),
        ]
    )
    def test_outdated_products(
            self,
            moked_datetime_date_today: mock.MagicMock,
            products: list,
            expected: list
    ) -> None:
        result = outdated_products(products)

        assert result == expected
