import datetime
from unittest import mock
import pytest
from app.main import outdated_products


class TestProducts:
    @pytest.mark.parametrize(
        "dict_of_product,expected_error",
        [
            (
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
                ["duck"]
            )
        ]
    )
    def test_outdated_products(
            self,
            dict_of_product, expected_error
    ):
        with mock.patch("app.main.datetime") as mocked_datetime:
            mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)

            assert outdated_products(dict_of_product) == expected_error
