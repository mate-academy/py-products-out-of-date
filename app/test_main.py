import pytest
import datetime
from unittest import mock

from app.main import outdated_products


class TestOutdatedProducts:
    @pytest.fixture(scope="function")
    def products_template(self) -> list:
        return \
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
            ]

    def test_should_check_non_list_argument(self) -> None:
        with pytest.raises(TypeError):
            outdated_products(None)

    @pytest.mark.parametrize(
        "date_today,result_expected",
        [
            pytest.param(
                datetime.date(2022, 1, 31),
                [],
                id="test empty result"
            ),
            pytest.param(
                datetime.date(2022, 2, 1),
                [],
                id="test border date"
            ),
            pytest.param(
                datetime.date(2022, 2, 5),
                ["duck"],
                id="test one element"
            ),
            pytest.param(
                datetime.date(2022, 2, 6),
                ["duck", "chicken"],
                id="test two elements"
            ),
            pytest.param(
                datetime.date(2022, 2, 10),
                ["duck", "chicken"],
                id="test two elements on border date"
            ),
            pytest.param(
                datetime.date(2022, 2, 11),
                ["duck", "chicken", "salmon"],
                id="test two elements"
            )
        ]
    )
    @mock.patch("datetime.date")
    def test_check_function(self,
                            # mocked_datetime_date_today,
                            mocked_today: object,
                            date_today: object, result_expected: str,
                            products_template: list) -> None:

        mocked_today.today.return_value = date_today
        assert sorted(outdated_products(products_template)) == \
               sorted(result_expected)
