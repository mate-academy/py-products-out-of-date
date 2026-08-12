import pytest

from datetime import date
from unittest import mock

from app.main import outdated_products


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "products, datetime_value, expected",
        [
            (
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
                ],
                date(2022, 2, 6),
                ["chicken", "duck"]
            ),
            (
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
                ],
                date(2022, 2, 11),
                ["salmon", "chicken", "duck"]
            ),
            (
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
                ],
                date(2022, 2, 1),
                []
            ),
            (
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
                ],
                date(2022, 2, 2),
                ["duck"]
            )
        ],
        ids=[
            "some products outdated",
            "all products outdated",
            "no products outdated",
            "one product outdated"
        ]
    )
    @mock.patch("app.main.datetime.date")
    def test_outdated_products(self,
                               mocked_datetime: mock.Mock,
                               products: list[dict],
                               datetime_value: date,
                               expected: list[str]) -> None:
        mocked_datetime.today.return_value = datetime_value
        assert outdated_products(products) == expected
        mocked_datetime.today.assert_called()
